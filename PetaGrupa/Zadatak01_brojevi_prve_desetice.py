#Napisi definiciju koja ce da prikaze koji su brojevi prve desetice


lista = []
def prvaDesetica ():
    for x in range (1,11):
        lista.append (x)
    return lista
print ("Brojevi prve desetice su: ",prvaDesetica())
