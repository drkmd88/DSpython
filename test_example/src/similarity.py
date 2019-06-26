import numpy as np
from numpy.linalg import norm
import numpy.random as rd


# sim = dot(a,b)/(|a|*|b|)

def similarity(a,b):
    '''calculate similarity'''
    return (np.dot(a,b)/(norm(a)*norm(b)))

# ctrl+J: move cursor down one line
# ctrl+P: move cursor up one line
# insert: o: begin a new line below the cursor; O: begin a new line above the cursor
# insert: a: insert after cursor; A: insert at the end of the line; i: insert before cursor
# delete: x: delete char at cursor; dw: delete a word; d0: delete to the beginning of a line; d$: delete to the end of a line; dd: delete line

