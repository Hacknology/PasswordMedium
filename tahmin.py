#c0d3r: Hacknology
#v1.1
import random
f = open('password.txt', 'w+')
sev = input("[*] GF name:: ")
dogum = input("[*] Birth: ")
ugurlu_Sayi = input("[*] Lucky number:: ")
dog_yer = input("[*] Birth place: ")
özel_tarih = input("[*] Special date: ")
isim = input("[*] Name: ")
sayi = ['1234567890']
bilgiler = [sev, dogum, ugurlu_Sayi, dog_yer, özel_tarih, isim]
bilgiler+=sayi
passw=[]
for d in bilgiler:
    passw.append(d.lower())

for d in bilgiler:
    for d2 in bilgiler:
        passw.append(d.lower()+d2.lower())
        passw.append(d.lower()+"."+d2.lower())
for d in bilgiler:
    for d2 in bilgiler:
        for d3 in bilgiler:
            passw.append(d.lower()+d2.lower()+d3.lower())
            passw.append(d.lower()+"."+d2.lower()+"."+d3.lower())
f.write("\n".join(passw))
f.close()
            
print("[+] Over.")
