from datetime import datetime
import pandas as pd
df = pd.read_csv("~\\Desktop\\file.csv")
print(df)
print("")

# 1/. Sửa dòng có Date có giá trị là null thành  02/24/2022
df = df.fillna("NaN")
for x in df.index:
    if(df.loc[x,"Date"] == "NaN" ):
        df.loc[x, "Date"] = "02/24/2022"
print(df)

# 2/. Xóa các dòng có Exchange là null
df2 = df.dropna(subset=['Exchange'])
print(df2)
# 3/. Sửa các dòng có Currency là ‘CAT’ thành ‘CAD’
for x in df.index:
     if (df.loc[x,"Currency"] == 'CAT'):
        df.loc[x,"Currency"] = "CAD"
print(df)
# 4/. Sửa các dòng có Date < 1/1/2022 thành 1/1/2022
df['Date'] = pd.to_datetime(df['Date'])
for x in df.index:
    if pd.Timestamp(df.loc[x, "Date"]) < datetime(2022,1,1):
       df.loc[x,"Date"] = datetime(2022,1,1)
print(df)
# 5/. Sửa các dòng có Date >4/20/2022  thành 4/15/2022
df['Date'] = pd.to_datetime(df['Date'])
for x in df.index:
    if pd.Timestamp(df.loc[x, "Date"]) > datetime(2022, 4,20):
        df.loc[x,"Date"] = datetime(2022,4,15)
print(df)
# 6/. Xóa các dòng dữ liệu trùng
df = df.drop_duplicates()
print(df)
# 7/. Sửa dòng có Currency là ‘CSS’  thành ‘CFT’
for x in df.index:
     if (df.loc[x,"Currency"] == 'CSS'):
        df.loc[x,"Currency"] = "CFT"
print(df)
# 8/. Xóa các dòng có Currency là ‘RUB’
for x in df.index:
    if df.loc[x, "Currency"] > 'RUB':
        df.drop(x, inplace = True)
print(df)
# 9/. Chuyển kiểu date cho cột Date và có dạng (m/d/y)
df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')
print(df)
# 10/. Ghi dữ liệu đã làm sạch vào tập tin DataCleaning_1003.csv.
df.to_csv('~\\Desktop\\DataCleaning_1003.csv', index = True, header=True)
print("Kết thúc chương trình")
