#Napisi definiciju koja ce da prikaze koji su brojevi prve desetice

lista=[]
    for broj in range(1, 11):
        print(broj)
        lista.append(broj)

print("lista brojeva je:",lista)