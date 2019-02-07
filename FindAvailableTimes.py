from collections import defaultdict
from operator import itemgetter
import sys


class FindAvailableTimes:

    def __init__(self, day_start, day_end, busy_intervals, times_to_check):
        self.day_start = day_start
        self.day_end = day_end
        self.busy_intervals = busy_intervals
        self.times_to_check = times_to_check

    def team_availability(self):
        """Creates a list of times, in half hour increments, when all team members are available."""

        day_start = time_to_number(self.day_start)
        day_end = time_to_number(self.day_end)
        busy_intervals = self.busy_intervals
        times_to_check = self.times_to_check

        formatted_busy_intervals = format_list_of_times(busy_intervals, is_number_format=True)
        busy_times_list = unavailable_time_and_duration(formatted_busy_intervals)
        busy_times_list = sorted(busy_times_list, key=itemgetter(0))

        first_busy_start_time, _ = busy_times_list[0]
        if first_busy_start_time < day_start:
            day_start = first_busy_start_time

        available_times_list = []
        available_times(day_start, day_end, busy_times_list, available_times_list)

        times_to_check = format_list_of_times(times_to_check, is_number_format=True)

        ok_times = check_available_times(times_to_check, available_times_list)
        ok_times = format_list_of_times(ok_times)

        available_time_intervals = format_list_of_times(available_times_list)

        return ok_times, available_time_intervals


def check_available_times(times_to_check, available_times_list):
    """Check for available times."""

    ok_time_intervals = []
    for start, end in times_to_check:
        for a_start, a_end in available_times_list:
            if start >= a_start and end<=a_end:
                ok_time_intervals.append([start, end])
                break

    return ok_time_intervals

def available_times(day_start, day_end, unavailable_times_list, available_times_list):
    """Recursive method to find all available times during the work day."""

    for bs, be in unavailable_times_list:

        if day_start == bs:
            day_start = be
            break

    if day_start < day_end:
        available_times_list.append([(day_start), (day_start + 30)])
        available_times(day_start+30, day_end, unavailable_times_list, available_times_list)


def format_list_of_times(intervals, is_number_format=False):
    """Changes format of date intervals to number or time format"""

    formatted_intervals = []
    if intervals!=[None] and(len(intervals)) > 0:
        for start, end in intervals:
            if is_number_format:
                formatted_intervals.append([time_to_number(start), time_to_number(end)])
            else:
                formatted_intervals.append([number_to_time(start), number_to_time(end)])

    return formatted_intervals


def unavailable_time_and_duration(busy_intervals):
    """Create a list of busy times and duration of busy time"""

    busy_times = []
    busy_dict = defaultdict(list)

    for start, end in busy_intervals:

        duration = end - start
        busy_times.append((start, duration))
        busy_dict[start].append(duration)

    busy_time_and_duration_list = []
    for key, value in busy_dict.items():
        busy_time_and_duration_list.append([key, key+max(value)])

    return busy_time_and_duration_list


def number_to_time(time):
    """Convert number to a time string"""

    time = time/60.00
    if time >12:
        time -=12
    minutes = ':30' if int(time%1*60) == 30 else ':00'
    hours = '12' if int(time) == 0 else str(int(time))
    time_string = hours+minutes

    return time_string


def time_to_number(time):
    """Convert time string to a number."""

    hour = int(time[:time.index(":")]) * 60
    minute = int(time[-2:])
    time_number = hour + minute
    if hour < 8*60:
        time_number = hour+12*60+minute

    return time_number


if __name__ == "__main__":
    """Main method calls team availability."""

    day_start_time = '8:30'
    day_end_time = '5:00'

    lunch_start_time = '12:00'
    lunch_end_time = '1:00'

    # Story 1
    # unavailable_times = [
    #     ['9:00', '9:30'], ['9:00', '11:30'], ['10:00', '11:00'], ['2:30', '3:00'], ['2:30', '3:30'],
    #     ['9:00', '2:00'], [lunch_start_time, lunch_end_time]
    # ]

    # Story 2
    unavailable_times = [['9:00', '9:30'], ['9:00', '11:30'], ['10:00', '11:00'], ['2:30', '3:00'], ['2:30', '3:30']]
    check_times = [['9:00', '10:30'],['11:30', '12:00'], ['2:00', '4:00']]

    FindAvailableTimes(day_start_time, day_end_time, unavailable_times, check_times).team_availability()
