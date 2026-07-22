import pandas as pd
from pathlib import Path
from neurofeaturefusion.core.base_parser import BaseParser
from neurofeaturefusion.core.base_sample import BaseSample
from neurofeaturefusion.core.base_modality import BaseModality

from .dataset import MODMADataset


class MODMAParser(BaseParser):
    """
    Parser for MODMA dataset.

    Converts raw MODMA resources into
    NeuroFeaturesFusion objects.
    """

    def __init__(self, config=None):
        super().__init__(
            dataset_name="MODMA",
            config=config
        )

    def parse(self, raw_data):
         """
         Convert MODMA raw resources into MODMADataset.
         """

         dataset = MODMADataset(
         config=self.config
         )

         metadata_path = raw_data["eeg_128_metadata"]
         df = pd.read_excel(metadata_path)
         
         for _, row in df.iterrows():

             sample = BaseSample(
                sample_id=str(row["subject id"]),
                dataset_name="MODMA",
                label=row["type"],
                metadata={
                     "age": row["age"],
                     "gender": row["gender"],
                     "education": row["education（years）"],
                     "PHQ-9": row["PHQ-9"],
                     "CTQ-SF": row["CTQ-SF"],
                     "LES": row["LES"],
                     "SSRS": row["SSRS"],
                     "GAD-7": row["GAD-7"],
                     "PSQI": row["PSQI"]
                }
            )


             # ---------- EEG modality ----------
             eeg_file = self._find_eeg_file(
                 row["subject id"],
                 Path(raw_data["eeg_128_path"])
             )

             if eeg_file is not None:

                 eeg_result = self._load_eeg_file(eeg_file)

                 eeg_modality = BaseModality(
                     name="resting_eeg",
                     modality_type="EEG",
                     data=eeg_result["data"],
                     metadata={
                         "sampling_rate": float(
                             eeg_result["sampling_rate"][0][0]
                         ),
                         "shape": eeg_result["data"].shape,
                         "signal_key": eeg_result["signal_key"]
                     }
                 )

                 sample.add_modality(
                     "eeg",
                     eeg_modality
                 )
             audio_folder = self._find_audio_folder(
                 row["subject id"],
                 Path(raw_data["audio_path"])
             ) 
            
             if audio_folder is not None:
            
                 audio_result = self._load_audio_folder(
                     audio_folder
                 )
            
                 audio_modality = BaseModality(
                     name="interview_audio",
                     modality_type="Audio",
                     data=audio_result,
                     metadata={
                         "num_recordings": len(audio_result)
                     }
                 )
            
                 sample.add_modality(
                     "audio",
                     audio_modality
                 )

                 

             dataset.add_sample(sample)

         dataset.set_metadata(
             {
                 "dataset": "MODMA",
                 "num_samples": len(dataset)
             }
       
             )

         return dataset


    def _load_eeg_file(self, file_path):
         """
         Load EEG signal from MODMA .mat file.
         """

         from scipy.io import loadmat

         mat = loadmat(file_path)

         signal_key = [
             key for key in mat.keys()
             if not key.startswith("__")
             and key not in [
                 "samplingRate",
                 "Impedances_0"
             ]
         ][0]

         eeg_signal = mat[signal_key]

         return {
             "data": eeg_signal,
             "sampling_rate": mat["samplingRate"],
             "signal_key": signal_key
         }


    def _get_subject_file_id(self, subject_id):
        return "0" + str(subject_id)


    def _find_eeg_file(self, subject_id, eeg_path):

        file_id = self._get_subject_file_id(subject_id)

        for file in eeg_path.glob("*.mat"):
            if file.name.startswith(file_id):
                return file

        return None


    def _find_audio_folder(self, subject_id, audio_path):

        file_id = self._get_subject_file_id(subject_id)

        folder = audio_path / file_id

        if folder.exists():
            return folder

        return None

    def _load_audio_folder(self, folder_path):
        """
        Load MODMA audio recordings for one subject.
        """
    
        import soundfile as sf
    
        audio_files = sorted(
            folder_path.glob("*.wav")
        )
    
        recordings = []
    
        for file in audio_files:
    
            try:

                signal, sr = sf.read(file)
            
                recordings.append(
                    {
                        "file": file.name,
                        "data": signal,
                        "sampling_rate": sr,
                        "status": "loaded"
                    }
                )
            
            except Exception as e:
            
                recordings.append(
                    {
                        "file": file.name,
                        "data": None,
                        "sampling_rate": None,
                        "status": "failed",
                        "error": str(e)
                    }
                )
    
        return recordings

    def validate(self):
        """
        Validate MODMA parser.
        """

        return super().validate()


    def summary(self):
        """
        Return parser information.
        """

        return {
            "parser": self.__class__.__name__,
            "dataset_name": "MODMA"
        }
