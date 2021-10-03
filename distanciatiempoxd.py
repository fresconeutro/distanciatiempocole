def velocidad(distancia, tiempo):

  resultado = ""

  velocidad = distancia / tiempo

  a = round((float(velocidad) * 3600),6)

  b = round((float(velocidad) * 1000),6)

  resultado = str(a) +" " "km/h" " " "o" " " + str(b) +" " "m/s"
  print("La velocidad es", str(resultado))

  return resultado


distancia = 0.01

tiempo = 1

velocidad (distancia, tiempo)
