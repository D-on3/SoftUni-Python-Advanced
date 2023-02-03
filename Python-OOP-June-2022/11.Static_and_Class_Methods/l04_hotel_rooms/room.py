class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    @staticmethod
    def can_take_room(is_taken, capacity, people):
        return not is_taken and capacity >= people

    def take_room(self, people):
        if not self.can_take_room(self.is_taken, self.capacity, people):
            return f"Room number {self.number} cannot be taken"
        self.guests += people
        self.is_taken = True

    def free_room(self):
        if not self.is_taken:
            return f"Room number {self.number} is not taken"
        self.is_taken = False
        self.guests = 0

