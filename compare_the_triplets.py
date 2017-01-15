# My Solution

Alice = 0
Bob = 0

if a0 > b0:
    Alice += 1
elif b0 > a0:
    Bob += 1
else:
    pass
if a1 > b1:
    Alice += 1
elif b1 > a1:
    Bob += 1
else:
    pass
if a2 > b2:
    Alice += 1
elif b2 > a2:
    Bob += 1
else:
    pass

print Alice, Bob



# Solution from the Discussion Board

Ascore = len([1 for a,b in zip(A,B) if a>b])
Bscore = len([1 for a,b in zip(A,B) if b>a])
print Ascore, Bscore


















