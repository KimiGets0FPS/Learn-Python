def student_names(students):
    """
    >>> student_names({96482:"Dream", 15548:"BadBoyHalo", 18545:"GeorgeNotFound"})
    ['Dream', 'BadBoyHalo', 'GeorgeNotFound']
    >>> student_names({48548:":\", 45865:":)", 54882:":|"})
    [':\', ':)', ':|']
    """
    student_list = []
    for student_num, student in students.items():
        student_list.append(student)
    return student_list


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
