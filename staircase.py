# Create a staircase of #
# Solution taken from the discussion board

for i in range(n):
    line =  " " * (n - i - 1) + "#" * (i + 1)
    print line
