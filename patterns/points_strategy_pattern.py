from abc import ABC, abstractmethod

class PointsStrategy(ABC):
    @abstractmethod
    def calculate_points(self, acerto):
        pass

# Encapsular a logica de calculo dos pontos
class EasyPointsStrategy(PointsStrategy):
    def calculate_points(self, acerto):
        return 1*acerto
    
class MediumPointsStrategy(PointsStrategy):
    def calculate_points(self, acerto):
        return 2*acerto
    
class HardPointsStrategy(PointsStrategy):
    def calculate_points(self, acerto):
        return 3*acerto
