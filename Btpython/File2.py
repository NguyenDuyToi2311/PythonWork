import pandas as pd
from datetime import datetime
df = pd.read_csv("E:\BaiThi\File_1.csv")
print(df)
print("---------------------")
print("1/. Sửa dòng có Date có giá trị là null thành  02/24/2022")
nan_rows = df[df["Date"].isnull()]
index = list(nan_rows.index)
for x in index:
    df.loc[x,"Date"] = datetime.date(2022,2,24)
print(df)
