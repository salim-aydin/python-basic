numbers = range(10)
print(numbers)

for number in numbers:
    print(number)




# Çift sayıların karesi alınarak bir sözlüğe eklenmesi istenmektedir.
# Key' ler orjinal değerler , value'ler ise değiştirilmiş değerler

numbers = range(10)
new_dict = {}
for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2
print(new_dict)

kanks = {n : n ** 2 for n in numbers if n % 2 == 0}
print(kanks)


-------





















# ['total', 'speeding", 'alcohol', 'not_distracted', 'no_previous", ins_premium", "ins_losses', 'abbrev']
# Bir veri setindeki değişken isimlerini değiştirmek

import seaborn as sns
df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]

---------
import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]
print(df.columns)































# İsminde "INS" olan değişkenlerin başına FLAG , diğerlerine NO_FLAG eklemek istiyoruz
# df.columns = Index(['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS',
       'INS_PREMIUM', 'INS_LOSSES', 'ABBREV'],
      dtype='object')

# İsminde "INS" olan değişkenlerin başına FLAG , diğerlerine NO_FLAG eklemek istiyoruz

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]
print(df.columns)

degisken1 = [col for col in df.columns if "INS" in col]
print(degisken1)


degisken2 = ["FLAG_" + col for col in df.columns if "INS" in col]
print(degisken2)

degisken3 = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns ]
print(degisken3)

df.columns =  ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns ]
print(df.columns)


