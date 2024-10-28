from data import Time


# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1: Time, time2: Time):
    sum_of_hours = time1.hour + time2.hour
    sum_of_minutes = time1.minute + time2.minute
    sum_of_seconds = time1.second + time2.second

    if sum_of_minutes >= 60:
        sum_of_hours += sum_of_minutes // 60
        sum_of_minutes = sum_of_minutes % 60


    sum_of_times = Time(sum_of_hours, sum_of_minutes, sum_of_seconds)
    return sum_of_times



# Part 4


# Part 5


# Part 6
