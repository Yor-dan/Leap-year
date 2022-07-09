def greet():
    print("\nWelcome to Leap Year Program!\n\nCheck if a year is a leap year or not!")

def restart():
    response = input("\nCheck another year? (yes/no): ").lower()
    if response == "yes":
        is_leap()
    else:
        print("\nSee You next time!")

def is_leap():
    leap = False
    year = int(input("\nEnter a year: "))
    
    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        leap = False
    if year % 400 == 0:
        leap = True
    
    if leap:
        print("\n%d is a leap year" % (year))
    else:
        print("\n%d is not a leap year" % (year))

    restart()

greet()
is_leap()