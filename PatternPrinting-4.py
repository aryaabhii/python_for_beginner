# Printing patten
# 1 2 3 4 5 6 7 8 9 
# 1 2 3 4 5 6 7 8 
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
for i in range(10,0,-1):
    for j in range(1,i):
        print(j ,end=" " )
    print("")