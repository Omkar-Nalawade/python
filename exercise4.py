class aircraft:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_left(self):
        print("moved left")
        self.x = self.x-1

    def move_right(self):
        print("moved right")
        self.x = self.x+1

    def move_up(self):
        self.y = self.y+1
        print("moved up")

    def move_down(self):
        print("moved down")
        self.y = self.y-1


if __name__=='__main__':

    inst=["instance1", "instance2", "instance3", "instance4", "instance5"]

    def directions():
        inst[i].move_right()
        inst[i].move_right()
        inst[i].move_up()
        inst[i].move_right()
        inst[i].move_left()
        inst[i].move_up()
        inst[i].move_up()
        inst[i].move_down()
        inst[i].move_up()
        inst[i].move_down()
        inst[i].move_up()
    def final_coord():
        for i in range(len(inst)):
            print("\nAircraft [",i,"]")
            print("final X-coordinate :", inst[i].x)
            print("final Y-coordinate:", inst[i].y)

    for i in range(len(inst)):
        if i==0: inst[i] = aircraft(0, 0)
        if i==1: inst[i] = aircraft(4, 8)
        if i==2: inst[i] = aircraft(8, 10)
        if i==3: inst[i] = aircraft(12, 14)
        if i==4: inst[i] = aircraft(18, 24)

        print("Making a new aircraft object:",i)
        print("initial X-coordinate :", inst[i].x)
        print("initial Y-coordinate :", inst[i].y)
        directions()

    final_coord()
