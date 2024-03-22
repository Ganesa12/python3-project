def fisika():
    print("="*40)
    print("selamat datang di kumpulan rumus fisika")
    print("menu fisika :")
    print("="*40)
    print("1. rumus kuat arus listrik")
    print("2. rumur resistor paralel")
    print("3. rumus resistor seri")
    print("4. rumus watt")
    print("5. rumus lilitan trafo")
    print("6. rumus lilitan trafo ferid")
    print("="*40)
    menu_fisika = str(input("Pilih rumus dari 1-6 : "))
    print("="*40)
    if menu_fisika == '1':
        return kuat_arus()
    elif menu_fisika == '2' :
        return resistor_paralel()
    elif menu_fisika == '3' :
        return resistor_seri()
    elif menu_fisika == '4' :
        return watt()
    elif menu_fisika == '5' :
        return rumus_trafo()
    else :
        print("input yang anda masukan salah, silahkan masukan kembali")
        return fisika()

def resistor_seri() :
    print("="*40)
    print("Untuk menghitung total resistansi dari rangkaian resistor yang")
    print("dihubungkan secara seri,Anda dapat menggunakan rumus berikut:")
    print("R total = R1 + R2 + R3")
    print("="*40)
    r1 = int(input("masukan nilai R1 : "))
    r2 = int(input("masukan nilai R2 : "))
    r3 = int(input("masukan nilai R3 : "))
    r_total = r1 + r2 + r3
    print("="*40)
    print("hasil R total adalah ",r_total)
    print("="*40)
    kembali =str(input("ingin kembali ke menu utama ? y/n : "))
    print("="*40)
    if kembali == 'y' :
        return fisika()
    else :
        print("terimakasih :-)")

def resistor_paralel():
    print("="*40)
    print("Untuk menghitung total resistansi dari rangkaian resistor yang")
    print("dihubungkan secara paralel, Anda dapat menggunakan rumus berikut:")
    print("1/R total = 1/R1 + 1/R2 + 1/R3")
    print("Keterangan :")
    print("- R total adalah resistansi total dari rangkaian paralel.")
    print("- R1, R2, R3 adalah resistansi masing-masing resistor yang")
    print("dihubungkan secara paralel.")
    print("="*40)
    r1 = int(input("masukan nilai resistor R1 : "))
    r2 = int(input("masukan nilai resistor R2 : "))
    r_total = 1/r1 + 1/r2
    print("="*40)
    print("R total adalah",r_total,"ohm")
    print("="*40)
    kembali =str(input("ingin kembali ke menu utama ? y/n : "))
    print("="*40)
    if kembali == 'y' :
        return fisika()
    else :
        print("terimakasih :-)")

def kuat_arus():

    print("="*40)
    print("Kuat arus listrik (I) dapat dihitung menggunakan rumus dasar")
    print("Hukum Ohm dalam konteks rangkaian listrik. Rumus Hukum Ohm adalah:")

    print("I = V/R")

    print("Keterangan :")
    print("- I adalah kuat arus listrik (dalam Ampere, A)")
    print("- V adalah tegangan listrik (dalam Volt, V)")
    print("- R adalah resistansi rangkaian (dalam Ohm, Ω)")
    print("="*40)
    v = int(input("Berapa tegangan yang anda gunakan? : "))
    r = int(input("Berapa nilai hambatan/resistensi yang anda gunakan? : "))
    hasil = v / r  # Perhitungan kuat arus
    print("="*40)
    print("Kuat arus yang anda hasilkan adalah", hasil, "Ampere")
    print("="*40)
    kembali =str(input("ingin kembali ke menu utama ? y/n : "))
    print("="*40)
    if kembali == 'y' :
        return fisika()
    else :
        print("terimakasih :-)")

