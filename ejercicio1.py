import turtle

class Tablero:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.screen = turtle.Screen()
        self.screen.setup(width=400, height=400)

    def dibujar_tablero(self):
        # Dibujar las líneas verticales
        for i in range(-1, 2, 2):
            self.t.penup()
            self.t.goto(i * 100, -300)
            self.t.pendown()
            self.t.goto(i * 100, 300)
        
        # Dibujar las líneas horizontales
        for i in range(-1, 2, 2):
            self.t.penup()
            self.t.goto(-300, i * 100)
            self.t.pendown()
            self.t.goto(300, i * 100)
        
        self.t.hideturtle()

class Circulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self):
        t = turtle.Turtle()
        t.penup()
        t.goto(self.x, self.y - 50)
        t.pendown()
        t.circle(50)
        t.hideturtle()

class Cruz:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dibujar(self):
        t = turtle.Turtle()
        t.penup()
        t.goto(self.x - 50, self.y + 50)
        t.pendown()
        t.goto(self.x + 50, self.y - 50)
        t.penup()
        t.goto(self.x + 50, self.y + 50)
        t.pendown()
        t.goto(self.x - 50, self.y - 50)
        t.hideturtle()

# Ejecución del programa
tablero = Tablero()
tablero.dibujar_tablero()

# Dibujar un círculo en la posición central del tablero
circulo = Circulo(0, 0)
# circulo.dibujar()

# Dibujar una cruz en la esquina superior izquierda del tablero
cruz = Cruz(-200, 200)
# cruz.dibujar()

# Mantener la ventana abierta
turtle.done()
