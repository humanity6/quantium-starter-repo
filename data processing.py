import csv

path0 = 'quantium-starter-repo/data/daily_sales_data_0.csv'
path1 = 'quantium-starter-repo/data/daily_sales_data_1.csv'
path2 = 'quantium-starter-repo/data/daily_sales_data_2.csv'

file = open("temp.csv",'w',newline='')
filewriter = csv.writer(file)
filewriter.writerow(["sales","date","region"])

for path in [path0, path1, path2]:
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == "pink morsel":
                quantity = int(row[2])
                price = float(row[1][1:])
                sales = quantity * int(price)
                filewriter.writerow([sales,row[3],row[-1]])
