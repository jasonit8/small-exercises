def knight(square1,square2):
    files = ['a','b','c','d','e','f','g','h']
    ranks = [1,2,3,4,5,6,7,8]
    paths = {square1}
    steps = 0
    while square2 not in paths:
        steps += 1
        new_paths = set()
        for square in paths:
            file_index = files.index(square[0])
            rank_index = ranks.index(int(square[1]))
            for i in [-2,-1,1,2]:
                for j in [-2,-1,1,2]:
                    if i+j in [-3,-1,1,3]:
                        new_paths.add(files[file_index + i] + str(ranks[rank_index + j])) if all([file_index + i in range(8),rank_index + j in range(8)]) else set()
        paths = new_paths
    return steps

'''
How many times must a knight jump
to move from one square to another
on a chessboard, at least?
'''

print(knight('f2','e7'))