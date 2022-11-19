from abc import abstractmethod, ABC

from model import Winery


class Queries(ABC):
    """
    Defines queries deal with wineries.
    """

    @abstractmethod
    def count_of_excellent_wineries(self) -> int:
        """
        Returns the count of the Excellent rated wineries

        :return: the count
        """

    @abstractmethod
    def order(self)->list[Winery]:
        """
        Returns a copy of wineries ordered by:

        *the location of the wineries
        *the count of wines in descending order
        :return: the sorted list
        """

    @abstractmethod
    def phone_number(self,phone_num: str)->Winery:
        """
        Returns the name of the winery that belong to the given number.


        :param phone_num: the phone number
        :return: the name of the winery
        """

    @abstractmethod
    def count_of_white_wines(self)->int:
        """
        Returns the number of white wines.

        :return: the count
        """
    @abstractmethod
    def group_by_rating(self)->dict[Winery.Rating,list[Winery]]:
        """
        Groups the wineries by their ratings

        :return: the grouping
        """
