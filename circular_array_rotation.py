# Rotate an array, output specific values based on user output
# Copied from discussion board, my solution was timing out for 
# certain test sets

b = a[:] # copy of the original array so no overwrites occur
for i in range(n):
    b[(i + k) % n] = a[i]

for a0 in range(q):
    m = int(raw_input().strip())
    print(b[m])
