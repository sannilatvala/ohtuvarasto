from varasto import Varasto

def print_varaston_luonti(varasto, nimi):
    print("Luonnin jälkeen:")
    print(f"{nimi}varasto: {varasto}")

def print_varasto_tiedot(varasto, nimi):
    print(f"{nimi} getterit:")
    print(f"saldo = {varasto.saldo}")
    print(f"tilavuus = {varasto.tilavuus}")
    print(f"paljonko_mahtuu = {varasto.paljonko_mahtuu()}")

def print_varasto_lisays(varasto, nimi, lisays):
    print(f"{nimi} setterit:")
    print(f"Lisätään {lisays}")
    varasto.lisaa_varastoon(lisays)
    print(f"{nimi}varasto: {varasto}")

def print_varasto_otto(varasto, nimi, otto):
    print(f"{nimi} setterit:")
    print(f"Otetaan {otto}")
    saatiin = varasto.ota_varastosta(otto)
    print(f"{nimi}varasto: {varasto}")
    print(f"Saatiin {saatiin}")

def print_virhetilanteita():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print_varaston_luonti(mehua, "Mehu")
    print_varaston_luonti(olutta, "Olut")

    print_varasto_tiedot(olutta, "Olut")

    print_varasto_lisays(mehua, "Mehu", 50.7)
    print_varasto_otto(mehua, "Mehu", 3.14)

    print_virhetilanteita()

    print_varasto_lisays(olutta, "Olut", 1000.0)

    print_varasto_lisays(mehua, "Mehu", -666.0)

    print_varasto_otto(olutta, "Olut", 1000.0)

    print_varasto_otto(mehua, "Mehu", -32.9)


if __name__ == "__main__":
    main()
