### zip
A function to convert the string representation of a puzzle into a dictionary form.
Recall that for the string:

grid = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
boxes = ['A1', 'A2', ... 'I9']
...we'd like to return the dictionary:

{
  'A1': '.'
  'A2': '.',
  'A3': '3',
  'A4': '.',
  'A5': '2',
  ...
  'I9': '.'
}

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
    return dict(zip(boxes, grid))

https://classroom.udacity.com/nanodegrees/nd889/parts/6be67fd1-9725-4d14-b36e-ae2b5b20804c/modules/237a9d0d-e2d0-45e4-a7fd-ff4bb88203c5/lessons/b1553784-de43-42c1-a7bf-c66a6e235c47/concepts/f2c9405a-76ae-4616-bf2b-8e60fc9f6ac4
https://docs.python.org/3.3/library/functions.html#zip

# sum
https://docs.python.org/3/library/functions.html#sum
source: 
```peers = dict((s, set(sum(units[s], [])) - set([s])) for s in squares)```

sum(units[s], []) here is to flat units[s] to a plain list because units[s] is a list of list, e.g [[], [], []]
```
print(units['A1'])
# output: [['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1'], ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9'], ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]

print(sum(units['A1'], []))
# output: ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
```

# set operations
source: 
```peers = dict((s, set(sum(units[s], [])) - set([s])) for s in squares)```


```
# Program to perform different set operations
# as we do in  mathematics
 
# sets are define
A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};
 
# union
print("Union :", A | B)
 
# intersection
print("Intersection :", A & B)
 
# difference
print("Difference :", A - B)
 
# symmetric difference
print("Symmetric difference :", A ^ B)
```

Output:
```
('Union :', set([0, 1, 2, 3, 4, 5, 6, 8]))
('Intersection :', set([2, 4]))
('Difference :', set([8, 0, 6]))
('Symmetric difference :', set([0, 1, 3, 5, 6, 8]))
```

# min
n,box_min_pos = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
 https://classroom.udacity.com/nanodegrees/nd889/parts/6be67fd1-9725-4d14-b36e-ae2b5b20804c/modules/237a9d0d-e2d0-45e4-a7fd-ff4bb88203c5/lessons/b1553784-de43-42c1-a7bf-c66a6e235c47/concepts/d54e395d-8918-44ec-bae7-5e261f51fc9b

# python can do multiple logic operation in one statement
`if 0 <= _x + dx < xlim`

# tuple operation
```
t = (0 ,1)
x, y = t
print (x, y)
# 0 1
```

# lambda function
https://classroom.udacity.com/nanodegrees/nd889/parts/6be67fd1-9725-4d14-b36e-ae2b5b20804c/modules/f719d723-7ee0-472c-80c1-663f02de94f3/lessons/9b1a742a-fa2d-4940-922c-ed426b44f81b/concepts/891af51b-052a-48f2-9a75-d9e5bfb64bf5
```
def minimax_decision(gameState):
    # The built in `max()` function can be used as argmax!
    return max(gameState.get_legal_moves(),
               key=lambda m: min_value(gameState.forecast_move(m)))
```
# Others
```
xlim = 3
ylim = 2
_board = [[0] * ylim for _ in range(xlim)]
```
