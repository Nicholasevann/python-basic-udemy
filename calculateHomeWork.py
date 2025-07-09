def calculate_homework_average(grades):
    if not grades:
        return 0
    total = sum(grades.values())
    average = total / len(grades)
    return average
