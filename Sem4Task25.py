mas = "a a a b c a a d c d d".split()
new = dict()
result = ""
for i in mas:
    if i not in new:
        new[i] = 1
        result += i
        print(new)
    else:
        result = result + (i + "_" + str(new [i]))
        new[i] += 1       
print (new)
print (result)