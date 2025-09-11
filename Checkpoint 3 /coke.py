nombre = input("Por favor, escribe tu nombre: ")
costo_coke = 50
monedas_insertadas = 0

while monedas_insertadas < costo_coke:
    restante = costo_coke - monedas_insertadas
    print("Monto restante:", restante)
    
    moneda = int(input("Inserta una moneda: "))
    
    if moneda == 25 or moneda == 10 or moneda == 5:
        monedas_insertadas = monedas_insertadas + moneda

cambio_devuelto = monedas_insertadas - costo_coke
print("Cambio devuelto:", cambio_devuelto)

print("¡Aquí tienes una Coca-Cola para", nombre, "!")

print("""
        _                                   
      .!.!.                             
       ! !                                   
       ; :                                
      ;   :                                
     ;_____:                                 
     ! Coke!                                 
     !_____!                                 
     :     :
     :     ;                                       
     .'   '.                             
     :     :                          
      '''''
""")
