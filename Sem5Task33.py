grades = [1,3,3,3,4,5,5,1]
for i in range (1, len(grades)):
    maxGrades = max(grades)
    minGrades = min(grades)
    if (grades[i] == maxGrades):
        grades[i] = minGrades
    print(maxGrades)
    print(minGrades)
    print(grades)
