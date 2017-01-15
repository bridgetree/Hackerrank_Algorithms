# Absolute difference between primary and seconday diagonal
# Solution taken from discussion board

print(abs(sum([a[i][i] for i in range(n)]) 
        - sum([a[i][abs(i-(n-1))] for i in range(n)])))
