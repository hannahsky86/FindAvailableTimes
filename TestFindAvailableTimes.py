import sys
sys.path.append("..")
from unittest import TestCase
import FindAvailableTimes as fats


class TestFindAvailableTimes(TestCase):

    def test_truhearing_base_case(self):

        # Assign
        day_start_time = '8:30'
        day_end_time = '5:00'

        lunch_start_time = '12:00'
        lunch_end_time = '1:00'

        unavailable_times = [
            ['9:00', '9:30'], ['9:00', '11:30'], ['10:00', '11:00'], ['2:30', '3:00'], ['2:30', '3:30'],
            [lunch_start_time, lunch_end_time]
        ]

        # Act
        available_times = fats.FindAvailableTimes(day_start_time, day_end_time, unavailable_times).team_availability()

        # Assert
        self.assertTrue(available_times == [['8:30', '9:00'], ['11:30', '12:00'], ['1:00', '1:30'], ['1:30', '2:00'],
                                            ['2:00', '2:30'], ['3:30', '4:00'], ['4:00', '4:30'], ['4:30', '5:00']])

    def test_unavailable_time_overlaps_entire_day(self):

        # Assign
        day_start_time = '8:30'
        day_end_time = '5:00'
        unavailable_times = [['8:00', '6:00']]

        # Act
        available_times = fats.FindAvailableTimes(day_start_time, day_end_time, unavailable_times).team_availability()

        # Assert
        self.assertTrue(available_times == [])

    def test_unavailable_time_overlaps_day_start_time(self):

        # Assign
        day_start_time = '8:30'
        day_end_time = '5:00'
        unavailable_times = [['8:00', '4:30']]

        # Act
        available_times = fats.FindAvailableTimes(day_start_time, day_end_time, unavailable_times).team_availability()

        # Assert
        self.assertTrue(available_times == [['4:30', '5:00']])

    def test_unavailable_time_overlaps_day_end_time(self):

        # Assign
        day_start_time = '8:30'
        day_end_time = '5:00'
        unavailable_times = [['9:00', '5:30']]

        # Act
        available_times = fats.FindAvailableTimes(day_start_time, day_end_time, unavailable_times).team_availability()

        # Assert
        self.assertTrue(available_times == [['8:30', '9:00']])

    def test_unavailable_time_overlaps_middle_of_day(self):

        # Assign
        day_start_time = '8:30'
        day_end_time = '5:00'
        unavailable_times = [['10:00', '4:30']]

        # Act
        available_times = fats.FindAvailableTimes(day_start_time, day_end_time, unavailable_times).team_availability()

        # Assert
        self.assertTrue(available_times == [['8:30', '9:00'], ['9:00', '9:30'], ['9:30', '10:00'], ['4:30', '5:00']])

    def test_unavailable_time_not_during_lunch(self):

        # Assign
        day_start_time = '8:30'
        day_end_time = '5:00'
        unavailable_times = [['8:30', '11:30'],['1:30', '5:30']]

        # Act
        available_times = fats.FindAvailableTimes(day_start_time, day_end_time, unavailable_times).team_availability()

        # Assert
        self.assertTrue(available_times == [['11:30', '12:00'], ['12:00', '12:30'], ['12:30', '1:00'], ['1:00', '1:30']])

    def test_check_if_times_are_available(self):

        # Assign
        day_start_time = '8:30'
        day_end_time = '5:00'
        unavailable_times = [['8:30', '11:30'],['1:30', '5:30']]
        times_to_check = [['9:00', '10:30'], ['11:30', '12:00'], ['2:00', '4:00']]

        # Act
        available_times = fats.FindAvailableTimes(day_start_time, day_end_time, unavailable_times, times_to_check).team_availability()

        # Assert
        self.assertTrue(available_times == [['11:30', '12:00']])
