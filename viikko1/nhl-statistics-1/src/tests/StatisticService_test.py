import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())
    
    def test_nimen_onnistunut_haku(self):
        pelaaja = self.stats.search("Semenko")

        self.assertEqual(pelaaja.name, "Semenko")
    
    def test_pelaajan_epäonnistunut_haku(self):
        pelaaja = self.stats.search("Messi")

        self.assertEqual(pelaaja, None)
    
    def test_tiimin_haku(self):
        tiimi = self.stats.team("EDM")

        self.assertEqual(tiimi[0].name, "Semenko")
    
    def test_top_points(self):
        top3 = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(top3[0].name, "Gretzky")

    def test_top_goals(self):
        top3 = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(top3[0].name, "Lemieux")

    def test_top_assists(self):
        top3 = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(top3[0].name, "Gretzky")       

            
        