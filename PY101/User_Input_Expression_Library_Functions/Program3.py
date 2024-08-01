'''
Problem Statement:
Write a Python program which accepts the radius of a sphere and computes the volume.
What is the volume and surface area of a sphere? The volume of a sphere with radius r is 4/3 πr3 .
'''
print('\nCalculate Sphere_volume_surface_area.py\n')

#getting input for radius of sphere and typecasting the values.
radius= int(input("Radius of sphere (in cm): "))

#calculations and value of pi
p=22/7
volume=((4/3)* p *(radius**3))
surface_area= ( 4*p *(radius**2))

#output
print(f"\n The volume of sphere is {round(volume,3)} cm^3,\n and the surface area of sphere is {round(surface_area,3)} cm^2." )
print()