# import time 
# import random 

# NUM = 10000

# start_time = time.time()

# list_number = list.append(NUM)


# end_time = time.time() - start_time



def is_leap_year(year):
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

year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# def schoolSelection(ages):
#     grade_levels = {
#         'Kindergarten': 0,
#         '1st grade': 0,
#         '2nd grade': 0,
#         '3rd grade': 0,
#         '4th grade': 0
#     }
    
#     for age in ages:
#         if age == 5:
#             grade_levels['Kindergarten'] += 1 
#         elif age == 6:
#             grade_levels['1st grade'] += 1 
#         elif age == 7:
#             grade_levels['2nd grade'] += 1
#         elif age == 8:
#             grade_levels['3rd grade'] += 1
#         elif age == 9:
#             grade_levels['4th grade'] += 1

#     return grade_levels

# ages = [5, 7, 4, 9, 10, 5, 15, 9, 5]
# result = schoolSelection(ages)
# print(result)
