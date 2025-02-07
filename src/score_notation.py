from enum import Enum


class TennisScore(Enum):
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3

    @classmethod
    def get_score_name(cls, score):
        try:
            return cls(score).name.capitalize()
        except ValueError:
            raise ValueError(f"Invalid score value: {score}")
