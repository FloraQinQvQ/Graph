class Node:
    def __init__(self, id):
        self.id = id
        self.children = []

    def add_edge(self, source, target):
        s = self._get_node(source)
        d = self._get_node(target)

        s.children.append(d)

    def dfs(source, target):
        s = self._get_node(source)
        d = self._get_node(target)

        visited = set()

        return _has_path_dfs(s, d, visited)

    def bfs(source, target):
        s = self._get_node(source)
        d = self._get_node(target)

        queue = []
        visited = set()

        queue.append(s)

        while len(queue) > 0:
            cur = queue.pop(0)

            if cur in visited:
                continue

            visited.add(cur)

            if cur.id == d.id:
                return True

            for child in s.children:
                queue.append(child)

        return False

    def _has_path_dfs(s, d, visited):
        if s in visited:
            return False

        visited.add(s)

        if (s.id == d.id):
            return True

        for child in s.children:
            if (self._has_path_dfs(child, d, visited)):
                return True

        return False

    def _get_node(self, id):
        pass

