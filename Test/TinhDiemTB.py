class Student:
    def __init__(self, math, literature, english):
        self.math = math
        self.literature = literature
        self.english = english

    def calculate_average(self):
        return (self.math + self.literature + self.english) / 3

    def is_excellent(self):
        if self.calculate_average() >= 8 and self.math >= 8 and self.literature >= 8 and self.english >= 6.5:
            return True
        return False

    def is_good(self):
        if self.is_excellent():
            return False
        if self.calculate_average() >= 6.5 and self.math >= 6.5 and self.literature >= 6.5 and self.english >= 5:
            return True
        return False

    def is_average(self):
        if self.is_excellent() or self.is_good():
            return False
        if self.calculate_average() >= 5 and self.math >= 5 and self.literature >= 5 and self.english >= 3.5:
            return True
        return False

    def is_weak(self):
        if self.is_excellent() or self.is_good() or self.is_average():
            return False
        if self.calculate_average() >= 3.5 and self.math >= 3.5 and self.literature >= 3.5 and self.english >= 2:
            return True
        return False

    def is_poor(self):
        if self.is_excellent() or self.is_good() or self.is_average() or self.is_weak():
            return False
        return True

math_score = float(input("Nhập điểm toán: "))
literature_score = float(input("Nhập điểm văn: "))
english_score = float(input("Nhập điểm Anh: "))

student = Student(math_score, literature_score, english_score)

if student.is_excellent():
    print("Học sinh giỏi")
elif student.is_good():
    print("Học sinh khá")
elif student.is_average():
    print("Học sinh trung bình")
elif student.is_weak():
    print("Học sinh yếu")
else:
    print("Học sinh kém")