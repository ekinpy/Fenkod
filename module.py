import os
os.system("title Fenkod v0.1")

def caprazla(gen1, gen2):
    if len(gen1) and len(gen2) == 2:
        if gen1.casefold() == gen2.casefold():
            gen1char1 = gen1[0]
            gen1char2 = gen1[1]
            gen2char1 = gen2[0]
            gen2char2 = gen2[1]
            result1 = gen1char1 + gen2char1
            result2 = gen1char1 + gen2char2
            result3 = gen1char2 + gen2char1
            result4 = gen1char2 + gen2char2
            print(gen1, gen2)
            print("|   |")
            print(result1, result2, result3, result4)
        else:
            print("(FK1) Hata:", gen1, gen2, "Farklı Genler.")
    else:
        print("(FK0) Hata:", gen1, gen2, "Çaprazlanamaz.")

def basinc(f, s):
    if type(f) and type(s) is not int:
        print("(FK2) Hata: Girilen Değerler Bir Tamsayı Değil.")
    else:
        p = f / s       
        print(p)

def pascal(newton, m2):
    if type(newton) and type(m2) is not int:
        print("(FK2) Hata: Girilen Değerler Bir Tamsayı Değil.")
    else:
        pa = newton / m2
        print(pa)

# İlk 30 Element.
def element(an):
    if an == 1:
        print("Hidrojen (H)")
    elif an == 2:
        print("Helyum (He)")
    elif an == 3:
        print("Lityum (Li)")
    elif an == 4:
        print("Berilyum (Be)")
    elif an == 5:
        print("Bor (B)")
    elif an == 6:
        print("Karbon (C)")
    elif an == 7:
        print("Azot (N)")
    elif an == 8:
        print("Oksijen (O)")
    elif an == 9:
        print("Flor (F)")
    elif an == 10:
        print("Neon (Ne)")
    elif an == 11:
        print("Sodyum (Na)")
    elif an == 12:
        print("Magnezyum (Mg)")
    elif an == 13:
        print("Alüminyum (Al)")
    elif an == 14:
        print("Silisyum (Si)")
    elif an == 15:
        print("Fosfor (P)")
    elif an == 16:
        print("Kükürt (S)")
    elif an == 17:
        print("Klor (Cl)")
    elif an == 18:
        print("Argon (Ar)")
    elif an == 19:
        print("Potasyum (K)")
    elif an == 20:
        print("Kalsiyum (Ca)")
    elif an == 21:
        print("Skandiyum (Sc)")
    elif an == 22:
        print("Titanyum (Ti)")
    elif an == 23:
        print("Vanadyum (V)")
    elif an == 24:
        print("Krom (Cr)")
    elif an == 25:
        print("Manganez (Mn)")
    elif an == 26:
        print("Demir (Fe)")
    elif an == 27:
        print("Kobalt (Co)")
    elif an == 28:
        print("Nikel (Ni)")
    elif an == 29:
        print("Bakır (Cu)")
    elif an == 30:
        print("Çinko (Zn)")
    else:
        print("(FK3) Hata: Böyle Bir Element Tanımlanmadı Veya Yok.")

def pH(value):
    if type(value) is int and value >= 0:
        if value >= 0 and value <= 6:
            print("Asidik")
        elif value == 7:
            print("Nötr")
        elif value >= 8 and value <= 14:
            print("Bazik")
    else:
        print("(FK4) Hata: Girilen pH Değeri Bir Sayı Değil Veya 0'dan Küçük.")

def CtoF(celsius):
    if type(celsius) is int or float:
        fahrenheit = celsius * 1.8 + 32
        print(fahrenheit, "°F")
    else:
        print("(FK5) Hata: Girilen Celcius Değeri Bir Ondalık Veya Tamsayı Değeri Değil.")

def FtoC(fahrenheit):
    if type(fahrenheit) is int or float:
        celsius = (fahrenheit - 32) / 1.8
        print(celsius, "°C")
    else:
        print("(FK6) Hata: Girilen Fahrenheit Değeri Bir Ondalık Veya Tamsayı Değeri Değil.")
