def calculate_duration(no_of_times,no_of_months):
    """
    This function calculates the time spent by a person to wash hands in minutes taken they wash their hands 21 seconds a time

    Parameters
    ---
    no_of_times - number of times a person washes hands in a day
    no_of_months - number of months the person follows this pattern

    Returns
    ---
    time_spent - time spent to wash hands in minutes and seconds
    """

    time_spent = (no_of_times * 21) * 30 * no_of_months
    time_spent_minutes = time_spent // 60
    time_spent_seconds = time_spent % 60

    return f"{time_spent_minutes} minutes and {time_spent_seconds} seconds"


no_of_times = 7
no_of_months = 9
print(calculate_duration(no_of_times,no_of_months))