class TennisGame1:
    
    POINT = 1
    MATCHPOINT = 3

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
        score_notation = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }

        if self.player1_points == self.player2_points:
            if self.player1_points < self.MATCHPOINT:
                return score_notation[self.player1_points] + "-All"
            else:
                return "Deuce"   
        elif max(self.player1_points, self.player2_points) > self.MATCHPOINT:
            difference_score = self.player1_points - self.player2_points

            if abs(difference_score) > 1:
                return f'Win for {self._how_has_high_score()}'
            else:
                return f'Advantage {self._how_has_high_score()}'
        else:
            return f'{score_notation[self.player1_points]}-{score_notation[self.player2_points]}'

    def _how_has_high_score(self):
        if self.player1_points > self.player2_points:
            return self.player1_name
        else:
            return self.player2_name
