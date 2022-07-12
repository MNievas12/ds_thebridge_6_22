import requests
import pandas as pd
import hashlib

def hash_params(timestamp,priv_key,pub_key):
    """ Marvel API requires server side API calls to include
    md5 hash of timestamp + public key + private key """

    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()

    return hashed_params


def llamar_api(timestamp,priv_key,pub_key,offset):
    params = {'ts': timestamp, 
        'apikey': pub_key, 
        'hash': hash_params(timestamp,priv_key,pub_key),
        'limit': 100,
        'offset': offset,
        }

    url = 'http://gateway.marvel.com/v1/public/characters'

    res = requests.get(url,params=params)
    respuesta_json = res.json()
    return respuesta_json

def json_to_df(respuesta_json):
    marvel_dict = {"id": [],
                    "name": [],
                    "picture_url": []
                    }

    for elem in respuesta_json['data']['results']:
        marvel_dict['id'].append(elem.get('id','no_id'))
        marvel_dict['name'].append(elem.get('name','no_name'))
        url_pic = elem.get('thumbnail', 'no_thumbnail').get('path', 'no_path') + '.' + elem.get('thumbnail','no_thumbnail').get('extension', 'no_extension')
        marvel_dict['picture_url'].append(url_pic)

    df_results = pd.DataFrame(marvel_dict)
    return df_results