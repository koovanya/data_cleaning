# data_cleaning
数据清理，自动处理从见微数据下载的财务报表.csv


1、origin_balance.csv 和 origin_profit.csv 是从见微数据下载的资产负债表和利润表（000001平安银行），其他公司的报表格式与之一致，代码应该可以直接套用；

2、balance.csv 和 profit.csv 是处理后的文件，删除了原始文件中不需要的字符。

3、本代码用到 pandas 和 openpyxl
