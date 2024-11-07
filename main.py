prekes = {
    "Saldainiai": 0.50,
    "Kramtomoji guma": 0.75,
    "Traskuciai": 1.00,
    "Gerimas": 1.50,
}

balansas=float(input('Įveskite sumą, kurią norite išleisti: €'))

if balansas < 0.50:
    print("Jūsų įvestos sumos nepakanka jokiems daiktams įsigyti")
else:
    if balansas < 0.75:
        print('1. Saldainiai: 0.50€')
    elif balansas < 1.00:
        print('1. Saldainiai: 0.50€')
        print('2. Kramtomoji guma: 0.75€')
    elif balansas < 1.50:
        print('1. Saldainiai: 0.50€')
        print('2. Kramtomoji guma: 0.75€')
        print('3. Traškučiai: 1.00€')
    else:
        print('1. Saldainiai: 0.50€')
        print('2. Kramtomoji guma: 0.75€')
        print('3. Traškučiai: 1.00€')
        print('4. Gėrimas: 1.50€')

    while True:
        produktas = int(input("Įveskite produkto numerį: "))

        if produktas == 1 and balansas >= 0.50:
            likutis = balansas - 0.50
            print("Pasirinkote Saldainiai")
            print("Dėkojame už jūsų pirkinį")
            print(f"Jūsų likutis yra €{likutis:.2f}")
            break
        elif produktas == 2 and balansas >= 0.75:
            likutis = balansas - 0.75
            print("Pasirinkote Kramtomoji Guma")
            print("Dėkojame už jūsų pirkinį")
            print(f"Jūsų likutis yra €{likutis:.2f}")
            break
        elif produktas == 3 and balansas >= 1.00:
            likutis = balansas - 1.00
            print("Pasirinkote Traškučiai")
            print("Dėkojame už jūsų pirkinį")
            print(f"Jūsų likutis yra €{likutis:.2f}")
            break
        elif produktas == 4 and balansas >= 1.50:
            likutis = balansas - 1.50
            print("Pasirinkote Gėrimas")
            print("Dėkojame už jūsų pirkinį")
            print(f"Jūsų likutis yra €{likutis:.2f}")
            break
        else:
            print("Pasirinkote neteisingą produkta arba turite nepakankamai pinigų")

# match produktas:
#     case "1":
# elif balansas >= 1.50:
#     print('Saldainiai: 0.50')
#     print('Traskuciai: 1.00')
#     print('Gerimas: 1.50')
#     print('Kramtomoji guma: 0.75')
# elif balansas <= 1.00 and balansas > 0.75:
#     print('Saldainiai: 0.50')
#     print('Traskuciai: 1.00')
#     print('Kramtomoji guma: 0.75')
# elif balansas <= 0.75 and balansas > 0.50:
#     print('Saldainiai: 0.50')
#     print('Kramtomoji guma: 0.75')
# elif balansas >= 0.50 and balansas < 0.75:
#     print('Saldainiai: 0.50')


