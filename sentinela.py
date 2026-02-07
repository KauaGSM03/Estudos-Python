servidor = input ("headtap")

espaco = float(input("Quanto de espaço resta (GB)?"))

if espaco < 10:
    #f-String; headtap

    print(f"Alerta: O servidor {servidor} está quase cheio")