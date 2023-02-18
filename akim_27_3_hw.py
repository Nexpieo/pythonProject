while True:
    num_letters = 0
    num_consonants = 0
    num_vowels = 0
    vowels = "aeiouyаеёиоуыэюя"
    consonants = "qwrtpsdfghjklzxcvbnmйцкнгшщзхъфвпрлджчсмтьб"

    word = input("Введите ваше слово: ")

    for e in word.lower():
        if e in vowels:
            num_vowels += 1

    for q in word.lower():
        if q in consonants:
            num_consonants += 1

    for i in word:
        num_letters += 1
    cons = (num_consonants / num_letters * 100).__round__(2)
    vow = (num_vowels / num_letters * 100).__round__(2)
    print(f"Слово:{word}")
    print(f"Количество букв: {num_letters}")
    print(f"Согласных букв: {num_consonants}")
    print(f"Гласных букв: {num_vowels}")
    print(f"Гласныe/Согласныe: {vow}%/{cons}%")
    if word == "exit":
        break
