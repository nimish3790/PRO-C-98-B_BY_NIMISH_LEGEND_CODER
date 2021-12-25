def swapFiles():
    file1 = input("Enter the file name-")
    file2 = input("Enter your file name which you want to swap-")

    with open(file1, 'r') as a:
        data1 = a.read()
    with open(file2, 'r') as x:
        data2 = x.read()

    with open(file1, 'w') as b:
        b.write(data2)
    with open(file2, 'w') as y:
        y.write(data1)

swapFiles()