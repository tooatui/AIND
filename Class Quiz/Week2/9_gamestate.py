import copy

xlim, ylim = 3, 2  # board dimension constants

class GameState:
    """
    Attributes
    ----------
    _board: list(list)
        Represent the board with a 2d array _board[x][y]
        where open spaces are 0 and closed spaces are 1
        and a coordinate system where [0][0] is the top-
        left corner, and x increases to the right while
        y increases going down (this is an arbitrary
        convention choice -- there are many other options
        that are just as good)
    
    _parity: bool
        Keep track of active player initiative (which
        player has control to move) where 0 indicates that
        player one has initiative and 1 indicates player two
    
    _player_locations: list(tuple)
        Keep track of the current location of each player
        on the board where position is encoded by the
        board indices of their last move, e.g., [(0, 0), (1, 0)]
        means player one is at (0, 0) and player two is at (1, 0)
    """
    def __init__(self):
        # single-underscore prefix on attribute names means
        # that the attribute is "private" (Python doesn't truly
        # support public/private members, so this is only a
        # convention)
        self._board = [[0] * ylim for _ in range(xlim)]
        self._board[-1][-1] = 1  # block lower-right corner
        self._parity = 0
        self._player_locations = [None, None]

    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """
        loc = self._player_locations[self._parity]
        
        if loc is None:
	        return self._get_empty_spaces()
	        
        moves = []

        # the player is able to move 8 directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dx, dy in directions:
            _x, _y = loc
            while 0 <= _x + dx < xlim and 0 <= _y + dy < ylim:
                _x, _y = _x + dx, _y + dy
                print(_x, _y)
                if self._board[_x][_y] == 0:
                    moves.append((_x, _y))
                else:
                    break
        return moves

    def _get_empty_spaces(self):
        return [(i,j) for i in range(xlim) for j in range(ylim) if self._board[i][j] == 0]

    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.
        
        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
            (e.g., (0, 0) if the active player will move to the
            top-left corner of the board)
        """
        if move not in self.get_legal_moves():
            raise RunTimeError("Illeagal move ", move)

        new_game_state = copy.deepcopy(self)
        new_game_state._player_locations[self._parity] = move
        new_game_state._parity = 1 - self._parity
        new_game_state._board[move[0]][move[1]] = 1

        return new_game_state



print("Creating empty game board...")
g = GameState()

print("Getting legal moves for player 1...")
p1_empty_moves = g.get_legal_moves()
print("Found {} legal moves.".format(len(p1_empty_moves or [])))

print("Applying move (0, 0) for player 1...")
g1 = g.forecast_move((0, 0))

print("Getting legal moves for player 2...")
p2_empty_moves = g1.get_legal_moves()

print("Applying move (1, 1) for player 2...")
g2 = g1.forecast_move((1, 1))

print("Round 2: Getting legal moves for player 1...")
p1_empty_moves_2 = g2.get_legal_moves()
print(p1_empty_moves_2)

