# import datetime
#
#
# class MyTime:
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def __str__(self):
#         return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
#
#     def to_seconds(self):
#         return self.hours * 3600 + self.minutes * 60 + self.seconds
#
#     @classmethod
#     def from_seconds(cls, total_seconds):
#         hours = total_seconds // 3600
#         total_seconds %= 3600
#         minutes = total_seconds // 60
#         seconds = total_seconds % 60
#         return cls(hours, minutes, seconds)
#
#     def __sub__(self, other):
#         seconds1 = self.to_seconds()
#         seconds2 = other.to_seconds()
#         result_seconds = seconds1 - seconds2
#         if result_seconds < 0:
#             result_seconds = 0
#         return MyTime.from_seconds(result_seconds)
#
#     def __mul__(self, other):
#         seconds = self.to_seconds()
#         result_seconds = seconds * other
#         return MyTime.from_seconds(result_seconds)
#
#     def __floordiv__(self, other):
#         seconds = self.to_seconds()
#         result_seconds = seconds // other
#         return MyTime.from_seconds(result_seconds)
#
#     def __mod__(self, other):
#         seconds = self.to_seconds()
#         result_seconds = seconds % other
#         return MyTime.from_seconds(result_seconds)
#
#     def __isub__(self, other):
#         result = self - other
#         self.hours = result.hours
#         self.minutes = result.minutes
#         self.seconds = result.seconds
#         return self
#
#     def __imul__(self, other):
#         result = self * other
#         self.hours = result.hours
#         self.minutes = result.minutes
#         self.seconds = result.seconds
#         return self
#
#     def __ifloordiv__(self, other):
#         result = self // other
#         self.hours = result.hours
#         self.minutes = result.minutes
#         self.seconds = result.seconds
#         return self
#
#     def __imod__(self, other):
#         result = self % other
#         self.hours = result.hours
#         self.minutes = result.minutes
#         self.seconds = result.seconds
#         return self
#
#
# c1 = MyTime(0, 10, 0)
# c2 = MyTime(0, 3, 20)
#
# print(f"c1: {c1}")
#
# print(f"c1 - c2: {c1 - c2}")
# print(f"c1 * c2: {c1 * 3}")
# print(f"c1 // c2: {c1 // 3}")
# print(f"c1 % c2: {c1 % 3}")
#
# c3 = MyTime(0, 10, 0)
# c4 = MyTime(0, 3, 20)
#
# c3 -= c4
# print(f"c1 -= c2: {c3}")
#
# c3 = MyTime(0, 10, 0)
# c3 *= 3
# print(f"c1 *= c2: {c3}")
#
# c3 = MyTime(0, 10, 0)
# c3 //= 3
# print(f"c1 //= c2: {c3}")
#
# c3 = MyTime(0, 10, 0)
# c3 %= 3
# print(f"c1 %= c2: {c3}")


class MyTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        total_seconds %= 3600
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)

    def __sub__(self, other):
        seconds1 = self.to_seconds()
        seconds2 = other.to_seconds()
        result_seconds = seconds1 - seconds2
        if result_seconds < 0:
            result_seconds = 0
        return MyTime.from_seconds(result_seconds)

    def __mul__(self, other):
        seconds = self.to_seconds()
        result_seconds = seconds * other
        return MyTime.from_seconds(result_seconds)

    def __floordiv__(self, other):
        seconds = self.to_seconds()
        result_seconds = seconds // other
        return MyTime.from_seconds(result_seconds)

    def __mod__(self, other):
        seconds = self.to_seconds()
        result_seconds = seconds % other
        return MyTime.from_seconds(result_seconds)

    def __isub__(self, other):
         result = self - other
         self.hours = result.hours
         self.minutes = result.minutes
         self.seconds = result.seconds
         return self

    def __imul__(self, other):
        result = self * other
        self.hours = result.hours
        self.minutes = result.minutes
        self.seconds = result.seconds
        return self

    def __ifloordiv__(self, other):
        result = self // other
        self.hours = result.hours
        self.minutes = result.minutes
        self.seconds = result.seconds
        return self

    def __imod__(self, other):
        result = self % other
        self.hours = result.hours
        self.minutes = result.minutes
        self.seconds = result.seconds
        return self
    def __gt__(self, other):
        return self.to_seconds() > other.to_seconds()

    def __ge__(self, other):
        return self.to_seconds() >= other.to_seconds()

    def __lt__(self, other):
        return self.to_seconds() < other.to_seconds()

    def __le__(self, other):
        return self.to_seconds() <= other.to_seconds()

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

    def __ne__(self, other):
        return self.to_seconds() != other.to_seconds()


c1 = MyTime(0, 10, 0)
c3 = MyTime(0, 15, 0)

print(f"c3 > c1 {c3 > c1}")
print(f"c3 >= c1 {c3 >= c1}")
print(f"c3 < c1 {c3 < c1}")
print(f"c3 <= c1 {c3 <= c1}")
