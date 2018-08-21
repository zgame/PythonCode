import csv


# 读csv文件

csv_reader = csv.reader(open('t.csv', encoding='utf-8'))
for row in csv_reader:
    print(row)

