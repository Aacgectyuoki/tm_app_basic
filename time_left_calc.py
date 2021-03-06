import math

# totals the time
minutes = 1
hours = minutes*60
total_time = (24*hours)

# ask user how many hours and minutes they work
work = input("Will you work? ")
if (work == "yes" or work == "YES" or work == "yES" or work == "Yes"):
    work_hours = input("Type in how many hours you work: ")
    work_minutes = input("Type the remaining minutes you work: ")
    print("You work " + work_hours + " hours and " +  work_minutes + " minutes.")
    total_time = total_time - ((int(work_hours))*60 + int(work_minutes))
else:
    pass
print("")

# ask user how many hours and minutes the user travels a day
travel = input("Will you travel/commute anywhere today? ")
if (travel == "yes" or travel == "YES" or travel == "yES" or travel == "Yes"):
    travel_hours = input("Type in how many hours you travel: ")
    travel_minutes = input("Type the remaining minutes you travel: ")
    print("You travel " + travel_hours + " hours and " +  travel_minutes + " minutes.")
    total_time = total_time - ((int(travel_hours))*60 + int(travel_minutes))
else:
    pass
print("")

# ask user how many hours and minutes the user breakfasts a day
exercise = input("Will you exercise today? ")
if (exercise == "yes" or exercise == "YES" or exercise == "yES" or exercise == "Yes"):
    exercise_hours = input("Type in how many hours you exercise: ")
    exercise_minutes = input("Type the remaining minutes you exercise: ")
    print("You exercise " + exercise_hours + " hours and " +  exercise_minutes + " minutes.")
    total_time = total_time - ((int(exercise_hours))*60 + int(exercise_minutes))
else:
    pass
print("")

# ask user how many hours and minutes the user eats breakfast a day
breakfast = input("Will you have breakfast today? ")
if (breakfast == "yes" or breakfast == "YES" or breakfast == "yES" or breakfast == "Yes"):
    breakfast_hours = input("Type in how many hours you eat breakfast: ")
    breakfast_minutes = input("Type the remaining minutes you eat breakfast: ")
    print("You breakfast " + breakfast_hours + " hours and " +  breakfast_minutes + " minutes.")
    total_time = total_time - ((int(breakfast_hours))*60 + int(breakfast_minutes))
else:
    pass
print("")

# ask user how many hours and minutes the user eats lunch a day
lunch = input("Will you have lunch today? ")
if (lunch == "yes" or lunch == "YES" or lunch == "yES" or lunch == "Yes"):
    lunch_hours = input("Type in how many hours you eat lunch: ")
    lunch_minutes = input("Type the remaining minutes you eat lunch: ")
    print("You lunch " + lunch_hours + " hours and " +  lunch_minutes + " minutes.")
    total_time = total_time - ((int(lunch_hours))*60 + int(lunch_minutes))
else:
    pass
print("")

# ask user how many hours and minutes the user eats dinner a day
dinner = input("Will you have dinner today? ")
if (dinner == "yes" or dinner == "YES" or dinner == "yES" or dinner == "Yes"):
    dinner_hours = input("Type in how many hours you eat dinner: ")
    dinner_minutes = input("Type the remaining minutes you eat dinner: ")
    print("You dinner " + dinner_hours + " hours and " +  dinner_minutes + " minutes.")
    total_time = total_time - ((int(dinner_hours))*60 + int(dinner_minutes))
else:
    pass
print("")

# ask user how many times they will snack today
try:
    snack = int(input("How many times will you snack today? (Enter an integer): "))
    i = []
    count = 0
    for i in range(snack):
        count += 1
        snack_hours = input("Type in how many hours you eat snack #{}: ".format(count))
        snack_minutes = input("Type the remaining minutes you eat your snack #{}: ".format(count))
        print("")
        total_time = total_time - ((int(snack_hours))*60 + int(snack_minutes))
except ValueError:
    snack = 0

# ask user how many hours and minutes of sleep the user needs per night
try:
    sleep_hours = int(input("Type in how many hours you sleep you need per night: (Enter an integer) "))
    sleep_minutes = int(input("Type the remaining minutes you sleep you need per night: (Enter an integer) "))
    total_time = total_time - ((int(sleep_hours))*60 + int(sleep_minutes))
except ValueError:
    sleep = 0
    print("Do you even sleep?!")
print("")

# ask to name any other commitments they have
other_com = input("Are you going to do anything else today?: ")
while (other_com == "yes" or other_com == "YES" or other_com == "yES" or other_com == "Yes"):
    oc = input("What else are you going to do today?: ")
    other_com_hours = input("Type in how many hours you {}: ".format(oc))
    other_com_minutes = input("Type the remaining minutes you {}: ".format(oc))
    total_time = total_time - ((int(other_com_hours))*60 + int(other_com_minutes))
    other_com = input("Are you going to do anything else today?: ")
print("")

# print the results
if (total_time < 0):
    print("No more time")
else:
    print(str("\n") + str("Spare time left: ") + repr(math.floor(total_time/60)) + str(" hours, ") + repr(total_time%60) + str(" minutes"))
