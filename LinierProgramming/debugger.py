# test subject
from pulp import *

# Menentukan Masalah LP pada kasus 3
prob = LpProblem("Maximize Case", LpMaximize)
x = LpVariable("x", lowBound=0, cat='Integer') #membuat variabel x (produk 1), x >= 0
y = LpVariable("y", lowBound=0, cat='Integer') #membuat variabel y (produk 2), y >= 0

# fungsi tujuan
prob += 4*x + 5*y
# Fungsi kendala
prob += 1*x + 2*y <= 10
prob += 6*x + 6*y <= 36
#menampilkan permasalahan LP
print(prob)


#Menunjukan Status Optimum
status = prob.solve() #menyelesaikannya dengan solver default (bawaan library puPL)
print(LpStatus[status]) #Mencetak status dari solusi yang diselesaikan

#Menampilkan solusi dari permasalahan LP
print(value(x), value(y), value(prob.objective))