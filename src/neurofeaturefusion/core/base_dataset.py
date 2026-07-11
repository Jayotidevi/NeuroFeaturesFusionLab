from abc import abstractmethod

from .base_component import BaseComponent


class BaseDataset(BaseComponent):
    """
    Abstract dataset interface.

    Responsible for providing samples
    to the framework.
    """

    def __init__(
        self,
        name: str,
        config=None
    ):
        super().__init__(name, config)
        self.metadata = {}

    @abstractmethod
    def __len__(self):
        """
        Return number of samples.
        """
        pass

    @abstractmethod
    def __getitem__(self, index):
        """
        Return one sample.
        """
        pass

    def set_metadata(self, metadata):
        """
        Store dataset metadata.
        """
        self.metadata = metadata

    def get_metadata(self):
        """
        Return dataset metadata.
        """
        return self.metadata

    def validate(self):
        """
        Validate dataset configuration.
        """
        return True
