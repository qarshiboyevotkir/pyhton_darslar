# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 20:16:11 2024

@author: qarsh
"""

#  7-DARSLAR LISTLAR 
# mevalar=["olma", "anjir", "shaftoli", 'behi']
# print(mevalar)
# sonlar=["bir", 'ikki', 3,4,5]
# print(sonlar)
# Agar bir qiymatlar ichidagi bittasini tanlab olmoqchi bo'lsak.
# unda indeksga qarab murojat qilamiz 
# sonlar=['bir','ikki','uch','tort','besh','olti']
#sonlar[0]= 'olma'
#print(sonlar[0])
#print(sonlar[-1])
# print(sonlar[1])
# print(sonlar[0].upper())
#     APPEND METODI  bu royxatga yana o'zgaruvchi qo'shadi 
#     APPEND metodi faqat ro'yxatni oxiriga qo'shadi 
#sonlar=['bir','ikki','uch','tort','besh','olti']
#sonlar.append('yetti')
#sonlar.append('sakkiz')
#print(sonlar)
#    INSERT metodi royxatga yana o'zgaruvchi qo'shadi 
#    faqat royxatni hohlagan joyiga qo'shishingiz mumkin 
# sonlar=['bir','ikki','uch','tort','besh','olti']
# sonlar.insert(3,'yigirma ikki')
# print(sonlar)
#     DEL funksiyasi ro'yxatni ichidagi indeksni olib tashlaydi 
# cars=['lasetti','cobalt','spark','nexia 3','jentra','malibu']
# del cars[0]
# del cars[1]
# print(cars)
#     REMOVE metodi royxatda narsalar kopligidan olib tashlamoqchi bo'lgan 
#     narsamizni indeksi nechinchi raqamda turishini bilmaganimizda yordam 
#     beradi
# cars=['lasetti','cobalt','spark','nexia 3','jentra','malibu']
# cars.remove('cobalt')
# cars.remove('malibu')
# print(cars)
#    REMOVE metodi yana afzalliklari ro'yxatda ikkita narsa tursa faqat 1-chi
#    turgan indeksni olib tashlaydi
#cars=['Lasetti','cobalt','spark','nexia 3','jentra','malibu', 'Lasetti','malibu2']
# cars.remove('Lasetti')
# print(cars)
#    POP metodi bu su'g'urib olish uchun xizmat xizmat qiladi 
# moshina=cars.pop(0)
# print('men ' + moshina +' sotib oldim ')
#    POP metodida ichiga indeks bermasak u ro'yxatni oxiridagi narsani tanlidi
# moshina=cars.pop()
# print('Men '+ moshina + ' sotib oldim')
#   Ro'yxatlarni ichiga qo'shish uchun quy amallar bajariladi
# narxlar=[4000,5000,6000,7000,8000,9000]
#narxlar[0]=narxlar[0]+571
#print(narxlar)

#               MISOLLLAR 
#ismlar=['Maxmud', 'Sarvar', 'Muzaffar', 'Oybek', 'Alijon']
#print('salom '+ ismlar[1]+ ' bugun choyxona bormi?' )
#print('salom '+ ismlar[2]+ ' bugun choyxona bormi?' )
#print('salom '+ ismlar[0]+ ' bugun choyxona bormi?' )
#print('salom '+ ismlar[3]+ ' bugun choyxona bormi?' )
#print('salom '+ ismlar[4]+ ' bugun choyxona bormi?' )
                #   2-MISOL
#sonlar=[10,15,-8,-5,10.5]
#sonlar[0]=sonlar[0]+10
#sonlar[1]=sonlar[0]+10
#sonlar[2]=sonlar[0]+10
#sonlar[3]=sonlar[0]+10
#print(sonlar[0])
#print(sonlar[2])
#print(sonlar[4])
                       # 3-MISOL
#t_shaxslar=['Amir Temur', 'Imom al Buxoriy', 'Alisher Navoiy', 'Bobur']
#z_shaxslar=['Stiv Jobs', 'Bil geyts', 'Shavkat Mirziyoyev', 'Putin']
#print('Men tarixiy shaxslardan '+ t_shaxslar.pop(0)+ ' korishishni hohlayman.Zamonaviy shaxslardan esa ' 
#      + z_shaxslar.pop(3)+ 'ni korishishni hohlayman')
                        # 4-MISOL
#friends=['Maxmud', 'Sarvar', 'Muzaffar', 'Oybek', 'Alijon']       
#friends.append('Akrom') 
#friends.append('saloxiddin') 
#friends.append('shoxjahon') 
#friends.append('Baxtishod') 
#friends.append('Elyor') 
#friends.remove('Sarvar')
#friends.remove('saloxiddin')
#friends.insert(0, 'otkir')
#print(friends)                
                        # 5-MISOL
friends=['Maxmud', 'Sarvar', 'Muzaffar', 'Oybek', 'Alijon'] 
yangi_mehmonlar=[]    
yangi_mehmonlar.append(friends.pop(1))
yangi_mehmonlar.append('saloxiddin')
yangi_mehmonlar.append('Akmal')
print(yangi_mehmonlar)                       















