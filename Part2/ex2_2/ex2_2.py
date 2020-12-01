# В первой строке дано три числа, соответствующие некоторой дате date -- год,
# месяц и день.
# Во второй строке дано одно число days -- число дней.
#
# Вычислите и выведите год, месяц и день даты, которая наступит,
# когда с момента исходной даты date пройдет число дней, равное days.
import datetime as dt

date = dt.date(*[int(i) for i in input().split()])
new_date = date + dt.timedelta(days=int(input()))
print(new_date.year, new_date.month, new_date.day)
