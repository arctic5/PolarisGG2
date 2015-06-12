import entity

class Character(entity.MovingObject):
    def __init__(self, x, y):
        # self.x = x
        # self.y = y
        # self.hspeed = 0
        # self.vspeed = 0
        # self.gravity = 0
        
        # self.canDoublejump = 0
        # self.canCloak = 0
        # self.canBuild = 0
        # self.jumpStrength = 8
        # self.capStrength = 1
        
        # self.hp = 100
        # self.flamecount = 0
        # self.invisible = False
        # self.intel = False
        # self.taunting = False
        # self.doublejumpUsed = 0
        # self.ubered = 0
        # self.stabbing = 0
        # self.onCabinet = 0
        # self.wantToJump = False
        # self.timeUnscathed = 0
        # self.syncWrongness = 0

        self.keyState = 0;
        self.lastKeyState = 0;
        self.pressedKeys = 0;
        self.releasedKeys = 0;
        self.aimDirection = 0;
        self.netAimDirection = 0;
        self.aimDistance = 0;