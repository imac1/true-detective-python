import calendar
from datetime import datetime

# def is_twodigit_odd(number):
#     pass
is_twodigit_odd = lambda x: x % 2 != 0 and x % 10 != 1

print(is_twodigit_odd(25))


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    return all(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_owner, writable_by_others, writable_by_group, sudo_mode)
    pass


def is_leap_year(year):
    return calendar.isleap(year)
    pass


def is_sunday(day, weekday_of_first):
    return datetime.today(day).weekday()
    pass


def should_bring_umbrella(rains, wind_scale, cloudy, 
red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    return all(rains, wind_scale >= 7, cloudy, red_sky, strong_flower_smell, 
    spiders_down, lying_cattle, strong_sunshine)
    pass


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    pass