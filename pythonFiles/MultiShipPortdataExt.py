import pandas as pd
import time
import math as mt
import os
import os.path
# filepath = '../TankerShips/412203480-r-00001'
#定义一个文件路径数组filepath
filepath=[]
suffix = '.csv'
bohaiFiles = 'D:/航海项目/数据相关/100shipdata/'
for parent, dirnames, filenames in os.walk(bohaiFiles):
    for filename in filenames:
        # print(bohaiFiles + filename)
        # data = data.append(pd.read_csv(bohaiFiles + filename, header=None))
        #将文件的路径保存在filepath中
        filepath.append(bohaiFiles + filename)
print(len(filepath))

#距离计算函数
def dist(p1, p2):
    radlat1 = mt.radians(p1[0])
    radlat2 = mt.radians(p2[0])
    a = radlat1 - radlat2
    b = mt.radians(p1[1]) - mt.radians(p2[1])
    s = 2 * mt.asin(mt.sqrt(pow(mt.sin(a / 2), 2) + mt.cos(radlat1) * mt.cos(radlat2) * pow(mt.sin(b / 2), 2)))
    earth_radius = 6378.137
    #计算距离转换成以m为单位
    # s = s * earth_radius
    s = s * earth_radius*1000

    if s < 0:
        return -s
    else:
        return s

fileslen=len(filepath)
for i in range(fileslen):
    print(filepath[i])
    out_df = pd.DataFrame()
    df = pd.read_csv(filepath[i], header=None)
    df = df.sort_index()
    df = df.sort_values(by=0)
    testlen = len(df)
    # print("--------------------")
    # print (testlen)
    for j in range(testlen - 1):
        p1 = [df.iloc[j, 7], df.iloc[j, 6]]
        p2 = [df.iloc[j + 1, 7], df.iloc[j + 1, 6]]
        t1 = df.iloc[j, 0]
        t2 = df.iloc[j + 1, 0]
        t = t2 - t1
        print('速度单位是：m/s')
        print(dist(p1, p2) / (t2 - t1))
        if (dist(p1, p2) / t <0.01):
            new_df = pd.DataFrame()
            new_df.insert(0, '0', [df.iloc[j, 7]])
            new_df.insert(0, '1', [df.iloc[j, 6]])
            out_df = out_df.append(new_df)

    out_df.to_csv('D:/航海项目/数据相关/gangkoudataTest/' + filepath[i].split('/')[4][:20] + suffix, index=False, header=False)