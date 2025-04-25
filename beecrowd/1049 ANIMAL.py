p1 = input()
p2 = input()
p3 = input()

if (p1=="vertebrado"):
    if (p2=="ave"):
        if (p3=="carnivoro"):
            print("aguia")
        elif (p3=="onivoro"):
            print("pomba")
    elif (p2=="mamifero"):
        if (p3=="onivoro"):
            print("homem")
        if (p3=="herbivoro"):
            print("vaca")
if (p1=="invertebrado"):
    if (p2=="inseto"):
        if(p3=="hematofago"):
            print("pulga")
        elif(p3=="herbivoro"):
            print("lagarta")
    elif (p2=="anelideo"):
        if (p3=="hematofago"):
            print("sanguessuga")
        elif (p3=="onivoro"):
            print("minhoca")

# vertebrado = ("ave","mamifero")
#invertebrado = ("inseto","anelideo")

#inseto = ("hematofago","herbivoro")
#ave = ("carnivoro", "onivoro")
#mamifero = ("onivoro","herbivoro")
#anelideo = ("hematofago","onivoro")

#hematofago = ("pulga","sanguessuga")
#herbivoro = ("lagarta","vaca",)
#onivoro = ("minhoca","homem","pomba")
#carnivoro = ("aguia")
