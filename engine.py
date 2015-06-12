from datetime import datetime
import time
__entities = []
# main entity, all objects inherit from this
class Entity():
    def __init__(self, sprite_index = -1):
        __entities.append(self)
        self.id = len(__entities)
        self.x = 0.0
        self.y = 0.0
        self.hspeed = 0.0
        self.vspeed = 0.0
        self.sprite_index = sprite_index
        if (self.sprite_index != -1):
            self.visible = True
        else:
            self.visible = False
        self.delta = 1
    def begin_step(self, delta = delta_time):
        self.delta = delta;
    # alarm keyboard and mouse
    def step(self, delta = delta_time):
        self.delta = delta;
    # set instances to new positions
    # collisions
    def end_step(self, delta_time):
        self.delta = delta;
    def destroy(self, state):
        del __entities[self.id]

if __name__ == '__main__':
    time = -1
    while(True):
        now = datetime.now()
        if (time == -1):
            delta_time = now - now
        else:
            delta_time = now - time
        for (ent in __entities): ent.begin_step()
        for (ent in __entities): ent.step()
        for (ent in __entities): ent.end_step()
        time = now
        time.sleep(1/60)