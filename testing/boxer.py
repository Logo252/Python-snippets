# -*- coding: utf-8 -*-

import requests


class Boxer:
    BAD_REQUEST_MESSAGE_UPCOMING_FIGHTS = "Couldn't get any upcoming fights! Bad request!"
    BAD_REQUEST_MESSAGE_STATISTICS = "Couldn't get any statistics! Bad request!"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_upcoming_fights(self, month):
        response = requests.get(
            "https://boxingschedule.boxingsociety.com/fights/{}/{}{}".format(month, self.first_name, self.last_name))
        return response.text if response.ok else self.BAD_REQUEST_MESSAGE_UPCOMING_FIGHTS

    def get_statistics(self):
        response = requests.get(
            "https://boxingschedule.boxingsociety.com/statistics/{}{}".format(self.first_name, self.last_name))
        return response.text if response.ok else self.BAD_REQUEST_MESSAGE_STATISTICS
