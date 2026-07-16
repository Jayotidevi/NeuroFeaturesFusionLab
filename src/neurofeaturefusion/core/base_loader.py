from abc import abstractmethod
from pathlib import Path

from .base_component import BaseComponent


"""
Base Loader Module.

Defines the abstract interface for loading raw data
from external sources into NeuroFeaturesFusionLab.

A loader is responsible only for data retrieval.
"""


class BaseLoader(BaseComponent):

    def __init__(
    self,
        dataset_name: str,
        data_path: str,
        config: dict | None = None,
    ):
        super().__init__(name=dataset_name)

        self.dataset_name = dataset_name
        self.data_path = data_path
        self.config = config or {}

    @abstractmethod
    def load(self):
        """
        Load MODMA raw dataset resources.

        Returns
        -------
        dict
            Paths to available MODMA resources.
        """

        return {
            "eeg_128_path": str(self.modma_config.eeg_128_path),
            "eeg_3_path": str(self.modma_config.eeg_3_path),
            "audio_path": str(self.modma_config.audio_path),
            "metadata_path": str(self.modma_config.metadata_path)
        }

    def validate_source(self):
        """
        Validate that the dataset source exists and is accessible.
        """

        path = Path(self.data_path)

        if not path.exists():
            raise FileNotFoundError(
                f"Dataset path does not exist: {self.data_path}"
            )

        if not path.is_dir():
            raise NotADirectoryError(
                f"Dataset path is not a directory: {self.data_path}"
            )

        return True

    def validate(self):
        """
        Validate loader configuration and dataset source.
        """

        return self.validate_source()

    def summary(self):
        """
        Return loader information.
        """

        return {
            "loader": self.__class__.__name__,
            "dataset_name": self.dataset_name,
            "data_path": self.data_path,
            "config": self.config,
        }