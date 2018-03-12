# this is what i try to do the sudoku defination by myself, after studying the source code
# with more examples and explanation for people new to python, and of course to make the sudoku problem easier to understand

def cross(A, B):
	return [ a + b for a in A for b in B]


rows = 'ABCDEFGHI'
cols = '123456789'
digits = cols

# define boxes, a box is a single cell in the sudoku
boxes = cross(rows, cols)

# define row unit list
# [['A1', 'A2', ..., 'A9'], ['B1',..., 'B9'], ['I1', ..., 'I9']]
row_unitlist = [cross(r, cols) for r in rows]

# define col unit list
# [['A1', 'B1', ..., 'I1'], ['A2',..., 'I2'], ['A9', ..., 'I9']]
col_unitlist = [cross(rows, c) for c in cols] 

# define square list, square means those boxes in the 3 X 3
# [['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3'], ..., ['G7', 'H7', 'I7', 'G8', 'H8', 'I8', 'G9', 'H9', 'I9']]
squares_unitlist = [cross(r, c) for r in ['ABC', 'DEF', 'GHI'] for c in ['123', '456', '789']]

# all unit list, 9 in each and therefore 27 in total
all_unitlist = row_unitlist + col_unitlist + squares_unitlist

# define box-unitlist dict
# e.g. {'A1': [['A1', 'A2', ..., 'A9'], ['A1', 'B1', ..., 'I1'], ['A1', 'B1', 'C1', 'A2', 'B2', 'C2', 'A3', 'B3', 'C3']]
# , 'B1': ..., 'I9':...}
box_unitlist_dict = dict((b, [u for u in all_unitlist if b in u]) for b in boxes)

# define square-peers dict, { key: square, value: set_of_sqaures }, the peers length is always 20 for a square
# e.g. {'A1': {'A2', 'A3', ..., 'A9', 'B1', 'C1', ..., 'I1','B2', 'C2', 'B3', 'C3'}, 'B1': {}, ..., 'I9': {}}
box_peers_dict = dict((b, set(sum(box_unitlist_dict[b], [])) - set([b])) for b in boxes)


print("======= squares ======================")
print(boxes)

print("========== all_unitlist ===================")
print(all_unitlist)
assert len(all_unitlist) == 27

print("========== box_unitlist_dict ===================")
print(box_unitlist_dict)

print("========== box_peers_dict ===================")
print(box_peers_dict)