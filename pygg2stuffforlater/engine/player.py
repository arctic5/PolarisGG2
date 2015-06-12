import constants

class Player:
    def __init__(self):
        object = -1
        team = TEAM_SPECTATOR
        player_class = CLASS_SCOUT
        socket = -1
        name = ""
        kicked = False
        stats = dict()
        roundStats = dict()
        #client setting stuff set to defaults
        queueJump = False

        #stat tracking array
        stats[constants.KILLS] = 0
        stats[constants.DEATHS] = 0
        stats[constants.CAPS] = 0
        stats[constants.ASSISTS] = 0
        stats[constants.DESTRUCTION] = 0
        stats[constants.STABS] = 0
        stats[constants.HEALING] = 0
        stats[constants.DEFENSES] = 0
        stats[constants.INVULNS] = 0
        stats[constants.BONUS] = 0
        stats[constants.DOMINATIONS] = 0
        stats[constants.REVENGE] = 0
        stats[constants.POINTS] = 0

        #statistic array for single life/arena
        roundStats[constants.KILLS] = 0
        roundStats[constants.DEATHS] = 0
        roundStats[constants.CAPS] = 0
        roundStats[constants.ASSISTS] = 0
        roundStats[constants.DESTRUCTION] = 0
        roundStats[constants.STABS] = 0
        roundStats[constants.HEALING] = 0
        roundStats[constants.DEFENSES] = 0
        roundStats[constants.INVULNS] = 0
        roundStats[constants.BONUS] = 0
        roundStats[constants.DOMINATIONS] = 0
        roundStats[constants.REVENGE] = 0
        roundStats[constants.POINTS] = 0

        timesChangedCapLimit = 0

        lastKnownx=0
        lastKnowny=0

        humiliated=0
        
        #Sentries for Engies
        sentry = -1