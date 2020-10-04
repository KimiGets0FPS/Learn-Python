import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print(yesterday.strftime("%d"))
print(today.strftime("%d"))
print(tomorrow.strftime("%d"))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)