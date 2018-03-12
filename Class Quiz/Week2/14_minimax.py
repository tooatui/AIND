# https://classroom.udacity.com/nanodegrees/nd889/parts/6be67fd1-9725-4d14-b36e-ae2b5b20804c/modules/f719d723-7ee0-472c-80c1-663f02de94f3/lessons/9b1a742a-fa2d-4940-922c-ed426b44f81b/concepts/977cc04a-50cc-41aa-8302-a6ecdc606c9d

def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    possible_moves = gameState.get_legal_moves()
    if len(possible_moves) == 0:
    	return True
    return False

def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if(terminal_test(gameState)):
    	return 1

    v = float("inf")

    for move in gameState.get_legal_moves():
    	v = min(v, max_value(gameState.forecast_move(move)))
    return v


def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    if(terminal_test(gameState)):
    	return -1

    v = float("-inf")

    for move in gameState.get_legal_moves():
    	v = max(v, min_value(gameState.forecast_move(move)))
    return v
