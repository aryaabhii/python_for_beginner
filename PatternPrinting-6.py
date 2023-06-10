# Printing patten
# 10 10 10 10 10 10 10 10 10 10 
# 9 9 9 9 9 9 9 9 9 
# 8 8 8 8 8 8 8 8
# 7 7 7 7 7 7 7
# 6 6 6 6 6 6
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
for i in range(10,0,-1):
    for j in range(0,i):
        print(i ,end=" " )
    print("")