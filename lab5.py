from operator import index

from data import Time
from data import Point

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1: Time, time2: Time) -> float:
    sum_of_hours = time1.hour + time2.hour
    sum_of_minutes = time1.minute + time2.minute
    sum_of_seconds = time1.second + time2.second

    if sum_of_minutes >= 60:
        sum_of_hours += sum_of_minutes // 60
        sum_of_minutes = sum_of_minutes % 60

    if sum_of_seconds >= 60:
        sum_of_minutes += sum_of_seconds // 60
        sum_of_seconds = sum_of_seconds % 60

    sum_of_hours = sum_of_hours % 24

    sum_of_times = Time(sum_of_hours, sum_of_minutes, sum_of_seconds)
    return sum_of_times

# Part 4
def is_descending(list: list[float]) -> bool:
    for idx in range(len(list) - 1):
        if list[idx] < list[idx + 1]:
            return False
    else:
        return True
# Part 5
def largest_between (list: list[int], lower:int, upper:int) -> int:
    if lower > upper:
        return None

    largest_number = lower
    for idx in range(lower, upper + 1):
        if list[idx] > list[largest_number]:
            largest_number = list[idx]
    else:
        return largest_number

# Part 6
def furthest_from_origin(point: list[Point]) -> list:
    start = 0
    total_distance = point[0].x**2 + point[0].y**2
    for idx in range(len(point)):
        distance = point[indx].x**2 ++ point[indx].y**2
        if distance > total_distance:
            total_distance = distance
            start = index
            \\\

