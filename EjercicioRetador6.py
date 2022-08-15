pasajeros = []; edad = []; destino = []
edadB = []; edadG =[]; edadJ=[]
listaOrdenada = []
pasajerosTotal = [];edadProm = []
####################INGRESO DE LOS DATOS####
cliente = input('Ingrese nombre: ')
while cliente != 'X':
  pasajeros.append(cliente)
  edad.append(int(input('Ingrese edad: ')))
  iata = 'n'
  while iata =='n': 
    iata = input('Ingrese IATA de destino: ')
    if iata == 'BJX' or iata =='GDL' or iata == 'JAL':
      destino.append(iata)
      print('')
    else:
      print('Destino Invalido')
      iata='n'
  cliente = input('Ingrese nombre: ')
print('')

datosCompletos=(list(zip(pasajeros,edad,destino)))#LISTA FORMADA
#####################EDADES##############
x=0
for list in datosCompletos:
  if list[2] == 'BJX':
    edadB.append(datosCompletos[x][1])
  elif list[2] == 'GDL':
    edadG.append(datosCompletos[x][1])
  elif list[2] == 'JAL':
    edadJ.append(datosCompletos[x][1])
  x=x+1
        ############CANTIDAD DE VUELOS POR DESTINO##########
bjx = destino.count('BJX')
gdl = destino.count('GDL')
jal = destino.count('JAL')
edadBjx=0
edadGdl=0
edadJal=0
if bjx != 0:
  edadBjx=sum(edadB)/bjx
if gdl != 0:
  edadGdl=sum(edadG)/gdl
if jal != 0:
  edadJal=sum(edadJ)/jal
######################ORDENADO DE MAYOR A MENOR#################
listaOrdenada.append(('BJX',bjx,edadBjx))
listaOrdenada.append(('GDL',gdl,edadGdl))
listaOrdenada.append(('JAL',jal,edadJal))
listaOrdenada.sort(reverse=True , key=lambda x:x[1])
###########LISTAS  A MOSTRAR##########3
for lista in listaOrdenada:
  pasajerosTotal.append(lista[0:2])
  edadProm.append(lista[0:3:2])
print('Detalles de Vuelos: ',pasajerosTotal)  
print('Edad Promedio de Vuelo: ',edadProm)
