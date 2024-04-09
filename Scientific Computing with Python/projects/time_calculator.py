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
def round_up(num, duration_min, start_min):
    integer = int(num)
    
    if duration_min + start_min > 60:
        return True
    
    if num > integer:
        return True
    else:
        return False

def get_individual_numbers(start, duration):
    start_time, start_period = start.split()
    start_hour, start_minute = start_time.split(':')
    duration_hour, duration_minute = duration.split(':')

    return start_period, start_hour, start_minute, duration_hour, duration_minute

def add_time(start, duration, day=None):
    next_day = False
    added_days = 0
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    # Unpacking individual numbers
    start_period, start_hour, start_minute, duration_hour, duration_minute = get_individual_numbers(start, duration)
    
    # Getting new hour and new minute
    new_hour = int(start_hour) + int(duration_hour)
    new_minute = int(start_minute) + int(duration_minute)
    
    if new_minute > 59:
        while new_minute > 59:
            new_minute = new_minute - 60
            new_hour = new_hour + 1
    
    if new_hour > 24:
        need_to_round_up = round_up(int(duration_hour)/24, int(duration_minute), int(start_minute))
        
        while new_hour > 24:
            new_hour = new_hour - 24
            added_days += 1
            
        if need_to_round_up:
            added_days += 1
    
    if new_hour > 12 and start_period == 'PM':
        new_hour = new_hour - 12
        start_period = 'AM'
    elif new_hour > 12 and start_period == 'AM':
        new_hour = new_hour - 12
        start_period = 'PM'
    elif new_hour == 12 and start_period == 'AM':
        start_period = 'PM'
    elif new_hour == 12 and start_period == 'PM':
        start_period = 'AM'
        
    if new_minute < 10:
        new_minute = f"0{new_minute}"

    string_return = f"{new_hour}:{new_minute}{' ' + start_period}"

    if added_days == 1:
        string_return += ' (next day)'
    
    if added_days > 1:
        string_return += f" ({added_days} days later)"

    if day:
        return f"{string_return}, {day}"
    else:
        return string_return

# print(add_time('3:00 PM', '3:10'))  # Output: 6:10 PM
# print(add_time('11:30 AM', '2:32', 'Monday'))  # Output: 2:02 PM, Monday
# print(add_time('11:43 AM', '00:20'))  # Output: 12:03 PM
# print(add_time('10:10 PM', '3:30'))  # Output: 1:40 AM (next day)
# print(add_time('11:43 PM', '24:20', 'tueSday'))  # Output: 12:03 AM, Thursday (2 days later)
# print(add_time('6:30 PM', '205:12'))  # Output: 7:42 AM (9 days later)

# print(add_time('2:59 AM', '24:00'))
# Returns: 2:59 AM (next day)

# print(add_time('8:16 PM', '466:02', 'tuesday'))
# Returns: '6:18 AM, Monday (20 days later)'

print(add_time('11:55 AM', '3:12'))
# Returns: '3:07 PM'
