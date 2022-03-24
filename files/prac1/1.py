# Exercise 1
# Write a program to display the number of days in a month, given the month and the year
def leap(year):
    if ((year % 4) and (not year % 100)) or (year % 400):
        return True
    return False

def main():
    month = int(input())
    year = int(input())
    days_in_month = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        if leap(year):
            print(29)
        else:
            print(28)
    else:
        print(days_in_month[month])
if __name__ == '__main__':
    main()