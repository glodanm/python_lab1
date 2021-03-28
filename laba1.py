class Helicopter:

    price = "1000 000 USD"
    @staticmethod
    def avg_price():
        return Helicopter.price


    def __init__(self, max_mass=0, name="missing value", max_height=0, color="missing value", height=0, producer="missing value"):
        self.max_mass = max_mass
        self.name = name
        self.max_height = max_height
        self.color = color
        self.height = height
        self.__producer = producer

    
    def __del__(self):
        pass
    
    def __str__(self):
        return "Max mass(in kilos): " + str(self.max_mass) + "\nName: " + self.name + "\nMax height(in meters): " + str(self.max_height) + "\nColor: " + self.color + "\nHeight(): " + str(self.height) + "\nProducer: " + self.__producer

    def get_producer(self):
        return self.__producer
    