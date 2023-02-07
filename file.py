# 1. Update Values in Dictionaries and Lists

# change the value 10 in x to 15
x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15 

# Change the last_name of first student form 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(students[0]['last_name'])
students[0]['last_name']=Bryant
print(students[0]['last_name'])


# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print(sports_directory[0]["soccer"][0])
sports_directory[0]["soccer"][0]=Andres
print[0]["soccer"][0]


# Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
print(z[0]['y'])
z[0]['y']=30
print(z[0]['y'])


# 2. Iterate through a list of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
for student in students:
    print (student)

# iterateDictionary(students) 
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# 3. Get Values from a List of Dictionaries
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
for student in students:
    print(student['first_name'])

for student in students:
    print(student['last_name'])


# 4. Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
for key, value_list in dojo.items():
    print(f'Coding Dojos {key} are:')
    for item in value_list:
        print(item)

def printInfo(dojoParam):
    print(len(dojoParam['locations'], "LOCATIONS"))
    for location in dojoParam['locations']:
        print(location)
    print()
    print(len(dojoParam['instructors'], "INSTRUCTORS"))
    for instructors in dojoParam['instructors']:
        print(instructors)


# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon