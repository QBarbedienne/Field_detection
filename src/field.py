class Terrain():
    def __init__(self, coordinates_prev=[0, 0], size_prev=[0, 0]):
        self.size = size_prev
        self.coordinates = coordinates_prev
        
    def reset(self, coordinates_prev=[0, 0], size_prev=[0, 0]):
        self.size = size_prev
        self.coordinates = coordinates_prev

    def updateSize(self, coordinates_prev, size_prev):
        self.size = size_prev
        self.coordinates = coordinates_prev
