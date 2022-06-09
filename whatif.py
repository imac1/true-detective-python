


def is_twodigit_odd(number):
    number2 = str(number)
    if len(number2) == 2:
        if number % 2 != 0:
            return True
        else:
            return False
    else:
        return False

    pass

# print(is_twodigit_odd(25))

def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    if user.isdigit() and users_groups and file_owner and writable_by_owner and file_group and sudo_mode:
        return True
    else:
        return False
    pass


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 4 == 0:
        return True
    else: 
        return False
    pass


def is_sunday(day, weekday_of_first):
    if weekday_of_first == 'M':
        if day in [7, 14, 21, 28]:
            return True
        else:
            return False
    elif weekday_of_first == 'Tu':
        if day in [6, 13, 28, 27]:
            return True
        else:
            return False
    elif weekday_of_first == 'We':
        if day in [5, 12, 19, 26]:
            return True
        else:
            return False
    elif weekday_of_first == 'Th':
        if day in [4, 11, 18, 25]:
            return True
        else:
            return False
    elif weekday_of_first == 'Fr':
        if day in [3, 9, 17, 24]:
            return True
        else:
            return False
    elif weekday_of_first == 'Sa':
        if day in [2, 8, 16, 23]:
            return True
        else:
            return False
    elif weekday_of_first == 'Su':
        if day in [1, 7, 15, 22]:
            return True
        else:
            return False
    pass


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    if wind_scale <= 7:
        if rains and cloudy and red_sky and strong_flower_smell and spiders_down and lying_cattle and strong_sunshine:
            return True
        else: 
            return False
    else:
        return False
        
    pass


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    pass

