##读取一艘船的数据，按照时间戳的递增顺序对轨迹序列进行排序，并计算相邻序列的速度，设定速度阈值，提取速度值<阈值的轨迹数据的经纬度。
import pandas as pd
import math as mt

filepath = 'D:/航海项目/数据相关/bohai-youlun/412203480-r-00001'

suffix = '.csv'

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


if __name__ == '__main__':
    out_df = pd.DataFrame()
    df = pd.read_csv(filepath, header=None)
    df = df.sort_index()
    df = df.sort_values(by=0)
    cur = 0
    order = 0
    testlen = len(df)
    # print(testlen)
    for i in range(testlen - 1):
        p1 = [df.iloc[i, 7], df.iloc[i, 6]]
        p2 = [df.iloc[i + 1, 7], df.iloc[i + 1, 6]]
        t1 =df.iloc[i,0]
        t2 =df.iloc[i+1,0]
        # print("时间间隔：")
        # print(t2-t1)
        # print("距离：")
        # print(dist(p1,p2))
        # # 速度的单位是：m/s
        print("速度：")
        print(dist(p1,p2)/(t2-t1))
        # if(dist(p1,p2)/(t2-t1)==0.0):
        #     print(df.iloc[i, 6],df.iloc[i, 7])
        if (dist(p1,p2)/(t2-t1)<0.01):
            # print(df.iloc[i, 6], df.iloc[i, 7])
            new_df = pd.DataFrame()
            new_df.insert(0,'0',[df.iloc[i, 7]])
            new_df.insert(0,'1',[df.iloc[i, 6]])
            out_df = out_df.append(new_df)

    out_df.to_csv('D:/航海项目/数据相关/splitdata/'+ filepath.split('/')[4][:20]+suffix, index=False, header=False)