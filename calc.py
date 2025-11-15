import math
from skyfield.api import load
from skyfield.framelib import ecliptic_frame
ephem = 'de430_1850-2150.bsp'
planets = load(ephem)  # ephemeris DE430
ts = load.timescale()
the_time = ts.now()


def calc_angle(planet_id,t):
    position = planets[planet_id].at(t)
    x, y, z = position.frame_xyz(ecliptic_frame).au
    angle = (180/math.pi) * math.atan2(y, x)
    return angle

def calc_dist(planet_id1, planet_id2, t):
    position1 = planets[planet_id1].at(t)
    x1, y1, z1 = position.frame_xyz(ecliptic_frame).au
    position2 = planets[planet_id2].at(t)
    x2, y2, z2 = position.frame_xyz(ecliptic_frame).au
if __name__ == "__main__":
    calc_dist(2, 2, the_time)