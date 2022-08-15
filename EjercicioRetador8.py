def agregarClientes():
  x=0
  print('Ingrese “X” en el ID del INE para salir')
  idIne=int(input('Ingrese Id del INE: '))
  while idIne != 'X':
      nombre = input("Ingrese nombre: ") 
      edad = int(input("Ingrese edad: "))
      iata = 'n'
      while iata =='n': 
        iata = input('Ingrese IATA de destino: ')
        if iata == 'BJX' or iata =='GDL' or iata == 'JAL':
          destino = iata
        else:
          print('Destino Invalido')
          iata='n'
      preferente = (input('Es cliente preferente? (Si/No): ').capitalize())   #lista de preferentes
      if preferente == 'Si':
        preferente = True
      else:
        preferente = False
      print('')
      x=x+1
      clientes[idIne]= [nombre, edad, destino, preferente]
      idIne = input('Ingrese Id del IFE: ')
  print('') 

def mostrarClientes():
  for key in clientes:
    print (key, ":", clientes[key])
    #print (clientes[key][0])

def clientesPreferentes():
  for key in clientes:
    if clientes[key][3] == True:
      print (key, ":", clientes[key])
      #print (clientes[key][3])

def eliminarClientes():
  mostrarClientes()
  idIne = int(input('\nIngrese Id a eliminar: '))
  if idIne in clientes.keys():
    print('Cliente: ', clientes[idIne], 'eliminado')
    del(clientes[idIne])
  else:
    print('Cliente no existe')
def edadPromedioTotal():
  prom =[]
  for key in clientes:
    prom.append(clientes[key][1])
  print('La edad promedio de todos los clientes es:',sum(prom))
  
def edadPromedioPreferente():
  prom =[]
  for key in clientes:
    if clientes[key][3] == True:
      prom.append(clientes[key][1])
  print('La edad promedio de todos los clientes es:',sum(prom))

clientes={
  45471:["Luis Perez",45,'BJX', True], 
  8944411:["Fernanda Garcia",25,'JAL', False], 
  15223:["Alejandra Ortiz",33,'GDL', True]}

salir = False
opcion = 0

while not salir:
  titulo = "MENU"
  print(titulo.center(60, "=")) 
  print()
  print ('\t [1]: Añadir Clientes'.upper())
  print ('\t [2]: Listar Clientes'.upper())
  print ('\t [3]: Clientes Preferentes'.upper())
  print ('\t [4]: Eliminar Clientes'.upper())
  print ('\t [5]: Edad promedio Clientes '.upper())
  print ('\t [6]: Edad Promedio Clientes Preferentes'.upper())
  print ('\t [7]. Salir'.upper())
  print()
     
  opcion = int(input(' ELIGE UNA OPCION: '))
  
  if opcion == 1:
    agregarClientes()
  elif opcion == 2:
    mostrarClientes()
  elif opcion == 3:
    clientesPreferentes()
  elif opcion == 4:
    eliminarClientes()
  elif opcion == 5:
    edadPromedioTotal()
  elif opcion == 6:
    edadPromedioPreferente()
  elif opcion == 7:
    salir = True
  else:
    print ("Introduce un numero entre 1 y 3")
 
print ("Fin")
