from abc import ABC, abstractmethod

class PointsStrategy(ABC):
    @abstractmethod
    def calculate_points(self):
        pass

class EasyPointsStrategy(PointsStrategy):
    def calculate_points(self):
        return 1
    
class MediumPointsStrategy(PointsStrategy):
    def calculate_points(self):
        return 2
    
class HardPointsStrategy(PointsStrategy):
    def calculate_points(self):
        return 3
