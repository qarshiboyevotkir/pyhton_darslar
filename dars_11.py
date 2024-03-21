# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 20:50:02 2024

@author: qarsh
"""

#     11-DARS  11-DARS 11-DARS 
#yosh= int(input("Yoshingiz nechada?\n>>>"))
#if yosh<=4:
 #   print('sizga kirish bepul')
#elif yosh<=12:
 #  print('Sizga kirish 5000 som')   
#elif yosh<=18:
 #   print("Sizga kirish bepul ")
#else:
 #  print("Sizga kirish 10000 so'm")   
    
    
#kun = input("Bugun kun nima?\n>>>")
#if kun.lower() =='shanba' or kun.lower()=='yakshanba': 
 #   print("Dam olish kuni")
#else:
 #   print("Bugun ish kuni")


#kun = input("Bugun kun nima?\n>>>")
#harorat=float(input("Havo harorati qanday?")) 
#if kun.lower()=="yakshanba"  and harorat>=30:
#    print("Cho'milishga ketdik")
#elif kun.lower()=="yakshanba" and harorat<30:
#    print("Uyda dam olamiz ")
    
#kun=input("Bugun kun nima?")   
#harorat=float(input("Havo harorati qanday?"))
#if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#    print("Cho'milgani ketdik")
#elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30: 
#    print("Uyda qolamiz")    
    
#narh=15000
#choy=1
#salat=0
#non=1
#kompot=1
#assorti=1
#if choy:
 #   print("Mijoz choy oldi")
 #   narh=narh+3000
#if salat:
 #  print("Mijoz salat oldi")
  # narh=narh+5000
#if non:
 #   print("Mijoz non oldi")
  #  narh=narh+2000
#if kompot:
 #   print("Mijoz kompot oldi")
  #  narh=narh+5000
#if assorti:
 #   print("Mijoz assorti oldi")
  #  narh=narh+15000
    
#print(f"Jami {narh} so'm bo'ldi")
    

#menu=["osh","qozon kabob","shashlik","norin","somsa"]
#ovqat=input("Nima ovqat yeysiz?>>>")
#if ovqat.lower() in menu:
 #   print("Buyurtma qabul qilindi")
#else:
 #   print("Afsuski bizda bunday ovqat yo'q")
    
    
#menu=["osh","qozon kabob","shashlik", "norin","somsa"]
#buyurtmalar=["osh","somsa","manti","shashlik"]
#if buyurtmalar:
 #for taom in buyurtmalar:
  #  if taom in menu:
   #     print(f"Menuda {taom} bor")
    #else:
     #   print(f"Kechirasiz, menuda {taom} yo'q")
 
   
   #     MISOLLAR MISOLLAR MISOLLAR MISOLLAR 
#           1-MISOL
#yosh=int(input("Yoshingizni kiriting?\n>>>"))
#if yosh<=4 or yosh>=60:
 #   print("Sizga kirish bepul")
#elif yosh<=18:
 #   print("Sizga 10.000 so'm")
#elif yosh>18:
 #   print("Sizga 20.000 so'm")
    #  2-MISOL
#x=int(input("birinchi sonni kiriting?\nx="))
#y=int(input("ikkinchi sonni kiriting?\ny="))
#if x>y:
 #   print(f"{x}>{y}")
#elif y>x:
 #   print(f"{y}>{x}")
#elif x==y:
 #   print("sonlar teng")
    
    #  3-MISOL   3-MISOL 3-MISOL
#mahsulotlar=["anor","uzum","olma","tarvuz","shaftoli","banan","kivi","mandarin","apelsin","tarvuz","qovun","handalak"]
#savat=[]
#for n in range(5):
#    savat.append(input(f"Savatga {n+1} mahsulotni qo'shing.\n>>>>"))

#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        print(f"Do'konimizda {mahsulot} bor")
#    else:
#        print(f"Do'konimizda {mahsulot} yo'q")
      #  4-Misol 4-Misol Misol 4-MISOL
#mahsulotlar=["anor","uzum","olma","tarvuz","shaftoli","banan","kivi","mandarin","apelsin","tarvuz","qovun","handalak"]
#savat=[]
#for n in range(5):
#   savat.append(input(f"Savatga {n+1} mahsulotni kiriting.\n>>>"))

#bor_mahsulot=[]
#mavjud_emas=[]
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        bor_mahsulot.append(mahsulot)
#    else:
#        mavjud_emas.append(mahsulot)
        
#if mavjud_emas:
#    print(f"Do'konimizda quyidagi mahsulotlar yo'q")
#    for mahsulot in mavjud_emas:
#        print(mahsulot)
#else:
#    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

#                    5-MISOL  5-MISOL 
son=int(input("Istalgan butun son kiriting?>>>"))
for x in range(2,11):
   if not (son%x) :
    print(f"{son}, {x} ga qoldiqsiz bolinadi ")
   else:
    print(f"{son},soni {x} ga qoldiqsiz bolinmaydi")






























