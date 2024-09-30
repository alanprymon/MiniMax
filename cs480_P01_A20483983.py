import cs480_P01_A20483983_tree_builder as tree
import 

global nodes_searched

def alpha_beta_search(game_at : tree.GameStateNode) -> int:
    player = game_at.whos_turn
    if player == 1:  # X's turn
        action = max_value_ab(game_at, -2, 2)
    elif player == -1:  # O's turn
        action = min_value_ab(game_at, -2, 2)
    else:
        raise KeyError  # Just to error check and make sure it is not getting here
    return action[1]  # get action out of tuple returned

def max_value_ab(game_state : tree.GameStateNode, alpha : int, beta : int) -> (int, int):
    global nodes_searched
    nodes_searched += 1
    if game_state.terminal:
        return game_state.win, -1
    alpha_ = alpha
    v = -2  # Only dealing with -1, 0, and 1 so -2 is less than everything else
    for a in game_state.possibilities:
        result = min_value_ab(game_state.children[a], alpha_, beta)
        if result[0] > v:
            v = result[0]
            finish = (result[0], a)
            if alpha_ < v:
                alpha_ = v
        if v >= beta:
            return v, a
    return finish

def min_value_ab(game_state : tree.GameStateNode, alpha : int, beta : int) -> (int, int):
    global nodes_searched
    nodes_searched += 1
    if game_state.terminal:
        return game_state.win, -1
    beta_ = beta
    v = 2  # Only dealing with -1, 0, and 1 so -2 is less than everything else
    for a in game_state.possibilities:
        result = max_value_ab(game_state.children[a], alpha, beta_)
        if result[0] < v:
            v = result[0]
            finish = (result[0], a)
            if beta_ > v:
                beta_ = v
        if v <= alpha:
            return v, a
    return finish

def mini_max_search(game_at : tree.GameStateNode) -> int:
    player = game_at.whos_turn
    if player == 1: #X's turn
        action = max_value(game_at)
    elif player == -1: #O's turn
        action = min_value(game_at)
    else:
        raise KeyError #Just to error check and make sure it is not getting here
    return action[1] #get action out of tuple returned

def max_value(game_state : tree.GameStateNode) -> (int, int):
    global nodes_searched
    nodes_searched += 1
    if game_state.terminal:
        return game_state.win, -1
    v = -2 #Only dealing with -1, 0, and 1 so -2 is less than everything else
    for a in game_state.possibilities:
        result = min_value(game_state.children[a])
        if result[0] > v:
            v = result[0]
            finish = (result[0], a)
    return finish

def min_value(game_state : tree.GameStateNode) -> (int, int):
    global nodes_searched
    nodes_searched += 1
    if game_state.terminal:
        return game_state.win, -1
    v = 2  # Only dealing with -1, 0, and 1 so -2 is less than everything else
    for a in game_state.possibilities:
        result = max_value(game_state.children[a])
        if result[0] < v:
            v = result[0]
            finish = (result[0], a)
    return finish

if __name__ == '__main__':
    global nodes_searched
    nodes_searched = 0
    game = tree.GameStateNode([0,0,0,0,0,0,0,0,0], 0, 0)
    action = mini_max_search(game)
    print(action)
    print(nodes_searched)
    print(game)