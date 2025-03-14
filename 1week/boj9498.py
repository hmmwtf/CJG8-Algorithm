def ABCDF(n):
    grade = ""
    if 90 <= n <= 100:
        grade = 'A'
    elif n >= 80:
        grade = 'B'
    elif n >= 70:
        grade = 'C'
    elif n >= 60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

test = int(input())
print(ABCDF(test))