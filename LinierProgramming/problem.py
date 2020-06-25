# Adding the problem to the formula

class Problem:

    def input_tujuan():
        xvar = int(input("Masukkan Variabel tujuan x: "))
        yvar = int(input("Masukkan variabel tujuan y: "))
        return (xvar, yvar)

    def input_kendala():
        xvar = int(input("Masukkan Variabel x: "))
        yvar = int(input("Masukkan Variabel y: "))
        cons = int(input("Masukkan Variabel Constraint: "))    
        return (xvar, yvar, cons)