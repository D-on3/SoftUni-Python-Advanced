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
        def conv_hours(hours):
            conv = hours % 24
            return conv

        def conv_minutes(minutes):
            conv = minutes % 60
            return conv

        if self.hours >= 24:
            self.hours = conv_hours(hours)
        if self.minutes > 60:
            self.hours += 1
            self.minutes = conv_minutes(minutes)
        if self.seconds > 60:
            self.minutes += 1
            self.seconds = conv_minutes(seconds)

    def get_time(self):

        # def conv_hours(hours):
        #     conv = hours % 24
        #     return conv
        #
        # def conv_minutes(minutes):
        #     conv = minutes % 60
        #     return conv

        # TODO: returns on the check
        # if self.hours > 24 or self.minutes > 59 or self.seconds > 59:
        #     self.hours = conv_hours(self.hours)
        #     if self.minutes > 59  or self.seconds > 59:
        #         self.hours += 1
        #         self.minutes = conv_minutes(self.minutes)
        #         if self.seconds > 59:
        #             self.minutes += 1
        #             self.seconds = conv_minutes(self.seconds)
        #             return self.seconds
        #         return self.minutes
        #     return self.hours

        if self.hours < 9 or self.minutes < 9 or self.seconds < 9:
            if self.minutes < 9 or self.seconds < 9:
                if self.seconds < 9:
                    return f"{self.hours}:{self.minutes}:0{self.seconds}"
                return f"{self.hours}:0{self.minutes}:{self.seconds}"
            return f"0{self.hours}:{self.minutes}:{self.seconds}"
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def next_second(self):
        self.seconds += 1
        self.check = self.get_time()
        self.acurracy = (self.hours * 60 * 60) + (self.minutes * 60) + self.seconds
        self.seconds = (self.acurracy % 60)
        self.minutes = (self.acurracy / 60) % 60
        self.hours = self.acurracy // 3600

        # if self.minutes >= 60:
        #     if
        #     self.minutes = self.
        #
        #


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())
