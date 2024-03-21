# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 08:54:48 2024

@author: qarsh
"""

#                8-DARS 
#    TARTIBLASH  sort alfabit bo'yicha tartiblaydi
#cars=['bmv','audio','nekia','cobalt','malibu','spark','juguli','tiko']
#cars.sort()
#print(cars)
#  reverse esa alfabitni teskari tomondan tartiblaydi
#cars.sort(reverse=True)
#cars.sort(reverse=False)
#print(cars)
#  SORTED METODI RO'YXATGA TEGINMAGAN HOLDA tartiblaydi
#cars=['bmv','audio','nekia','cobalt','malibu','spark','juguli','tiko']
#print(sorted(cars))

#sonlar=[5,12,36,98,102,145,65,80,-3,-9,-52]
#sonlar.sort()
#print(sonlar)
#print(sorted(sonlar))
#        LEN funksiya royxatda nechtaligini aniqlab beradi 
#cars=['bmv','audio','nekia','cobalt','malibu','spark','juguli','tiko']
#print(len(cars))
 
#       RANGE FUNKSIYASI sonlarni yaratadi
#sonlar=[list(range(0,40))]
#print(sonlar)
#toq_sonlar=[list(range(1,40,2))]
#juft_sonlar=[list(range(0,40,2))]
#print(toq_sonlar)
#print(juft_sonlar)
#          MAX MIN SUM funksiyalari 

#narxlar=[1200,1450,1690,1890,6500,7000,8950,9000,10500,12350] 
#arzon=min(narxlar)
#qimmat=max(narxlar)
#jami=sum(narxlar)
#print(arzon)
#print(qimmat)
#print(jami)
#print('eng arzon narx ', arzon, ' eng qimmat narx ', qimmat ,' jami esa ',jami)

#             ROYXATLARNI KESISH
#cars=['bmv','audio','nekia','cobalt','malibu','spark','juguli','tiko']
#my_cars=cars[0:3]
#print(my_cars)
#print(cars[0:4])
#           NUSXA OLISH 
#cars=['bmv','audio','nekia','cobalt','malibu','spark','juguli','tiko']
#my_cars=cars[:]
#print(my_cars)

#            TUPLES o'zgarmas ro'yxat buni ichiga hech nima qo'sholmaymiz ham ololmaymiz ham 
#toys=('bus','car','bear','snake','lizard')
#print(toys)
#print(toys[0])
#                      MISOLLAR
#davlatlar=['uzbekistan','tajikistan','afganistan','qozogistan','russia','ukraina']
#print(davlatlar)
#print(sorted(davlatlar))
#davlatlar.sort(reverse=True)
#print(davlatlar)
sonlar=list(range(120,1200,2))
#print(sonlar)
#   sonlarni boshidan ortasidan va oxiridan royxat chiqarish
#print(sum(sonlar))
#print(max(sonlar)-min(sonlar))
#print(len(sonlar))
#print(sonlar[:20])
#print(sonlar[-20:])
#print(sonlar[530:550])
#           YANGI MISOL
taomlar=['osh','mastava','shorva','moshkichiri','xalim']
nonushta=taomlar[:]
nonushta.append('baliq')
nonushta.append('shashlik')
nonushta=tuple(nonushta)
print(nonushta)
print(taomlar)











