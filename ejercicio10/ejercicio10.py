class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def darArea(self):
        import math
        print math.pi*(self.radio**2)
p = Circulo(1)
p.darArea()
