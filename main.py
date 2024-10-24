prekes = {
    "Saldainiai": 0.50,
    "Traskuciai": 1.00,
    "Gerimas": 1.50,
    "Kramtomoji guma": 0.75
}

balansas=float(input('Iveskite suma, kuria norite isleisti:'))

if balansas< 0.50:
    print("Jūsų įvestos sumos nepakanka jokiems daiktams įsigyti")
else:
    print("Galite pirkti sias prekes:")

if balansas >= 1.50:
    print('Saldainiai: 0.50')
    print('Traskuciai: 1.00')
    print('Gerimas: 1.50')
    print('Kramtomoji guma: 0.75')