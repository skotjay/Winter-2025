#only the updates are commented
start = 1
count = 1

#outer loop upsated from 3 to 5 rows
while count <= 5:
    row = 0
    current = start
    #innter loop updated from 3 to 5 items of data
    while row < 5:
        print(current, end=" ")
        current += 1
        row += 1
    print()
    
    #the function has been updated
    start = (start*10) + 20
    count += 1