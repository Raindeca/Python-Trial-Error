from pulp import *
from problem import Problem


class Calculation:

        def __init__(self, tujuan, kendala):
            self.tujuan = tujuan
            self.kendala = kendala

        def calculation(self):
            # Mengerjakan Formulasi LP dengan 2 variabel
            prob = LpProblem("Maximize Case", LpMaximize)
            x = LpVariable("X", lowBound=0, cat='integer') # Membuat Variabel X (produk 1), di mana X >= 0
            y = LpVariable("y", lowBound=0, cat='integer') # Membuat Variabel y (produk 2), di mana y >= 0

            #membuat fungsi tujuan
            prob += self.tujuan[0]*x + self.tujuan[1]*y

            #Membuat fungsi kendala
            print(self.kendala)
            for problem in range(len(self.kendala)):
                # element = self.kendala[problem]
                # f_tuple = self.kendala[problem][0]
                prob += self.kendala[problem][0]*x + self.kendala[problem][1]*y <= self.kendala[problem][2]
            
            #Menanpikan Permasalahan LP
            # print(int(prob)) masih error

            # Menunjukan Status Optimum
            status = prob.solve() # menyelesaikannya dengan solver default (bawaan library puPL)
            print(LpStatus[status]) # Mencetak status dari solusi yang diselesaikan

            # Menampilkan solusi dari permasalahan LP
            print(value(x), value(y), value(prob.objective))