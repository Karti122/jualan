
daftar_barang = {
"Beras": 10000,

"Gula": 8000,

"Telur": 2000,

"Minyak Goreng": 15000,

"Garam": 5000

}
 

print("Daftar Barang:")

for barang, harga in daftar_barang.items(): 
    print(f"{barang}: Rp {harga}")


total_belanja = 0

jumlah_barang = int(input("\nMasukkan jumlah barang yang dibeli: "))


for i in range(jumlah_barang):

  barang = input(f"\nMasukkan nama barang ke-{i+1}: ")

if barang in daftar_barang:

  total_belanja += daftar_barang [barang]

else:

  print(f"(barang) tidak ada dalam daftar barang.")

print(f"\nTotal belanjaan Anda: Rp {total_belanja}")
