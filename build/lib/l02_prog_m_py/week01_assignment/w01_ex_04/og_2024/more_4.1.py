# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - more_4.1.py
#
# Veckouppgift 1
# Vecka 2, 8/1
#
# 4 Fler övningar - Lite mer avancerad nivå
#
# 1a
# Det är ca 470 km mellan Stockholm och Göteborg.
# Skriv ett program som räknar ut hur lång tid det tar att köra från
# Stockholm till Göteborg.
# Du behöver fråga användaren hur fort man ska köra, i km/h.
#
# Notera att "1b" samt "1c" även dessa hanteras
#####################################################################


#import os


print("\nThis is 4:1a (also b and c further down)")
input("\nPress Enter to continue!")


# Basic start information from assignment
distance_km = 470 # Distance in km between Stockholm and Göteborg
distance_m = distance_km * 1000

# Ask for and save an integer in a variable, as km/h
# Throw ValueError if incorrect input, then try again
print("You will be asked to input your speed as km/h")
while True:
    try:
        user_speed_kmh = int(input("\nPlease enter speed as an integer,"
                               " range 30 to 120, then press enter: "))
        if user_speed_kmh < 30 or user_speed_kmh > 120:
            print("The selected speed", user_speed_kmh, "is not valid!")
            continue
        else:
            break
    except ValueError:
        print("Not an integer, please try again!")

print("\nYour selected speed was:", user_speed_kmh , "km/h")

# Convert km/h into m/s
user_speed_mps = user_speed_kmh / 3.6

# Calculate the time in seconds, minutes and hours
time_s = distance_m / user_speed_mps # seconds
time_m = time_s / 60 # minutes
time_h = time_m / 60 # hours

print("\nThe total time in seconds is" , time_s , "sec")
print("The total time in minutes is" , time_m , "min")
print("The total time in hours is" , time_h , "h")


input("\nPress Enter to continue!")
# Below would clear the terminal, if running in an actual terminal
# Does not work in PyCharm
#os.system('cls' if os.name == 'nt' else 'clear')


# Display a bit different using built-in feature
import time
time_format = time.strftime("%H:%M:%S", time.gmtime(time_s))
print("\nTime in different format:" , time_format , "(Hr:Min:Sec)")


input("\nPress Enter to continue!")
# Below would clear the terminal, if running in an actual terminal
# Does not work in PyCharm
#os.system('cls' if os.name == 'nt' else 'clear')


# Another way to get the values, more for "1c" of assignment
print("\nAnd yet another way to display the time!")

calc_hour = time_s // 3600 # h as the integral part of the quotient
print(int(calc_hour) , "h")

remaining_seconds = time_s % 3600
calc_min = remaining_seconds // 60
print(int(calc_min) , "min")

calc_sec = int(remaining_seconds % 60)
print(int(remaining_seconds % 60) , "sec")

print("\n1c:" , int(calc_hour) , "hours" , int(calc_min) ,
      "minutes" , calc_sec , "seconds")

input("\nPress Enter to continue!")
# Below would clear the terminal, if running in an actual terminal
# Does not work in PyCharm
#os.system('cls' if os.name == 'nt' else 'clear')
