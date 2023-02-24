import math

for a in range(1, 151):
    for b in range(1, 151):
        for c in range(1, 151):
            for d in range(1, 151):
                for e in range(1, 151):
                    if math.pow(a,5) + math.pow(b,5) + math.pow(c,5) + math.pow(d,5) == math.pow(e,5):
                        print(a + b + c + d + e)