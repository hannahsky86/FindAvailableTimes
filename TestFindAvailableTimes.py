import sys
sys.path.append("..")
from unittest import TestCase
import FindAvailableTimes as fats


class TestFindAvailableTimes(TestCase):
    #
    # def test1(self):
    #
    #     # Assign
    #     day_start_time = '8:30'
    #     day_end_time = '5:30'
    #
    #     # lunch_start_time = '12:00'
    #     # lunch_end_time = '1:00'
    #
    #     unavailable_times = [['9:00', '5:00']]
    #                          # [lunch_start_time, lunch_end_time]]
    #
    #     find = fats.FindAvailableTimes(day_start_time, day_end_time, unavailable_times)
    #
    #
    #     #Act
    #     available_times = find.team_availability()
    #     print(available_times)
    #
    #
    #     # Assert
    #     self.assertTrue(available_times == [['8:30', '9:00'], ['5:00', '5:30']])

    def test2(self):

        # Assign
        day_start_time = '8:30'
        day_end_time = '5:30'

        # lunch_start_time = '12:00'
        # lunch_end_time = '1:00'

        unavailable_times = []
                             # [lunch_start_time, lunch_end_time]]

        find = fats.FindAvailableTimes(day_start_time, day_end_time, unavailable_times)


        #Act
        available_times = find.team_availability()
        # print(available_times)


        # Assert
        # self.assertTrue(available_times == [['8:30', '9:00'], ['5:00', '5:30']])
