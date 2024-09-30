
class GameStateNode:
    #If who is 0 then it builds the tree and action doesn't matter
    def __init__(self, parent_state : list, action : int, who : int):

        self.game_state = parent_state.copy()
        self.game_state[action] = who
        self.terminal = False
        self.win = 0
        self.possibilities = []
        self.children = []

        if who == 1: #X's turn check all possible win states
            if self.game_state[0] == 1:
                if self.game_state[1] == 1:
                    if self.game_state[2] == 1:
                        self.terminal = True
                        self.win = 1
                if self.game_state[4] == 1:
                    if self.game_state[8] == 1:
                        self.terminal = True
                        self.win = 1
                if self.game_state[3] == 1:
                    if self.game_state[6] == 1:
                        self.terminal = True
                        self.win = 1
            if self.game_state[4] == 1:
                if self.game_state[1] == 1:
                    if self.game_state[7] == 1:
                        self.terminal = True
                        self.win = 1
                if self.game_state[2] == 1:
                    if self.game_state[6] == 1:
                        self.terminal = True
                        self.win = 1
                if self.game_state[3] == 1:
                    if self.game_state[5] == 1:
                        self.terminal = True
                        self.win = 1
            if self.game_state[8] == 1:
                if self.game_state[2] == 1:
                    if self.game_state[5] == 1:
                        self.terminal = True
                        self.win = 1
                if self.game_state[6] == 1:
                    if self.game_state[7] == 1:
                        self.terminal = True
                        self.win = 1
        elif who == 2: #O's turn check all possible win states
            if self.game_state[0] == -1:
                if self.game_state[1] == -1:
                    if self.game_state[2] == -1:
                        self.terminal = True
                        self.win = -1
                if self.game_state[4] == -1:
                    if self.game_state[8] == -1:
                        self.terminal = True
                        self.win = -1
                if self.game_state[3] == -1:
                    if self.game_state[6] == -1:
                        self.terminal = True
                        self.win = -1
            if self.game_state[4] == -1:
                if self.game_state[1] == -1:
                    if self.game_state[7] == -1:
                        self.terminal = True
                        self.win = -1
                if self.game_state[2] == -1:
                    if self.game_state[6] == -1:
                        self.terminal = True
                        self.win = -1
                if self.game_state[3] == -1:
                    if self.game_state[5] == -1:
                        self.terminal = True
                        self.win = -1
            if self.game_state[8] == -1:
                if self.game_state[2] == -1:
                    if self.game_state[5] == -1:
                        self.terminal = True
                        self.win = -1
                if self.game_state[6] == -1:
                    if self.game_state[7] == -1:
                        self.terminal = True
                        self.win = -1
        #else: #should never be here
            #raise AttributeError
        if who == 0:
            for x in range(9):
                self.possibilities.append(x)
                child = GameStateNode(self.game_state, x, 1)
                self.children.append(child)
        else:
            if not self.terminal:
                for x in range(9):
                    if self.game_state[x] == 0:
                        self.possibilities.append(x)
                        child = GameStateNode(self.game_state, x, (-1 * who))
                        self.children.append(child)
                    else:
                        self.children.append(None)
                if len(self.possibilities) == 0:
                    self.terminal = True