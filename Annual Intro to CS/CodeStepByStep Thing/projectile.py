import math

def projectile():
    print("This program computes the trajectory of a projectile given")
    print("its initial velocity and angle relative to the horizontal.")
    print("")

    x, y, t = 0, 0, 0
    v = int(input("Velocity  (m/s)? "))
    theta = int(input("Angle (degrees)? "))
    s = int(input("Number of steps? "))

    print()
    print(f"{'step':<8}{'x':<8}{'y':<8}{'time':<8}")
    print("----------------------------")

    theta_radians = math.radians(theta)
    vx = round(v * math.cos(theta_radians), 4)
    vy = round(v * math.sin(theta_radians), 4)
    
    print(f"{0:<8}{0:<8.2f}{0:<8.2f}{0:<8.2f}")

    total_time = (2 * vy) / 9.81
    dt = total_time / s

    for i in range(s):
        t += dt
        x = vx * t
        y = abs(vy * t + 0.5 * -9.81 * t * t)
        print(f"{i+1:<8}{x:<8.2f}{y:<8.2f}{t:<8.2f}")
        

def hi():
    return "hi"

def six_seven():
    return 67

projectile()