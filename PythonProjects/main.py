import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7503d61f283361253e65c3f7391f73eb'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN }

body_registration = {
    "trainer_token": TOKEN,
    "email": "german@dolnikov.ru",
    "password": "Iloveqa1"
}

body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 8
}
body_change = {
    "pokemon_id": "167506" ,
    "name": "kuka",
    "photo_id": 8
}

body_catch = {
    "pokemon_id": "167506"
}
'''response = requests.post(url= f'{URL}/trainers/reg', headers= HEADER, json=body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url= f'{URL}/trainers/confirm_email', headers= HEADER, json=body_confirmation)
print(response_confirmation.text)'''

response_create = requests.post(url= f'{URL}/pokemons', headers= HEADER, json=body_create)
print(response_create.text)
pokemon_id = response_create.json().get('id')
print(pokemon_id)

response_change = requests.put(url = f'{URL}/pokemons', headers= HEADER, json = body_change)
print(response_change.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json = body_catch)
print(response_catch.text)