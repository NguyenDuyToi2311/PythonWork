a = input("Nhập set 1: ")
b = input("Nhập set 2: ")
st1 =  set(a.split(','))
st2 =  set(b.split(','))
print(st1)
print(st2)
print("")
def A_difference_B(set1, set2):
    dfr = set1 - set2
    print("Kết quả Set 1 - Set 2 là: ", dfr)
    return set1, set2
def B_difference_A(set1, set2):
    dfr = set2 - set1
    print("Kết quả Set 2 - Set 1 là: ", dfr)
    return set1, set2
def intersection(set1, set2):
    dfr = set1.intersection(set2)
    print("Kết quả Set 1 giao Set 2 là: ", dfr)
    return set1, set2
def union(set1, set2):
    dfr = set1.union(set2)
    print("Kết quả Set 1 hội Set 2 là: ", dfr)
    return set1, set2
def symmetric_difference(set1, set2):
    dfr = set1.symmetric_difference(set2)
    print("Kết quả Set 1 đối xứng Set 2 là: ", dfr)
    return set1, set2


A_difference_B(st1,st2)
B_difference_A(st1,st2)
intersection(st1,st2)
union(st1,st2)
symmetric_difference(st1,st2)