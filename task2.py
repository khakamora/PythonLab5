import csv

with open('students.csv', 'r', encoding='utf-16') as myfiles:
    reader = csv.reader(myfiles, delimiter=';')
    student_list = [row for row in reader]
#print(student_list)
student_list.pop(0)

n = input('Сортировать по номеру группы (4), фамилии (2), возрасту (3): ')
n = int(n)-1

print(n)

def sort_col(i):
    return i[n]

student_list.sort(key=sort_col)

print(student_list)

s = input('По увеличению возраста всех студентов на 1 - (3):')
s = int(s)-1

myfile = open('students.csv', 'w', encoding='utf-16')
for student_row in student_list:
    
    student_row[s] = str(int(student_row[s]) + 1)
    myfile.write(';'.join(student_row))
    myfile.write('\n')
print('You are God')