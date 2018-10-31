'''
Created on 28 жовт. 2018 р.

@author: F
'''

with open("students.csv", "r", encoding='utf-8') as ins:
    array = []
    for line in ins:
        array.append([line])

#with open('students.csv', 'r', encoding='utf-8') as f: lines = [line for line in f]

#test_lines = [x.rstrip('\n') for x in array]
array.pop(0)
#print(array)

k = len(array)

test_lines = []
j = 0

for i in array:

    list_element = str(i)
    print(list_element)
    new_element = list_element.split(';')
    print(new_element)
    test_lines.append(new_element)
  
    
print(test_lines)
#lines1 = [['петя',10,130,35], ['вася',11,135,39],['женя',9,140,33],['дима',10,128,30]]
#print(lines1)


#n = input('Сортировать по номеру группы (1), фамилии (2), возрасту (3): ')
#n = int(n)-1

#def sort_col(i):
 #   return i[n]
    

#array.sort(key=sort_col)

#for i in array:
 #   print("%7s %3d %4d %3d" % (i[0],i[1],i[2],i[3]))
#print(lines)


    
    
