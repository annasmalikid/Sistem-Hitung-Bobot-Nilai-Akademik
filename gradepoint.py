def hitung_nilai_akhir(nilai_tugas, nilai_absen, nilai_uts, nilai_uas):
    # Bobot nilai
    bobot_tugas = 0.15
    bobot_absen = 0.05
    bobot_uts = 0.35
    bobot_uas = 0.45

    # Hitung nilai akhir
    nilai_akhir = (nilai_tugas * bobot_tugas) + (nilai_absen * bobot_absen) + (nilai_uts * bobot_uts) + (nilai_uas * bobot_uas)

    return nilai_akhir

# Input nilai dari pengguna
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_absen = float(input("Masukkan nilai absen: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

# Validasi input (pastikan nilai berada dalam rentang 0-100)
if 0 <= nilai_tugas <= 100 and 0 <= nilai_absen <= 100 and 0 <= nilai_uts <= 100 and 0 <= nilai_uas <= 100:
    # Hitung dan tampilkan nilai akhir
    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_absen, nilai_uts, nilai_uas)
    print("\nNilai Tugas: {:.2f}".format(nilai_tugas))
    print("Nilai Absen: {:.2f}".format(nilai_absen))
    print("Nilai UTS: {:.2f}".format(nilai_uts))
    print("Nilai UAS: {:.2f}".format(nilai_uas))
    print("\nNilai Akhir: {:.2f}".format(nilai_akhir))
else:
    print("Input nilai tidak valid. Pastikan nilai berada dalam rentang 0-100.")
