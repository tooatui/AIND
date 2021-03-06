https://classroom.udacity.com/nanodegrees/nd889/parts/6be67fd1-9725-4d14-b36e-ae2b5b20804c/modules/f719d723-7ee0-472c-80c1-663f02de94f3/lessons/9b1a742a-fa2d-4940-922c-ed426b44f81b/concepts/49c5de60-40b7-4863-bf5d-dfc2f781a055

The following was my initial solution which didn't pass all tests after submission.

```python
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
        list_to_return = []
        current_player_location = self._player_locations[0] if self._parity == 0 else self._player_locations[1]
        
        if current_player_location is None:
	        for i, cells in enumerate(self._board):
	            for j, cell in enumerate(cells):
	            	if self._board[i][j] == 0:
	            		list_to_return.append((i, j))
	        return list_to_return
	        
        for i, cells in enumerate(self._board):
            for j, cell in enumerate(cells):
                if self._board[i][j] == 0 and not (i == current_player_location[0] and j == current_player_location[1]):
                    # check if the current play can move to here
                    # if i == current_player_location[0] and nothing in between 
                    if i == current_player_location[0]:
                        the_range = range(j, current_player_location[1]) if j < current_player_location[1] else range(current_player_location[1], j)
                        if not any(self._board[i][k] == 1 for k in the_range):  
                            list_to_return.append((i, j))
                    elif j == current_player_location[1]:   
                        the_range = range(i, current_player_location[0]) if i < current_player_location[0] else range(current_player_location[0], i)
                        if not any(self._board[k][j] == 1 for k in the_range):
                            list_to_return.append((i, j))
                    elif ((i == current_player_location[0] - 1 and j == current_player_location[1] - 1)
                        or (i == current_player_location[0] - 1 and j == current_player_location[1] + 1)
                        or (i == current_player_location[0] + 1 and j == current_player_location[1] - 1)
                        or (i == current_player_location[0] + 1 and j == current_player_location[1] + 1)):
                            list_to_return.append((i, j))
       
        return list_to_return

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
        new_game_state = copy.deepcopy(self)
        new_game_state._parity = 1 - self._parity
        if self._parity == 0:
            new_game_state._player_locations[0] = move
        else:
            new_game_state._player_locations[1] = move
                    
        for i, cells in enumerate(new_game_state._board):
            for j, cell in enumerate(cells):
                if i == move[0] and j == move[1]:
                    new_game_state._board[i][j] = 1
                    return new_game_state
                    
        return new_game_state
```  

## Something's wrong with the get_legal_moves function
- The result is wrong for the following test
```
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

# output
# Applying move (0, 0) for player 1...
# Applying move (1, 1) for player 2...
# Round 2: Getting legal moves for player 1...
# []
```
The correct result for player 1 (the last output) should be [(0, 1),(1, 0), (2, 0)]
- The logic is not right. The active player can move to any open cell diagonal from the current position given no blocker on the way. What I implented was the player can only move to the diagonal one step away. 

## First solution
The following code sovle the above mentioned first issue. The root cause is that when calculating anything in between the open space and the current position in the same row or column, it included the the current position, which would always be already be occupied and therefore leads to no available places (i.e the range function is wrong). This passed the overall udacity test only because the boardis 3 * 2 and therefore the diagonal error (the above mentioned second issue) is hidden.  

