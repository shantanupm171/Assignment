year = int(input("Enter the Year: "))
def leap_year(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))
if (leap_year(year)):
    print(f"{year} is leap Year")
else:
    print(f"{year} is Not Leap Year")