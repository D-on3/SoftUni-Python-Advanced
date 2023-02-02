from room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        # self.guests = 0

    @property
    def guests(self):
        return sum([r.guests for r in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    @staticmethod
    def find_room(rooms, room_number):
        return [room for room in rooms if room_number == room.number][0]

    def take_room(self, room_number, people):
        room = self.find_room(self.rooms, room_number)
        return room.take_room(people)

    def free_room(self, room_number):
        room = self.find_room(self.rooms, room_number)
        return room.free_room()

    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(free_rooms)}\n" \
               f"Taken rooms: {', '.join(taken_rooms)}"
