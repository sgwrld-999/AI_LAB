from Queue import PriorityQueue

def is_valid_state(state):
    missionaries, cannibals, boat = state
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False
    if missionaries > 0 and missionaries < cannibals:
        return False
    if missionaries < 3 and (3 - missionaries) < (3 - cannibals):
        return False
    return True

def get_next_states(state):
    states = []
    missionaries, cannibals, boat = state

    if boat == 'left':
        for i in range(3):
            for j in range(3):
                if i + j > 2:
                    continue
                new_state = (missionaries - i, cannibals - j, 'right')
                if is_valid_state(new_state):
                    states.append(new_state)
    else:
        for i in range(3):
            for j in range(3):
                if i + j > 2:
                    continue
                new_state = (missionaries + i, cannibals + j, 'left')
                if is_valid_state(new_state):
                    states.append(new_state)

    return states

def uniform_cost_search():
    start_state = (3, 3, 'left')
    goal_state = (0, 0, 'right')

    frontier = PriorityQueue()
    frontier.put((0, start_state))
    explored = set()

    while not frontier.empty():
        cost, current_state = frontier.get()
        if current_state == goal_state:
            return cost

        explored.add(current_state)

        for next_state in get_next_states(current_state):
            if next_state not in explored:
                new_cost = cost + (10 * abs(current_state[0] - next_state[0])) + (20 * abs(current_state[1] - next_state[1]))
                frontier.put((new_cost, next_state))

    return -1

cost = uniform_cost_search()
print "Minimum cost:", cost
