from typing import Callable, List

def question_01(test_funcs: List[Callable]):
    result_a = None
    result_b = None
    try:
        salary = 8000
        def printSalary():
            salary = 12000
            result_a = salary
            return result_a

        result_a = printSalary()
        result_b = salary

    except Exception:
        print("Something went wrong")


print(question_01())
