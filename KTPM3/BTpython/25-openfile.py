import pandas as pd
df = pd.read_csv("C:\\Users\\Duy\\Desktop\\Book2.csv")

# 1 sửa item go và gol thành gold
for x in df.index:
    if(df.loc[x,"Item"] == 'Gol' or df.loc[x,"Item"] == 'Go'):
        df.loc[x, "Item"] = 'Gold'

# 2 sửa crude  thành crude oil, pad thành paddy
for x in df.index:
    if (df.loc[x, "Item"] == 'Crude'):
        df.loc[x, "Item"] = 'Crude Oil'
    elif (df.loc[x, "Item"] == 'Pad'):
        df.loc[x, "Item"] = 'Paddy'
# 3 Xóa các dòng có Date < 27/12/2019
df = df[df.Date > "27/12/19"]

# 4 Sửa dòng có Date < 10/01/2021 thành 10/01/2021
df = df[df.Date > "27/12/19"]
for x in df.index:
    if(df.loc[x,"Date"] > '10/1/21'):
        df.loc[x, "Date"] = '10/1/21'

# 5 Sửa dòng có Date > 10/04/2021 thành 10/04/2021
for x in df.index:
    if(df.loc[x,"Date"] > "10/04/21"):
        df.loc[x, "Date"] = "10/04/21"

# 6 Sửa các dòng Gas , 10/04/2021 có Price là 0 thành 4.1
for x in df.index:
    if(df.loc[x,"Date"] == "10/04/21" and df.loc[x,"Item"] == "Gas"):
        if(df.loc[x,"Price"] == 0.0):
            df.loc[x, "Price"] = 4.1

# 7 Xóa các dòng có giá trị null
df = df.dropna()

# 8 Xóa các dòng dữ liệu trùng
df = df.drop_duplicates()

# 9 Chuyển kiểu date cho cột Date
df['Date'] = pd.to_datetime(df['Date'])

# 10 Ghi dữ liệu đã làm sạch vào tập tin File30.csv
df.to_csv ('C:\\Users\\Duy\\Desktop\\Test30.csv', index = True, header=True)
print(df)
