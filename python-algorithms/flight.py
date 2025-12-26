class Flight:
    def __init__(self, code, destination, departure_time, status):
        self.code = code
        self.destination = destination
        self.departure_time = departure_time
        self.status = status

        self.seats = ["_", "_", "X", "_", "_", "_", "X", "_", "_", "_"]


        self.gates_graph = {
            "Gate A": ["Gate B", "Gate C"],
            "Gate B": ["Gate A", "Gate D"],
            "Gate C": ["Gate A"],
            "Gate D": ["Gate B"]
        }

    # ------------------------------------------------------------
    # ALGORITHM 1: TWO POINTERS
    # ------------------------------------------------------------
    def find_seat_two_pointers(self, preference):
        left = 0
        right = len(self.seats) - 1

        while left <= right:
            if preference == "window":
                if self.seats[left] == "_":
                    return left
                if self.seats[right] == "_":
                    return right


            if preference == "aisle":
                mid = len(self.seats) // 2
                if self.seats[mid] == "_":
                    return mid

            left += 1
            right -= 1

        return None  # No seat found

    # ------------------------------------------------------------
    # ALGORITHM 2: SLIDING WINDOW
    # ------------------------------------------------------------
    def find_k_consecutive_seats(self, k):
        free = 0

        for i in range(k):
            if self.seats[i] == "_":
                free += 1

        if free == k:
            return 0

        for i in range(k, len(self.seats)):
            if self.seats[i] == "_":
                free += 1
            if self.seats[i - k] == "_":
                free -= 1

            if free == k:
                return i - k + 1

        return None

    # ------------------------------------------------------------
    # ALGORITHM 3: BINARY SEARCH
    # ------------------------------------------------------------
    def binary_search_seat(self, target):
        low = 0
        high = len(self.seats) - 1

        while low <= high:
            mid = (low + high) // 2

            if mid == target:
                return mid
            elif mid < target:
                low = mid + 1
            else:
                high = mid - 1

        return None

    # ------------------------------------------------------------
    # ALGORITHM 4: PREFIX SUM
    # ------------------------------------------------------------
    def prefix_sum_baggage(self, baggage_weights):
        prefix = [0]

        for weight in baggage_weights:
            prefix.append(prefix[-1] + weight)

        return prefix

    # ------------------------------------------------------------
    # ALGORITHM 5: BFS
    # ------------------------------------------------------------
    def bfs_nearest_gate(self, start, target):
        from collections import deque

        queue = deque([start])
        visited = set([start])

        while queue:
            gate = queue.popleft()
            if gate == target:
                return True

            for neighbor in self.gates_graph[gate]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False

    # ------------------------------------------------------------
    # ALGORITHM 6: DFS
    # ------------------------------------------------------------
    def dfs_paths(self, start, target, path=None):
        if path is None:
            path = []

        path = path + [start]

        if start == target:
            return [path]

        paths = []

        for neighbor in self.gates_graph[start]:
            if neighbor not in path:
                new_paths = self.dfs_paths(neighbor, target, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    # ------------------------------------------------------------
    # ASSIGN SEATS
    # ------------------------------------------------------------
    def assign_seat(self, passenger):
        seat = self.find_seat_two_pointers(passenger.seat_preference)

        if seat is None:
            return f"No available seat for {passenger.name}."

        self.seats[seat] = "X"
        return f"{passenger.name} assigned to seat {seat}."
