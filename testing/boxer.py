# -*- coding: utf-8 -*-

import requests


class Boxer:
    """Contains Boxer info."""

    BAD_REQUEST_MESSAGE_UPCOMING_FIGHTS = "Couldn't get any upcoming fights! Bad request!"
    BAD_REQUEST_MESSAGE_STATISTICS = "Couldn't get any statistics! Bad request!"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.boxing_url = "https://boxingschedule.boxingsociety.com"

    @property
    def full_name(self):
        """Returns the full name."""
        return '{} {}'.format(self.first_name, self.last_name)

    def get_upcoming_fights(self, month):
        """Returns upcoming fights at specific month."""
        response = requests.get(
            "{0}/fights/{1}/{2}{3}".format(self.boxing_url, month, self.first_name, self.last_name))
        return response.text if response.ok else self.BAD_REQUEST_MESSAGE_UPCOMING_FIGHTS

    def get_statistics(self):
        """Returns statistics."""
        response = requests.get(
            "{0}/statistics/{1}{2}".format(self.boxing_url, self.first_name, self.last_name))
        return response.text if response.ok else self.BAD_REQUEST_MESSAGE_STATISTICS


# if __name__ == '__main__':
#     boxer = Boxer('', '')
#     boxer.get_upcoming_fights('55')
