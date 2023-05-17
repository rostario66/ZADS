def hash_klic(k, velikost_tabulky):
    return hash(str(k)) % velikost_tabulky

def hash_dalsi(k, velikost_tabulky):
    return 1 + (hash(str(k)) % (velikost_tabulky - 1))

def vloz_do_tabulky(table, k, hodnota):
    index = hash_klic(k, len(table))
    dalsi = hash_dalsi(k, len(table))

    while table[index] is not None:
        if table[index][0] == k:
            break
        index = (index + dalsi) % len(table)

    table[index] = (k, hodnota)

def hledej_rok(table, k):
    index = hash_klic(k, len(table))
    dalsi = hash_dalsi(k, len(table))

    while table[index] is not None:
        if table[index][0] == k:
            return table[index][1]
        index = (index + dalsi) % len(table)

    return "Tento rok se nic nestalo."

T = [None] * 1000
with open("ukol-1.txt", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.split(';')
        year = int(parts[0])
        description = " ".join(parts[1:])
        vloz_do_tabulky(T, year, description)

print("Rok 650:" + hledej_rok(T,650))
print("Rok 100:" + hledej_rok(T,100))
print("Rok 490:" + hledej_rok(T,490))


