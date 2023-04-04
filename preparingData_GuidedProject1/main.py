# file = open("preparingData_GuidedProject1/employee_revenue.txt", "r") 

# data = file.read()
# print(data)

# lines = data.splitlines()
# print(lines)

# string = lines[0]
# print(string)

# ****************************************************************************

# string_strip = string.strip(" ")
# print(string_strip)

# ****************************************************************************

# string_lower = string.lower()
# print(string_lower)

# ****************************************************************************

# string_capitalize  = string.capitalize()
# print(string_capitalize)

# ****************************************************************************

# string_split = string.split()
# print(string_split)

# ****************************************************************************

# name = string_split[0]
# print(name)

# ****************************************************************************

# call_number = string_split[2]
# print(call_number)

# ****************************************************************************

# for i in string_split:
#     if "$" in i :
#         average_deal_size = i.split("$")[0]
# print(average_deal_size)

# ****************************************************************************

# dollars_index = string_split.index("dollars")
# print(dollars_index)

# ****************************************************************************

# revenue_index = dollars_index - 1
# print(revenue_index) 

# ****************************************************************************

# revenue = string_split[revenue_index]
# print(revenue)

# ****************************************************************************

# print("Name:", name)
# print("Number of calls:", call_number)
# print("Average deal size:", average_deal_size)
# print("Revenue:", revenue)

# ****************************************************************************

# print("Name:", type(name))
# print("Number of calls:", type(call_number))
# print("Average deal size:", type(average_deal_size))
# print("Revenue:", type(revenue))

# ****************************************************************************

# average_deal_size = int(average_deal_size)
# call_number = int(call_number)
# revenue = int(revenue)
# print("Name:", type(name))
# print("Number of calls:", type(call_number))
# print("Average deal size:", type(average_deal_size))
# print("Revenue:", type(revenue))

# ****************************************************************************

# file = open("preparingData_GuidedProject1/employee_revenue.txt", "r") 
# data = file.read()
# lines = data.splitlines()

# names_list = []
# call_numbers = []
# average_deal_sizes = []
# revenues = []

# for employee in lines:
    
#     employee = employee.strip()
#     employee = employee.lower()
#     employee = employee.capitalize()

#     split_employee = employee.split(" ")

#     name = split_employee[0]
#     call_number = int(split_employee[2])

#     for i in split_employee:
#         if "$" in i :
#             average_deal_size = i
#     average_deal_size = int(average_deal_size.split("$")[0])

#     dollars_index = split_employee.index("dollars")
#     revenue_index = dollars_index - 1
#     revenue = int(split_employee[revenue_index])

#     names_list.append(name)
#     call_numbers.append(call_number)
#     average_deal_sizes.append(average_deal_size)

#     print("Name:", name)
#     print("Number of calls:", call_number)
#     print("Average deal size:", average_deal_size)
#     print("Revenue:", revenue)

# ****************************************************************************

file = open("preparingData_GuidedProject1/employee_revenue.txt", "r") 
data = file.read()
lines = data.splitlines()

names = []
callNumbers = []
averageDealSizes = []
revenues = []

def cleanExtract(lines):
    for employee in lines:
        
        employee = employee.strip(" ")
        employee = employee.lower()
        employee = employee.capitalize()

        splitEmployee = employee.split(" ")

        name = splitEmployee[0]
        callNumber = splitEmployee[2]

        for i in splitEmployee:
            if "$" in i :
                averageDealSize = i
                averageDealSize = averageDealSize.split("$")[0]
        
        dollarsIndex = splitEmployee.index("dollars")
        revenueIndex = dollarsIndex - 1
        revenue = splitEmployee[revenueIndex]

        averageDealSize = int(averageDealSize)
        callNumber = int(callNumber)
        revenue = int(revenue)

        names.append(name)
        callNumbers.append(callNumber)
        averageDealSizes.append(averageDealSize)
        revenues.append(revenue)

    return names, callNumbers, averageDealSizes, revenues

names, callNumbers, averageDealSizes, revenues = cleanExtract(lines)

print("Names:", names)
print("Number of calls:", callNumbers)
print("Average deal size:", averageDealSizes)
print("Revenue:", revenues)

print("len names:", len(names))

IDs = list(range(0,11))
print("IDs:", IDs)

dictionary1 = dict(zip(IDs, names))
print("Dictionary1:", dictionary1)

dictionary2 = dict(zip(revenues, names))
print("dictionary2:", dictionary2)

sortedDictionary = sorted(dictionary2)[0:3]
for i in sortedDictionary:
    print("sortedDictinary 1:", dictionary2[i])

sortedDictionary = sorted(dictionary2, reverse=True)[0:3]
for i in sortedDictionary:
    print("sortedDictinary 2:", dictionary2[i])
