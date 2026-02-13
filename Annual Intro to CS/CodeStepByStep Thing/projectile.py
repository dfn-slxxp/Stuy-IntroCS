def projectile(v, theta, s):
    x, y, t = 0
    v = int(input("Velocity  (m/s)? "))
    theta = int(input("Angle (degrees)? "))
    s = int(input("Number of steps? "))

    for i in range(s):
        t += 0.47
        