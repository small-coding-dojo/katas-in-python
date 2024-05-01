# Gear up! We're going in!

BOMB = 'B'
COUNTER_TERRORIST = 'CT'
DEFUSE_KIT = 'K'

TIME_TO_DEFUSE_WITHOUT_KIT = 10
TIME_TO_DEFUSE_WITH_KIT = 5


def bomb_has_been_planted(m, time):
    bomb, counter_terrorist, defuse_kit = None, None, None

    # Locate bomb, counter terrorist and defuse kit
    for y, row in enumerate(m):
        if BOMB in row:
            bomb = (row.index(BOMB), y)
        if COUNTER_TERRORIST in row:
            counter_terrorist = (row.index(COUNTER_TERRORIST), y)
        if DEFUSE_KIT in row:
            defuse_kit = (row.index(DEFUSE_KIT), y)

    # Time needed without defuse kit
    time_required = TIME_TO_DEFUSE_WITHOUT_KIT + distance(bomb, counter_terrorist)

    # Time needed with defuse kit
    if defuse_kit:
        time_with_defuse_kit = (TIME_TO_DEFUSE_WITH_KIT
                                + distance(bomb, defuse_kit)
                                + distance(defuse_kit, counter_terrorist))
        time_required = min(time_required, time_with_defuse_kit)

    return time_required <= time


def distance(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))
