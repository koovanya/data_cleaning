#自动处理从见微数据下载的资产负债表.csv

import pandas as pd
import openpyxl

#导入从见微数据下载的csv文件
csv = pd.read_csv('origin_balance.csv')
#导入dataframe
csv_df = pd.DataFrame(csv)

#去除每一列不需要的字符
col1 = csv_df['科目'].str.split('(',expand=True)[0]
col2 = csv_df['20220331'].str.split(' 同比',expand=True)[0]
col3 = csv_df['20211231'].str.split(' 同比',expand=True)[0]
col4 = csv_df['20201231'].str.split(' 同比',expand=True)[0]
col5 = csv_df['20191231'].str.split(' 同比',expand=True)[0]
#合并成新dataframe
csv_df = pd.concat([col1,col2,col3,col4,col5],axis=1)
csv_df.columns = ['科目','20220331','20211231','20201231','20191231']

#去除每一列不需要的字符
col1 = csv_df['科目']
col2 = csv_df['20220331'].str.split(':',expand=True)[1]
col3 = csv_df['20211231'].str.split(':',expand=True)[1]
col4 = csv_df['20201231'].str.split(':',expand=True)[1]
col5 = csv_df['20191231'].str.split(':',expand=True)[1]
#合并成新dataframe
csv_df = pd.concat([col1,col2,col3,col4,col5],axis=1)
csv_df.columns = ['科目','20220331','20211231','20201231','20191231']

#将 -- 替换成 0
csv_df = csv_df.replace('--','0')

#保存
csv_df.to_csv('balance.csv',index=False)

#导入从见微数据下载的csv文件
csv = pd.read_csv('origin_profit.csv')
#导入dataframe
csv_df = pd.DataFrame(csv)

#去除每一列不需要的字符
col1 = csv_df['科目'].str.split('(',expand=True)[0]
col2 = csv_df['20220331'].str.split(' 同比',expand=True)[0]
col3 = csv_df['20211231'].str.split(' 同比',expand=True)[0]
col4 = csv_df['20201231'].str.split(' 同比',expand=True)[0]
col5 = csv_df['20191231'].str.split(' 同比',expand=True)[0]
#合并成新dataframe
csv_df = pd.concat([col1,col2,col3,col4,col5],axis=1)
csv_df.columns = ['科目','20220331','20211231','20201231','20191231']

#去除每一列不需要的字符
col1 = csv_df['科目']
col2 = csv_df['20220331'].str.split(':',expand=True)[1]
col3 = csv_df['20211231'].str.split(':',expand=True)[1]
col4 = csv_df['20201231'].str.split(':',expand=True)[1]
col5 = csv_df['20191231'].str.split(':',expand=True)[1]
#合并成新dataframe
csv_df = pd.concat([col1,col2,col3,col4,col5],axis=1)
csv_df.columns = ['科目','20220331','20211231','20201231','20191231']

#将 -- 替换成 0
csv_df = csv_df.replace('--','0')
#print(csv_df)

#保存
csv_df.to_csv('profit.csv',index=False)

