from src.score_notation import TennisScore


class TennisGame1:

    POINT = 1
    NUM_GAME_POINTS = 4

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += self.POINT
        else:
            self.player2_points += self.POINT

    def score(self):
        if self.player1_points == self.player2_points:
            if self.player1_points >= self.NUM_GAME_POINTS - 1:
                return "Deuce"
            else:
                return f"{TennisScore.get_score_name(self.player1_points)}-All"
        elif (
            max(self.player1_points, self.player2_points)
            >= self.NUM_GAME_POINTS
        ):
            difference_score = self.player1_points - self.player2_points

            if abs(difference_score) > 1:
                return f"Win for {self._how_has_high_score()}"
            else:
                return f"Advantage {self._how_has_high_score()}"
        else:
            return f"{TennisScore.get_score_name(self.player1_points)}-{TennisScore.get_score_name(self.player2_points)}"

    def _how_has_high_score(self):
        return (
            self.player1_name
            if self.player1_points > self.player2_points
            else self.player2_name
        )
