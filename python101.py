#yorum satırı
9 #integer
9.2 #float
9+9 # F9'la çalıştırırsan 18
9*9 # F9'la çalıştırırsan 81
"Bu ifade bir stringtir" #F9'la çalıştırırsan, yazdığın değeri döndürür 

#print() 
#Eğer ekrana gerçekten basmak istersen print() kullanırsın
#Örnek
print(9)

#Python programlama dilinde her şey nesnelerden oluşur
#Her şey nesne olarak tutulur

#type() 
#Tipini öğrenmek için type() fonksiyonunu kullanırsın
type(9)
type(9.2)
type("hello") # TEK TIRNAKLA DA KULLANILIR, FARKETMİYOR


print(type(9))
print(type("hello"))





#Karakter Dizilerini Yakından Tanıyalım
#STRİNGLER

"a" + "b" # çıktı ab
#veya
"a" "b" # çıktı ab
"a""b" # çıktı ab

"a"*3 # çıktı aaa
"a "*3 # çıktı a a a



#STRİNG METODLARI

#len() boyutu inceler, sadece stringlerde kullanılmaz
mvk = "gelecegi_yazanlar"
len(mvk) #çıktı da 17 gözükür ,1 den başlar :D

a = 9
b = 10

a*b # f9 la çalıştırırsan 90 eder

#del değişken silmek için
del a # a değişkenini siler
# a*b # a değişkeni olmadığı için çarpma işlemi yapmaz






# Büyük/Küçük Harf Dönüşümleri: upper & lower Metodları
# upper() lower() atama işlemi yapmazzz
mvk = "gelecegi_yazanlar"
# .upper() 
# .lower()
# .capatalize()  sadece İLK harf büyükle başlar

mvk.upper() # çıktıda GELECEGI_YAZANLAR
mvk.lower() # çıktıda gelecegi_yazanlar
mvk.capitalize() # çıktıda Gelecei_yazanlar

# Eğer mevcut karakter dizisini değiştirmek istiyorsanız, 
# bu yöntemi bir atama ifadesi içinde kullanmanız gerekir. 
# Örneğin, mvk = mvk.upper() gibi. 


# Küçük mü büyük mü diye , soru sormak için
# .islower yahut .isupper
# True yahut, False dönderir
mvk.islower()
mvk.isupper()





# Karakter Değiştirme: replace Metodu, atama işlemi yapmazzz
# ilk , neyi değiştirmek istediğin 
# ikinci, neyle değiştirmek istediğin
mvk.replace("e","a")
# değişen şeyi atamak için

ata = mvk.replace("e","a")

ata.replace("a","i") # çıktı da gilicigi_yizinler






# Karakter Kırpma İşlemleri: strip Metodu
# strip() default olarak boşlukları siler, atama işlemi yapmazzz
deneme = "   her     taraftaki     boşlukları     mı    siliyor   "
deneme.strip() # sadece baştaki ve sondaki boşlukları siler

# "   her     taraftaki     boşlukları     mı    siliyor   "
# 'her     taraftaki     boşlukları     mı    siliyor'
# yukarıdakini aşağıdakine çevirir

yildiz = "**yıldızları sil**"
yildiz.strip("**") # çıktı 'yıldızları sil'
yildiz.strip("*") # çıktı 'yıldızları sil'

# Kendin öğrenmek için dir(degisken) , bir nevi console.log()
# Kendin öğrenmek için dir(degisken) , bir nevi console.log()
# Kendin öğrenmek için dir(degisken) , bir nevi console.log()
# Kendin öğrenmek için dir(degisken) , bir nevi console.log()
# Kendin öğrenmek için dir(degisken) , bir nevi console.log()
mvk = "gelecegi_yazanlar"
dir(mvk)

# bütün kelimelerin ilk harfini büyültmek için
# .title
mvk.title() # çıktıda Gelecegi_Yazanlar


#substring
mvk[0] #g
mvk[1] #e
mvk[2] # l
mvk[3] #e
mvk[4] #c
mvk[5] #e
mvk[6] #g
mvk[7] #i
mvk[8] #_

############ sol dahil , sağ hariç , e kadar seçim yap yani
mvk[0:3] # çıktı'da 'gel' yazar
######## iki nokta ifadesi soldaki sayıdan sağdaki sayıya kadar seçim yap demek

karmasik = 4+2j # complex sayı tanımlayabiliyoruz

############ type dönüşümleri
############ type dönüşümleri
############ type dönüşümleri
############ type dönüşümleri
############ type dönüşümleri
############ type dönüşümleri 
toplama_bir = input()
toplama_iki = input()

type(toplama_bir)
toplama_bir + toplama_iki # string olduğu için yan yana koyar
######## düzeltmek için
int(toplama_bir) + int(toplama_iki)

float(5) # 5.0
int(5.0) # 5
int(5.3) # 5

str(12)


############## print fonksiyonu hakkında
############## print fonksiyonu hakkında
############## print fonksiyonu hakkında
############## print fonksiyonu hakkında
############## print fonksiyonu hakkında
############## print fonksiyonu hakkında
############## print fonksiyonu hakkında
############## print fonksiyonu hakkında
print("deniyoruz")
print("gelecegi","yazanlar") # klasik javascript'teki gibi
print("gelecegi","yazanlar",sep="_") # arayı değiştirmek için 
## sep bir argümandır, argüman fonksiyonların genel amaçlarını,
# biçimlendirmek için kullanılan alt görev belirticilere denir

# fonksiyonların detaylı bilgilerine erişmek için
# ?print yazılır , yani başına soru işareti koyulur

# fonksiyonların detaylı bilgilerine erişmek için
# ?print yazılır , yani başına soru işareti koyulur

# fonksiyonların detaylı bilgilerine erişmek için
# ?print yazılır , yani başına soru işareti koyulur

# fonksiyonların detaylı bilgilerine erişmek için
# ?print yazılır , yani başına soru işareti koyulur

# "9"+1 type error verir 

"_Python_".strip("_") # Python

ifade = "gelecek_geldi"
ifade.replace("i", "ı") # 'gelecek_geldı'

degisken = 4
degisken*degisken # 16

a = "bu uzun bir metindir"
a[2:5]

type(3.14) # float

ifade = "Merhaba! "
ifade.strip("") # 'Merhaba! '



