#!python3
import turtle


class Koch:
    def __init__(self, speed=None, angle=60):
        self.t = turtle.Turtle()
        if speed:
            self.t.speed(speed)
        self.turn = 180-angle
        self.f = self.t.forward
        self.l = self.t.left
        self.r = self.t.right
        self.rlr = [(angle, self.r), (180-angle, self.l), (angle, self.r)]

    def move(self, layers, distance):
        if not layers:
            self.f(distance)
            return
        for angle, mv in self.rlr:
            self.move(layers-1, distance/3)
            mv(angle)
        self.move(layers-1, distance/3)

    def snowflake(self, layers, distance):
        for x in range(int(3)):
            self.move(layers, distance)
            self.l(self.turn)


			
if __name__ == "__main__":
	flake = Koch(-1)

	flake.snowflake(10, 500)

	input("Press enter to exit")
