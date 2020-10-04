def homework_3():
    student_info = {"Class": {"Student": {"Name": "Mike", "Marks": {"Physics": 70, "History": 80}}}}
    student_grade = student_info["Class"]["Student"]["Marks"]["History"]
    print(f"\n{student_grade}")


homework_3()
