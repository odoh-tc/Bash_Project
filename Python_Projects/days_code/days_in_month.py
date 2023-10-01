def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month <= 0:
    print("put a valid month number")
  elif month >= 13:
    print("put a valid month number")
  elif month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1] 
 
year = int(input("Enter the year you want: ")) # Enter a year
month = int(input("Enter the month you want: ")) # Enter a month
days = days_in_month(year, month)
print(days)
