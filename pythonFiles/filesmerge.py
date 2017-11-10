#合并文件夹中的多个csv文件为一个csv文件
import pandas as pd
import os.path

out_df = pd.DataFrame()
data = pd.DataFrame()
files=[]
filepath = 'D:/航海项目/data/'
suffix = '.csv'
for parent, dirnames, filenames in os.walk(filepath):
    for filename in filenames:
        f=filepath+filename
        out_f = pd.read_csv(f, header=None)
        print(out_f)
        out_df = out_df.append(out_f)
        out_df.to_csv('D:/航海项目/DBScanFile/1test.txt',header=False,index=False)