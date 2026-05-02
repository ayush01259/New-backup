from array import array
adk = array("I", [10, 20, 30, 40, 50])
print("Addded 60 at the end of the array : ", adk.append(60), adk)
print("inserted 15 at the second positon :", adk.insert(1,15), adk)
print("Your array's element 30 is removed :", adk.remove(30), adk)
print("Your 2nd element of the arrays is deleted :", adk.pop(2))
adk.append(70)
print(adk)