import pandas as pd
import datetime
import variables as v
import functions as f
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df_results = pd.DataFrame({'id':[],
                            'name':[],
                            'picture_url':[]})



for n_requests in range(0,v.n_llamadas):
    print("Llamando a la api por", n_requests, "vez")

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')
    response = f.llamar_api(timestamp,v.priv_key,v.pub_key, n_requests * 100)
    df = f.json_to_df(response)

    df_results = pd.concat([df_results, df], axis=0)

df_results.reset_index(drop=True, inplace=True)
df_results.to_csv("marvel_characthers.csv")