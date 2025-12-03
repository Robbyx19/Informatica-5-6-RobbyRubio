def main():
    respuesta = input("de que fruta te gustaria saber las calorias?")
    list = {
        "apple": [["calories", 130], ["sugars", 25], ["proteins", 1]],
        "avocado": 
        [["calories", 50],
          ["sugars", 0], 
          ["proteins", 1]],
        "banana": 
        [["calories", 110],
          ["sugars", 19], 
          ["proteins", 1]],
        "orange": 
        [["calories", 80],
          ["sugars", 14],
            ["proteins", 1]],
        "peach": 
        [["calories", 60],
          ["sugars", 13],
            ["proteins", 1]]
    }
    while True:

        try:
            
            
            for food in list[respuesta]:
                print(f"{food[0]}: {food[1]}") 
    
            break
              

            
         
        except ValueError:
             print("fruta no encontrada, intenta de nuevo")
main()

