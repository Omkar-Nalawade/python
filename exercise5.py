class aircraft:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print(self.x)
        print(self.y)

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

    inst=["instance1", "instance2", "instance3", "instance4", "instance5"]
    def inst_create(self):
        for i in range(len(inst)):
            if i==0: inst[i] = aircraft(0, 0)
            if i==1: inst[i] = aircraft(4, 8)
            if i==2: inst[i] = aircraft(10, 15)
            if i==3: inst[i] = aircraft(12, 20)
            if i==4: inst[i] = aircraft(18, 24)

    def final_coord(self):
        for i in range(len(inst)):
            print("\nAircraft [",i,"]")
            print("final X-coordinate :", inst[i].x)
            print("final Y-coordinate :", inst[i].y)

    def initial_coord(self):
        print("Making a new aircraft object:",i)
        print("initial X-coordinate :", inst[i].x)
        print("initial Y-coordinate :", inst[i].y)

    def directn(self):
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

class Boeing_747(aircraft):

    def __init__(self,x,y,x_d,y_d):
        self.x = x
        self.y = y
        self.x_d = x_d
        self.y_d = y_d


if __name__=='__main__':

    inst=["instance1", "instance2", "instance3", "instance4", "instance5"]
    for i in range(len(inst)):
        if i==0: inst[i] = Boeing_747(11, 11, 51, 58)
        if i==1: inst[i] = Boeing_747(11, 10, 59, 51)
        if i==2: inst[i] = Boeing_747(11, 15, 56, 56)
        if i==3: inst[i] = Boeing_747(5, 14, 64, 50)
        if i==4: inst[i] = Boeing_747(7, 9, 69, 59)

        inst[i].initial_coord()
        print("New Boeing 747 Object Has Just Been Iniitalized:", i)
        print("X-Coord:", inst[i].x_d)
        print("Y-Coord:", inst[i].y_d)
        inst[i].directn()
    inst[i].final_coord()