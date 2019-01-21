class vehicle:
    def __init__(self,name):
        self.name=name
    def drive(self):
        raise NotImplementedError("subclass must imp[lement abstract method")
    def stop(self):
        raise NotImplementedError("subclass must imp[lement abstract method")
class sportscar(vehicle):
    def drive(self):
        return"sportscar driving"
    def stop(self):
        return"sportscar braking"
class truck(vehicle):
    def drive(self):
        return"truck id driving  slowly "
    def stop(self):
        return"truck has been stopped"
cars=[truck("bananatruck"),truck("orangetruck"),sportscar("maclaren"),sportscar("audi")]
for vehicle in cars:
    print(vehicle.name+ " "+ vehicle.drive())
    print(vehicle.name+ " "+ vehicle.stop())
