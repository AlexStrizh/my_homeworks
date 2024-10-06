my_dict = {'Alexey': 1996, 'Ivan': 2001, 'Petr': 1988, 'Roman': 2004, 'Maxim': 1991}
print(my_dict)
print(my_dict.get('Roman'))
print(my_dict.get('Egor'))
my_dict.update({'Irina': 1985,
               'Lena': 2005})
DV = my_dict.pop('Petr')
print(DV)
print(my_dict)

my_set = {1,3,7,5,'Set',3,5,'Set',(9,8,7),False,1,(9,8,7),7,False }
print(my_set)
my_set.add((45,67,89))
my_set.add('Word')
my_set.remove((9,8,7))
print(my_set)