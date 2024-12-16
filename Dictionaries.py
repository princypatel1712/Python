person = {
    'first_name':'abc',
    'last_name':'xyz',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person)
print(len(person))  # 7
print(person['first_name']) # abc
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person.get('first_name')) # abc
print(person.get('country'))    # Finland

#ADD

person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)

#modifying dictionary
person['first_name'] = 'Eyob'
person['age'] = 252

#pop
person.pop('first_name')        #  removes the item with the specified key name:
person.popitem()                #  removes the last item
del person['is_married']        #  removes an item with specified key name

# items() method changes dictionary to a list of tuples.
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])


# don't want the items in a dictionary we can clear them using clear() method
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None

#do not use the dictionary we can delete it completely
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct


#Iterate Through  Dictionary

country_capitals = {
  "United States": "Washington D.C.",
  "Italy": "Rome"
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)

print()

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(capital)


## Nested Dictionaries

course ={
     'php':{'duration':'3 month','fees':15000},
     'java': {'duration': '2 month', 'fees': 14400},
     'python':{'duration': '2 month', 'fees': 154000},

}
print(course)
course['java']['fees']=200000    #update

print(course['php'])
print(course['php']['fees'])

for k,v in course.items():
     print(k,v['duration'],v['fees'])