# Exercise #1:  A Basic Aircraft

# Exercise 1, part 1
print("Part1")
aircrafts = {"x": 12, "y": 96}
print(aircrafts["x"])
print(aircrafts["y"])

# Exercise 1, part 2
print("\nPart 2")
def convert(list):
    s = [str(i) for i in list]
    res = int("".join(s))
    return (res)

fleet = {"aircraft1":{11:91},"aircraft2":{21:81},"aircraft3":{31:71},"aircraft4":{41:61},"aircraft5":{51:9}}
print("Aircraft number 1\n")
x1 = convert(list(fleet["aircraft1"].keys()))
y1 = convert(list(fleet["aircraft1"].values()))
print("x-coordinates = ",x1)
print("y-coordinates = ",y1)
print("Aircraft number 2\n")
x2 = convert(list(fleet["aircraft2"].keys()))
y2 = convert(list(fleet["aircraft2"].values()))
print("x-coordinates = ",x2)
print("y-coordinates = ",y2)
print("Aircraft number 3\n")
x3 = convert(list(fleet["aircraft3"].keys()))
y3 = convert(list(fleet["aircraft3"].values()))
print("x-coordinates = ",x3)
print("y-coordinates = ",y3)
print("Aircraft number 4\n")
x4 = convert(list(fleet["aircraft4"].keys()))
y4 = convert(list(fleet["aircraft4"].values()))
print("x-coordinates = ",x4)
print("y-coordinates = ",y4)
print("Aircraft number 5\n")
x5 = convert(list(fleet["aircraft5"].keys()))
y5 = convert(list(fleet["aircraft5"].values()))
print("x-coordinates = ",x5)
print("y-coordinates = ",y5)