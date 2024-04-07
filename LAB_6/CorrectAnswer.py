import heapq


def is_valid_state(state):
    m, c, _ = state
    return (m == 0 or m >= c) and (3 - m == 0 or (3 - m) >= (3 - c))


def generate_successors(state):
    successors = []
    m, c, b = state

    # Generate successor states based on boat position
    if b == 0:  # Boat on the starting bank
        for m_move in range(3):
            for c_move in range(3):
                if 0 < m_move + c_move <= 2:
                    successor = (m - m_move, c - c_move, 1)
                    if is_valid_state(successor):
                        successors.append((successor, 10 * m_move + 20 * c_move, (m, c), (m - m_move, c - c_move)))
    else:  # Boat on the destination bank
        for m_move in range(3):
            for c_move in range(3):
                if 0 < m_move + c_move <= 2:
                    successor = (m + m_move, c + c_move, 0)
                    if is_valid_state(successor):
                        successors.append((successor, 10 * m_move + 20 * c_move, (m, c), (m + m_move, c + c_move)))

    return successors


def uniform_cost_search():
    start_state = (3, 3, 0)
    goal_state = (0, 0, 1)

    # Priority queue to store states with minimum cost
    priority_queue = [(0, start_state, None, None)]
    heapq.heapify(priority_queue)

    while priority_queue:
        current_cost, current_state, prev_state, move_state = heapq.heappop(priority_queue)

        if current_state == goal_state:
            print("Goal state reached! Minimum cost:", current_cost)
            print_steps(start_state, prev_state, move_state)
            return current_cost

        successors = generate_successors(current_state)
        for successor, cost, move_from, move_to in successors:
            total_cost = current_cost + cost
            heapq.heappush(priority_queue, (total_cost, successor, move_from, move_to))
            print_step(current_state, successor, move_from, move_to, total_cost)


def print_step(current_state, successor_state, move_from, move_to, total_cost):
    print(f"Move from {move_from} to {move_to}. Current state: {current_state}. Total cost: {total_cost}")


def print_steps(start_state, prev_state, move_state):
    if prev_state is not None:
        print_steps(start_state, prev_state[0], prev_state[1])
        print_step(prev_state[0], move_state, move_state[2], move_state[3], move_state[1])
    else:
        print("Initial state:", start_state)


# Run the uniform cost search
uniform_cost_search()