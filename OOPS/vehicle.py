class Vehicle:
    def start(self):
        print("vehicle start method")

    def accelerate(self):
        print("vehicle accelerate method")


class Swift(Vehicle):
    pass

swift_instance=swift()
swift_instance.accelerate()
swift_instance.start()