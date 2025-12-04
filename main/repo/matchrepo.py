from main.IO.matchIO import MatchIO

class MatchRepository:
    def __init__(self):
        self.io = MatchIO()
        self.match = self.load_match()

    def load_match(self):
        rows = self.io.read_file()
        matches = []