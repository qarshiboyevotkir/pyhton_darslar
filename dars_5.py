# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 08:15:26 2024

@author: qarsh
"""
# 5-DARS STRING matnlar bilan ishlash 
# maxsus uni codlar  ushbu saytda amalga oshiriladi:
#https://symbl.cc/en/collections/symbols-for-steam/
# + belgisi matnlarni qo'shishda ishlatiladi 
#ism="O'tkir"
#print("Mening ismim"+ism)

#ism="O'tkirjon"
#familiya="Qarshiboyev"
#print(ism+familiya)


# ism va familiya orasida joy qoldirish uchun '' belgisidan foydalanish kerak
#ism="O'tkirjon"
#familiya="Qarshiboyev"
#print(ism + '   '+familiya)

# f -string
# matnlarni birlashtirishda ishlatiladi
#ism="O'tkir"
#familiya="Qarshiboyev"
#ism_familiya= f"{ism}     {familiya}"
#print(ism_familiya)

#ism="O'tkirjon"
#familiya="Qarshiboyev"
#print(f"Salom, mening ismim {ism} {familiya} ")


# MAXSUS BELGILAR 
# \t  va belgisi uzun boshliq qoldiradi
# \n belgisi sozlarni keyingi qatorga tushiradi. 
#print('Hello world')
#print('hello           \tworld')
#print('hello\nworld')


#  STRING METODLAR
# upper-harflarni katta qiladi 
# lower- harflarni kichkina qiladi 
# title va capitalize esa sozlarni bosh harflarini katta qiladi 

#ism='James'
#familiya='Bond'
#ism_familiya=f"{ism} {familiya}"
#print(ism_familiya.upper())
#print(ism_familiya.lower())
#print(ism_familiya.title())
#print(ism_familiya.capitalize())


# BO'SHLIQLARNI  olib tashlovchi metodlar 
# lstrip- chap tomonni olib tashlaydi
# rstrip- ong tomonni olib tashlaydi
# strip- ikkala tomonni olib tashlaydi

#meva='               olmani               '
#print(meva)
#print("Men" + meva + "yaxshi ko'raman")
#print("Men " +meva.lstrip() + "yaxshi ko'raman")
#print("Men" +meva.rstrip() + " yaxshi ko'raman")
#print("Men "+ meva.strip() + " yaxshi ko'raman")


# INPUT  sorov funksiyasi

#ism=input("Ismingiz nima?")
#print("Assalomu alaykum," + ism)

#ism= input("Ismingiz nima? \n >>>>>>")
#print("Assalomu alaykum, " +ism.upper())

# MISOLLAR MISOLLAR MISOLLAR MISOLLAR MISOLLAR MISOLLAR MISOLLAR MISOLLAR 
#kocha= "Bogbon"
#mahalla= "Sogbon"
#tuman= "Bodomzor"
#viloyat= "Samarqand"
#1-misol
#print(kocha.title() + " ko'chasi", mahalla.capitalize() + " mahallasi" , viloyat.upper() + " Viloyati")
#2-misol
#print(kocha + " ko'chasi \n", mahalla + " mahallasi \n", viloyat + " Viloyati")
#3-misol
#kocha=input("Ko'changiz nomi nima? \n>>>>>")
#mahalla=input("Mahallangiz nomi nima? \n>>>>>")
#tuman=input("Tumaningiz nomi nima? \n>>>>>")
#viloyat=input("Viloyatingiz nomi nima? \n>>>>>")
#print(kocha + " ko'chasi", mahalla + " mahallasi", tuman + " tumani", viloyat + " Viloyati")



# MUSTAXKAMLASH UCHUN MASHQLAR
               #1-misol
#kocha= "Bogbon"
#mahalla= "Sogbon"
#tuman= "Bodomzor"
#viloyat= "Samarqand"
#print(kocha + " ko'chasi,", mahalla + " Mahallasi,", tuman + " tumani,", viloyat + " Viloyati")

#             2-misol
#kocha = input("Ko'changiz nomi nima? \n >>>>")
#mahalla = input("Mahallangiz nomi nima? \n >>>>")
#tuman = input("Tumaningiz nomi nima? \n>>>>")
#viloyat = input("Viloyatingiz nomi nima? \n>>>")
#print(kocha + " ko'chasi,", mahalla + " Mahallasi,", tuman + " tumani,", viloyat + " Viloyati")
#                3-misol
#kocha = input("Ko'changiz nomi nima? \n >>>>")
#mahalla = input("Mahallangiz nomi nima? \n >>>>")
#tuman = input("Tumaningiz nomi nima? \n>>>>")
#viloyat = input("Viloyatingiz nomi nima? \n>>>")
#print(kocha + " ko'chasi, \n", mahalla + " Mahallasi, \n", tuman + " tumani, \n", viloyat + " Viloyati")
#                  4-misol
#kocha= "Bogbon"
#mahalla= "Sogbon"
#tuman= "Bodomzor"
#viloyat= "Samarqand"
#yangi_manzil= f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati."
#print(yangi_manzil)
#                  5-misol
kocha= "Bogbon"
mahalla= "Sogbon"
tuman= "Bodomzor"
viloyat= "Samarqand"
#print(kocha.upper() + " ko'chasi,", mahalla.upper() + " Mahallasi,", tuman.upper() + " tumani,", viloyat.upper() + " Viloyati")
#print(kocha.capitalize() + " ko'chasi,", mahalla.capitalize() + " Mahallasi,", tuman.capitalize() + " tumani,", viloyat.capitalize() + " Viloyati")
#print(kocha.lower() + " ko'chasi,", mahalla.lower() + " Mahallasi,", tuman.lower() + " tumani,", viloyat.lower() + " Viloyati")




















