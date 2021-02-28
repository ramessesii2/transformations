import matplotlib.pyplot as plt
import sys

def brnhms(x1, y1, x2, y2): 
    x_data = []
    y_data = []
    x_data.append(x1)
    y_data.append(y1)
    dx = abs(x2 - x1) 
    dy = abs(y2 - y1)  
    if (x2 > x1): 
        xs = 1
    else: 
        xs = -1
    if (y2 > y1): 
        ys = 1
    else: 
        ys = -1
  
    if (dx > dy):         
        p1 = 2 * dy - dx 
        while (x1 != x2): 
            x1 += xs 
            if (p1 >= 0): 
                y1 += ys 
                p1 -= 2 * dx 
            p1 += 2 * dy 
            x_data.append(x1)
            y_data.append(y1)
  
    elif (dy >= dx):        
        p1 = 2 * dx - dy 
        while (y1 != y2): 
            y1 += ys 
            if (p1 >= 0): 
                x1 += xs 
                p1 -= 2 * dy 
            p1 += 2 * dx 
            x_data.append(x1)
            y_data.append(y1)
    return (x_data,y_data)

def bres(a, b, c, d):
    # from dda_line_drawing import *
    # x, y = dda(2, 3, 10, 11)
    x, y = brnhms(a, b, c, d)
    for i in range( len(x)):
        print(f"x = {x[i]}  y = {y[i]}")
    plt.plot(
        x,
        y,
        color="green",
        linestyle="dashed",
        linewidth=2,
        marker="o",
        markerfacecolor="blue",
        markersize=8,
    )

    # setting x and y axis range
    plt.ylim(0, 50)
    plt.xlim(0, 48)

    # naming the x axis
    plt.xlabel("x - axis")
    # naming the y axis
    plt.ylabel("y - axis")

    # giving a title to my graph
    plt.title("Bresenham's Visualizer")

    # function to show the plot
    plt.show()



def ddaline(x0, y0, X, Y):
    dx = abs(X - x0)
    dy = abs(Y - y0)
    sx = (X - x0) // dx
    sy = (Y - y0) // dy
    x = [x0]
    y = [y0]
    if (dx) > (dy):
        steps = dx
    else:
        steps = dy
    prevx = x0
    prevy = y0
    for i in range(1, steps + 1):
        prevx = prevx + (dx / (steps) * sx)
        prevy = prevy + (dy / (steps) * sy)
        x.append(round(prevx, 1))
        y.append(round(prevy, 1))
    return (x, y)

def dda(a, b, c, d):
    # from dda_line_drawing import *
    # x, y = dda(2, 3, 10, 11)
    x, y = ddaline(a, b, c, d)
    for i in range( len(x)):
        print(f"x = {x[i]}  y = {y[i]}")
    plt.plot(
        x,
        y,
        color="green",
        linestyle="dashed",
        linewidth=2,
        marker="o",
        markerfacecolor="blue",
        markersize=8,
    )

    # setting x and y axis range
    plt.ylim(0, 50)
    plt.xlim(0, 48)

    # naming the x axis
    plt.xlabel("x - axis")
    # naming the y axis
    plt.ylabel("y - axis")

    # giving a title to my graph
    plt.title("DDA Visualizer")

    # function to show the plot
    plt.show()
# dda(3,2,7,6)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def solver(center, r):
    x = 0
    y = r
    p = 1 - r
    points = []
    points.extend(
        [
            (center.x, y + center.y),
            (center.x, -y + center.y),
            (y + center.x, x + center.y),
            (-y + center.x, x + center.y),
        ]
    )
    while x <= y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * x - 2 * y + 1
        if x > y:
            break
        points.extend(
            [
                (x + center.x, y + center.y),
                (-x + center.x, y + center.y),
                (x + center.x, -y + center.y),
                (-x + center.x, -y + center.y),
            ]
        )
        if x != y:
            points.extend(
                [
                    (y + center.y, x + center.x),
                    (-y + center.y, x + center.x),
                    (y + center.y, -x + center.x),
                    (-y + center.y, -x + center.x),
                ]
            )
    # points.sort(key=lambda x: x[0])
    points.sort(key=lambda i: 0 if i[1] == 0 else -1 / i[1])
    return points

def circle(c1, c2, r):
    x = list(map(lambda y: y[0], solver(Point(c1, c2), r)))
    y = list(map(lambda x: x[1], solver(Point(c1, c2), r)))
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel("x - axis")
    # naming the y axis
    plt.ylabel("y - axis")

    # giving a title to my graph
    plt.title("CIRCLE ")

    # function to show the plot
    # plt.show()
    plt.plot(
        x,
        y,
        color="green",
        linestyle="dashed",
        linewidth=2,
        marker="o",
        markerfacecolor="blue",
        markersize=8,
    )

    # setting x and y axis range
    plt.ylim(-61, 61)
    plt.xlim(-61, 61)

    # naming the x axis
    plt.xlabel("x - axis")
    # naming the y axis
    plt.ylabel("y - axis")

    # giving a title to my graph
    plt.title("Circle ")

    # function to show the plot
    plt.show()


def ellipse(rx, ry, xc, yc):
    x = 0
    y = ry

    # Initial decision parameter of region 1
    d1 = (ry * ry) - (rx * rx * ry) + (0.25 * rx * rx)
    dx = 2 * ry * ry * x
    dy = 2 * rx * rx * y

    # For region 1
    while dx < dy:

        # Print points based on 4-way symmetry
        print("(", x + xc, ",", y + yc, ")")
        print("(", -x + xc, ",", y + yc, ")")
        print("(", x + xc, ",", -y + yc, ")")
        print("(", -x + xc, ",", -y + yc, ")")

        # Checking and updating value of
        # decision parameter based on algorithm
        if d1 < 0:
            x += 1
            dx = dx + (2 * ry * ry)
            d1 = d1 + dx + (ry * ry)
        else:
            x += 1
            y -= 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d1 = d1 + dx - dy + (ry * ry)

    # Decision parameter of region 2
    d2 = (
        ((ry * ry) * ((x + 0.5) * (x + 0.5)))
        + ((rx * rx) * ((y - 1) * (y - 1)))
        - (rx * rx * ry * ry)
    )

    # Plotting points of region 2
    while y >= 0:

        # printing points based on 4-way symmetry
        print("(", x + xc, ",", y + yc, ")")
        print("(", -x + xc, ",", y + yc, ")")
        print("(", x + xc, ",", -y + yc, ")")
        print("(", -x + xc, ",", -y + yc, ")")

        # Checking and updating parameter
        # value based on algorithm
        if d2 > 0:
            y -= 1
            dy = dy - (2 * rx * rx)
            d2 = d2 + (rx * rx) - dy
        else:
            y -= 1
            x += 1
            dx = dx + (2 * ry * ry)
            dy = dy - (2 * rx * rx)
            d2 = d2 + dx - dy + (rx * rx)
