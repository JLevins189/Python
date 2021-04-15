class Vehicle:
    def __init__(self,year = 0000, model = "", mileage = 0, VIN = 123456, transmission_gears = 0, owners = 0, engine_size = 0, engine_bhp = 0):
        self.year = year
        self.model = model
        self.mileage = mileage
        self.VIN = VIN
        self.transmission_gears =transmission_gears
        self.owners = owners
        self.engine = Engine(engine_size,engine_bhp)
        self.type = type

    def __str__(self):
        return_str = "Year: {}\nModel: {}\nMileage: {}\nOwners: {}\nVIN: {}\nTransmission Gears: {}\n{}\n".format(
                        self.year, self.model, self.mileage, self.owners, self.VIN, self.transmission_gears, str(self.engine))
        return return_str


class Car(Vehicle):
    def __init__(self, body_type = "", passengers = 0, airbags = 0, year = 0000, model = "", mileage = 0, VIN = 123456, transmission_gears = 0, owners = 0, engine_size = 0, engine_bhp = 0):
        self.body_type = body_type
        self.passengers = passengers
        self.airbags = airbags
        Vehicle.__init__(self, year, model, mileage, VIN, transmission_gears, owners, engine_size, engine_bhp)

    def __str__(self):
        return_str = ""
        if self.body_type != "":
            return_str += "Body Type: {}\n".format(self.body_type)

        if self.passengers > 0:
            return_str += "Passengers: {}\n".format(self.passengers)

        if self.airbags > 0:
            return_str += "Airbags: {}\n".format(self.airbags)

        return_str += Vehicle.__str__(self)
        return return_str



class Minivan(Vehicle):
    def __init__(self, passengers = 0, length = 0, year = 0000, model = "", mileage = 0, VIN = 123456, transmission_gears = 0, owners = 0, engine_size = 0, engine_bhp = 0):
        self.passengers = passengers
        self.length = length
        Vehicle.__init__(self, year, model, mileage, VIN, transmission_gears, owners, engine_size, engine_bhp)

    def __str__(self):
        return_str = ""
        if self.passengers > 0:
            return_str += "Passengers: {}\n".format(self.passengers)

        if self.length > 0:
            return_str += "Length: {}m\n".format(self.length)
        return_str += Vehicle.__str__(self)
        return return_str

class Truck(Vehicle):
    def __init__(self, passengers = 0, length = 0, max_load = 0, year = 0000, model = "", mileage = 0, VIN = 123456, transmission_gears = 0, owners = 0, engine_size = 0, engine_bhp = 0):
        self.passengers = passengers
        self.length = length
        self.max_load = max_load
        Vehicle.__init__(self, year, model, mileage, VIN, transmission_gears, owners, engine_size, engine_bhp)

    def __str__(self):
        return_str = ""
        if self.passengers > 0:
            return_str += "Passengers: {}\n".format(self.passengers)

        if self.max_load > 0:
            return_str += "Max load: {}KG\n".format(self.max_load)

        if self.length > 0:
            return_str += "Length: {}m\n".format(self.length)
        return_str += Vehicle.__str__(self)
        return return_str

class SUV(Vehicle):
    def __init__(self, passengers = 0, airbags = 0, year = 0000, model = "", mileage = 0, VIN = 123456, transmission_gears = 0, owners = 0, engine_size = 0, engine_bhp = 0):
        self.passengers = passengers
        self.airbags = airbags
        Vehicle.__init__(self, year, model, mileage, VIN, transmission_gears, owners, engine_size, engine_bhp)

    def __str__(self):
        return_str = ""
        if self.passengers > 0:
            return_str += "Passengers: {}\n".format(self.passengers)

        if self.airbags > 0:
            return_str += "Airbags: {}\n".format(self.airbags)

        return_str += Vehicle.__str__(self)
        return return_str


class Engine():
    def __init__(self, engine_size = 0, engine_bhp = 0):
        self.engine_size = engine_size
        self.engine_bhp = engine_bhp

    def __str__(self):
            return_str = ""
            if self.engine_size > 0:
                return_str += "Engine Size: {}\n".format(self.engine_size)

            if self.engine_bhp > 0:
                return_str += "BHP: {}\n".format(self.engine_bhp)

            return return_str


#Main


#Vehicle Basis
#year, model, mileage, VIN, transmission_gears, owners, engine_size, engine_bhp
vehicle1 = Vehicle(2020, "Corolla", 190401, 435196, 6, 4, 2.1, 479 )
vehicle2 = Vehicle(2019, "BigMan", 19000, 437427, 7, 1, 6.0, 967 )
#print(vehicle1)

#Car
#Car = body_type,passengers, airbags, year, model, mileage, VIN, transmission_gears, owners, engine_size, engine_bhp
#car1 = Car("saloon", 5, 2, 2020, "Corolla", 190401, 435196, 6, 4, 2.1, 479 )
#car1 = Car("saloon", 5, 2, vehicle1)
#print(car1)

#Truck
#Passengers,Length, Max Load, Vehicle
#truck1 = Truck(3, 5, 9000, vehicle2)
#print(truck1)

#SUV
#Passengers, Airbag_num, Vehicle
#SUV1 = SUV(7, 2, vehicle2)
#print(SUV1)

#Minivan
#Passenger, Length, Vehicle
#mini1 = Minivan(12, 3, vehicle1)
#print(mini1)
