def percent(marks):
    p = (sum(marks)/400)*100
    return p

marks1 = [45, 78, 54, 89]
percentage1 = percent(marks1)
# percentage1 = (sum(marks)/400 )*100

marks2 = [75, 98, 54, 89]
percentage2 = percent(marks2)
# percentage2 = (sum(marks)/400 )*100

marks3 = [55, 45, 34, 60]
percentage3 = percent(marks3)
print(percentage1 , percentage2 , percentage3)