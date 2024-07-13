import turtle

class Jugador:
    def __init__(self, tipo):
        self.tipo = tipo
        self.valor = 0 if tipo == 'jugador' else 1

class Dibujo:
    def __init__(self, cell_size=200):
        self.cell_size = cell_size

    def dibujar_circulo(self, x, y):
        t = turtle.Turtle()  # Creamos un nuevo objeto Turtle para dibujar el círculo.
        t.penup()
        t.goto(x, y - self.cell_size // 2)
        t.pendown()
        t.circle(self.cell_size // 2)
        t.hideturtle()  # Ocultamos el objeto Turtle.

    def dibujar_cruz(self, x, y):
        t = turtle.Turtle()  # Creamos un nuevo objeto Turtle para dibujar la cruz.
        t.penup()
        t.goto(x - self.cell_size // 2, y + self.cell_size // 2)  # Movemos el lápiz al punto inicial de la cruz.
        t.pendown()
        t.goto(x + self.cell_size // 2, y - self.cell_size // 2)  # Dibujamos la primera línea diagonal de la cruz.
        t.penup()
        t.goto(x + self.cell_size // 2, y + self.cell_size // 2)  # Movemos el lápiz al punto inicial de la segunda línea.
        t.pendown()
        t.goto(x - self.cell_size // 2, y - self.cell_size // 2)  # Dibujamos la segunda línea diagonal de la cruz.
        t.hideturtle()

    def dibujar_punto(self, x, y):
        t = turtle.Turtle()  # Creamos un nuevo objeto Turtle para dibujar el punto.
        t.penup()
        t.goto(x, y)
        t.dot(10)  # Dibujamos un punto de tamaño 10.
        t.hideturtle()  # Ocultamos el objeto Turtle.

    def dibujar_linea_ganadora(self, x1, y1, x2, y2):
        t = turtle.Turtle()
        t.pencolor("red")  # Establecemos el color de la línea a rojo.
        t.pensize(5)  # Establecemos el grosor de la línea.
        t.penup()
        t.goto(x1, y1)  # Movemos el lápiz al primer punto de la línea.
        t.pendown()
        t.goto(x2, y2)  # Dibujamos la línea hasta el último punto.
        t.hideturtle()

class Tablero:
    def __init__(self, size=400):
        self.t = turtle.Turtle()  # Creamos un objeto Turtle para dibujar.
        self.t.speed(0)  # Establecemos la velocidad de dibujo al máximo.
        self.screen = turtle.Screen()  # Creamos una ventana gráfica.
        self.screen.setup(width=400, height=400)  # Configuramos el tamaño de la ventana.
        self.cell_size = size // 2  # Definimos el tamaño de cada celda del tablero.

    def dibujar_tablero(self):
        # Dibujamos las líneas verticales del tablero.
        for i in range(-1, 2, 2):
            self.t.penup()  # Levantamos el lápiz para movernos sin dibujar.
            self.t.goto(i * 100, -300)  # Movemos el lápiz a la posición inicial de la línea.
            self.t.pendown()  # Bajamos el lápiz para empezar a dibujar.
            self.t.goto(i * 100, 300)  # Dibujamos la línea vertical.

        # Dibujamos las líneas horizontales del tablero.
        for i in range(-1, 2, 2):
            self.t.penup()
            self.t.goto(-300, i * 100)
            self.t.pendown()
            self.t.goto(300, i * 100)

        self.t.hideturtle()  # Ocultamos el objeto Turtle para que no se vea en el tablero.

    def get_cell_centers(self):
        centers = []  # Lista para almacenar los centros de las celdas.
        offset = self.cell_size  # Offset para calcular las posiciones de los centros.
        for i in range(-1, 2):  # Recorremos las filas del tablero.
            for j in range(-1, 2):  # Recorremos las columnas del tablero.
                centers.append((i * offset, j * offset))  # Añadimos el centro de la celda a la lista.
        return centers  # Devolvemos la lista de centros de las celdas.

class Juego:
    def __init__(self, primer_turno):
        self.turno = primer_turno  # Variable para controlar el turno: 0 para círculo, 1 para cruz.
        self.ocupadas = []  # Lista para registrar las celdas ocupadas.
        self.prime_2 = []  # Lista para registrar las celdas ocupadas por círculos.
        self.prime_3 = []  # Lista para registrar las celdas ocupadas por cruces.
        self.ganado = False  # Variable para indicar si alguien ha ganado.
        self.numero_jugadas = 0  # Variable para almacenar la cantidad de jugadas.
        self.tablero = Tablero()
        self.dibujo = Dibujo(self.tablero.cell_size)
        self.centros = self.tablero.get_cell_centers()  # Obtenemos los centros de las celdas.
        self.jugadas = ' ' * 9  # Cadena para registrar las jugadas.

    def verificar_victoria(self, lista):
        # Lista de condiciones ganadoras (filas, columnas y diagonales).
        condiciones_ganadoras = [
            [(0, 0), (0, 1), (0, 2)],  # Fila superior
            [(1, 0), (1, 1), (1, 2)],  # Fila central
            [(2, 0), (2, 1), (2, 2)],  # Fila inferior
            [(0, 0), (1, 0), (2, 0)],  # Columna izquierda
            [(0, 1), (1, 1), (2, 1)],  # Columna central
            [(0, 2), (1, 2), (2, 2)],  # Columna derecha
            [(0, 0), (1, 1), (2, 2)],  # Diagonal principal
            [(0, 2), (1, 1), (2, 0)]   # Diagonal secundaria
        ]
        for condicion in condiciones_ganadoras:  # Recorremos cada condición ganadora.
            if all(celda in lista for celda in condicion):  # Verificamos si todas las celdas de la condición están en la lista del jugador.
                return condicion  # Si hay una condición ganadora, la devolvemos.
        return None  # Si no hay ninguna condición ganadora, devolvemos None.

    def obtener_celda(self, x, y):
        # Función para obtener la celda en la que se hizo clic.
        for i, centro in enumerate(self.centros):
            cx, cy = centro
            # Verificamos si las coordenadas (x, y) están dentro de los límites de la celda centrada en (cx, cy).
            if abs(x - cx) < self.tablero.cell_size // 2 and abs(y - cy) < self.tablero.cell_size // 2:
                return i // 3, i % 3  # Devolvemos las coordenadas de la celda en formato (fila, columna).
        return None  # Si no se encuentra ninguna celda, devolvemos None.

    def manejar_click(self, x, y):
        # Función para manejar el evento de clic.
        if self.ganado:  # Si alguien ya ha ganado, no hacemos nada.
            return

        celda = self.obtener_celda(x, y)  # Obtenemos la celda en la que se hizo clic.
        if celda is None or celda in self.ocupadas:  # Si la celda no es válida o ya está ocupada, no hacemos nada.
            return

        self.ocupadas.append(celda)  # Añadimos la celda a la lista de ocupadas.
        fila, columna = celda
        x, y = self.centros[fila * 3 + columna]  # Obtenemos las coordenadas del centro de la celda.

        if self.turno == 0:  # Si es el turno del círculo:
            self.dibujo.dibujar_circulo(x, y)  # Dibujamos un círculo en la celda.
            self.prime_2.append(celda)  # Añadimos la celda a la lista de círculos.
            self.jugadas = self.jugadas[:fila * 3 + columna] + 'O' + self.jugadas[fila * 3 + columna + 1:]  # Registramos la jugada en la cadena.
            condicion_ganadora = self.verificar_victoria(self.prime_2)  # Verificamos si hay una condición ganadora para los círculos.
            if condicion_ganadora:
                print("¡Círculo ha ganado!")  # Mostramos un mensaje indicando que el círculo ha ganado.
                x1, y1 = self.centros[condicion_ganadora[0][0] * 3 + condicion_ganadora[0][1]]
                x2, y2 = self.centros[condicion_ganadora[2][0] * 3 + condicion_ganadora[2][1]]
                self.dibujo.dibujar_linea_ganadora(x1, y1, x2, y2)  # Dibujamos la línea ganadora.
                self.ganado = True  # Establecemos que alguien ha ganado para terminar el ciclo.
            self.turno = 1  # Cambiamos el turno a la cruz.
        else:
            self.dibujo.dibujar_cruz(x, y)  # Dibujamos una cruz en la celda.
            self.prime_3.append(celda)  # Añadimos la celda a la lista de cruces.
            self.jugadas = self.jugadas[:fila * 3 + columna] + 'X' + self.jugadas[fila * 3 + columna + 1:]  # Registramos la jugada en la cadena.
            condicion_ganadora = self.verificar_victoria(self.prime_3)  # Verificamos si hay una condición ganadora para las cruces.
            if condicion_ganadora:
                print("¡Cruz ha ganado!")  # Mostramos un mensaje indicando que la cruz ha ganado.
                x1, y1 = self.centros[condicion_ganadora[0][0] * 3 + condicion_ganadora[0][1]]
                x2, y2 = self.centros[condicion_ganadora[2][0] * 3 + condicion_ganadora[2][1]]
                self.dibujo.dibujar_linea_ganadora(x1, y1, x2, y2)  # Dibujamos la línea ganadora.
                self.ganado = True  # Establecemos que alguien ha ganado para terminar el ciclo.
            self.turno = 0  # Cambiamos el turno al círculo.

        self.numero_jugadas += 1  # Incrementamos la cantidad de jugadas.

        print(f'{self.jugadas}')  # Imprimimos la cadena de jugadas actual.

        if not self.ganado and self.numero_jugadas == 9:
            print("¡Ha habido un empate!")  # Se dice que nadie ha ganado.
            self.ganado = True  # Se termina el juego.

# Función principal que inicia el juego.
def main():
    screen = turtle.Screen()
    # Preguntamos quién quiere empezar.
    while True:
        turno = screen.textinput("Turno inicial", "¿Quién quiere empezar? (circulo/cruz): ").strip().lower() # Con funciones strip quitamos espacios y con funcion lower hacemos todo en minusculas
        # Se definen los turnos.
        if turno == "circulo": 
            primer_turno = 0
            jugador = Jugador('jugador')
            ia = Jugador('IA')
            break
        elif turno == "cruz":
            primer_turno = 1
            jugador = Jugador('jugador')
            ia = Jugador('IA')
            break
        else:
            print("Entrada no válida. Intente de nuevo")


    juego = Juego(primer_turno)
    juego.tablero.dibujar_tablero()  # Dibujamos el tablero.

    # Obtener y mostrar las posiciones de las celdas
    centros = juego.centros  # Obtenemos los centros de las celdas.
    for centro in centros:
        print(f'Centro de la celda: {centro}')  # Mostramos las coordenadas del centro de la celda.
        juego.dibujo.dibujar_punto(centro[0], centro[1])  # Dibujamos un punto en el centro de la celda.

    juego.tablero.screen.onclick(juego.manejar_click)  # Configuramos el evento de clic para la pantalla.
    turtle.done()  # Mantenemos la ventana abierta.

main()
