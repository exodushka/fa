"""#12.10
#a)
tupl = (1,1,1,2,3,4,5)
element = int(input('input element for search: '))

count = tupl.count(element)

if count > 0:
    print('element', element, 'founded for', count, 'times')
else:
    print('element', element, 'not founded in tuple')
#b)
user_input = input('input string with comma: ')
string_list = [s.strip() for s in user_input.split(',')]

unique_list = []
for item in string_list:
    if item not in unique_list:
        unique_list.append(item)

result_tuple = tuple([unique_list])
print('tuple without repetions elements', result_tuple)"""

q = [1,2,3]
g = q.pop(1)
print (g)
