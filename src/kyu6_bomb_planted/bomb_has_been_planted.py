# Gear up! We're going in!

BOMB = 'B'
COUNTER_TERRORIST = 'CT'
DEFUSE_KIT = 'K'

TIME_TO_DEFUSE_WITHOUT_KIT = 10
TIME_TO_DEFUSE_WITH_KIT = 5


def bomb_has_been_planted(m, time):
    bomb_x = None
    bomb_y = None
    counter_terrorist_x = None
    counter_terrorist_y = None
    defuse_kit_x = None
    defuse_kit_y = None

    for row_number, row in enumerate(m):
        if BOMB in row:
            bomb_x = row.index(BOMB)
            bomb_y = row_number
        if COUNTER_TERRORIST in row:
            counter_terrorist_x = row.index(COUNTER_TERRORIST)
            counter_terrorist_y = row_number
        if DEFUSE_KIT in row:
            defuse_kit_x = row.index(DEFUSE_KIT)
            defuse_kit_y = row_number

    distance_bomb_counter_terrorist = max(abs(bomb_x - counter_terrorist_x), abs(bomb_y - counter_terrorist_y))
    time_without_defuse_kit = TIME_TO_DEFUSE_WITHOUT_KIT + distance_bomb_counter_terrorist

    time_with_defuse_kit = time_without_defuse_kit
    if defuse_kit_x is not None and defuse_kit_y is not None:
        distance_bomb_defuse_kit = max(abs(defuse_kit_x - bomb_x), abs(defuse_kit_y - bomb_y))
        distance_defuse_kit_counter_terrorist = max(abs(defuse_kit_x - counter_terrorist_x), abs(defuse_kit_y - counter_terrorist_y))
        time_with_defuse_kit = TIME_TO_DEFUSE_WITH_KIT + distance_bomb_defuse_kit + distance_defuse_kit_counter_terrorist

    return time_without_defuse_kit <= time or time_with_defuse_kit <= time
