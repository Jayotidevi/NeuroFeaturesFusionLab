from neurofeaturefusion.core.base_loader import BaseLoader
from .config import MODMAConfig


class MODMALoader(BaseLoader):
    """
    Loader for the MODMA multimodal dataset.

    Responsible only for loading raw MODMA resources.
    """

    def __init__(self, config: MODMAConfig):

        super().__init__(
            dataset_name="MODMA",
            data_path=str(config.dataset_root),
            config=config
        )

        self.modma_config = config

    def load(self):
        return {
            "eeg_128_path": str(self.modma_config.eeg_128_path),
            "eeg_3_path": str(self.modma_config.eeg_3_path),
            "audio_path": str(self.modma_config.audio_path),
            "eeg_128_metadata": str(self.modma_config.eeg_128_metadata),
            "eeg_3_metadata": str(self.modma_config.eeg_3_metadata),
        }