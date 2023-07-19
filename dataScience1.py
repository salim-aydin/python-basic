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



















# ['total', 'speeding", 'alcohol', 'not_distracted', 'no_previous", ins_premium", "ins_losses', 'abbrev']
# Bir veri setindeki değişken isimlerini değiştirmek

import seaborn as sns
df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]






