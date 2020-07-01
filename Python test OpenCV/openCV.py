def py(n,m,k):
    for row in range(n):
        for spaceSP in range(k-n):
            print(' ',end='')
        for space in range(n-row):
            print(' ',end='')
        for star in range(row):
            print('*',end='')
        for star in range(row+1):
           print('*',end='')
        for space in range(k-1,row-1,-1):
            print(' ',end='')
        print()
    for row in range(m-n,m):
        for spaceSP in range(k-m):
            print(' ',end='')
        for space in range(m-row):
            print(' ',end='')
        for star in range(row):
            print('*',end='')
        for star in range(row+1):
           print('*',end='')
        for space in range(k-1,row-1,-1):
            print(' ',end='')
        print()
    for row in range(k-m,k):
        for space in range(k-row):
            print(' ',end='')
        for star in range(row):
            print('*',end='')
        for star in range(row+1):
           print('*',end='')
        for space in range(k-1,row-1,-1):
            print(' ',end='')
        print()

    for row in range((n+m+k)//4):
        for space in range(k-1):
            print(' ',end='')
        for star in range(3):
            print('*',end='')
        for space in range(k-1,0,-1):
            print(' ',end='')
        print()

py(10,12,14) 

            