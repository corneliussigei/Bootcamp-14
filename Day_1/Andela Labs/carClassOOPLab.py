class Car(object):
    """docstring for Car"""
    def __init__(self, name=None, model=None, carType=None):
        # initialize speed to 0
        self.speed = 0

        # intialize name to General
        if name is None:
            self.name = 'General'
            self.num_of_doors = 4
        else:
            self.name = name

        # set default model to GM
        if model is None:
            self.model = 'GM'
        else:
            self.model = model

        # default type is saloon, unless otherwise
        if carType is None:
            self.carType = 'saloon'
        else:
            self.carType = carType

        # trailer has more wheels
        if carType == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

        # set Porsche & Koennigsegg doors to two
        if name is not None and (name == 'Porshe' or name == 'Koenigsegg'):
            self.num_of_doors = 2
        elif name is not None and (name != 'Porshe' or name != 'Koenigsegg'):
            self.num_of_doors = 4
        else:
            pass

    def is_saloon(self):
        # Return true if carType is a saloon
        if self.carType == 'saloon':
            return True
        else:
            return False

    def drive(self, velocity):
        assert isinstance(velocity, int), "Drive argument must be integer"
        # set trailer speed
        if self.carType == 'trailer':
            self.speed = velocity * 11
            return self
        # set saloon speed
        elif self.carType == 'saloon':
            self.speed = 10 ** velocity
            return self
        else:
            pass