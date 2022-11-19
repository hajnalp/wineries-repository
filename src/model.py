from __future__ import annotations

from dataclasses import field,dataclass
from enum import Enum

@dataclass
class Winery:
    """
    Represents Wineries.
    """

    phone_number: str = field(hash=True)
    """phone number"""
    name: str = field(compare=False)
    """name of the winery"""
    location: str = field(compare=False)
    """location of the winery"""
    rating: Rating = field(compare=False,default_factory=lambda: Winery.Rating.UNKNOWN)
    """rating of the winery"""
    wines: list[Wine] = field(compare=False, repr=False, default_factory=lambda: [])
    """wines of the winery"""


    @dataclass
    class Wine:
        """
        Represents wines.
        """
        type: str = field(compare=False)
        """type of the wine"""
        vintage: int = field(compare=False)
        """year in which the wine was produced"""
        barcode: str = field(hash=True)
        """barcode of the wine"""

    class Rating(Enum):
        """
        Represents the rating of the winery.

        * UNKNOWN = "Unknown"
        * VERY_POOR = "Very Poor"
        * POOR = "Poor"
        * AVERAGE = "Average"
        * GOOD = "Good"
        * EXCELLENT = "Excellent"
        """

        UNKNOWN = "Unknown"
        VERY_POOR = "Very Poor"
        POOR = "Poor"
        AVERAGE = "Average"
        GOOD = "Good"
        EXCELLENT = "Excellent"