def watt() :
    print("="*40)
    print("Rumus dasar untuk watt dalam fisika adalah:")
    print("Daya (Watt)=Tegangan (Volt)×Arus (Ampere)")
    print("Ini merupakan rumus dasar dalam listrik. Ini menggambarkan hubungan")
    print("antara daya (dalam watt), tegangan (dalam volt), dan arus (dalam ampere).")
    print("Dengan kata lain, daya adalah hasil perkalian antara tegangan dan arus listrik.")
    print("="*40)
    v = int(input("berapa tegangan yang yang anda gunakan? : "))
    i = int(input("berapa ampere kuat arus nya ? : "))
    hasil = v*i
    print("="*40)
    print("daya yang anda hasilkan adalah",hasil,"Watt")
    print("="*40)
    kembali =str(input("ingin kembali ke menu utama ? y/n : "))
    print("="*40)
    if kembali == 'y' :
        return fisika()
    else :
        print("terimakasih :-)")

def rumus_trafo() :
    print("="*40)
    print("Rumus untuk menghitung jumlah lilitan pada sebuah transformator")
    print("(trafo) step-up dapat dijelaskan dengan menggunakan perbandingan")
    print("tegangan dan lilitan antara lilitan primer dan sekunder. Perbandingan")
    print("ini sesuai dengan hukum dasar transformator:")
    print("Np/Ns = Vp/Vs")
    print("Keterangan :")
    print("- Np = Jumlah lilitan pada lilitan primer (primary winding)")
    print("- Ns = Jumlah lilitan pada lilitan sekunder (secondary winding)")
    print("- Vp = Tegangan pada lilitan primer")
    print("- Vs = Tegangan pada lilitan sekunder")
    print("="*40)
    print("apa yang ingin anda tanyakan ?")
    print("1. Np")
    print("2. Ns")
    print("3. Vp")
    print("4. Vs")
    print("="*40)
    jawab = str(input("pilih pertanyaan anda : "))
    print("="*40)
    if jawab == '1' or jawab == 'np' or jawab == 'Np' :
        print("="*40)
        ns = int(input("masukan nilai Np (Lilitan Skunder) : "))
        vp = int(input("masukan nilai Vp (Volt Primer) : "))
        vs = int(input("masukan nilai Vs (Volt Skunder) : "))
        hasil = ns / (vp / vs)
        print("="*40)
        print("nilai dari Np (Lilitan Primer Adalah : )",hasil)
        print("="*40)
    elif jawab == '2' or jawab == 'ns' or jawab == 'Ns' :
        print("="*40)
        np = int(input("masukan nilai Np (Lilitan Primer) : "))
        vp = int(input("masukan nilai Vp (Volt Primer) : "))
        vs = int(input("masukan nilai Vs (Volt Skunder) : "))
        hasil = np / (vp / vs)
        print("="*40)
        print("nilai dari Np (Lilitan Skunder Adalah : )",hasil)
        print("="*40)
    elif jawab == '3' or jawab == 'vp' or jawab == 'Vp' :
        np = int(input("masukan nilai Np (Lilitan Primer) : "))
        ns = int(input("masukan nilai Vp (Lilitan Skunder) : "))
        vs = int(input("masukan nilai Vs (Volt Skunder) : "))
        hasil = vs / (np / ns)
        print("nilai dari Vp (Volt Skunder Adalah : )",hasil)
    elif jawab == '4' or jawab == 'vs' or jawab == 'Vs' :
        vp = int(input("masukan nilai Np (Volt Primer) : "))
        np = int(input("masukan nilai Vp (Lilitan Primer) : "))
        ns = int(input("masukan nilai Vs (Lilitan Skunder) : "))
        hasil = vp / (np / ns)
        print("nilai dari Np (Lilitan Skunder Adalah : )",hasil)
    else :
        print("pastikan input yang anda masukan adalah angka")
        return rumus_trafo()
    kembali =str(input("ingin kembali ke menu utama ? y/n : "))
    if kembali == 'y' :
        return fisika()
    else :
        print("terimakasih :-)")

def main():
    fisika()

# Panggil fungsi main() agar program dijalankan
if __name__ == "__main__":
    main()
