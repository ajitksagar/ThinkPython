from swampy.TurtleWorld import  *

world1 = TurtleWorld()
bob = Turtle()

print bob
for i in range(4):
    fd(bob,100)
    lt(bob)

wait_for_user()