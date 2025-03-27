from datetime import datetime
def stopwatch(start_time,end_time):
    """
    Returns the time elapsed between the start and the end time

    Parameters:
    start: time when stopwatch is started
    end: time when stopwatch is stopped

    Returns:
    Time between start and end time
    """
    return end-start

start_prompt = input("Type 'Start' to start the stopwatch: ")
start = datetime.now()

end_prompt = input("Type 'Stop' to stop the stopwatch: ")
end = datetime.now()

print(stopwatch(start,end))