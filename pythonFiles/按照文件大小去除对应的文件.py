import pandas as pd
import os.path

data = pd.DataFrame()
filepath = 'D:/航海项目/数据相关/500shipout/'
suffix = '.csv'
for parent, dirnames, filenames in os.walk(filepath):
    for filename in filenames:
        f=filepath+filename
        print(filepath + filename)
        print(f)
        print(os.path.getsize(filepath+filename))
        # 添加判断条件，如果文件大小为0的话则删除此文件
        if(os.path.getsize(filepath+filename)==0):
            os.remove(filepath+filename)