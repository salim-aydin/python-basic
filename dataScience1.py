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






