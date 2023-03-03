### VERİ YAPILARI
### LİSTELER
# 1 Değiştirilebilir
# 2 Kapsayıcıdır(farklı tipte verileri tutabilir)
# 3 Sıralıdır (indeks işlemleri yapılabilir)

## Liste oluşturmanın iki yolu var
# Birincisi : []
# İkincisi : list() 

notlar = [90,80,70,50]
type(notlar)

liste = ["a",19.3,90]
list_genis = ["a",19.3,90,notlar]

len(list_genis) # çıktıda 4

list_genis[0] # çıktıda 'a'
type(list_genis[0]) # çıktıda str

tum_liste = [liste, list_genis] # iki listeyi birleştirme

del tum_liste

###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################

liste = [10,20,30,40,50]
liste[0] #10
liste[1] #20
liste[0:2] # [10,20]
liste[:2] # [10,20]
liste[2:] # [30,40,50]

###############################
###############################
###############################
###############################
###############################

yeni_liste = ["a",10,[20,30,40,50]]
yeni_liste[2][1] #30

###############################
###############################
###############################
###############################
###############################

# LİSTELER , ELEMAN DEĞİŞTİRME

liste = ["ali", "veli","berkcan","ayse"]
liste

liste[1] = "velinin_babasi"
liste


###############################
###############################
###############################
###############################

liste = ["ali", "veli","berkcan","ayse"]
liste[0:3]

liste[0:3] = "alinin_babasi", "velinin_babasi" , "berkcanin_babasi"
liste # ['alinin_babasi', 'velinin_babasi', 'berkcanin_babasi', 'ayse']

###############################
###############################
# LİSTEDEKİ ELEMANI SİLME

del liste[2]

#################################################
# Metodlar ile Eleman Ekleme ve Silme: append ve remove

dir(liste)
liste
liste.append("berkcan")
liste

## liste değiştirilebilir olduğu için, atama yapmadan
## metod'la direkt olarak değiştirebildik

liste.remove("berkcan")
liste.remove("velinin_babasi")

###########################################
# Indekse Göre Eleman Ekleme ve Silme: insert ve pop

liste = ["ali", "veli", "isik"]
liste
liste.insert(0,"ayse")
liste

len(liste)
liste.insert(len(liste), "beren") #direkt olarak sona eklemek için
# 0 1 2 vs diye sayarsın, listeden 1 az çıkar 
# ama zaten oraya ekleme yapacaktın :D

liste.pop(0)
liste.pop(2)


###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
# Diğer Liste Metodları

#count sayma
liste = ["ali", "veli", "isik","ali","veli"]
liste.count("ali") #2 , yani aliden 2 tane var

#copy kopyalama
liste_yedek = liste.copy() # yedekleme yapmak için

#extend birleştirme
liste.extend(["a","b",10])
liste.extend(liste_yedek)

#index, bir elemanın hangi indexte olduğunu öğrenme
liste.index("ali")

#reverse listeyi tersine çevirme
liste.reverse()

liste = [10,40,5,90]
#sort sıralama yapmak için kullanılır
liste.sort()
liste

#tüm listeyi silmek için
#clear

liste.clear()


###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
##############################################################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
##############################################################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################

# VERİ YAPILARI 
#TUPLE

#Listeler; 
#1 kapsayıcıdır(birbirinden farklı tipleri barındırabilir)
#2 sıralıdır, index işlemleri gerçekleştirilebilir
#3 değiştirilebilir

#TUPLE'DA İŞTE BU 3.DURUM FARKLI
#TUPLE değiştirilemez

t = ("ali","veli",1,2,3.2,[1,2,3,4])
t = "ali","veli",1,2,3.2,[1,2,3,4]

#liste = [1, 2, 3, 4, 5]
#tuple_nesnesi = tuple(liste)
#print(tuple_nesnesi)

#tek elemanlı tuple oluşturmak için
t = ("eleman",) #tek elemanlı TUPLE oluştururken, sona virgül ekleniyor
type(t)

#DEĞİŞTİRİLEMEZ OLDUĞUNU KANITI
t = ("ali","veli",1,2,3.2,[1,2,3,4])
t[0]
t[0:3]

# t[2] = 99 ,,,,    DEĞİŞTİRİLEMEZ... DEĞİŞTİRİLEMEZ... DEĞİŞTİRİLEMEZ...

###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
##############################################################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
##############################################################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################
###############################

# VERİ YAPILARI , DİCTİONARY(SÖZLÜK)
#Listeler; 
#1 kapsayıcıdır(birbirinden farklı tipleri barındırabilir)
#2 sıralıdır, index işlemleri gerçekleştirilebilir
#3 değiştirilebilir
 
# dictionary, de 2.olan durum farklıdır, SIRASIZDIR
# KEY VALUE durumu

sozluk = {"REG":"Regresyon Modeli",
          "lOJ": "Lojistik Regresyon",
          "CART":"Classification and Reg"}
sozluk
len(sozluk) #3


sozluk = {"REG":10,
          "lOJ": 20,
          "CART":30}
sozluk 


sozluk = {"REG":["RMSE",10],
          "lOJ": ["MSE",20],
          "CART":["SSE",30]}
sozluk 


#Sözlük Eleman Seçme İşlemleri 
sozluk = {"REG":"Regresyon Modeli",
          "lOJ": "Lojistik Regresyon",
          "CART":"Classification and Reg"}
sozluk
# sozluk[0] la seçim yapılmaz, çünkü sıra yok ki
sozluk["REG"] #'Regresyon Modeli'

##############################################
##############################################
sozluk = {"REG":{"RMSE":10,"MSE":20,"SSE":30},
          "lOJ":{"RMSE":10,"MSE":20,"SSE":30},
          "CART":{"RMSE":10,"MSE":20,"SSE":30}
          }

sozluk
sozluk["REG"]["SSE"]
