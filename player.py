from constants import *
from array import *

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
        stats[KILLS] = 0
        stats[DEATHS] = 0
        stats[CAPS] = 0
        stats[ASSISTS] = 0
        stats[DESTRUCTION] = 0
        stats[STABS] = 0
        stats[HEALING] = 0
        stats[DEFENSES] = 0
        stats[INVULNS] = 0
        stats[BONUS] = 0
        stats[DOMINATIONS] = 0
        stats[REVENGE] = 0
        stats[POINTS] = 0

        #statistic array for single life/arena
        roundStats[KILLS] = 0
        roundStats[DEATHS] = 0
        roundStats[CAPS] = 0
        roundStats[ASSISTS] = 0
        roundStats[DESTRUCTION] = 0
        roundStats[STABS] = 0
        roundStats[HEALING] = 0
        roundStats[DEFENSES] = 0
        roundStats[INVULNS] = 0
        roundStats[BONUS] = 0
        roundStats[DOMINATIONS] = 0
        roundStats[REVENGE] = 0
        roundStats[POINTS] = 0

        timesChangedCapLimit = 0

        lastKnownx=0
        lastKnowny=0

        humiliated=0
        
        #Sentries for Engies
        sentry = None