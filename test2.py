# 2.Write a Python program to extract any email id (take input from user)

import re

text = str(input("Please Enter the string to find email :-"))
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
print(emails)


# sample
# input string - "my email id is yajurvedi62@gmail.com and my friend email id is rahul15@outlook.com"
# output =['yajurvedi62@gmail.com', 'rahul15@outlook.com']
