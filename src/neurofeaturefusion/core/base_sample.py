from abc import ABC, abstractmethod


class BaseSample(ABC):
    """
    Abstract representation of a single multimodal sample.

    A sample contains the data required by the framework:
    - modality information
    - labels
    - metadata
    """

    def __init__(
        self,
        sample_id: str,
        label=None,
        metadata=None
    ):
        self.sample_id = sample_id
        self.label = label
        self.metadata = metadata if metadata is not None else {}

    @abstractmethod
    def get_modalities(self):
        """
        Return available modalities in this sample.
        """
        pass

    def summary(self):
        """
        Return sample information.
        """
        return {
            "sample_id": self.sample_id,
            "label": self.label,
            "modalities": self.get_modalities(),
            "metadata": self.metadata
        }
