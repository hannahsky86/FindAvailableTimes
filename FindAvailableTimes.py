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

        formatted_busy_intervals = create_formatted_list_of_intervals(busy_intervals)
        unavailable_times_list = unavailable_time_and_duration(formatted_busy_intervals)
        unavailable_times_list = sorted(unavailable_times_list, key=itemgetter(0))

        first_st, _ = unavailable_times_list[0]
        if first_st < day_start:
            day_start = first_st

        available_times_list = []
        available_times(day_start, day_end, unavailable_times_list, available_times_list)
        formatted_intervals_to_check = create_formatted_list_of_intervals(times_to_check)

        ok_times = []
        ok_times.append(check_available_times(formatted_intervals_to_check, available_times_list))

        unformatted_ok_times = create_unformatted_list_of_intervals(ok_times)
        unformatted_available_times = create_unformatted_list_of_intervals(available_times_list)

        return unformatted_ok_times, unformatted_available_times


def check_available_times(times_to_check, available_times_list):

    for start, end  in times_to_check:
        for a_start, a_end in available_times_list:

            if start >= a_start and end<=a_end:
                return [start,end]


def available_times(day_start, day_end, unavailable_times_list, available_times_list):
    """Recursive method to find all available times during the work day."""

    for bs, be in unavailable_times_list:

        if day_start == bs:
            day_start = be
            break

    if day_start < day_end:
        available_times_list.append([(day_start), (day_start + 30)])
        available_times(day_start+30, day_end, unavailable_times_list, available_times_list)


def create_formatted_list_of_intervals(intervals):

    formatted_intervals = []
    if intervals != [None] and (len(intervals)) > 0:
        for start, end in intervals:
            formatted_intervals.append([time_to_number(start), time_to_number(end)])

    return formatted_intervals


def create_unformatted_list_of_intervals(intervals):

    unformatted_intervals = []
    if intervals!=[None] and(len(intervals)) > 0:
        for start, end in intervals:
            unformatted_intervals.append([number_to_time(start), number_to_time(end)])

    return unformatted_intervals



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

    # unavailable_times = [
    #     ['9:00', '9:30'], ['9:00', '11:30'], ['10:00', '11:00'], ['2:30', '3:00'], ['2:30', '3:30'],
    #     ['9:00', '2:00'], [lunch_start_time, lunch_end_time]
    # ]

    unavailable_times = [['9:00', '9:30'], ['9:00', '11:30'], ['10:00', '11:00'], ['2:30', '3:00'], ['2:30', '3:30']]
    times_to_check = [['9:00', '10:30'],['11:30', '12:00'], ['2:00', '4:00']]

    FindAvailableTimes(day_start_time, day_end_time, unavailable_times, times_to_check).team_availability()
