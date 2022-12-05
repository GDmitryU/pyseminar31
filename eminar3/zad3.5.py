numb=int(input("номер элемента: "))
arrFib=[0]*(2*numb+1)
for ind in range(numb+1):
    if ind==0:
        arrFib[numb+ind]=0
    if ind==1:
        arrFib[numb+ind] = 1
        arrFib[numb-ind] = 1
    if ind > 1:
        arrFib[numb+ind] = arrFib[numb+ind-2]+arrFib[numb+ind-1]
        arrFib[numb-ind] = arrFib[(numb-ind)+2]-arrFib[(numb-ind)+1]
print(arrFib)

