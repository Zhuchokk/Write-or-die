from abc import ABCMeta, abstractmethod


class ITkinterInterface(object):
    """Visual interface to configure the program
    Settings:
    allowable_time - Allowed inactivity time (in minutes)
    selected_pakosti -The tricks the program will use
    timeout - Timeout between shenanigans (in minutes)
    """

    @abstractmethod
    def save_pakosti(self):
        """Save all settings in the data.json"""
