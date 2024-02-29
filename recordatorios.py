recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

#Enunciado dice: Agregue un evento el 2 de Febrero de 2021 a las 6 de la mañana para “Empezar el Año”. 
#Pero el resultado esperado es el 2021-01-02
recordatorios.append(["2021-01-02","06:00","Empezar el año"])
recordatorios.append(["2021-12-24","22:00","Cena de Navidad"])
recordatorios.append(["2021-12-31","22:00","Cena de Año Nuevo"])
actividad_eliminar =[]
for i, actividad in enumerate(recordatorios):
    if actividad[0] == "2021-07-15":
        #Actualizar registro
        actividad[0] = "2021-07-16"
        recordatorios[i] = actividad
    if actividad[0]=="2021-05-01":
        #Si elimino directamente no actualiza el registro de julio porque cambian los indices
        actividad_eliminar=actividad
recordatorios.remove(actividad_eliminar)

#Ordenar
recordatorios.sort()

#Print para hacer mas facil la comprobación
#for recordatorio in recordatorios:
#    print(recordatorio)

# Output
print(recordatorios)
