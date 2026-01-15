# pylint: skip-file
# noqa
#####################################################################
# Jan Berglund - more_4.3.py
#
# Veckouppgift 1
# Vecka 2, 8/1
#
# 4 Fler övningar - Lite mer avancerad nivå
#
# "3"
# Skriv ett program som talar om dagens datum.
#####################################################################


# ------------------------------
# 3a
# ------------------------------

from datetime import datetime
from datetime import date

print("\nExercise 4.3a")
#print("\nToday it is (date and time)", datetime.now())

print("\nToday it is (date)", date.today())

input("\nPress Enter to continue!")


# ------------------------------
# 3b
# ------------------------------
from datetime import timedelta

days_to_add = 7

date_today = date.today()

# Add 7 days
new_date = date_today + timedelta(days=days_to_add)

print("\n\nExercise 4.3b")
print("\nNew date:" , new_date , "after adding" , days_to_add , "days")

input("\nPress Enter to continue!")
