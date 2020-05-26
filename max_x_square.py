import random


class Main:
    filas = 6
    columnas = 5
    nGanadores = 3
    nGenes = 5  # Numeros en el rango [0,31]
    poblacion = []
    poblacionTemp = []
    parejas = []
    ganadores = []
    sumatoria = 0
# Custom methods

    def PoblacionInicial(self):
        print("******************************************************")
        print("************************Iniciando Poblacion***********************")
        print("******************************************************")
        individuo = ""
        r = random
        for i in range(self.filas):
            individuo = ""
            aux = []
            for j in range(self.nGenes):
                individuo += str(r.randint(0, 1))+","
            self.poblacion[i][0] = str(i)
            self.poblacion[i][1] = str(individuo)

    def convertir_individuo(self):
        valorInteger = 0
        for i in range(self.filas):
            valorInteger = 0
            valores = self.poblacion[i][1].split(",")
            valores.pop()
            valores.reverse()
            indice = 0
            aux = []
            for j in range(len(valores)):
                valorInteger = valorInteger + (float(valores[j])*(2**indice))
                indice += 1

            self.poblacion[i][2] = str(valorInteger)

    def funcion_Fx(self, x):
        return x*x

    def calidad_individuo(self):
        mayor = float(self.poblacion[0][2])
        valor = 0
        aux = []
        for i in range(self.filas):
            valor = self.funcion_Fx(float(self.poblacion[i][2]))
            # aux = self.poblacion[i][:]
            # aux.append(str(valor))
            # self.poblacion[i] = aux
            self.poblacion[i][3] = str(valor)
            self.sumatoria += valor
            if mayor < valor:
                mayor = valor
        print("*********************** Individuo mas Apto *******************")
        print("--> "+str(mayor))
        return mayor

    def cruce_mutacion(self):
        print("*********************** Cruce y Mutacion ************************")
        print("_________________________________________________________________")
        r = random
        puntoCruce = 0
        individuoA = []
        individuoB = []
        parejaA = ""
        # Cruce
        for i in range(self.filas//2):
            individuoA = self.poblacion[i][1].split(",")
            individuoA.pop()
            parejaA = self.parejas[i]
            cadAdn = ""
            individuoB = self.poblacion[int(parejaA)][1].split(",")
            individuoB.pop()
            puntoCruce = r.randint(0, 3)
            print("punto de cruce: ["+str(puntoCruce)+"]- posicion individuoA: ["+self.poblacion[i][0]+"]- IndividuoA : ["+self.poblacion[i][1] +
                  "] --> Cruza con: Posicion individuoB: ["+self.poblacion[int(parejaA)][0]+"] -  IndividuoB: ["+self.poblacion[int(parejaA)][1]+"]")

            for j in range(puntoCruce):
                cadAdn += individuoA[j]+","
            print(cadAdn)
            for j in range(puntoCruce, len(individuoA)):
                cadAdn += individuoB[j]+","
            print("******************* Nuevo Individuo " +
                  cadAdn + "*******************")
            self.poblacionTemp[i][0] = str(i)
            self.poblacionTemp[i][1] = cadAdn
        for i in range(len(self.parejas)):
            self.poblacion[i][0] = self.poblacionTemp[i][0]
            self.poblacion[i][1] = self.poblacionTemp[i][1]

        # Mutacion
        mutado = (len(self.parejas)//2)+1
        individuoA = self.poblacion[mutado][1].split(",")
        individuoA.pop()
        print("*********************** Mutacion **********************")
        print("****** Individuo ***************** Resultado ***********")
        gen = r.randint(0, 4)
        if individuoA[gen] == "0":
            individuoA[gen] = "1"
        else:
            individuoA[gen] = "0"
        cadAdn = ""
        cadAdn += ",".join(individuoA)+","
        print("[" + self.poblacion[mutado][0] + "]-[" + self.poblacion[mutado][1] + "]" + " Posicion gen Mutado: ["
              + str(gen) + "] Resultado => Posicion individuo [" + self.poblacion[mutado][0] + "]-[" + cadAdn + "]")
        self.poblacion[mutado][1] = cadAdn

    def copiarse(self):
        print("***************** Copiarse ************************")
        indice = 0
        t = 0
        for i in range(len(self.ganadores)):
            ganador = int(self.ganadores[i])
            self.poblacionTemp[indice][0] = str((i+t))
            self.poblacionTemp[indice+1][0] = str(i+t+1)
            for j in range(1, self.columnas):
                self.poblacionTemp[indice][j] = self.poblacion[ganador][j]
                self.poblacionTemp[indice+1][j] = self.poblacion[ganador][j]
            indice += 2
            t += 1
        for i in range(self.filas):
            self.poblacion[i][0] = self.poblacionTemp[i][0]
            self.poblacion[i][1] = self.poblacionTemp[i][1]

    def ver_ganadores(self):
        print("*************** Ganadores ****************")
        win = 0
        for i in range(len(self.ganadores)):
            win = int(self.ganadores[i])
            print("[" + self.poblacion[win][0] + "][" + self.poblacion[win][1] + "][" + self.poblacion[win][2] + "]["
                  + self.poblacion[win][3] + "]")

    def torneo(self):
        print("***************** Torneo *********************")
        desempenoA = ""
        parejaA = ""
        desempenoB = ""
        indP = 0
        for i in range(self.filas//2):
            desempenoA = self.poblacion[i][3]
            parejaA = self.parejas[i]
            desempenoB = self.poblacion[int(parejaA)][3]
            print("[" + self.poblacion[i][0] + "][" + self.poblacion[i][1] + "][" + self.poblacion[i][2] + "]["
                  + desempenoA +
                  "] contra => [" +
                  self.poblacion[int(parejaA)][0] + "]["
                  + self.poblacion[int(parejaA)][1] + "][" +
                  self.poblacion[int(parejaA)][2] + "]["
                  + str(desempenoB) + "]")
            if float(desempenoA) >= float(desempenoB):
                self.ganadores[indP] = self.poblacion[i][0]
            else:
                self.ganadores[indP] = parejaA
            indP += 1

    def seleccion_parejas(self):
        self.parejas = []
        print("**************************************************************")
        print("****************** Seleccion de Parejas ******************")
        for i in range(self.filas):
            self.parejas.append(self.poblacion[i][0])
        self.parejas.reverse()
        # self.parejas[(self.filas-1)-i] = self.poblacion[i][0]

        # print("Seleccion de Parejas test: ", self.parejas)

    def adaptabilidad(self):
        aux = []
        for i in range(self.filas):
            self.poblacion[i][4] = str(
                float(self.poblacion[i][3])/self.sumatoria)

    def ver_poblacion(self, _poblacion, pareja):
        print("***************** Poblacion Actual *********************")
        cadena = ""
        for i in range(self.filas):
            for j in range(self.columnas):
                cadena += "[" + _poblacion[i][j] + "]"
            if pareja:
                cadena += "Pareja " + self.parejas[i] + "\n"
            else:
                cadena += "" + "\n"
        print(cadena)

    def llenar(self):
        for i in range(self.filas):
            self.parejas.append("null")
        for i in range(self.nGanadores):
            self.ganadores.append("null")
        # for i in range(self.nGanadores):
        #     self.ganadores.append("null")
        # for i in range(self.filas):
        #     lista = []
        #     for j in range(self.columnas):
        #         lista.append("")
        #     self.poblacionTemp.append(lista)
        # for i in range(self.filas):
        #     lista = []
        #     for j in range(self.columnas):
        #         lista.append("")
        #     self.poblacion.append(lista)

    def llenarPoblacion(self):
        for i in range(self.filas):
            lista = []
            for j in range(self.columnas):
                lista.append("")
            self.poblacion.append(lista)
        for i in range(self.filas):
            lista = []
            for j in range(self.columnas):
                lista.append("")
            self.poblacionTemp.append(lista)


if __name__ == "__main__":

    c = Main()
    c.llenarPoblacion()
    c.PoblacionInicial()
    adaptados = 0
    c.llenar()
    while adaptados < 961:
        c.convertir_individuo()
        adaptados = c.calidad_individuo()
        c.adaptabilidad()
        c.ver_poblacion(c.poblacion, True)
        c.seleccion_parejas()
        c.torneo()
        c.ver_ganadores()
        c.copiarse()
        c.ver_poblacion(c.poblacionTemp, True)
        c.seleccion_parejas()
        c.cruce_mutacion()

    c.poblacion = c.poblacionTemp
    adaptados = c.calidad_individuo()
    c.ver_poblacion(c.poblacion, False)
