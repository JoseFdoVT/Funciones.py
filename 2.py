#Funcion de Saludo
def saludar(nombre):
  return f"Hola, {nombre}! ¿Cómo estás?"


print(saludar("Benling"))

#Funcion de suma
def sumar(a, b):
  return a + b


print(sumar(5, 3))
#Area de un Rectangulo
def area_rectangulo(base, altura):
  return base * altura


print(area_rectangulo(4, 5))
#Numero par o impar
def es_par(numero):
  return numero % 2 == 0


print(es_par(4))
print(es_par(7))
#conversion de grados celsius a fahrenheit
def celsius_a_fahrenheit(celsius):
  return (celsius * 9/5) + 32


print(celsius_a_fahrenheit(25))
#Maximo de tres numeros
def maximo_de_tres(a, b, c):
  return max(a, b, c)


print(maximo_de_tres(10, 5, 8))



#palidromo
def es_palindromo(texto):
  texto = texto.lower().replace(" ", "")
  return texto == texto[::-1]


print(es_palindromo("Anita lava la tina"))



#Factorial
def factorial(n):
  if n == 0 or n == 1:
      return 1
  else:
      return n * factorial(n-1)


print(factorial(5))
#Contar Vocales
def contar_vocales(texto):
  vocales = "aeiouAEIOU"
  return sum(1 for letra in texto if letra in vocales)


print(contar_vocales("Hola Mundo"))
#Numeros primos
def es_primo(numero):
  if numero < 2:
      return False
  for i in range(2, int(numero**0.5) + 1):
      if numero % i == 0:
          return False
  return True


print(es_primo(17))
print(es_primo(4))
