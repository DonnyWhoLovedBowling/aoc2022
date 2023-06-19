import heapq


def dijkstra(graph, source, end):
    priority_queue = []
    heapq.heappush(priority_queue, (0, source))
    visited = {}
    while priority_queue:
        (current_distance, current) = heapq.heappop(priority_queue)
        visited[current] = current_distance
        if current not in graph:
            continue
        if end in visited:
            return visited
        for neighbour, distance in graph[current].items():
            if neighbour in visited:
                continue
            if end in visited:
                break
            new_distance = current_distance + distance
            heapq.heappush(priority_queue, (new_distance, neighbour))

    return visited
