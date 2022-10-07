#la funcion init es el constructor de la clase, se ejecuta cuando se 
#instancia el objeto

class Animal:

    def __init__(self, especie, edad, color):
        self.especie = especie
        self.edad = edad
        self.color = color
    def mePresento(self):
        print('Hola, soy ', self.especie, ', de color ', self.color, 'y tengo', self.edad, 'años')
    def cumplirAños(self):
        self.edad = self.edad + 1

a1 = Animal('Ratón', 2, 'Marrón')
print(a1.especie)
print(a1.edad)

a2 = Animal('Liebre', 3, 'Gris')
print(a2.especie)
print(a2.edad)

a1.mePresento()
a2.mePresento()
a1.cumplirAños()
a1.mePresento()
