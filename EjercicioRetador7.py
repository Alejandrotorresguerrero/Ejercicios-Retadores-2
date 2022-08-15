usuarios = {
  "ineId": [], 
  "nombre": [], 
  "edad": [], 
  "destino": [], 
  "preferente": []
}
x=0

salir = False
opcion = 0

while not salir:
  titulo = "MENU"
  print(titulo.center(60, "=")) 
  print()
  print ('\t [1]: Añadir Cliente'.upper())
  print ('\t [2]: Listar Clientes'.upper())
  print ('\t [3]: Clientes Preferentes'.upper())
  print ('\t [4]. Salir'.upper())
  print()
     
  opcion = int(input(' ELIGE UNA OPCION: '))
  
  if opcion == 1:
    x=0 
    print('Ingrese “X” en el ID del INE para salir')
  
    idIne=input('Ingrese Id del INE: ')
   
    while idIne != 'X':
      usuarios["ineId"].append(idIne)  #lista de Id de IFE
      nombre = input("Ingrese nombre: ")  # lista de nombres
      usuarios["nombre"].append(nombre)   # lista de nombres
      edad = input("Ingrese edad: ")
      usuarios["edad"].append(edad)       #Lista de edades
      iata = 'n'
      while iata =='n': 
        iata = input('Ingrese IATA de destino: ')
        if iata == 'BJX' or iata =='GDL' or iata == 'JAL':
          usuarios["destino"].append(iata)     #lista de destinos
        else:
          print('Destino Invalido')
          iata='n'
      usuarios["preferente"].append(input('Es cliente preferente? (Si/No): ').capitalize())   #lista de preferentes
      print('')
      x=x+1
      idIne = input('Ingrese Id del IFE: ')
  
    print('')
    
  elif opcion == 2:
    print("\nCLIENTES")
    for i in range(x):
      print("Id IFE:", usuarios["ineId"][i],"Cliente:", usuarios["nombre"][i])
      
  elif opcion == 3:
    print("\nCLIENTES PREFERENTES")
    for i in range(x):
      if usuarios["preferente"][i] == 'Si':
        print("Id IFE:", usuarios["ineId"][i],"Cliente:", usuarios["nombre"][i])
        
  elif opcion == 4:
    salir = True
  else:
    print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
