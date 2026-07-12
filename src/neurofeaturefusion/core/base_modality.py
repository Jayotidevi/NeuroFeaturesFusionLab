from typing import Any, Dict, Optional

from .base_component import BaseComponent

class BaseModality(BaseComponent):
    """
    Represnents a single modality within a mulitmodal sample.

    A modality stores the original data together with its metadata,
    independent of the specific modality type (EEG, Audio, Video, Clinical , MRI, etc.).

    BaseModality provides a common interface for all modality types before harmonization and deep representaion learning.

    """
    def __init__(
            self,
            name: str,
            modality_type: str,
            data: any,
            metadata: Optional[Dict] = None

    ):
        super().__init__(name=name)

        self.modality_type= modality_type
        self.data= data
        self.metadata= metadata if metadata is not None else{}

    
    def validate(self):

        if not self.name:
            return False

        if not self.modality_type:
            return False
        if self.data is None:
            return False
        return True

    def summary(self):
        """
        Return modality information.
        """

        return {
        "name": self.name,
        "modality_type": self.modality_type,
        "data_type": type(self.data).__name__,
        "metadata": self.metadata
        }


