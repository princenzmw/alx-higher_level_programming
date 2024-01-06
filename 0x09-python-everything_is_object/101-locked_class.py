#!/usr/bin/python3

""" Locked class """


class LockedClass:
    """ this class is locked """

    __slots__ = ["first_name"]

    def __init__(self, first_name=None) -> None:
        """ locked class

        Args:
            first_name (str, optional): first name. Defaults to None.
        """
        self.first_name = first_name
