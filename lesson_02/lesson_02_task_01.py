class Car:

    service_is_complete = False

    def __init__(self, model, color):
        self.base_color = color
        self.model = model

    def repainting(self, color):
        self.base_color = color
        print("Color of your car is changed. It\'s {} now". format(self.base_color))

    def service(self):
        self.service_is_complete = True
        print("Service completed successfully!")


class PassengerCar(Car):
    cabin_color = 'White'
    doors_color = 'White'
    is_repainting = False
    is_repainting_cabin = False
    is_repainting_doors = False

    def repainting(self, color):
        self.base_color = color
        self.is_repainting = True
        print("Color of your car {} is changed. It\'s {} now".format(self.model, self.base_color))

    def repainting_cabin(self, cabin_col):
        self.cabin_color = cabin_col
        self.is_repainting_cabin = True
        print("Color of your cabin car {} is changed. It\'s {} now". format(self.model, self.cabin_color))

    def repainting_doors(self, cabin_col, doors_col):
        self.doors_color = doors_col
        self.is_repainting_doors = True
        print("Color of your doors car {0} is changed. It\'s {1} now". format(self.model, self.doors_color))

    def car_info(self):
        print("\n\nInformation about your car:\nModel: {0}". format(self.model))
        if self.is_repainting:
            print("\nYour car is repainted: {}". format(self.base_color))
        if self.is_repainting_cabin:
            print("\nYour cabin car is repainted:\nCabin: {}". format(self.cabin_color))
        if self.is_repainting_doors:
            print("\nYour doors car is repainted:\nDoors: {}". format(self.doors_color))


class Truck(Car):
    cabin_color = 'White'
    doors_color = 'White'
    is_repainting_cabin = False
    is_repainting_doors = False

    def repainting(self, cabin_col):
        self.cabin_color = cabin_col
        self.is_repainting_cabin = True
        print("Color of your cabin car {} is changed. It\'s {} now".format(self.model, self.cabin_color))

    def service(self):
        self.service_is_complete = True
        print("\n\nYour truck has been serviced successfully!")
        print("\n1.Oil changed.\n2.Breaks is good.\n3.Wheels changed")


toyota = PassengerCar('Toyota RX-7', 'White')
toyota.repainting('Yellow')
toyota.repainting_cabin('Black')
toyota.car_info()

man = Truck('Man', 'Purple')
man.service()
man.repainting('Blue')
