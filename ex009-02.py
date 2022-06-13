cont=1

while cont != 0:
    num=int(input("Digite o numero da tabuada que deseja ou 0 para sair: "))
    cont=num
    if num != 0:
        if num <= 10:
            for count in range(10):
                print("%d x %d = %d" % (num, count+1, num*(count+1)))
        else:
            print("Numero tem que ser menor ou igual a 10")
    else:
        print("Fim da tabuada")