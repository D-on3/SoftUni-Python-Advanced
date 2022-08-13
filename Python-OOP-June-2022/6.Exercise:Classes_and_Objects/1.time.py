class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.time = [hours, minutes, seconds]

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.time = [hours, minutes, seconds]

    def get_time(self):

        for idx, value in enumerate(self.time):
            if len(str(value)) <= 1:
                self.time[idx] = str(self.time[idx])
                self.time[idx] = f"0{self.time[idx]}"

        return f"{self.time[0]}:{self.time[1]}:{self.time[2]}"

    def next_second(self):
        self.time[2] += 1
        if self.time[2] > 59:
            self.time[2] = 0
            self.time[1] += 1
            if self.time[1] > 59:
                self.time[0] += 1
                self.time[1] = 0
                if self.time[0] > 23:
                    self.time[0] = 0

        return self.get_time()


time = Time(23, 59, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(9, 30, 59)
print(time.next_second())
