import requests

def guessed_word():
    url = "https://random-word-api.vercel.app/api?words=1&length=5"
    response = requests.get(url)

    if response.status_code == 200:
        word = response.json()[0]
        return word
    else:
        raise Exception("Failed to fetch word")

def input_check():
    while True:
        try:
            player_word = input("Zgadnij jakie pięcio literowe słowo wybrałem:")
            if len(player_word) < 5:
                print("Podałeś za krótkie słowo. Spróbuj jeszcze raz.")
            elif len(player_word) > 5:
                print("Podałeś za długie słowo. Spróbuj jeszcze raz.")
            else:
                return player_word
        except ValueError:
            print("To nie jest słowo. Spróbuj jeszcze raz.")

