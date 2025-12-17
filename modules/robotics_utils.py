import math, random, time

class Motor:
    def __init__(self, name):
        self.name = name
        self.speed = 0

    def set_speed(self, speed):
        self.speed = speed
        return f"{self.name} motor speed set to {speed}"

    def stop(self):
        self.speed = 0
        return f"{self.name} motor stopped"

def forward_kinematics(theta1, theta2, l1=1.0, l2=1.0):
    x = l1 * math.cos(theta1) + l2 * math.cos(theta1 + theta2)
    y = l1 * math.sin(theta1) + l2 * math.sin(theta1 + theta2)
    return x, y

def line_follow_step():
    sensor = random.choice([0, 1, 2])
    if sensor == 0:
        return "Adjust left"
    elif sensor == 1:
        return "Adjust right"
    else:
        return "Go straight"