def speed(distance, time):
    print("Formula=> Speed(Velocity) = Distance/Time")
    return distance/time

def distance(speed, time):
    print("Formula=> Distance = Speed(Velocity) * Time")
    return speed*time

def time(distance, speed):
    print("Formula=> Time = Distance/Speed(Velocity)")
    return distance/speed

def moment(force, distance):
    print("Formula=> Moment = Force * Distance")
    return force*distance

def kinetic(mass, speed):
    print("Formula=> Kinetic Engergy(KE) = 1/2 * Mass * Speed(Velocity)^2")
    return 0.5*mass*speed**2

def GPE(mass, gravity, height):
    print("Formula=> Gravitational Potential Energy(GPE) = Mass * Gravitational Field Strength(Newton(s)/Unit) * Height")
    return mass*gravity*height

def EPE(force, extension):
    print("Formula=> Elastic Potential Energy = 1/2 * Spring Constant(Newton(s)/Meter(s)) * Extenstion(Meter)^2")
    return 0.5*force*extension**2

def density(mass, volume):
    print("Formula=> Density = Mass/Volume")
    return mass/volume

def pressure(force, area):
    print("Formula=> Pressure = Force/Surface Area")
    return force/area

def acceleration(final, initial, time):
    print("Formula=> Acceleration = (Final Speed - Initial Speed)/Time")
    return (final - initial)/time

choices=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
print("Physics Formula Calculator By Kaung Myat Ko Ko")
while True:
    print('''
1. Speed           | 6.  | Gravitational Potential Energy
2. Distance        | 7.  | Elastic Potential Energy
3. Time            | 8.  | Density
4. Moment          | 9.  | Pressure
5. Kinetic Energy  | 10. | Acceleration
11. Quit           |  -  |     -
''')
    option=input("Please enter your option(1 to 11 only): ")
    if option not in choices:
        print("Not an option :(")
        continue
    elif option == '11':
        break
    elif option == '1':
        try:
            distance=float(input("Enter Distance: "))
            time=float(input("Enter Time: "))
            print(f"The Answer: {speed(distance,time)}")
        except:
            print("Please enter valid numbers!")
    elif option == '2':
        try:
            speed=float(input("Enter Speed: "))
            time=float(input("Enter Time: "))
            print(f"The Answer: {distance(speed,time)}")
        except:
            print("Please enter valid numbers!")
    elif option == '3':
        try:
            distance=float(input("Enter Distance: "))
            speed=float(input("Enter Speed: "))
            print(f"The Answer: {time(distance,speed)}")
        except:
            print("Please enter valid numbers!")
    elif option == '4':
        try:
            force=float(input("Enter Force: "))
            distance=float(input("Enter Distance: "))
            print(f"The Answer: {moment(force,distance)}")
        except:
            print("Please enter valid numbers!")
    elif option == '5':
        try:
            mass=float(input("Enter Mass: "))
            speed=float(input("Enter Speed: "))
            print(f"The Answer: {kinetic(mass,speed)}")
        except:
            print("Please enter valid numbers!")
    elif option == '6':
        try:
            mass=float(input("Enter Mass: "))
            gravity=float(input("Enter Gravity: "))
            height=float(input("Enter Height: "))
            print(f"The Answer: {GPE(mass,gravity,height)}")
        except:
            print("Please enter valid numbers!")
    elif option == '7':
        try:
            force=float(input("Enter Force: "))
            extension=float(input("Enter Extension: "))
            print(f"The Answer: {EPE(force,extension)}")
        except:
            print("Please enter valid numbers!")
    elif option == '8':
        try:
            mass=float(input("Enter Mass: "))
            volume=float(input("Enter Volume: "))
            print(f"The Answer: {density(mass,volume)}")
        except:
            print("Please enter valid numbers!")
    elif option == '9':
        try:
            force=float(input("Enter Force: "))
            area=float(input("Enter Area: "))
            print(f"The Answer: {pressure(force,area)}")
        except:
            print("Please enter valid numbers!")
    elif option == '10':
        try:
            final=float(input("Enter Final Speed: "))
            initial=float(input("Enter Initial Speed: "))
            time=float(input("Enter Time: "))
            print(f"The Answer: {acceleration(final,initial,time)}")
        except:
            print("Please enter valid numbers!")