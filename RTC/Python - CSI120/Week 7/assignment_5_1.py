#declare var "start" for initial output data
start = 1

#declare var "count" for outer loop counter
count = 1

#outer loop prints 3 rows
while count <= 3:
    #declare var "row" for inner loop counter
    row = 0
    current = start
    #inner loop prints 3 data items
    while row < 3:
        print(current, end="")
        current += 1
        row += 1
    
    #moves to the next line after 3 items printed
    print()
    
    #updates the value of the data for the next outer loop
    start += 2
    #updates outer loop counter
    count += 1
    

