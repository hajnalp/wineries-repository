from __future__ import annotations

from itertools import chain
from typing import cast

from model import Winery
from queries import Queries
from common.repository import Repository


class Solution(Repository, Queries):

    @staticmethod
    def type_mapper(values: dict[str, any]) -> Winery | Winery.Wine:
        match values:
            case {"phone_number": _}:
                winery = Winery(**values)
                winery.rating = next(
                    Winery.Rating[entry.name]
                    for entry in Winery.Rating
                    if entry.value == winery.rating
                )
                return winery
            case {"barcode": _}:
                return Winery.Wine(**values)

    @property
    def entities(self) -> list[Winery]:
        return cast(list[Winery], super().entities)

    def count_of_excellent_wineries(self) -> int:
        return len(
            [
                winery
                for winery in self.entities
                if winery.rating == winery.rating.EXCELLENT
            ]
        )

    def order(self) -> list[Winery]:
        return sorted(
            self.entities,
            key=lambda winery: (winery.location,-len(winery.wines))
        )

    def phone_number(self, phone_num: str) -> Winery:
        return next(
            winery
            for winery in self.entities
            if winery.phone_number == phone_num
        )


    def count_of_white_wines(self) -> int:
        return len(
            [
                wines.type
                for wines in chain.from_iterable(
                [
                    winery.wines
                    for winery in self.entities

                ]

            )
            if wines.type == "White"
            ]
        )

    def group_by_rating(self) -> dict[Winery.Rating, list[Winery]]:
        return {
            rating: [
                winery
                for winery in self.entities
            ]
            for rating in {
                winery.rating
                for winery in self.entities
            }
        }


def main() -> None:
    repository = Solution(r"../data/wineries.json")

    for winery in repository.entities:
        print(winery)
    print("\n")
    print("_________________________"+"\nNumber of excellent wineries")
    print(Solution.count_of_excellent_wineries(repository))
    print("_________________________"+"\nWineries in order")
    print(Solution.order(repository))
    print("_________________________"+"\nWinery that belongs to the given phone number")
    print(Solution.phone_number(repository,"06 30 455 2855"))
    print("_________________________"+"\nThe count of white wines")
    print(Solution.count_of_white_wines(repository))
    print("_________________________"+"\nWineries grouped by their rating")
    print(Solution.group_by_rating(repository))





if __name__ == "__main__":
    main()
