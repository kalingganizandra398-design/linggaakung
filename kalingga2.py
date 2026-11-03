print("=== PROGRAM PEMBELIAN BARANG ===")

nama = input("Nama pembeli: ")
barang = input("Nama barang: ")
harga = int(input("Harga barang: "))
jumlah = int(input("Jumlah barang: "))

total = harga * jumlah

print("\n=== STRUK PEMBELIAN ===")
print("Nama:", nama)
print("Barang:", barang)
print("Total pembayaran:", total)

if total >= 100000 and jumlah >= 2:
    print("Pembelian dalam jumlah besar")

elif total >= 100000 or jumlah >= 2:
    print("Pembelian memenuhi salah satu syarat")

elif not (total >= 100000):
    print("Total pembelian di bawah 100000")

else:
    print("Pembelian biasa")