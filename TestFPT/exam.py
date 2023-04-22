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
        pass
    # Fill your answers here-------------------------
    # calculate result_a and result_b values
    your_answer_of_result_a = '12000'
    your_answer_of_result_b =  '8000'
    # End your answer--------------------------------

    # Your explanation
    # result_a nằm trong func printSalary nên giá trị là 12000
    # result_b không nằm trong prinSalary nên chỉ lấy giá trị gán phía trên nên có giá trị là 8000


def question_02(test_funcs: List[Callable]):
    result_equal_operation = None
    result_is_operation = None
    try:
        listOne = [20, 40, 60, 80]
        listTwo = [20, 40, 60, 80]

        result_equal_operation = (listOne == listTwo)
        result_is_operation = (listOne is listTwo)
    except Exception:
        pass

    # Fill your answers here-------------------------
    # calculate result values
    your_answer_of_result_equal_operation = 'True'
    your_answer_of_result_is_operation = 'False'
    # End your answer--------------------------------

    # Your explanation
    # result_equal_operation là kiểm tra giá trị gán của 2 list trả ra giá trị True và False
    # result_is_operation kiểm tra so sánh các đối tượng tham chiếu


def question_03(test_funcs: List[Callable]):
    result = None
    try:
        x = 100
        y = 50
        result = x and y
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result_a and result_b values
    your_answer_of_result = '50'
    # End your answer--------------------------------

    # Your explanation
    # Toán tử logic and cho ra kết quả 50
    #



def question_04(test_funcs: List[Callable]):
    result = None
    try:
        def outer_fun(a, b):
            def inner_fun(c, d):
                return c + d
            return inner_fun(a, b)
        result = outer_fun(5, 10)

    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = '15'
    # End your answer--------------------------------

    # Your explanation
    # từ outer_fun truyền tham số vào inner_fun sau đó inner_fun trả ra giá trị 15
    #


def question_05(test_funcs: List[Callable]):
    result = None
    try:
        x = 0
        for i in range(5):
            for j in range(-1, -5, -1):
                x += 1
        result = x
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = '20'
    # End your answer--------------------------------

    # Your explanation
    # cho vòng lặp j chạy từ -1 đến -4 bước nhảy -1 trong vòng lặp i từ 0 đến 4 và x + 1 mỗi lần tăng vòng lặp
    # kết quả giá trị cho ra cuối cùng là 20


def question_06(test_funcs: List[Callable]):
    result_a = None
    result_b = None
    result_c = None
    try:
        samples = [10, 20, 30, 40, 50, 60, 70, 80]
        result_a = samples[2:-2]
        result_b = samples[:4]
        result_c = samples[3:]
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer_of_result_a = '[30,40,50,60]'
    your_answer_of_result_b = '[10, 20, 30, 40]'
    your_answer_of_result_c = '[40, 50, 60, 70, 80]'
    # End your answer--------------------------------

    # Your explanation
    # slicing result_a chạy từ 2 (ký tự thứ 3) đến -2 (chạy ngược từ phải qua ký tự 3) có kết quả như trên
    # slicing result_b chạy từ 0 (không ghi gì được tính là ký tự đầu tiên) đến 4 (ký tự thứ 4)
    # slicing result_c chạy từ 3 (tính từ 0,1,2,3 ký tự thứ 4) chạy đến hết danh sách.

def question_07(test_funcs: List[Callable]):
    result = None
    try:
        sample = (5, 10, 15, 25)
        result = sample[::-2]
    except Exception:
        pass
    # Fill your answers here-------------------------
    # calculate result values
    your_answer = '(25,10)'
    # End your answer--------------------------------
    
    # Your explanation
    # slicing result [::-2] chạy hết danh sách với bước nhảy từ phải qua trái là 2


def question_08():
    pass
    """
    Create source code, upload to github.com
    Use Django, DjangoRestFramework

    Implement JWT authentication plugin
    Has 1 middleware to log to a file: total time to process a request/response
    Has an app
    Connect to 2 database (postgresql/mariadb/mysql) run in replication mode (1 master, 1 slave)
        create a db-router to write only to master database
                              read only from slave database
    Deploy with Gunicorn (3 concurrent workers)
    """
