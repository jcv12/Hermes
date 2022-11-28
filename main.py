from datetime import datetime, timedelta



# ASCII design for Hermes
print("  _   _ ")                              
print(" | | | | ___ _ __ _ __ ___   ___  ___ ")
print(" | |_| |/ _ \ '__| '_ ` _ \ / _ \/ __| ")
print(" |  _  |  __/ |  | | | | | |  __/\__ \ ")
print(" |_| |_|\___|_|  |_| |_| |_|\___||___/ ")
print("                                       ")
print("Welcome to Hermes!")

flightDateString = str(input("What is the date of your departing flight(ddmmyyyy? "))
flightDateObj = datetime.strptime(flightDateString, "%d%b%Y")
officialFlightDate = flightDateObj.date()
print(officialFlightDate)
print("   ")

airline = input("What is the airline you will be traveling? ")
print(airline)
print("   ")

takeOffTimeString = str(input("What time is take off? "))
dateTimeOffObj = datetime.strptime(takeOffTimeString, "%H:%M")
officialTimeOff = dateTimeOffObj.time()
print(officialTimeOff)
print("   ")

# getting to airport time TO DO
