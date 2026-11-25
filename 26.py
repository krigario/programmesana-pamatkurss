# 02.12.26 Kristaps Gailis, spēles mērķis ir aprēķināt duelī iegūto punktu skaitu.

vards = input("Ievadi varoņa vārdu: ")

speks = int(input("Uzbrukuma spēks: "))

veiksme = float(input("Veiksmes koeficients: "))

rezultats = (speks ** 2) * veiksme

print(f"{vards} duelī iegūst {rezultats:.1f} punktus!")

# Uzbrukuma spēks tiek kāpināts kvadrātā, pēc tam tas tiek reizināts ar veiksmes koeficientu.