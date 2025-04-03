def sum_of_pairs(num):
    for i in range(len(num)-1):
        yield num[i] + num[i+1]
    
num = [1,2,3,4,5,2]
sum = list(sum_of_pairs(num))
print(sum)
