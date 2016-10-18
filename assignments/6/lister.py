# lag en liste number_list med tall fra 0 til og med 99
number_list = list(range(100))

# summer alle tall i listen som er delelig 3 eller 10
print(sum(i for i in number_list if i % 3 == 0 or i % 10 == 0))

# iterer tall-listen med steps på 2 - altså partallene
for i in range(0, len(number_list) - 1, 2):
    # neste element lik dette elementet, dette elementet lik neste
    number_list[i + 1], number_list[i] = number_list[i], number_list[i + 1]

# print tall-listen
print(number_list)

# lag en tom liste siden man ikke kan sette verdier på indexer utenfor lista
reversed_list = [0] * 100

# sett siste element lik første, nest siste lik andre
for i in range(len(number_list)): reversed_list[i] = number_list[-i-1]

# print den reverserte lista
print(reversed_list)
