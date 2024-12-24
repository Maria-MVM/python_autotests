import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '7503d61f283361253e65c3f7391f73eb'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN }
TRAINER_ID = '13058'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID })
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID })
    assert response_get.json()["data"][0]["trainer_name"]=="Стрекоза"

@pytest.mark.parametrize('key,value',[('id',TRAINER_ID),('trainer_name', 'Стрекоза'),('city','Tokyo')])
def test_parametrize(key,value):
        response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID })
        assert response_parametrize.json()["data"][0][key]== value