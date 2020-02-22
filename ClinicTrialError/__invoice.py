from __patients import Patients
from __services import Services
from tabulate import tabulate

class Invoice:

    total = Services.get_drug + Services.medical_action + Services.maternity_services

    def invoice():
        print("Biodata Pasien:")
        print("\t- Nama Pasien: ", Patients.get_full_name)
        print("\t- Nama Wali: ", Patients.get_guardian_name)
        print("\t- Alamat: ", Patients.get_address)
        print("\t= No. Telepon: ", Patients.get_phone)
        print("\t- Gol. Darah: ", Patients.get_blood_type)
        print("Pembayaran:\n")
        
        print(
            tabulate(
                [
                    [Services.get_room, 
                    Services.medical_action, 
                    Services.maternity_services, 
                    Services.get_drug, 
                    total]
                ],

                headers= [
                    "Biaya menginap (RP)",
                    "Penanganan (RP)",
                    "Layanan (Rp)",
                    "Obat (Rp)",
                    "TOTAL (Rp)"
                ],

                tablefmt="orgtbl"
            )
        )