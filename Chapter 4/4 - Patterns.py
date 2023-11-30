n = 1
f = 5.5
pattern = "*"
print(n * 4)
print(n * 4.4)
print(n * pattern)
while n < 10:
    print(" " + n * pattern)
    n += 1
def makeTreePattern(n):
    h = 1
    while h < n:
        h += 1