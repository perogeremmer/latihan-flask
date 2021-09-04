from abc import ABCMeta, abstractmethod

class UserInterface(metaclass=ABCMeta):
    """Abstract class for user interface"""
    
    @abstractmethod
    def create(self, **kwargs):
        """Create user"""
        pass

    @abstractmethod
    def auth(self, **kwargs):
        """Authenticate user"""
        pass