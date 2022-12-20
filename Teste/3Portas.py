def Portas():
    from random import choice as Esc
    
    Trocar=NTrocar=0
    
    Doors = ["Porta1","Porta2","Porta3"]
    
    for i in range(100):
        portaPc = Esc(Doors)
        
        if portaPc != Doors[0]: #Doors[0] = user
            Trocar+=1
            
        else: 
            NTrocar+=1

    print(f"Trocar: {Trocar}\nNão Trocar: {NTrocar}")

Portas()
