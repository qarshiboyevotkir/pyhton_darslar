# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:27:21 2024

@author: qarsh
"""

#    FOR TAKRORLASH OPERATORI
#mehmonlar=['Ali','Vali','Hasan','Husan','Olim']
#for mehmon in mehmonlar:
 #   print('Salom ', mehmon)
  #  print('Hayr ', mehmon)


#mehmonlar=['Ali','Vali','Hasan','Husan','Olim']
#for mehmon in mehmonlar:
 #   print(f"Hurmatli {mehmon}, sizni 20 - dekabr kuni nahorgi oshga taklif etamiz")
  #  print("Hurmat bilan Axbotayevlar oilasi")
    
#sonlar=list(range(1,11))
#for son in sonlar:
 #    print(f"{son} ning kvadrati {son**2} ga teng")

#sonlar=list(range(11))    # range ichiga 1 ta son kiritsak u 0 dan boshlab ro'yxat chiqazib beradi
#sonlar_kvadrati=[]
#for son in sonlar:
 #   sonlar_kvadrati.append(son**2)
#print(sonlar)
#print(sonlar_kvadrati)


#dostlar=[]
#print('5 ta eng yaqin dostingiz kim?')
#for n in range(5):
 #   dostlar.append(input(f"{n+1} - do'stingizni kiriting? \n" ))
  #  print(dostlar)

 #                MISOLLAR
#dostlar=["ali",'vali','gani','sardor','muzaffar']
#for dost in dostlar:
 #   print('salom', dost)
#print(f"{len(dostlar)} marta takrorlanayapti")    # len() royxatni uzunligini aniqlaydi
  

#sonlar=range(11,100,2)    # 10 dan 
#for son in sonlar:
  #  print(son*son*son)  # bunda ham sonni kubini hisoblaydi
   # print(son**3)   #  bunda sonni kubini hisoblaydi


#kinolar=[]
#print('5 ta eng sevimli kinolaringizni kiriting?')
#for n in range(5):
 #   kinolar.append(input(f'{n+1} - kinoyingizni kiriting?\n'))   
  #  print(kinolar)
  
n_people=int(input('bugun nechta odam bilan suxbat qurdingiz?>>>\n'))
ismlar=[]
for n in range(n_people):
    ismlar.append(input(f'{n+1} suxbat qilgan odamingiz kim edi?'))
    print(ismlar)
    
