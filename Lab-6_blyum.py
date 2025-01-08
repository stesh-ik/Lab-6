class Car:
    def __init__(self, fuel_capacity, fuel_consumption, average_speed):
        self.fuel_capacity = fuel_capacity  
        self.fuel_consumption = fuel_consumption  
        self.average_speed = average_speed

    def calculate_distance(self):
        """
        Calculate the distance the car can travel on a full tank.
        :return: distance in kilometers
        """
        return (self.fuel_capacity / self.fuel_consumption) * 100

class Truck(Car):
    def __init__(self, fuel_capacity, fuel_consumption, average_speed, cargo_weight):
        super().__init__(fuel_capacity, fuel_consumption, average_speed)
        self.cargo_weight = cargo_weight  

    def fuel_efficiency_ratio(self, distance=250):
        """
        Calculate the ratio of cargo weight to fuel consumed over a given distance.
        :param distance: Distance in kilometers (default is 250 km)
        :return: Ratio of cargo weight to fuel consumption
        """
        fuel_used = (self.fuel_consumption / 100) * distance
        return self.cargo_weight / fuel_used

class Bus(Car):
    def __init__(self, fuel_capacity, fuel_consumption, average_speed, passenger_count):
        super().__init__(fuel_capacity, fuel_consumption, average_speed)
        self.passenger_count = passenger_count

    def passenger_fuel_ratio(self, distance=250):
        """
        Calculate the ratio of passenger count to fuel consumed over a given distance.
        :param distance: Distance in kilometers (default is 250 km)
        :return: Ratio of passengers to fuel consumption
        """
        fuel_used = (self.fuel_consumption / 100) * distance
        return self.passenger_count / fuel_used

#Example usage:
truck = Truck(300, 30, 80, 5000)
print(truck.calculate_distance())
print(truck.fuel_efficiency_ratio())

bus = Bus(200, 20, 60, 50)
print(bus.calculate_distance())
print(bus.passenger_fuel_ratio())