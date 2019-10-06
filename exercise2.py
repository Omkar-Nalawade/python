# Exercise #2:  An Aircraft Object
class aircraft:
    x = y = 0
    acc = 1

    def move_left(self):
        print("Moved Left")
        self.x = self.x-1

    def move_right(self):
        print("Moved Right")
        self.x = self.x+1

    def move_up(self):
        self.y = self.y+1
        print("Moved Up")

    def move_down(self):
        print("Moved Down")
        self.y = self.y-1

p = aircraft()
print("initial x-coordinate :", p.x)
print("initial y-coordinate :", p.y)
p.move_right()
p.move_up()
p.move_up()
p.move_left()
p.move_left()
p.move_up()
print("current x-coordinate :", p.x)
print("current y-coordinate :", p.y)
p.move_down()
p.move_down()
p.move_right()
p.move_down()
p.move_up()
print("final x-coordinate :", p.x)
print("final y-coordinate :", p.y)