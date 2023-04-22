# có thể chứa tuple và nhiều phần tử khác nhưng không chứa được list và chính nó

set1= {5, 8, 9}
set2= {'String', 'tri', 69, 50, }
set3= set('hahahzxcsaqt')
print(set1, type(set1))
print(set2, type(set2))
print(set3, type(set3))

print((1, 2) in {(1, 2), 3})
# sử dụng (&) (-) (|) (^)  
print({3, 8, 8, 6, 7} & {7, 8})