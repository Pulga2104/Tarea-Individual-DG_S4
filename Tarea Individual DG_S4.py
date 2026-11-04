import time
from collections import deque

# Definición del estado inicial y objetivo
ESTADO_INICIAL = (3, 3, 1)
ESTADO_OBJETIVO = (0, 0, 0)

# Conjunto de acciones: (misioneros_en_bote, canibales_en_bote)
ACCIONES = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def es_valido(estado):
    m, c, b = estado
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False
    # Validar orilla izquierda
    if m > 0 and m < c:
        return False
    # Validar orilla derecha
    m_der, c_der = 3 - m, 3 - c
    if m_der > 0 and m_der < c_der:
        return False
    return True

def obtener_sucesores(estado):
    sucesores = []
    m, c, b = estado
    for m_bote, c_bote in ACCIONES:
        if b == 1:
            nuevo_estado = (m - m_bote, c - c_bote, 0)
        else:
            nuevo_estado = (m + m_bote, c + c_bote, 1)
            
        if es_valido(nuevo_estado):
            sucesores.append(nuevo_estado)
    return sucesores

def bfs():
    inicio_tiempo = time.perf_counter()
    cola = deque([(ESTADO_INICIAL, [])])
    visitados = set([ESTADO_INICIAL])
    nodos_expandidos = 0
    
    while cola:
        estado_actual, camino = cola.popleft()
        nodos_expandidos += 1
        
        if estado_actual == ESTADO_OBJETIVO:
            fin_tiempo = time.perf_counter()
            return camino, nodos_expandidos, (fin_tiempo - inicio_tiempo)
            
        for sucesor in obtener_sucesores(estado_actual):
            if sucesor not in visitados:
                visitados.add(sucesor)
                cola.append((sucesor, camino + [sucesor]))
                
    return None, nodos_expandidos, 0

def dfs():
    inicio_tiempo = time.perf_counter()
    pila = [(ESTADO_INICIAL, [])]
    visitados = set([ESTADO_INICIAL])
    nodos_expandidos = 0
    
    while pila:
        estado_actual, camino = pila.pop()
        nodos_expandidos += 1
        
        if estado_actual == ESTADO_OBJETIVO:
            fin_tiempo = time.perf_counter()
            return camino, nodos_expandidos, (fin_tiempo - inicio_tiempo)
            
        for sucesor in reversed(obtener_sucesores(estado_actual)):
            if sucesor not in visitados:
                visitados.add(sucesor)
                pila.append((sucesor, camino + [sucesor]))
                
    return None, nodos_expandidos, 0

# Ejecución y Benchmarking
camino_bfs, nodos_bfs, tiempo_bfs = bfs()
camino_dfs, nodos_dfs, tiempo_dfs = dfs()

print("-" * 65)
print(f"{'Algoritmo':<15} | {'Nodos Expandidos':<18} | {'Tiempo (s)':<15} | {'Longitud Camino'}")
print("-" * 65)
print(f"{'BFS (Cola)':<15} | {nodos_bfs:<18} | {tiempo_bfs:<15.6f} | {len(camino_bfs)}")
print(f"{'DFS (Pila)':<15} | {nodos_dfs:<18} | {tiempo_dfs:<15.6f} | {len(camino_dfs)}")
print("-" * 65)