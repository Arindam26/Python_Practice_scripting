
class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return "Device : {} connected by {}".format(self.name, self.connected_by)

    def disconnect(self):
        self.connected = False
        print("Disconnected")
        return None


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return "{} {} pages remaining".format(super().__str__(), self.remaining_pages)

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        print("Printing {} pages".format(pages))
        self.remaining_pages -= pages


printer = Printer("Printer", 'USB', 500)
printer.print(20)
print(printer)
