class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque()
        visited = [[False]*(2**n) for _ in range(n)]
        end_state = (1 << n) - 1
        shortest_path = 0
        for i in range(n):
            queue.append((i, 1 << i))
            visited[i][(1 << i)] = True
        while(len(queue) > 0):
            level_searches = len(queue)
            for i in range(level_searches):
                u, bitmask = queue.popleft()
                if bitmask == end_state:
                    return shortest_path
                for v in graph[u]:
                    new_bitmask = bitmask | (1 << v)
                    if not visited[v][new_bitmask]:
                        if new_bitmask == end_state:
                            print("end found")
                            return shortest_path + 1
                        queue.append((v, new_bitmask))
                        visited[v][new_bitmask] = True
            shortest_path += 1
        return shortest_path