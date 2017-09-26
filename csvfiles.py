import csv


def writeCsv(fileNm):

    file1 = open(fileNm, 'wb')
    writer = csv.writer(file1)
    for i in range(1,10):
        writer.writerow([i, i*10, i*20])
    file1.close()


def printFile(fileNm):

    file2 = open(fileNm, 'rb')
    reader = csv.reader(file2)
    for row in reader:
        print row
    file2.close();


writeCsv('table.csv')
printFile('table.csv')

