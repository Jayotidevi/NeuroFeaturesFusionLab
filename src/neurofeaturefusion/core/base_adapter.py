
from abc import abstractmethod
from .base_component import BaseComponent
from typing import Optional, Dict

class BaseAdapter(BaseComponent):
    def __init__(
            self,
           dataset_name: str,
            data_path: str,
            config: Optional[Dict]= None
    ):
        super().__init__(name=dataset_name, config=config)
        self.dataset_name = dataset_name
        self.data_path= data_path
    @abstractmethod
    def load(self):
        """
         Load raw dataset files.

         Returns
         raw_data:
        Dataset-specific raw representation.
        
        """
    pass        
    

    @abstractmethod
    def parse(self, raw_data):
         """
        Parse loaded dataset into structured information.

        Parameters
        raw_data:
        Output from load()

        Returns
         parsed_data:
        Structured dataset information.
        
        """
    pass

    @abstractmethod
    def create_samples(self, parsed_data):
        """
        Create BaseSample objects from parsed dataset information.

        Parameters
        parsed_data:
            Structured dataset information from parse()

        Returns
        samples:
            List of BaseSample objects
        """
        pass
    def summary(self):
        """
        Return adapter information.
        """    
        return {
            "dataset_name": self.dataset_name,
            "data_path": self.data_path,
            "config": self.config,
            "initialized": self.initialized
        } 
