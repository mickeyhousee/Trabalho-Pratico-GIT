def calcular_area_triangulo(base, altura):
  """
  Função para calcular a área de um triângulo.

  Argumentos:
    base: A base do triângulo (float).
    altura: A altura do triângulo (float).

  Retorno:
    A área do triângulo (float).
  """

  area = (base * altura) / 2
  return area

# Exemplo de uso
base = 5
altura = 10

area_triangulo = calcular_area_triangulo(base, altura)

print(f"A área do triângulo com base {base} e altura {altura} é {area_triangulo}")
