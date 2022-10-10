import z3
### 8 Queens
# 8x8 board
# 8 queens
# no two queens on the same row, column, or diagonal
### define the board


## solve
s=z3.Solver()
for i in range(8):
    for j in range(8):
        exec("q_%d_%d = z3.Bool('q_%d_%d')" % (i,j,i,j))
## at least one queen per row
for i in range(8):
    exec("s.add(z3.Or(" + ",".join(["q_%d_%d" % (i,j) for j in range(8)]) + "))")
## at least one queen per column
for j in range(8):
    exec("s.add(z3.Or(" + ",".join(["q_%d_%d" % (i,j) for i in range(8)]) + "))")
## at most one queen per diagonal
for i in range(8):
    for j in range(8):
        for k in range(1,8):
            if i+k < 8 and j+k < 8:
                exec("s.add(z3.Or(z3.Not(q_%d_%d), z3.Not(q_%d_%d)))" % (i,j,i+k,j+k))
            if i+k < 8 and j-k >= 0:
                exec("s.add(z3.Or(z3.Not(q_%d_%d), z3.Not(q_%d_%d)))" % (i,j,i+k,j-k))
            if i-k >= 0 and j+k < 8:
                exec("s.add(z3.Or(z3.Not(q_%d_%d), z3.Not(q_%d_%d)))" % (i,j,i-k,j+k))
            if i-k >= 0 and j-k >= 0:
                exec("s.add(z3.Or(z3.Not(q_%d_%d), z3.Not(q_%d_%d)))" % (i,j,i-k,j-k))
## at most one queen per row
for i in range(8):
    for j in range(8):
        for k in range(j+1,8):
            exec("s.add(z3.Or(z3.Not(q_%d_%d), z3.Not(q_%d_%d)))" % (i,j,i,k))
## at most one queen per column
for i in range(8):
    for j in range(8):
        for k in range(i+1,8):
            exec("s.add(z3.Or(z3.Not(q_%d_%d), z3.Not(q_%d_%d)))" % (i,j,k,j))
if s.check() == z3.sat:
    m = s.model()
    for i in range(8):
        for j in range(8):
            if m.eval(eval("q_%d_%d" % (i, j))):
                print("Q", end="")
            else:
                print(".", end="")
        print()