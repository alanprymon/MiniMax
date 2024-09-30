import cs480_P01_A20483983_tree_builder as tree
import sys

global nodes_searched

def alpha_beta_search(game_at : tree.GameStateNode) -> int:
    player = game_at.whos_turn
    if player == 1:  # first's turn
        action = max_value_ab(game_at, -2, 2)
    elif player == -1:  # second's turn
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
    v = 2  # Only dealing with -1, 0, and 1 so 2 is greater than everything else
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
    if player == 1: #first's turn
        action = max_value(game_at)
    elif player == -1: #second's turn
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
    v = 2  # Only dealing with -1, 0, and 1 so 2 is greater than everything else
    for a in game_state.possibilities:
        result = max_value(game_state.children[a])
        if result[0] < v:
            v = result[0]
            finish = (result[0], a)
    return finish

def start_text(algo : str, first : str, mode : str):
    print('Prymon, Alan, A20483983 solution:')
    if algo == '1':
        print('Alforithm: MiniMax')
    else:
        print('MiniMax with alpha-beta pruning')
    print('First: ' + first)
    if mode == '1':
        print('Mode: human versus computer')
    else:
        print('Mode: computer versus computer')

#toggle 1 if X is first and toggle -1 if O is first
def print_game(state : tree.GameStateNode, toggle : int) -> None:
    pretty_print_table = []
    for x in state.game_state:
        if x == 0:
            pretty_print_table.append('   ')
        elif x == (1 * toggle):
            pretty_print_table.append(' X ')
        elif x == (-1 * toggle):
            pretty_print_table.append(' O ')
        else:
            raise KeyError  # should never get here
    print(pretty_print_table[0] + '|' + pretty_print_table[1] + '|' + pretty_print_table[2])
    print(2 * ('-' * 3 + '+') + '-' * 3)
    print(pretty_print_table[3] + '|' + pretty_print_table[4] + '|' + pretty_print_table[5])
    print(2 * ('-' * 3 + '+') + '-' * 3)
    print(pretty_print_table[6] + '|' + pretty_print_table[7] + '|' + pretty_print_table[8])

if __name__ == '__main__':
    if not len(sys.argv) == 4:
        print("ERROR: Not enough/too many/illegal input arguments.")
        exit()
    algo = sys.argv[1] #string
    first = sys.argv[2] #string
    mode = sys.argv[3] #string
    global nodes_searched
    nodes_searched = 0
    game = tree.GameStateNode([0, 0, 0, 0, 0, 0, 0, 0, 0], 0, 0)
    root = game #Only for debugging
    if mode == '1': #human vs computer
        '1'
    elif mode == '2': #computer vs computer
        if first == 'X': #computer vs computer, X first
            if algo == '1': #MiniMax(1), X first(X), computer vs computer(2)
                start_text(algo, first, mode)
                done = False
                first_person = True
                while not done:
                    if first_person:
                        next_move = mini_max_search(game)
                        print('X\'s selected move: ' + str(next_move + 1) + '. Number of search tree nodes generated: ' + str(nodes_searched))
                        nodes_searched = 0
                        game = game.children[next_move]
                        first_person = False
                    else:
                        next_move = mini_max_search(game)
                        print('O\'s selected move: ' + str(next_move + 1) + '. Number of search tree nodes generated: ' + str(nodes_searched))
                        nodes_searched = 0
                        game = game.children[next_move]
                        first_person = True
                    print_game(game, 1)
                    if game.terminal:
                        done = True
                if game.win == -1:
                    print('O WON')
                elif game.win == 0:
                    print('TIE')
                elif game.win == 1:
                    print('X WIN')
                else:
                    raise EOFError
            elif algo == '2': #Alpha Beta(2), X first(X), computer vs computer(2)
                start_text(algo, first, mode)
                done = False
                first_person = True
                while not done:
                    if first_person:
                        next_move = alpha_beta_search(game)
                        print('X\'s selected move: ' + str(next_move + 1) + '. Number of search tree nodes generated: ' + str(nodes_searched))
                        nodes_searched = 0
                        game = game.children[next_move]
                        first_person = False
                    else:
                        next_move = alpha_beta_search(game)
                        print('O\'s selected move: ' + str(next_move + 1) + '. Number of search tree nodes generated: ' + str(nodes_searched))
                        nodes_searched = 0
                        game = game.children[next_move]
                        first_person = True
                    print_game(game, 1)
                    if game.terminal:
                        done = True
                if game.win == -1:
                    print('O WON')
                elif game.win == 0:
                    print('TIE')
                elif game.win == 1:
                    print('X WIN')
                else:
                    raise EOFError
            else:
                print("ERROR: Not enough/too many/illegal input arguments.")
                exit()
        elif first == 'O': #computer vs computer, O first
            if algo == '1': #MiniMax(1), O first(O), computer vs computer(2)
                start_text(algo, first, mode)
                done = False
                first_person = True
                while not done:
                    if first_person:
                        next_move = mini_max_search(game)
                        print('O\'s selected move: ' + str(next_move + 1) + '. Number of search tree nodes generated: ' + str(nodes_searched))
                        nodes_searched = 0
                        game = game.children[next_move]
                        first_person = False
                    else:
                        next_move = mini_max_search(game)
                        print('X\'s selected move: ' + str(next_move + 1) + '. Number of search tree nodes generated: ' + str(nodes_searched))
                        nodes_searched = 0
                        game = game.children[next_move]
                        first_person = True
                    print_game(game, -1)
                    if game.terminal:
                        done = True
                if game.win == -1:
                    print('X WON')
                elif game.win == 0:
                    print('TIE')
                elif game.win == 1:
                    print('O WIN')
                else:
                    raise EOFError
            elif algo == '2': #Alpha Beta(2), O first(O), computer vs computer(2)
                start_text(algo, first, mode)
                done = False
                first_person = True
                while not done:
                    if first_person:
                        next_move = alpha_beta_search(game)
                        print('O\'s selected move: ' + str(
                            next_move + 1) + '. Number of search tree nodes generated: ' + str(nodes_searched))
                        nodes_searched = 0
                        game = game.children[next_move]
                        first_person = False
                    else:
                        next_move = alpha_beta_search(game)
                        print('X\'s selected move: ' + str(
                            next_move + 1) + '. Number of search tree nodes generated: ' + str(nodes_searched))
                        nodes_searched = 0
                        game = game.children[next_move]
                        first_person = True
                    print_game(game, -1)
                    if game.terminal:
                        done = True
                if game.win == -1:
                    print('X WON')
                elif game.win == 0:
                    print('TIE')
                elif game.win == 1:
                    print('O WIN')
                else:
                    raise EOFError
            else:
                print("ERROR: Not enough/too many/illegal input arguments.")
                exit()
        else:
            print("ERROR: Not enough/too many/illegal input arguments.")
            exit()
    else:
        print("ERROR: Not enough/too many/illegal input arguments.")
        exit()