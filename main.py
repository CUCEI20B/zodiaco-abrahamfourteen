def toInt(dia, mes):
  return (mes - 1) * 30 + dia

dia = int(input())
mes = int(input())
actual = toInt(dia, mes)
# print(actual)

signos = ["acuario", "piscis", "aries", "taurus", "geminis", "cancer", "leo", "virgo", "libra", "escorpio", "sagitario", "capricornio"]
fecha1 = [[21, 1], [19, 2], [21, 3], [21, 4], [21, 5], [22, 6], [23, 7], [23, 8], [23, 9], [23, 10], [23, 11], [22, 12]]
fecha2 = [[18, 2], [20, 3], [20, 4], [20, 5], [21, 6], [22, 7], [22, 8], [22, 9], [22, 10], [22, 11], [21, 12], [20, 1]]

for i in range(len(signos)):
  izq = toInt(fecha1[i][0], fecha1[i][1])
  der = toInt(fecha2[i][0], fecha2[i][1])
  # print(izq, der)
  if izq <= der and izq <= actual and actual <= der:
      print(signos[i])
      break
  else:
    # Cambia de año, entonces le subo un año a las fechas para hacer el tiempo circular
    if izq <= actual + 360 and actual + 360 <= der + 360:
      print(signos[i])
      break