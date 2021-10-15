from abc import ABCMeta, abstractmethod


class IPakosti(object):
    """Does dirty tricks on the user"""

    @abstractmethod
    def create_pakost(self, selected_pakosti=['backspace', 'звук', 'картинка', 'статья', 'клавиши']):
        """Random creater dirty tricks
        selected_pakosti - possible tricks"""