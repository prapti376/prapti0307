import csv
with open(r"E:\college\Python\lab10Q1.csv",'r',newline='') as f:
    r=csv.reader(f)
    for i in r:
        print(i)