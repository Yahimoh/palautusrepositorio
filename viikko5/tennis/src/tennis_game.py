class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.draw_score(self.m_score1)

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.over_4()
        else:
            return self.jotain()
    
    def draw_score(m_score1, self):
        if m_score1 == 0:
            return "Love-All"
        elif m_score1 == 1:
            return "Fifteen-All"
        elif m_score1 == 2:
            return "Thirty-All"
        else:
            return "Deuce"
        
    def over_4(m_score1, m_score2, self):
        minus_result = m_score1 - m_score2

        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def jotain(self):
        temp_score = 0
        score = ""

        for i in range(1, 3):
            if i == 1:
                temp_score = self.m_score1
            else:
                score = score + "-"
                temp_score = self.m_score2

                if temp_score == 0:
                    return  score + "Love"
                elif temp_score == 1:
                    return score + "Fifteen"
                elif temp_score == 2:
                    return  score + "Thirty"
                elif temp_score == 3:
                    return score + "Forty"