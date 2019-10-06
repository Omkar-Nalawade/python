# Exercise #3: Create a small fleet of Aircraft

class aircraft:
    x = y = 0
    acc = 1

    def move_left(self):
        self.x = self.x-1

    def move_right(self):
        self.x = self.x+1

    def move_up(self):
        self.y = self.y+1

    def move_down(self):
        self.y = self.y-1

inst=["instance1", "instance2", "instance3", "instance4", "instance5"]
for i in range(len(inst)):
    inst[i] = aircraft()
    print("Creating New Aircraft Object:",i)
    print("initial X-coordinate :", inst[i].x)
    print("initial Y-coordinate :", inst[i].y)

for i in range(len(inst)):
    if i==0:
        print("Aircraft Instance",i,"has moved down")
        inst[i].move_down()
        print("Aircraft Instance",i,"has moved left")
        inst[i].move_left()
        print("Aircraft Instance",i,"has moved down")
        inst[i].move_down()
        print("Aircraft Instance",i,"has moved left")
        inst[i].move_left()

    if i==1:
        print("Aircraft Instance",i,"has moved down")
        inst[i].move_down()
        print("Aircraft Instance",i,"has moved left")
        inst[i].move_left()
        print("Aircraft Instance",i,"has moved left")
        inst[i].move_left()

    if i==2:
        print("Aircraft Instance",i,"has moved down")
        inst[i].move_down()
        print("Aircraft Instance",i,"has moved left")
        inst[i].move_left()
        print("Aircraft Instance",i,"has moved down")
        inst[i].move_down()
        print("Aircraft Instance",i,"has moved right")
        inst[i].move_right()
        print("Aircraft Instance",i,"has moved right")
        inst[i].move_right()

    if i==3:
        print("Aircraft Instance",i,"has moved right")
        inst[i].move_right()
        print("Aircraft Instance",i,"has moved right")
        inst[i].move_right()
        print("Aircraft Instance",i,"has moved left")
        inst[i].move_left()
        print("Aircraft Instance",i,"has moved up")
        inst[i].move_up()

    if i==4:
        print("Aircraft Instance",i,"has moved right")
        inst[i].move_right()
        print("Aircraft Instance",i,"has moved right")
        inst[i].move_right()
        print("Aircraft Instance",i,"has moved up")
        inst[i].move_up()
        print("Aircraft Instance",i,"has moved left")
        inst[i].move_left()
        print("Aircraft Instance",i,"has moved up")
        inst[i].move_up()

for i in range(len(inst)):
    print("\nAircraft [",i,"]")
    print("final x-coordinate :", inst[i].x)
    print("final y-coordinate :", inst[i].y)