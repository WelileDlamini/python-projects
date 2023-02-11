#Write a program called ‘coordinates.py’ to check if a set of six numbers is a pair of
#geographical/GPS coordinates or not, assuming the degrees/minutes/seconds form:
def is_gps_coordinate(coords):
    lat_deg, lat_min, lat_sec, lon_deg, lon_min, lon_sec = coords

    # check if the latittude degrees are within the range [-90,90]
    if not (-90 <= lat_deg <= 90):
        return False

    # check if the longitude degrees are within the range [-180,180]
    if not (-180 <= lon_deg <= 180):
        return False

    # check if the latitude minutes and seconds are within the range [0, 60]
    if not (0 <= lat_min <= 60) or not (0 <= lat_sec < 60):
        return False

    # check if the longitude minutes and seconds are within the range [0,60]
    if not(0 <= lon_min <= 60) or not (0 <= lon_sec < 60):
        return False
coords = [-90, 50, 30, 180, 50, 0]

if is_gps_coordinate(coords):
    print("The set of number is a pair of GPS coordinates")
else:
    print("The set of numbers is not a pair of GPS coordinates")
