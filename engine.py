from datetime import datetime
import time
__entities = []
# main entity, all objects inherit from this
class Entity():
    def __init__(self, x, y, sprite_index = -1):

        self.x = x;
        self.y = y;
        self.sprite_index = sprite_index;
        if (self.sprite_index != -1):
            self.visible = True;
        else:
            self.visible = false;
    begin_step(delta):
        self.delta = delta;
    # alarm keyboard and mouse
    step(delta):
        self.delta = delta;
    # set instances to new positions
    # collisions
    end_step(delta):
        self.delta = delta;
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