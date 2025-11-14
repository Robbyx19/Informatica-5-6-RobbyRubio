import requests 
API_KEY = "b96dc44f21b4a86575bc5037fa6e0aec45affa8f5e3c2f44c90c6e1bc2e53469"
while True:
    try:
        bitcoin = float(input("How many bitcoin do you want to buy? "))
        break
    except ValueError:
        print ("type a number you fool ")


response = requests.get("https://rest.coincap.io/v3/asstes/bitcoin?apiKey=" + API_KEY)
bitcoin_price = float(response.json()['data']['priceUsd'])
print (f"the total is : ${total:2f}")
