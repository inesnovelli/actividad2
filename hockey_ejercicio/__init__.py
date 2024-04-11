# función para generar la estructura de datos con las estadísticas de los jugadores y jugadoras 
def construir_estadisticas(names, goals, goals_avoided, assists):
    estadisticas = []
    for nombre, goles, goles_evitados, asistencias in zip(names, goals, goals_avoided, assists):
        jugador = { 'nombre': nombre, 'goles': goles, 'goles_evitados': goles_evitados,'asistencias': asistencias}
        estadisticas.append(jugador)
    return estadisticas

# función para obtener el nombre del goleador/a y la cantidad de goles que realizó
def encontrar_goleador(estadisticas):
    goleador = max(estadisticas, key=lambda x: x['goles'])
    return goleador['nombre'], goleador['goles']

# función para obtener el nombre del jugador/a más influyente
def jugador_mas_influyente(estadisticas):
    influyente = max(estadisticas, key=lambda x: (x['goles'] * 1.5) + (x['goles_evitados'] * 1.25) + x['asistencias'] * 1)
    return influyente['nombre']

# función para obtener el promedio de goles por partido del equipo en general. (25 partidos en la temporada)
def promedio_goles_equipo(goals):
    total_goles = sum(goals)
    return total_goles / 25

# función para obtener el promedio de goles por partido del goleador/a. (25 partidos en la temporada)
def promedio_goles_goleador(goles_goleador):
    return goles_goleador / 25