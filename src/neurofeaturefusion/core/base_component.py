from abc import ABC, abstractmethod


class BaseComponent(ABC):
    """
    Base class for all NeuroFeaturesFusion framework components.

    Provides:
    - component identity
    - configuration handling
    - lifecycle management
    - validation interface
    """

    def __init__(self, name: str, config=None):
        self.name = name
        self.config = config if config is not None else {}
        self.initialized = False

    def initialize(self):
        """
        Initialize component.
        """
        self.initialized = True

    @abstractmethod
    def validate(self):
        """
        Validate component configuration.
        """
        pass

    def summary(self):
        """
        Return component information.
        """
        return {
            "name": self.name,
            "initialized": self.initialized,
            "config": self.config
        }
