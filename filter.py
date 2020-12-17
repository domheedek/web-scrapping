# import re
# import pandas as pd 
# simple = ['Iphone 12','Iphone 12 Pro','Iphone 12 Pro Max']

# for i in simple:
#     j = i.split()
#     print(type(j))
#     print(j)
    
list1 = ['Perl', 'PHP', 'Java', 'ASP']
list2 = ['JavaScript is client-side scripting language',
         'PHP is a server-side scripting language',
         'Java is a programming language',
         'Bash is a scripting language']

# Filter the second list based on first list
filter_data = [x for x in list2 if
              all(y not in x for y in list1)]

# Print list data before filter and after filter
print("The content of the first list:", list1)
print("The content of the second list:", list2)
print("The content of the second list after filter:", filter_data)
