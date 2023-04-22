import string
def vonglap():
    # vòng lặp for
    for letter in 'Python': # First Example
        print ('Current Letter :', letter)
    #-------------------------------------------------#
    fruits = ['banana','apple','mango']
    for fruit in fruits: # Second Example
        print ('Current fruit :', fruit )
    #-------------------------------------------------#
    print("Alphabet from a-z:")
    for letter in string.ascii_lowercase:
       print(letter, end = " "),
    #-------------------------------------------------#
    print("Alphabet from A-Z:")
    for letter in string.ascii_uppercase:
       print(letter, end = " "),
    #-------------------------------------------------#
    #vòng lặp While
    count = 0
    while count < 9:
        print(count)
        count = count + 1
    #-------------------------------------------------#


#tạo hàm và dùng hàm    
def sum(a, b):
    c = a + b
    return(c)


def chuoilist():
    str1 = "Baybyhahahahsaxxx"
    str2 = 'asdasda'
    #nối chuỗi
    kq = str1+ " "+ str2
    # lấy độ dài của chuỗi
    print (str1[-8:])
    print(kq)
    #-------------------------------------------------#
    #Đếm ký tự
    str1 = len('aslkdjlasdjasjdlasjdlasld')
    print('Chuỗi có độ dài là ', str1, ' ký tự')
    #-------------------------------------------------#
    #thay thế nội dung
    str = 'Hello world'
    newstr = str.replace('Hello','Bye')
    print (newstr)
    #-------------------------------------------------#
    # tìm vị trí chuỗi con có thể dùng find và rfind
    str = 'Hello world'
    print (str.find('world'))
    #(hiển thị 6)
    print (str.find('Bye'))
    #(hiển thị -1)
    # tách chuỗi
    str = 'Hello world'
    print (str.split(' '))
#-------------------------------------------------#
def sudungmang():
    num = [1, 2, 3, 4]
    mynu = num.pop()
    print(num)
    print ('Lấy phần từ cuối của mảng: ',mynu)
    #-------------------------------------------------#
    list = ['ok', 'baby', 'yeah']
    print('Kiểm tra giá trị có trong chuỗi xuất ra true và false')
    print ('a' in list)
    print ('b' not in list)
    #-------------------------------------------------#
    num = [0,8,6,4,8,3,1,2,5,4]
    print('Mảng:', num)
    del num[4]
    print('Xóa ở ký tự thứ 5: ',num)
    del num[1:3]
    print('Xóa ở ký tự thứ từ 2 đến 4: ',num)
    #-------------------------------------------------#
    List = [123,'xyz','zara','abc'];
    print(List)
    print (" xya nằm ở thứ tự : ", List.index('xyz'))
    print (" zara nằm ở thứ tự : ", List.index('zara'))
    #-------------------------------------------------#
    numbers = [1, 2, 3, 4]
    print(numbers)
    numbers.reverse()
    print ('Đảo ngược mảng: ', numbers)
    #-------------------------------------------------#
    tuple = ('x', 'y', 'z')
    list = ['x','y','z']
    print('Cấu trúc tuple: ', tuple, '\nCấu trúc List:', list)
    #-------------------------------------------------#
    point = {'x': 5, 'y': 8, 'b': 10}
    print(point)
    print ('Chọn đối tượng dựa trên key: ',point['b'])
    #-------------------------------------------------#
    user = {'name': 'Jone','age': 30}
    user['country'] = 'Vietnam'
    print(user)
    print ('',user)
#-------------------------------------------------#

def cacphuongthuc():
    # Phương thức thông dụng
    user = {'x': 5, 'y': 8, 'b': 10}
    value = 'Pro'
    #-------------------------------------------------------------------------------------------------------------#
    haha = dict.keys(user)                  # trả về list chứa các khóa
    baby = dict.values(user)                # trả về list chứa value
    #closer = dict.clear(user)              # xóa dữ liệu trong mảng
    past = dict.copy(user)                  # tạo một bản sao của chuỗi
    dono = dict.fromkeys(user, value)       # tạo một đối tượng với list chứa các khóa và truyền key làm phần tử
    #print(dict.has_key('x'))            # kiểm tra key có tồn tại không

    print('tạo bản sao: ', past)
    print('chỉ chứa key: ',haha)
    print('chỉ chứ value: ',baby)
    print(dono)