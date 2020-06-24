# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:16:13 2020
@author: Satish
"""


import datetime


#### Problem: 1

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month
      
    Returns:
      The number of days in the input month.
    """
    
    if year < datetime.MINYEAR or year > datetime.MAXYEAR:
        return 0   
    
    if month > 12 or month < 1:
        return 0
    
    if month == 12:
        year = year+1
        month = 1
    
    this_month = datetime.date(year, month, 1)
    next_month = datetime.date(year, month + 1, 1)
    return (next_month-this_month).days


#    
#Mt = input("Enter month: ")
#Yr = input("Enter year: ")

#print(days_in_month(int(Yr), int(Mt)))

#### Problem: 2


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day
      
    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    valid_date = True
    
    if month < 1 or month > 12:
        valid_date = False
    
    if year < datetime.MINYEAR or year > datetime.MAXYEAR:
        valid_date = False
    
    if day > days_in_month(year, month) or day < 1:
        valid_date = False

        
    return valid_date

    
#day_in = input("Enter day: ")
#month_in = input("Enter month: ")
#year_in = input("Enter year: ")    
#    
#print(is_valid_date(int(year_in), int(month_in), int(day_in)))

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """
    
    if is_valid_date(year1, month1, day1) is False or is_valid_date(year2, month2, day2) is False:
        return 0
    
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    
    if date2 < date1:
        return 0
    
#    print(date1)
#    print(date2)

    num_days = date2 - date1
    return num_days.days

#date1_day_in = input("Enter date 1 day: ")
#date1_month_in = input("Enter date 1 month: ")
#date1_year_in = input("Enter date 1 year: ") 
#
#date2_day_in = input("Enter date 2 day: ")
#date2_month_in = input("Enter date 2 month: ")
#date2_year_in = input("Enter date 2 year: ") 
#
#p3 = days_between(int(date1_year_in), int(date1_month_in), int(date1_day_in), int(date2_year_in)
#            , int(date2_month_in), int(date2_day_in))

#print(p3)

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
      
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """


    
    if is_valid_date(year, month, day) is False:
        return 0
    
    dob = datetime.date(year, month, day)
    
    if dob > datetime.date.today():
        return 0
    
    age = datetime.date.today() - dob
    
    return age.days


    

#age_day_in = input("Enter dob day: ")
#age_month_in = input("Enter dob month: ")
#age_year_in = input("Enter dob year: ") 
#
#age_ans = age_in_days(int(age_year_in),int(age_month_in),int(age_day_in))
#print(age_ans)
    
