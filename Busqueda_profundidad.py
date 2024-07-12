def dfs(graph, start, target, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    if start == target:
        return [start]

    for neighbor in graph[start]:
        if neighbor not in visited:
            path = dfs(graph, neighbor, target, visited)
            if path:
                return [start] + path

    return None

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de grafo como un diccionario de listas de adyacencia
    graph = {
        'F': ['A', 'E', 'G'],
        'A': ['B', 'C', 'E', 'F'],
        'E': ['A', 'C', 'F', 'G'],
        'C': ['A', 'E'],
        'G': ['E', 'H'],
        'H': []
    }

    start_node = 'A'
    target_node = 'G'

    path = dfs(graph, start_node, target_node)

    if path:
        print("Ruta encontrada:", ' -> '.join(path))
    else:
        print("No se encontró una ruta entre los nodos especificados.")
