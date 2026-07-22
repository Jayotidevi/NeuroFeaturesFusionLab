from abc import abstractmethod
from .base_component import BaseComponent


class BaseHarmonizer(BaseComponent):

    def __init__(self, config=None):
        super().__init__(config)


    @abstractmethod
    def harmonize(self, dataset):
        """
        Apply harmonization to entire dataset.

        Parameters
        ----------
        dataset : BaseDataset
            Input dataset

        Returns
        -------
        BaseDataset
            Harmonized dataset
        """
        pass
    
    def update_metadata(self, dataset, report):
        """
        Attach harmonization information
        to dataset metadata.
        """

        metadata = dataset.get_metadata()

        metadata["harmonization"] = report

        dataset.set_metadata(metadata)

        return dataset

   


    def validate(self, dataset):
        """
        Check dataset compatibility before harmonization.
        """
        return True


    def summary(self):
        """
        Return harmonizer information.
        """
        return {
            "name": self.__class__.__name__
        
            }
