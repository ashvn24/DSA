list1=[1,2,3,4,5]


result=lambda num: [i*i for i in num]

res=result(list1)
print(res)


resu=[i**2 if i%2==0 else i**3 for i in list1]
print(resu)