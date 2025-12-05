"""
Functions used for accessing data from JPL Ephemeris and calculating information to display
based on the data.
JPL Ephemeris are collections of data charting planet movements.
"""
import math
#Load JPL ephemeris that program is based around
from skyfield.api import load
from skyfield.framelib import ecliptic_frame
ephem = 'de430_1850-2150.bsp'

#store planet information in list
planets = load(ephem)  # ephemeris de430_1850-2150

#set the default time
ts = load.timescale()
the_time = ts.now()

#calculate the velocity at which a given planet is orbiting the barycenter of the solar system
#also convert it into the desired unit
def calc_velocity(planet_id, unit, t):
    if unit == "au":
        x, y, z = planets[planet_id].at(t).observe(planets[10]).velocity.au_per_d
        unit_f = "au/day"
    else:
        if unit == "km":
            x, y, z = planets[planet_id].at(t).observe(planets[10]).velocity.km_per_s
            unit_f = "km/s"            
        if unit == "mi":
            unit_f = "mi/s"
            x, y, z = planets[planet_id].at(t).observe(planets[10]).velocity.km_per_s
            x = x * 0.621371
            y = y * 0.621371
            z = z * 0.621371
    vel = (x ** 2 + y ** 2 + z ** 2) ** 0.5
        
    return f"{planet_names[planet_id]} is orbiting the barycenter of the Solar System at {vel:,.3f} {unit_f}"

#Calculate a planets angle from the barycenter on the ecliptic frame
#I don't think I wound up using this
def calc_barycenter_angle(planet_id, t):
    position = planets[planet_id].at(t)
    x, y, z = position.frame_xyz(ecliptic_frame).au
    angle = (180/math.pi) * math.atan2(y, x)
    return angle

#Calculate a planets angle from the sun on the ecliptic frame
def calc_sun_angle(planet_id, t):
    x, y, z = planets[10].at(t).observe(planets[planet_id]).frame_xyz(ecliptic_frame).au
    angle = (180/math.pi) * math.atan2(y, x)
    return angle
                                               
#Calculate the distance from one planet to another                                               
def calc_dist(planet_id1, planet_id2, unit, t):
    astrometric = planets[planet_id1].at(t).observe(planets[planet_id2])
    ra, dec, distance = astrometric.radec()
    if unit == "km":
        dist_f = '{:,.0f} km'.format(distance.km)
    elif unit == "mi":
        dist_f = '{:,.0f} mi'.format(distance.km * 0.621371)
    elif unit == "ls":
        dist_f = '{:,.0f} light-seconds'.format(distance.km * (1/299792))
    elif unit == "lm":
        dist_f = '{:,.0f} light-minutes'.format(distance.km * (1/(60*299792)))
    else:
        dist_f = '{:,.3f} au'.format(distance.au)    
    return dist_f


planet_names = ["","Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]

#Calculate the distance from the sun to a planet
def sun_dist(planet_id, unit, t):
    dist = calc_dist(planet_id, 10, unit, t)
    return f"{planet_names[planet_id]} is {dist} away from the Sun" 

#calculate the distances of a planet from all other planets and return it as input for a textbox
def planet_dists(planet_id, unit, t):
    dists = ""
    for i in range(1, 9):
        if i !=  planet_id:
            dist = calc_dist(planet_id, i, unit, t)            
            dists = dists + f"\n{planet_names[planet_id]} is {dist} away from {planet_names[i]}\n"
    return(f"Distances of {planet_names[planet_id]} from all planets: \n" + dists)


if __name__ == "__main__":
    print(calc_vel(1,"km", the_time))
    #print(planets)