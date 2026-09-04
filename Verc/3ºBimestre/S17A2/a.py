notas = [1,2,3,4,5,6,7,8,9,10]

s = 0
for i in range(0, len(notas)):
    s = s + notas[i]

media = s / len(notas)

print("Média final:", media)
