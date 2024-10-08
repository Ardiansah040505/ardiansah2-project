import random

nama = "Ardiansah" #string tandanya ada petik dua
usia = 19 #interger
#variabel berfungsi untuk memanage data yang ada

print(f"Ardiansa  {nama}  {usia}")
print("Ardiansah")

welome = "SELAMAT DATANG"

print("*****************")
print(f"*** {welome} ***")
print("*****************")

nomor_ryan = 4

if nomor_ryan == 4: #== artinya dalah bernilai sama dengan
      print("Iyaa nomor saya itu") #jika nomor_ryan tidak sama dengan 4 maka tidak muncul
else: #tapi jika tidak
      print("Engga bukan nomor saya itu")

kucing_posisi = random.randint(1, 4) #perbedaan tipe data membuat output berbeda

      
nama_user = input("Masukkan nama anda: ")      
print(f"Halo {nama_user} selamat datang")
print(f"{nama_user} Tolong perhatikan tulisan ini ya")
print(f'''
Halo {nama_user}! Tolong Lihat Kotak ini
|_| |_| |_| |_| 
      ''')
pilihan_user = int(input("Menurut kamu kucingnya ada di kotak berapa? [1/2/3/4] "))

print(f"pilihan kamu adalah {pilihan_user}")

confirm_user = input(f"apakah kamu yakin memilih {pilihan_user} [iya/tidak]?")

if confirm_user == "iya":
      print("Kita Kunci Jawaban")
else:
      pilihan_second = int(input("Silahkan Pilih Lagi [1/2/3/4]"))

if confirm_user == kucing_posisi:
      print(f" Selamat {nama_user} kamu telah menemukan kucing. Kucing Berada di Nomor {kucing_posisi}")
else:
      print(f"Mohon maaf kamu gagal menemukan kucing. Kucing berada di kotak nomor {kucing_posisi}. Kamu memilih kotak nomor {confirm_user}")

if pilihan_second == kucing_posisi:
      print(f"Selamat {nama_user} kamu telah memilih kotak yang benar. Kucing berada di kotak nomor {kucing_posisi}")
else:
      print(f"Mohon maaf kamu gagal menemukan kucing. Kucing berada di kotak nomor {kucing_posisi}. Kamu memilih kotak nomor {pilihan_second} Pada awalnya kamu memilih kotak nomor {pilihan_user}")


# if pilihan_user == kucing_posisi :
#       print(f"Selamat {nama_user} Menemukan Kucing. Posisi Kucing ada di kotak {pilihan_user}")
# else:
#       print(f"{nama_user} Kamu Gagal Gada Kucing Di Situ. Kucing ada di nomor {kucing_posisi}. Kamu memilih kotak {pilihan_user}")      

# #perlu melihat tipe data yang ada dan harus cocok


