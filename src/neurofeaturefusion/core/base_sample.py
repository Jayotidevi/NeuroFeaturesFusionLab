from typing import Dict, Optional

from .base_component import BaseComponent

class BaseSample(BaseComponent):
    """
    Represents one multimodal sample in the framework.

    A sample contains:
    - sample identity
    - label information
    - metadata
    - multiple modalities
    """

    def __init__(
        self,
        sample_id: str,
        dataset_name: str,
        label=None,
        metadata: Optional[dict] = None
    ):
        super().__init__(name=sample_id)

        self.sample_id = sample_id
        self.dataset_name = dataset_name
        self.label = label
        self.metadata = metadata if metadata is not None else {}

        # Stores modality objects
        # Example:
        # {
        #     "eeg": EEGModality(),
        #     "audio": AudioModality()
        # }
        self.modalities: Dict[str, object] = {}

    def add_modality(self, name: str, modality):
        """
        Add a modality to this sample.

        Parameters
        ----------
        name : str
            Modality identifier.
            Example: "eeg", "audio"

        modality :
            BaseModality object
        """
        self.modalities[name] = modality

    def get_modality(self, name: str):
        """
        Retrieve a modality by name.
        """
        return self.modalities.get(name)

    def has_modality(self, name: str) -> bool:
        """
        Check whether a modality exists.
        """
        return name in self.modalities

    def list_modalities(self):
        """
        Return available modality names.
        """
        return list(self.modalities.keys())

    def remove_modality(self, name: str):
        """
        Remove a modality from the sample.
        """
        if name in self.modalities:
            del self.modalities[name]

    def summary(self):
        """
        Return sample information.
        """
        return {
            "sample_id": self.sample_id,
            "dataset_name": self.dataset_name,
            "label": self.label,
            "modalities": self.list_modalities(),
            "metadata": self.metadata
        }
    def validate(self):
        """
        Validate sample structure.
        """
        if not self.sample_id:
            raise ValueError("Sample ID cannot be empty.")

        if not isinstance(self.modalities, dict):
            raise TypeError("Modalities must be stored as a dictionary.")

        return True
        
