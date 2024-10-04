from itertools import filterfalse

immutable_var = (16, 'word', False)
print(immutable_var)
#immutable_var [2] = True
#print(immutable_var) ошибка, так как tuple - это неизменяемая упорядоченная коллекция, которая может содержать в себе разные типы данных
mutable_list = ['string', 'the number of pi', 16]
mutable_list[1] = 3.14
mutable_list.append(True)
mutable_list.remove('string')
mutable_list.extend(['string', 3])
print(mutable_list)