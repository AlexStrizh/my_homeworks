grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_avg = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
students_lst = list(students)
students_lst_sort = sorted(students_lst)
avg_list = {students_lst_sort[0]:grades_avg[0], students_lst_sort[1]:grades_avg[1], students_lst_sort[2]:grades_avg[2], students_lst_sort[3]:grades_avg[3], students_lst_sort[4]:grades_avg[4]}
print(avg_list)

