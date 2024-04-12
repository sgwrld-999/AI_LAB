import random
def heuristic_value(pile_size):
    # Improved heuristic:
    # Smaller piles are better for the current player
    return pile_size

def alpha_beta(node, depth, alpha, beta, maximizingPlayer):
    if node == 0 or depth == 0:
        return heuristic_value(node)
    
    if maximizingPlayer:
        maxEval = float('-inf')
        for child in [node - 1, node - 2]:
            if child >= 0:
                eval = alpha_beta(child, depth - 1, alpha, beta, False)
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return maxEval
    else:
        minEval = float('inf')
        for child in [node - 1, node - 2]:
            if child >= 0:
                eval = alpha_beta(child, depth - 1, alpha, beta, True)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return minEval

def ai_move(pile_size, depth):
    # Get evaluations for removing 1 or 2 stones
    score1 = alpha_beta(pile_size - 1, depth, float('-inf'), float('inf'), False) + random.uniform(-0.1, 0.1)
    score2 = alpha_beta(pile_size - 2, depth, float('-inf'), float('inf'), False) + random.uniform(-0.1, 0.1)
    
    # Choose move with better score (or prioritize removing fewer stones if scores are close)
    if abs(score1 - score2) < 1e-6:
        return random.choice([1, 2])
    if score1 > score2:
        return 1
    return 2

def play_game(depth=10):
    pile_size = 50
    current_player = "AI" if random.randint(0, 1) == 0 else "Human"

    while pile_size > 0:
        print(f"Current pile size: {pile_size}. It's {current_player}'s turn.")

        if current_player == "AI":
            stones_removed = ai_move(pile_size, depth)
            print(f"AI removes {stones_removed} stones.")
        else:
            stones_removed = int(input("Remove 1 or 2 stones: "))
            while stones_removed not in [1, 2]:
                stones_removed = int(input("Invalid move. Remove 1 or 2 stones: "))
        
        pile_size -= stones_removed
        
        if pile_size <= 0:
            print(f"{current_player} loses!")
            break
        
        current_player = "AI" if current_player == "Human" else "Human"

if __name__ == "__main__":
    play_game()

