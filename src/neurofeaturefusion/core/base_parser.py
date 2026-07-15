from abc import abstractmethod

from .base_component import BaseComponent
"""
Base Parser Module.

Defines the abstract interface for converting
raw loaded data into standardized framework objects.

A parser is responsible for interpreting raw data
structures and creating BaseSample-compatible outputs.
"""

class BaseParser(BaseComponent):

    """
    Abstract base class for dataset parsers.

    Parsers transform raw data produced by loaders
    into standardized representations.
    """

    def __init__(
        self,
        dataset_name: str,
        config: dict | None = None,
    ):
        super().__init__(name=dataset_name)

        self.dataset_name = dataset_name
        self.config = config or {}


    @abstractmethod
    def parse(self, raw_data):
        """
        Parse raw dataset data into standardized representations.

        Parameters
        raw_data : object
            Raw data produced by a loader.

        Returns
        object
            Parsed output, typically BaseSample objects.
        """
        pass

    def validate(self):
        """
        Validate parser configuration.

        This method implements the validation contract
        inherited from BaseComponent.
        """
        if not self.dataset_name:
            raise ValueError(
                "Parser dataset_name cannot be empty."
        )
        return True

    def summary(self):
        
        """
        Return parser information.
        """
        return {
            "parser": self.__class__.__name__,
            "dataset_name": self.dataset_name,
            "config": self.config,
        }