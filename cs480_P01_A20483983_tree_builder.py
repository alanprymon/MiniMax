#first is 1 and second is -1
class GameStateNode:
    #When building the tree feed who 0 and action doesn't matter what it is as long as its between 0-8
    def __init__(self, parent_state : list, action : int, who : int):

        self.game_state = parent_state.copy()
        self.game_state[action] = who
        self.terminal = False
        self.win = 0
        self.possibilities = []
        self.children = []
        self.whos_turn = -1 * who

        if who == 1: #first's turn check all possible win states
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
        elif who == -1: #second's turn check all possible win states
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
        else:
            if who == 0 and self.game_state == [0,0,0,0,0,0,0,0,0]:
                self.whos_turn = 1
            else: #should never be here
                raise AttributeError #Just to error check and make sure it is not getting here
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
                if len(self.possibilities) == 0: #If all spaces filled then also terminal
                    self.terminal = True