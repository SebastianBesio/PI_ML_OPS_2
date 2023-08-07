from typing import Annotated
from fastapi import FastAPI, Query
import json

app = FastAPI()

########################################
## TODO: Add validations
########################################

@app.get("/")
def read_root(): 
    return {"PI_ML_OPS": "Sebastian Besio"}

@app.get("/genero/{Year}")
def genero(Year: str): 
    """
    Se ingresa un año y devuelve un diccionario con los 5 géneros más vendidos en el orden correspondiente.
    """
    # Read data
    with open("datasets/steam_games_endpoint_1_genero.json") as json_file:
        genres_dict = json.load(json_file)

    # TODO Add validation

    # Since data is already sorted, get the first 5 as top 5.
    top5 = dict(list(genres_dict[Year].items())[0:5])
    return top5


@app.get("/juegos/{Year}")
def juegos( Year: str ):
    """
    Se ingresa un año y devuelve un diccionario con los juegos lanzados en el año.
    """
    # Read data
    with open("datasets/steam_games_endpoint_2_juegos.json") as json_file:
        juegos_list = json.load(json_file)

    # TODO Add validation

    return {"Año": Year, "Juegos": juegos_list[Year]}


@app.get("/specs/{Year}")
def specs( Year: str ):
    """
    Se ingresa un año y devuelve un diccionario con los 5 specs que más se repiten en el mismo en el orden correspondiente.
    """
    # Read data
    with open("datasets/steam_games_endpoint_3_specs.json") as json_file:
        specs_dict = json.load(json_file)

    # TODO Add validation

    # Since data is already sorted, get the first 5 as top 5.
    top5 = dict(list(specs_dict[Year].items())[0:5])
    return top5


@app.get("/earlyacces/{Year}")
def earlyacces( Year: str ):
    """
    Cantidad de juegos lanzados en un año con early access.
    """
    # Read data
    with open("datasets/steam_games_endpoint_4_earlyaccess.json") as json_file:
        earlyaccess_dict = json.load(json_file)

    # TODO Add validation, Top5 si teine al menos 5
    
    return {"Año": Year, "Early Access": earlyaccess_dict['early_access'][Year]}


@app.get("/sentiment/{Year}")
def sentiment( Year: str ):
    """
    Según el año de lanzamiento, se devuelve una lista con la cantidad de registros que se encuentren categorizados con un análisis de sentimiento.

    Ejemplo de retorno: {Mixed = 182, Very Positive = 120, Positive = 278}
    """
    # Read data
    with open("datasets/steam_games_endpoint_5_sentiment.json") as json_file:
        sentiment_dict = json.load(json_file)

    # TODO Add validation

    return {"Año": Year, "Sentiment": sentiment_dict[Year]}

@app.get("/metascore/{Year}")
def metascore( Year: str ):
    """
    Top 5 juegos según año con mayor metascore.
    """
    # Read data
    with open("datasets/steam_games_endpoint_6_metascore.json") as json_file:
        metascore_dict = json.load(json_file)

    # TODO Add validation, ademas de cantidad menor 5.

    # Since data is already sorted, get the first 5 as top 5.
    top5 = dict(list(metascore_dict[Year].items())[0:5])
    return top5

@app.get("/prediccion/")
def prediccion(earlyaccess: bool, sentiment: str, year: int,
               genre: Annotated[list[str] | None, Query()]):
    """
    Retorna el precio predicho dado los parametros pasados y **RMSC** del modelo.

    Input example:
    prediccion(
        earlyaccess=False,
        sentiment= 'Mostly Positive',
        year=2018,
        genre=['Action', 'Casual', 'Indie', 'Simulation', 'Strategy'],
        tags=['Strategy', 'Action', 'Indie', 'Casual', 'Simulation'],
        specs=['Single-player']
    )
    """
    import sklearn
    import pickle
    import json
    import numpy as np

    # print(sentiment, type(sentiment))
    # print(genre, type(genre))

    # Open saved model
    fname = 'Steam_Games_Model_SB.sav'
    steam_games_price_model = pickle.load(open(fname, 'rb'))

    # Read extra Misc information, RMSE, name of features and Sentiment Dictionary.
    with open("Steam_Games_Model_Misc.json") as json_file:
        misc_dict = json.load(json_file)
    
    rmse = misc_dict["RMSE"]
    feat_names = misc_dict["Features"]
    sentiment_dict = misc_dict["SentimentDict"]
    # print(feat_names)

    # Prepare data
    # TODO: Would like to put this on a Pipeline instead of doing this.

    # First let's create the x feature list and start putting its values.
    x = []
    
    # TODO VALIDATE
    if earlyaccess in (0, 1):
        x.append(earlyaccess)
    else:
        print("Error: Insert boolean value.")

    # For the sentiment one we should convert it to the same number we used before.
    if sentiment in sentiment_dict.keys():
        x.append(sentiment_dict[sentiment])
    else:
        x.append(0)

    if year > 1969 and year < 2024:
        x.append(year)
    else:
        print("Error: insert correct year as an int.")

    feat_names.remove("early_access")
    feat_names.remove("sentiment")
    feat_names.remove("year")

    for f in feat_names:
        if f.startswith("genre_"):
            f_aux = f.replace("genre_", "")
            x.append(f_aux in genre)
        # elif f.startswith("tags_"):
        #     f_aux = f.replace("tags_", "")
        #     x.append(f_aux in tags)

        # elif f.startswith("specs_"):
        #     f_aux = f.replace("specs_", "")
        #     x.append(f_aux in specs)
        else:
            x.append(0)
    
    # Make an array
    x = np.array(x).reshape(1, -1)

    pred_price = float(steam_games_price_model.predict(x))

    return {"Price" : pred_price, "RMSE": rmse}