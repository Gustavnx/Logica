cor1 = str("vermelho")
cor2 = str("verde")
cor3 = str("amarelo")
#lower.() minúsculo
#upper.() maiúsculo
#strip.() tira os espaços 

cor = str(input("ESCOLHA UMA COR ENTRE VERMELHO/ VERDE/ AMARELO: ")).lower().strip()

if cor1 == cor:
    print("PARE!!!")
elif cor2 == cor:
    print("ACELERA!!!")
elif cor3 == cor:
    print("ATENÇÃO!!!") 
else: 
    print("COR INVÁLIDA!!!")
