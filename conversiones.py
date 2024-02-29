import sys
#Son 5 argumentos ya que los indices empiezan en 0 y nosotros estamos utilizando desde 1
if(len(sys.argv)==5):
    diccionarioConversion = {"Soles":float(sys.argv[1])}
    diccionarioConversion["Pesos Argentinos"]=float(sys.argv[2])
    diccionarioConversion["Dólares"]=float(sys.argv[3])
    montoConvertir = int(sys.argv[4])
    
    print(f"Los {montoConvertir} pesos equivalen a:")
    for moneda,monto in diccionarioConversion.items():
        print(f"{monto*montoConvertir} {moneda}")
else:
    print("Por favor ejecutar con los siguientes argumentos: tasa de conversión a Soles, a Pesos Argentinos, a dólares y el monto a convertir.")

    