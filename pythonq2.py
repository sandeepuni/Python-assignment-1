# -*- coding: utf-8 -*-

costph = 0.51
# Cost per Day
costpd = costph* 24
print(f"Cost per day: {costpd}")
# Cost per Week
costpw = costpd * 7
print(f"Cost per week: {costpw}")
# Cost per month
costpm = costpw * 30
print(f"Cost per month: {costpm}")
# Days with $918
timepw = 918/(0.51*24)
print(f"$918 can get you: {timepw} days")
