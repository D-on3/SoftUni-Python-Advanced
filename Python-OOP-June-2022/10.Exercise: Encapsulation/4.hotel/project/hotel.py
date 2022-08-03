class Hotel:

    def __init__(self, name):
        self.name = name

        self.rooms = []

    @property
    def guests(self):
        return sum([r.guest for r in self.rooms])

    @classmethod
    def from_stars(cls, star_count):
        return cls(f"{star_count} stars Hotel")

    def add_room(self, rooms):
        self.rooms.append(rooms)

    def take_room(self, room_number, people):
        # at the end of the list : start from 0 index : [0]
        room = [r for r in self.rooms if r.number == room_number][0]
        return room.take_room(people)

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        return f"Hotel {self.name} has {self.guests} total guest\n"\
               f"Free rooms: {', '.join(free_rooms)}\n"\
               f"Taken rooms: {', '.join(taken_rooms)}"
