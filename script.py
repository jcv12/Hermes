from datetime import datetime, timedelta

#todo: Make Hermes look pretty when starting
print("Hermes")

choice = int(input("Schedule(1) or Time Check(2) "))

# 1)Booking via email to the travel people

if choice == 1:
    print("Schedule a travel email")

    leaving = input("Leaving: ")
    home = input("Coming Back: ")

    print("Y", leaving, "-", home)

    print("Does this look Correct")
    print("Y", leaving, "-", home)
    final = int(input("Yes(1) or No(2) "))
    
    if final == 1:
        print("Confirming...")
#todo add a loading bar
    else:
        print("Start Over")
# Grab travel document
# Modify the travel document with my dates that I input
# go to my email
# type in email to travel team
# attach the text file and write in a text to send to them
# send the email
# todo: send confirmations to ayana, mother and father

# 2) Schedule of travels

if choice == 2:
    print("Flight Time Check")
    depart = str(input("Depart time: "))
    time_object = datetime.strptime(depart, '%H:%M')

    airport_timeObj = time_object - timedelta(hours = 2, minutes = 30)
    board_timeObj = time_object - timedelta(minutes = 30)
    arrive_time = airport_timeObj.strftime('%H:%M')
    board_time = board_timeObj.strftime('%H:%M')

    print("Get to the airport at: ", arrive_time)
    print("Boarding time: ", board_time)

# todo:figure out layovers
# todo:API states time zones