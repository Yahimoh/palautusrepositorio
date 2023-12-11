class Matcher:
    def test(self, player):
        pass

class AllMatcher(Matcher):
    def test(self, player):
        return True

class PlaysInMatcher(Matcher):
    def __init__(self, team):
        self.team = team

    def test(self, player):
        return player.team == self.team

class HasAtLeastMatcher(Matcher):
    def __init__(self, value, attribute):
        self.value = value
        self.attribute = attribute

    def test(self, player):
        player_value = getattr(player, self.attribute)
        return player_value >= self.value

class HasFewerThanMatcher(Matcher):
    def __init__(self, value, attribute):
        self.value = value
        self.attribute = attribute

    def test(self, player):
        player_value = getattr(player, self.attribute)
        return player_value < self.value

class AndMatcher(Matcher):
    def __init__(self, matchers):
        self.matchers = matchers

    def test(self, player):
        return all(matcher.test(player) for matcher in self.matchers)

class QueryBuilder:
    def __init__(self):
        self.conditions = []

    def playsIn(self, team):
        self.conditions.append(PlaysInMatcher(team))
        return self

    def hasAtLeast(self, value, attribute):
        self.conditions.append(HasAtLeastMatcher(value, attribute))
        return self

    def hasFewerThan(self, value, attribute):
        self.conditions.append(HasFewerThanMatcher(value, attribute))
        return self

    def build(self):
        return AndMatcher(self.conditions)