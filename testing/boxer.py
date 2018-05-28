# -*- coding: utf-8 -*-

import requests


class Boxer:
    """Contains Boxer info."""

    BAD_REQUEST_MESSAGE_UPCOMING_FIGHTS = "Couldn't get any upcoming fights! Bad request!"
    BAD_REQUEST_MESSAGE_STATISTICS = "Couldn't get any statistics! Bad request!"
    BAD_REQUEST_MESSAGE_NEXT_OPPONENT = "Couldn't get next opponent info! Bad request!"

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self._boxing_url = "https://boxingschedule.boxingsociety.com"

    @property
    def first_name(self):
        """Returns the first name."""
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first name with given value."""
        self._first_name = first_name

    @property
    def full_name(self):
        """Returns the full name."""
        return '{} {}'.format(self.first_name, self._last_name)

    def get_upcoming_fights(self, month):
        """Returns upcoming fights at specific month."""
        response = requests.get(
            "{0}/fights/{1}/{2}{3}".format(self._boxing_url, month, self._first_name, self._last_name))
        return response.text if response.ok else self.BAD_REQUEST_MESSAGE_UPCOMING_FIGHTS

    def get_next_opponent(self):
        """Returns next opponent's info."""
        response = requests.get(
            "{0}/{1}{2}/next-opponent".format(self._boxing_url, self._first_name, self._last_name))
        return response if response is not None else self.BAD_REQUEST_MESSAGE_NEXT_OPPONENT

    def get_statistics(self):
        """Returns statistics."""
        response = requests.get(
            "{0}/statistics/{1}{2}".format(self._boxing_url, self._first_name, self._last_name))
        return response.text if response.ok else self.BAD_REQUEST_MESSAGE_STATISTICS

# if __name__ == '__main__':
#     boxer = Boxer('', '')
#     boxer.get_upcoming_fights('55')
