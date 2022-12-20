#Fibonacci

num=int(input("Digite seu Número: "))

count=0
a1=1
a2=1

while count!=num-3:
    if count==0:
        print("0 --> 1 --> 1 --> ",end=" ")

    a3=a1+a2

    a2=a1

    a1=a3

    print(a1,end=" --> ")

    count+=1

print("FIM")
