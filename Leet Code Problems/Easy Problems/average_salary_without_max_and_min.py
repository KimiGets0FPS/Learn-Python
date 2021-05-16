def average_salary(salary: list[int]) -> float:
    salary.sort()
    return (sum(salary)-salary[0]-salary[-1]) / (len(salary)-2)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
