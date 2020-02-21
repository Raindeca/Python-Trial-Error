
for i in range(0,3):
    for k in range(0,3):
        c[i,k] = 0
        for j in range(0,3):
            c[i,k] = c[i,k] + a[i,j] * b[j,k]
        
    

print(c[i,k])
