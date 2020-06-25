from problem import Problem
from calculation import Calculation


counter = int(input("Berapa Jumlah Fungsi Kendala yang diberikan: "))
# Problem.input_tujuan()
# for problem in range(counter):
#     Problem.input_kendala()
mainKendala = [Problem.input_kendala() for kendala in range(counter)]
print(mainKendala)
result = Calculation(Problem.input_tujuan(), mainKendala)
app = result.calculation()