#funciones principales

def añadir(matricula,modelo):
    matricula=input("Ingrese la matrícula de la nueva aeronave: ")
    modelo=input("Ingrese el modelo de la aeronave: ")
    ra[matricula] = {
        "modelo": modelo ,
        "horasdevuelo": 0 , 
    }
    p[matricula] = {
        "motor": 0,
        "tren": 0,
        "estabilizadores": 0
    }
    return ra[matricula],p[matricula]

def modificacion(matricula,parte):
    lipichita = []
    matricula = input("ingrese la matricula de la aeronave: ")
    parte = input ("ingrese el componente: ")
    
    horasant = int(input("Ingrese cuantas horas suma el componente: ")) #horas anteriores
    lim = p[matricula][parte] + horasant
    p[matricula][parte] = horasant
    if lim >= 200:
        print("Se ha llegado al limite de ahoras maximas antes del mantenimiento")
        p[matricula][parte] = 0
        lipichita.append(print(f"/{matricula},{parte}/"))
    
    return p[matricula][parte],lipichita

def hadv(matricula,horasdevuelo):
    matricula=input("Ingrese la matrícula de la aeronave: ")
 
    hva = int(input("Ingrese el incremento en las horas de vuelo: "))
    ra[matricula][horasdevuelo] += hva
    print(f"se han añadido {hva}h acicionales a la aeronave de matrícula {matricula}")
    return hva

#def ingrepartes(matricula,nuevaparte):
#    matricula=input("Ingrese la matrícula de la aeronave: ")
#    nuevaparte = str(input("Ingrese el nuevo componente: "))
#    if matricula in p:
#        p[matricula] = nuevaparte
#        p[matricula][nuevaparte] = 0
#    else:
#        print("La matricula no se encuentra en el registro de aeronaves")
#    return p[matricula][nuevaparte]

        
#registro de aeronaves
ra  = {
    "HK1" : {
            "modelo": "B737",
            "horas de vuelo": 0
        },
        
    "HK2" : {
            "modelo": "A320",
            "horas de vuelo": 0
        }
}
#programado mantenimiento
p = {
   "HK1" :{
           "motor": 0,
           "tren": 0,
           "estabilizadores": 0
        },
    "HK2" :{
           "motor": 0,
           "tren": 0,
           "estabilizadores": 0
        }       
}



lista = ["1.Añadir aeronave","2.Modificar horas de componente", "3.Anadir horas de vuelo","4.SALIR"]

u = True

while u == True:
    
    print(lista)
    print(f"\n")
    menu = int(input("Seleccione una opcion: "))
    sel = menu  - 1
   
    if sel == 0:
        print(f"\n")
        z = añadir("matricula","modelo")
        print(f"{z}")
        
    elif sel == 1:
        print(f"\n")
        i = modificacion("matricula","parte")
        print(f"{p}")
        
    elif sel == 2:
        print(f"\n")
        k = hadv("matricula","horasdevuelo")

#    elif sel == 3:
#        print(f"\n")
#        l = ingrepartes("matricula","nuevaparte")

    elif sel == 3:
        u = False
