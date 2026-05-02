from array import array
akd = array("I", [1,4,5,6,73,6])
print(sum(akd))
i = 0
total = 0
while i < len(akd):
    total += akd[i]
    i += 1
print(total)
jod = 0
for num in akd:
    jod += num
    print(jod)
print(jod)