```python
def get_legal_moves(self):
        list_to_return = []
        current_player_location = self._player_locations[0] if self._parity == 0 else self._player_locations[1]
        
        if current_player_location is None:
	        for i, cells in enumerate(self._board):
	            for j, cell in enumerate(cells):
	            	if self._board[i][j] == 0:
	            		list_to_return.append((i, j))
	        return list_to_return
	        
        for i, cells in enumerate(self._board):
            for j, cell in enumerate(cells):
                if self._board[i][j] == 0 and not (i == current_player_location[0] and j == current_player_location[1]):
                    # check same column,  
                    if i == current_player_location[0]:
                        the_range = range(j + 1, current_player_location[1]) if j < current_player_location[1] else range(current_player_location[1] + 1, j)
                        if not any(self._board[i][k] == 1 for k in the_range):  
                            list_to_return.append((i, j))
                    # check same row   
                    elif j == current_player_location[1]: 
                        the_range = range(i + 1, current_player_location[0]) if i < current_player_location[0] else range(current_player_location[0] + 1, i)
                        if not any(self._board[k][j] == 1 for k in the_range):
                            list_to_return.append((i, j))
                    # check diagonal
                    elif ((i == current_player_location[0] - 1 and j == current_player_location[1] - 1)
                        or (i == current_player_location[0] - 1 and j == current_player_location[1] + 1)
                        or (i == current_player_location[0] + 1 and j == current_player_location[1] - 1)
                        or (i == current_player_location[0] + 1 and j == current_player_location[1] + 1)):
                            list_to_return.append((i, j))
       
        return list_to_return
```

## Final solution:
Let the current player move along the 8 possible directions and add the open position to list until a blocker is reached.

```python
    def get_legal_moves(self):
        list_to_return = []
        current_player_location = self._player_locations[0] if self._parity == 0 else self._player_locations[1]
        
        if current_player_location is None:
	        for i, cells in enumerate(self._board):
	            for j, cell in enumerate(cells):
	            	if self._board[i][j] == 0:
	            		list_to_return.append((i, j))
	        return list_to_return
	        
        # the player is able to move 8 directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for direction in directions:
            next_position = (current_player_location[0] + direction[0], current_player_location[1] + direction[1])
            while next_position[0] < xlim and next_position[0] > -1 and next_position[1] < ylim and next_position[1] > -1:
                print(next_position)
                if self._board[next_position[0]][next_position[1]] == 0:
                    list_to_return.append(next_position)
                    next_position = (next_position[0] + direction[0], next_position[1] + direction[1])
                else:
                    break
       
        return list_to_return
```

## The Solution provided by Udacity
A new things to notice:
- It considers the illegal move in forecast_move function
```python
if move not in self.get_legal_moves():
    raise RuntimeError("Attempted forecast of illegal move")
```
- the python techniques in get_legal_moves function

```python
from copy import deepcopy

xlim, ylim = 3, 2  # board dimensions

class GameState:
    """
    Attributes
    ----------
    _board: list(list)
        Represent the board with a 2d array _board[x][y]
        where open spaces are 0 and closed spaces are 1
    
    _parity: bool
        Keep track of active player initiative (which
        player has control to move) where 0 indicates that
        player one has initiative and 1 indicates player 2
    
    _player_locations: list(tuple)
        Keep track of the current location of each player
        on the board where position is encoded by the
        board indices of their last move, e.g., [(0, 0), (1, 0)]
        means player 1 is at (0, 0) and player 2 is at (1, 0)
    
    """

    def __init__(self):
        self._board = [[0] * ylim for _ in range(xlim)]
        self._board[-1][-1] = 1  # block lower-right corner
        self._parity = 0
        self._player_locations = [None, None]

    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.
        
        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
        """
        if move not in self.get_legal_moves():
            raise RuntimeError("Attempted forecast of illegal move")
        newBoard = deepcopy(self)
        newBoard._board[move[0]][move[1]] = 1
        newBoard._player_locations[self._parity] = move
        newBoard._parity ^= 1
        return newBoard

    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.)
        """
        loc = self._player_locations[self._parity]
        if not loc:
            return self._get_blank_spaces()
        moves = []
        rays = [(1, 0), (1, -1), (0, -1), (-1, -1),
                (-1, 0), (-1, 1), (0, 1), (1, 1)]
        for dx, dy in rays:
            _x, _y = loc
            while 0 <= _x + dx < xlim and 0 <= _y + dy < ylim:
                _x, _y = _x + dx, _y + dy
                if self._board[_x][_y]:
                    break
                moves.append((_x, _y))
        return moves

    def _get_blank_spaces(self):
        """ Return a list of blank spaces on the board."""
        return [(x, y) for y in range(ylim) for x in range(xlim)
                if self._board[x][y] == 0]

```
