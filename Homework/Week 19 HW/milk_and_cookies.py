from time import time
import holidays


def milk_and_cookies(date):
    north_america = holidays.CA()
    if north_america.get(time()) != 'Christmas':
        return "It's not the time for milk and cookies"
    else:
        return "It's the time for milk and cookies"


print(milk_and_cookies(time()))
