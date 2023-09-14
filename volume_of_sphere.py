import math


def calculate_volume_of_sphere(radius):
    # Calculate the volume of a sphere using the formula: V = (4/3) * π * r^3
    volume = (4/3) * math.pi * radius**3
    return volume


# Compute and print the volume of spheres with radii 30 and 40
radius1 = 30
volume1 = calculate_volume_of_sphere(radius1)
print(
    f"The volume of a sphere with radius {radius1} is {volume1:.2f} cubic units.")

radius2 = 40
volume2 = calculate_volume_of_sphere(radius2)
print(
    f"The volume of a sphere with radius {radius2} is {volume2:.2f} cubic units.")
