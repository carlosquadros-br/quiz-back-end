from abc import ABC, abstractmethod

class PointsStrategy(ABC):
    @abstractmethod
    def calculate_points(self):
        pass

# Encapsular a logica de calculo dos pontos
class EasyPointsStrategy(PointsStrategy):
    def calculate_points(self, peso=1, acerto=1):
        return peso*acerto
    
class MediumPointsStrategy(PointsStrategy):
    def calculate_points(self):
        return peso*acerto
    
class HardPointsStrategy(PointsStrategy):
    def calculate_points(self):
        return 3
