"""
Write a function named add_time that takes in two required parameters and one optional parameter:

- a start time in the 12-hour clock format (ending in AM or PM)
- a duration time that indicates the number of hours and minutes
- (optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.
"""

def get_individual_numbers(start, duration):
    start_time, start_period = start.split()
    start_hour, start_minute = start_time.split(':')
    duration_hour, duration_minute = duration.split(':')

    return start_period, start_hour, start_minute, duration_hour, duration_minute

def add_time(start, duration, day=None):

    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    # Unpacking individual numbers
    start_period, start_hour, start_minute, duration_hour, duration_minute = get_individual_numbers(start, duration)
    
    # Getting new hour and new minute
    new_hour = int(start_hour) + int(duration_hour)
    new_minute = int(start_minute) + int(duration_minute)

    # Verifying and correcting if new_minute is over 59
    if new_minute > 59:
        new_hour = new_hour + (int(new_minute/60))
        while new_minute > 59:
            new_minute = new_minute - 60

    if new_hour >= 12:
        if start_period == 'AM':
            start_period = 'PM'
        else:
            start_period = 'AM'

    # Verifying and correcting if new_hour is over 12
    if new_hour > 12:
        new_hour = new_hour - 12
    
    # Verifying and correcting if new_minute is under 10
    if new_minute < 10:
        new_minute = f"0{new_minute}"

    if day:
        return f"{new_hour}:{new_minute}{' ' + start_period}, {day}"
    else:
        return f"{new_hour}:{new_minute}{' ' + start_period}"

print(add_time('3:00 PM', '3:10'))
# Returns: 6:10 PM

print(add_time('11:30 PM', '2:32', 'Monday'))
# Returns: 2:02 AM, Monday (next day)

print(add_time('11:43 AM', '00:20'))
# Returns: 12:03 PM
