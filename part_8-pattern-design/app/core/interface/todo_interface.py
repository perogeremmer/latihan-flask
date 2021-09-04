from abc import ABCMeta, abstractmethod

class TodoInterface(metaclass=ABCMeta):
    """Abstract class for todo interface"""
    
    @abstractmethod
    def create(self, **kwargs):
        """Create todo"""
        pass

    @abstractmethod
    def get_by_id(self, id, **kwargs):
        """Get todo by ID"""
        pass

    @abstractmethod
    def get(self, **kwargs):
        """Get all Todo"""
        pass

    @abstractmethod
    def update(self, id, **kwargs):
        """Update todo"""
        pass

    @abstractmethod
    def delete(self, id, **kwargs):
        """Delete todo"""
        pass
