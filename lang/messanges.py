"""Messanges module."""


class Message:
    """Class for messages to user."""
    unauthorized = (
        'Only registered users can create a personal account and fully use the service.'
        ' Please register or login.'
    )
    success_register = 'You have successfully registered'
    error_register = 'Registration error'
    city_does_not_exist = 'Such city does not exist!'
    city_alredy_added = 'City has already added recently!'
    city_successfully_added = 'City has already added!'
    city_removed = 'City has already removed!'
