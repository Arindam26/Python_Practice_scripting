def leap_year(leap):
    return leap % 4 == 0 and (leap % 400 == 0 or leap % 100 != 0)


year = int(input())
print(leap_year(year))
