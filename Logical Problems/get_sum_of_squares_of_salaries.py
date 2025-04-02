from functools import reduce

list1 = [{"Name":"A","Age":20,"Salary":30000},{"Name":"B","Age":26,"Salary":40000},{"Name":"C","Age":29,"Salary":80000},{"Name":"D","Age":30,"Salary":300000}]


sum_of_salaries = reduce(lambda sum,x: sum+x ,list(map(lambda x:x[1]*x[1] ,list(filter(lambda x: x[0] >25 ,[[person["Age"],person["Salary"]] for person in list1])))))
print(sum_of_salaries)