# -*- coding: utf-8 -*-

import requests


class Boxer:

    def __init__(self, first_name, last_name, nationality):
        self.first_name = first_name
        self.last_name = last_name
        self.nationality = nationality

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_upcoming_fights(self, month):
        response = requests.get(
            "https://boxingschedule.boxingsociety.com/fights/{}/{}{}".format(month, self.first_name, self.last_name))
        if response.ok:
            return response.text
        else:
            return "Bad Response!"

    def get_statistics(self):
        response = requests.get(
            "https://boxingschedule.boxingsociety.com/statistics/".format(self.first_name, self.last_name))
        if response.ok:
            return response.text
        else:
            return "Bad Response!"
