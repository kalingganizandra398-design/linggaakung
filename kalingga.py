print("=== PROGRAM NILAI SISWA ===")

nama = input("Masukkan nama siswa: ")
nilai = int(input("Masukkan nilai: "))
kehadiran = int(input("Masukkan persentase kehadiran: "))

if nilai >= 75 and kehadiran >= 80:
    print("Nama:", nama)
    print("Keterangan: LULUS")

elif nilai >= 60 or kehadiran >= 80:
    print("Nama:", nama)
    print("Keterangan: REMEDIAL")

else:
    print("Nama:", nama)
    print("Keterangan: TIDAK LULUS")