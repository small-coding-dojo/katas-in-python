# Gear up! We're going in!

BOMB = 'B'
COUNTER_TERRORIST = 'CT'
DEFUSE_KIT = 'K'

TIME_TO_DEFUSE_WITHOUT_KIT = 10
TIME_TO_DEFUSE_WITH_KIT = 5


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(a, b):
    return max(abs(a.x - b.x), abs(a.y - b.y))


def bomb_has_been_planted(m, time):
    bomb = None
    counter_terrorist = None
    defuse_kit = None

    # Locate the bomb, counter terrorist and defuse kit
    for row_number, row in enumerate(m):
        if BOMB in row:
            bomb = Coordinate(row.index(BOMB), row_number)
        if COUNTER_TERRORIST in row:
            counter_terrorist = Coordinate(row.index(COUNTER_TERRORIST), row_number)
        if DEFUSE_KIT in row:
            defuse_kit = Coordinate(row.index(DEFUSE_KIT), row_number)

    # Time needed without defuse kit
    distance_bomb_counter_terrorist = distance(bomb, counter_terrorist)
    time_without_defuse_kit = TIME_TO_DEFUSE_WITHOUT_KIT + distance_bomb_counter_terrorist

    # Time needed with defuse kit
    time_with_defuse_kit = time_without_defuse_kit
    if defuse_kit is not None:
        distance_bomb_defuse_kit = distance(bomb, defuse_kit)
        distance_defuse_kit_counter_terrorist = distance(defuse_kit, counter_terrorist)
        time_with_defuse_kit = TIME_TO_DEFUSE_WITH_KIT + distance_bomb_defuse_kit + distance_defuse_kit_counter_terrorist

    return time_without_defuse_kit <= time or time_with_defuse_kit <= time
