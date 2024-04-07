from queue import PriorityQueue

'''
Write a python code to solve the following task using uniform cost search:
Three missionaries and three cannibals must cross a river with minimum cost using a
boat which can carry at most two people, under the constraint that, for both banks,
that the missionaries present on the bank cannot be outnumbered by cannibals. The
boat will charge Rs 10 for missionaries and Rs 20 for cannibals.
'''


class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False
        if self.missionaries > self.cannibals and self.missionaries < 3:
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0

    def successors(self):
        successors = []
        if self.boat == 'left':
            if self.missionaries >= 2:
                successors.append(State(self.missionaries - 2, self.cannibals, 'right'))
            if self.missionaries >= 1:
                successors.append(State(self.missionaries - 1, self.cannibals, 'right'))
            if self.cannibals >= 2:
                successors.append(State(self.missionaries, self.cannibals - 2, 'right'))
            if self.cannibals >= 1:
                successors.append(State(self.missionaries, self.cannibals - 1, 'right'))
            if self.missionaries >= 1 and self.cannibals >= 1:
                successors.append(State(self.missionaries - 1, self.cannibals - 1, 'right'))
        else:
            if self.missionaries <= 1:
                successors.append(State(self.missionaries + 1, self.cannibals, 'left'))
            if self.missionaries <= 2:
                successors.append(State(self.missionaries + 2, self.cannibals, 'left'))
            if self.cannibals <= 1:
                successors.append(State(self.missionaries, self.cannibals + 1, 'left'))
            if self.cannibals <= 2:
                successors.append(State(self.missionaries, self.cannibals + 2, 'left'))
            if self.missionaries <= 2 and self.cannibals <= 2:
                successors.append(State(self.missionaries + 1, self.cannibals + 1, 'left'))
        return successors

    def cost(self, successor):
        if self.boat == 'left':
            return 10 * (self.missionaries - successor.missionaries) + 20 * (self.cannibals - successor.cannibals)
        else:
            return 10 * (3 - self.missionaries - (3 - successor.missionaries)) + 20 * (3 - self.cannibals - (3 - successor.cannibals))

def uniform_cost_search():
    start_state = State(3, 3, 'left')
    if start_state.is_goal():
        return [start_state]
    frontier = PriorityQueue()
    frontier.put((0, [start_state]))
    explored = set()
    while not frontier.empty():
        cost, path = frontier.get()
        current_state = path[-1]
        if current_state.is_goal():
            return path
        explored.add(current_state)
        for successor in current_state.successors():
            if successor not in explored:
                new_cost = cost + current_state.cost(successor)
                new_path = path + [successor]
                frontier.put((new_cost, new_path))
    return []

solution = uniform_cost_search()
if solution:
    for i, state in enumerate(solution):
        print(f"Step {i+1}: {state.missionaries} missionaries, {state.cannibals} cannibals, boat on {state.boat} bank")
else:
    print("No solution found.")