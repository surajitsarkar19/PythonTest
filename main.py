import person
from robot import Robot
from school import *
from person import Person
from iterator import PowTwo


p = Person("srs")
p.say_hi()
print(Person.msg)


# droid1 = Robot("R2-D2")
# droid1.say_hi()
# Robot.how_many()
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# Robot.how_many()
#
# print("\nRobots can do some work here.\n")
#
# print("Robots have finished their work. So let's destroy them.")
# droid1.die()
# droid2.die()
#
# Robot.how_many()

# t = Teacher('Mrs. Shrividya', 40, 30000)
# s = Student('Swaroop', 25, 75)
#
# # prints a blank line
# print
#
# members = [t, s]
# for member in members:
#     # Works for both Teachers and Students
#     member.tell()

for i in PowTwo(5):
    print(i)