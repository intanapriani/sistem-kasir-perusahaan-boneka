print("---supermarket boneka---")
print("===============================")
def hitung_harga_boneka(jumlah_boneka):
    if 1 <= jumlah_boneka <= 12:
        harga_boneka = 20000
    elif 13 <= jumlah_boneka <= 24:
        harga_boneka = 19500
    elif 25 <= jumlah_boneka <= 50:
        harga_boneka = 18000
    elif jumlah_boneka > 50:
        harga_boneka = 17000
    else:
        return "Jumlah boneka tidak valid."
    
    total_harga = jumlah_boneka * harga_boneka
    return total_harga

jumlah_boneka = int(input("Masukkan jumlah boneka: "))
total = hitung_harga_boneka(jumlah_boneka)

print(f"Total harga untuk {jumlah_boneka} boneka adalah: Rp. {total}")
print("total harga adalah: ", total)