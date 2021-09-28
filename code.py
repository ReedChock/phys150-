from adafruit_circuitplayground import cp
import time
import math
cp.pixels.brightness = .05
grav = 9.80665


# while True:
    # x, y, z = cp.acceleration
    # r = int(abs(x / grav * 127))
    # g = int(abs(y / grav * 127))
    # b = int(abs(z / grav * 127))
    # cp.pixels.fill([r, g, b])
    # x_angle = math.asin(x / grav)*180/3.1415926535
    # y_angle = math.asin(y / grav)*180/3.1415926535
    # print((x_angle,y_angle))
    # time.sleep(.05)
while True:
    for i in [1,2,3,6,7,8]:
        x, y, z = cp.acceleration
        x_angle = math.asin(x / grav)*180/3.1415926535
        y_angle = math.asin(y / grav)*180/3.1415926535
#        if ((x_angle) > 50) or ((x_angle) < -50):
#            cp.pixels[i]=((0, 0, 0))
        if ((x_angle) > 15) or ((x_angle) < -15):
            cp.pixels[i]=((255, 0, 0))
        if ((x_angle) < 15) and ((x_angle) > -15):
            cp.pixels[i]=((255, 255, 255))
        if ((x_angle) < 2) and ((x_angle) > -2):
            cp.pixels[i]=((0, 255, 0))
        time.sleep(.00000)
        print((x_angle))

    for h in [0,4,5,9]:
        x, y, z = cp.acceleration
        x_angle = math.asin(x / grav)*180/3.1415926535
        y_angle = math.asin(y / grav)*180/3.1415926535
        if ((y_angle) > 15) or ((y_angle) < -15):
            cp.pixels[h]=((255, 0, 0))
        if ((y_angle) < 15) and ((y_angle) > -15):
            cp.pixels[h]=((255, 255, 255))
        if ((y_angle) < 2) and ((y_angle) > -2):
            cp.pixels[h]=((0, 255, 0))
        time.sleep(.00000)
