import random

modelVector=[9,9,9,9,9,9,9,9,9,9]  # Modelo de vector a llegar(esperado).
largoIndividuo=10  # Número de elementos del vector

num = 10  # Cantidad de individuos
generaciones = 100  # Generaciones
seleccion_individuos = 3  # Individuos>2
mutacion_probabilidad = 0.2

def individuo(min, max):
    """LLenamos un vector con numeros aleatorios.
        Creacion de un individuo
    """
    return [random.randint(min,max) for i in range(largoIndividuo)]

def newPoblacion():
    """Creacion de un vector de vectores.
        Creacion de la poblacion de tamaño num.
    """
    return [individuo(0,9) for i in range(num)]

def funcion_objetivo(individuo):
    """Calcula el numero de coincidencias con el el modelVector de cada elemento."""
    aptitud=0
    for i in range(len(individuo)):
        if individuo[i]==modelVector[i]:
            """Comprobamos q un individuo en una posicion x tenga el valor igual al valor esperado"""
            aptitud+=1  # Numero maximo de aptitud = 10
    return aptitud
    
def seleccion_y_reproduccion(poblacion):
    evaluacion=[(funcion_objetivo(i),i) for i in poblacion]
    print("eval",evaluacion)
    evaluacion = [i[1] for i in sorted(evaluacion)]
    print("eval",evaluacion)
    poblacion=evaluacion
    selected=evaluacion[(len(evaluacion)-seleccion_individuos):]
    for i in range(len(poblacion)-seleccion_individuos): # i:[0,6]
        puntoCambio=random.randint(1,largoIndividuo-1)  # Devuelve un numero en el intervalo de [1,9]
        padre=random.sample(selected,2)
        poblacion[i][:puntoCambio]=padre[0][:puntoCambio]
        poblacion[i][puntoCambio:]=padre[1][puntoCambio:]
    return poblacion


def mutacion(poblacion):
    for i in range(len(poblacion)-seleccion_individuos):
        if random.random()<= mutacion_probabilidad:
            puntoCambio=random.randint(1,largoIndividuo-1)  # Devuelve un numero en el intervalo de [1,9]
            nuevo_valor=random.randint(0,9)  # Rango de nuevo_valor: [0,9]
            while nuevo_valor==poblacion[i][puntoCambio]:
                nuevo_valor=random.randint(0,9)
            poblacion[i][puntoCambio]=nuevo_valor
    return poblacion
# Main

poblacion=newPoblacion()
print("\nPoblacion Inicial: \n %s"%(poblacion))
print("numero de elemento de poblacion %s"%(len(poblacion)))
poblacion=seleccion_y_reproduccion(poblacion)
print("\nSeleccion:\n %s"%(poblacion))
print("numero de elemento de poblacion despues de reproduccion %s"%(len(poblacion)))