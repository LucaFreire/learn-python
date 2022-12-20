#Um programa que faça o fatorial de um número (for/while)

#for

num=int(input("Digite Seu Número: "))
fatorial=1

for i in range(1,num+1):
    fatorial*=i
   
    if num==i:
        print(i,end=" = ")
    else:
        print(i,end=" X ")
    
print(fatorial)                                                                                                                             

#while 

num=int(input("Digite Seu Número: "))

count=1
fatorial=1

print(1,end=" X ")
while count!=num:
    count+=1
    fatorial*=count

    if count==num:
        print(count,end=" = ")
    else:
        print(count,end=" X ")

print(fatorial)