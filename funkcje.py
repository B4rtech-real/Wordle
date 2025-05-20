import requests

def guessed_word():
    url = "https://random-word-api.herokuapp.com/word?length=7"
    response = requests.get(url)

    if response.status_code == 200:
        word = response.json()[0]
        return word
    else:
        raise Exception("Failed to fetch word")

def input_check():
    while True:
        try:
            player_word = input("Zgadnij jakie pięcio literowe słowo wybrałem:"))
            if len(player_word) == 5:
                return player_word

            else:
                print("Podana liczba jest poza zakresem. Spróbuj jeszcze raz.")
        except ValueError:
            print("To nie jest liczba. Spróbuj jeszcze raz.")
