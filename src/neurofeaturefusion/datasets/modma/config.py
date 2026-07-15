from pathlib import Path
"""
MODMA Configuration Module.

Provides configuration for locating and accessing
the MODMA dataset within NeuroFeaturesFusionLab.

This class is responsible only for dataset paths
and configuration. It does not load or parse data.
"""
class MODMAConfig:
    """
    Configuration  class for the MODMA dataset.

    """
    def __init__(self, dataset_root:str):
        """
        Initialize MODMA dataset configuration.

        parameters
        dataset_root: str
            Root directory of th MODMA dataset

        """
        self.dataset_root = Path(dataset_root)
        self.eeg_128_path  =(
            self.dataset_root / 
            "EEG_128channels_resting_lanzhou_2015"
        )
        self.eeg_3_path  = (
            self.dataset_root /
            "EEG_3channels_resting_lanzhou_2015"
        )
        self.audio_path = (
            self.dataset_root /
            "audio_lanzhou_2015"
        )

    def validate(self):
        """
        Validate MODMA dataset paths.
        """
        required_paths = {
        "dataset_root": self.dataset_root,
        "eeg_128_path": self.eeg_128_path,
        "eeg_3_path": self.eeg_3_path,
        "audio_path": self.audio_path,
    }

        for name, path in required_paths.items():
            if not path.exists():
                raise FileNotFoundError(
                    f"{name} does not exist: {path}"
                )

        return True

    def summary(self):
        """
        Return loader information.
        """

        return {
            "dataset_root": self.dataset_root,
            "eeg_128_path": self.eeg_128_path,
            "eeg_3_path": self.eeg_3_path,
            "audio_path": self.audio_path
            }

