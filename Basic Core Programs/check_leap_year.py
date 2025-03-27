def check_leap_year(year):
    """
    Checks if the given year is a Leap Year or not

    Parameters:
    year: a integer 

    Returns:
    Invalid input if year has less than 4 digits, else tells if the year is leap year or not
    """
    if year<1000:
        print("Invalid Input")
        return


    if year % 400 == 0:
        print("Leap Year")
    elif year % 4 == 0 and year % 100 != 0:
        print("Leap Year")
    else:
        print("Not a Leap Year")


year = int(input())
check_leap_year(year)