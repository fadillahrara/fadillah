def pertambahan(a,b):
    print("Hasil dari", a ,"+", B, "=" , A+B)
def pengurangan(A,B):
    print("hasil dari", A ,"-", B , "=" , A-B)
def perkalian(A,B):
    print("hasil dari", A ,"X", B , "=" , A*B)
def pembagian(A,B):
    if B == 0 :
        print("bilangan tidak bisa dibagi 0")
    else:
        print("hasil dari", A ,":", B , "=" , A/B)
while True:
   print("SELAMAT DATANG DIPROGRAM KALKULATOR")
   print("===================================")
   print("-------------KALKULATOR------------")
   print("silahkan enter untuk melanjutkan program")
   print("===================================\n")
   print("============Input angka============")
   A = float(input("angka pertama :"))
   B = float(input("angka kedua :"))
   print("\n==========")
   print("1.Pertambahan")
   print("2.Pengurangan")
   print("3.Perkalian")
   print("4.Pembagian")
   pilih =input("Masukan Pilihan : ")
   print("\n====output====")
   if pilih == '1':
       pertambahan(A,B)
       break
   elif pilih == '2':
       pengurangan(A,B)
       break
   elif pilih == '3':
       perkalian(A,B)
       break
   elif pilih == '4':
       pembagian(A,B)
       break
   else:
       print("Pilihan tidak valid")
   print("===========TERIMAKASIH==========")
   print("--------------------------------")
   
   