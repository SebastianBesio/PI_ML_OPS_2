<p align=center><img src=https://www.trustedreviews.com/wp-content/uploads/sites/54/2021/06/Steam-920x518.jpg width="500"><p>

# <h1 align=center> **STEAM GAMES PRICE PREDICTION AND DATA DEPLOYED ON RENDER WITH FASTAPI** </h1>

## **Objetivo del proyecto:**

Disponibilizar datos historicos de juegos de steam y una prediccion de precios utilizando el framework FastAPI. Es un proyecto educativo y por eso tambien tiene el objetivo de aprendizaje y ganar más experiencia con estas herramientas.

## **Descripción del proyecto:**

En este proyecto se basa en trabajar con un dataset de juegos de steam.

### Datos Históricos:
En la cual se crearon los las siguientes consultas.

+ def **genero( *`Year`: str* )**:
    Se ingresa un año y devuelve una lista con los 5 géneros más vendidos en el orden correspondiente.

+ def **juegos( *`Year`: str* )**:
    Se ingresa un año y devuelve una lista con los juegos lanzados en el año.

+ def **specs( *`Year`: str* )**:
    Se ingresa un año y devuelve una lista con los 5 specs que más se repiten en el mismo en el orden correspondiente. 

+ def **earlyacces( *`Year`: str* )**:
    Cantidad de juegos lanzados en un año con early access.

+ def **sentiment( *`Year`: str* )**:
    Según el año de lanzamiento, se devuelve una lista con la cantidad de registros que se encuentren categorizados con un análisis de sentimiento. 

+ def **metascore( *`Year`: str* )**:
    Top 5 juegos según año con mayor metascore.

Dado a que los datos de entrada son estáticos, se opto por preparar un archivo especificamente optimizado para cada una de esas consultas. De esta forma se va a hacer la menor cantidad de procesamiento posible cada vez que se llame a la consulta del API. Todo esta preparacion de los datos y su analisis detallado se encuentra en [0_Preprocessing](0_Preprocessing.ipynb).

### Predicción de precios:
Lo siguiente que se quería disponibilizar era un modelo de predicción de precios dadas ciertas caracteristicas del juego.

+ def **predicción( *`earlyaccess`: bool, `sentiment`: str, `year`: int, `genre`: Annotated[list[str] | None, Query()], `tags`: Annotated[list[str] | None, Query()], `specs`: Annotated[list[str] | None, Query()]* )**:
    Retorna el precio predicho dado los parametros pasados y **RMSC** del modelo.
    
Para esto se realizó limpieza del dataset, se descartaron varias columns, se analizadon e imputaron datos en distintos casos. Luego se probaron varios modelos de Machine Learning para regresión, utilizando al final Random Forest Regressor.

Todo ese analisis detallado se encuentra en [1_EDA](1_EDA.ipynb).

### FAST API y Render:
Se utilizó FastAPI porque era una forma muy rapida y sencilla de crear una API.

Además luego se hizo un deployment en Render para poder disponibilizarlo en el siguiente link.

[Deployed on Render](https://pi-ml-ops-sebastian-besio.onrender.com)


## **Conclusiones:**

En esté proyecto se lograron disponibilizar los datos históricos de una forma eficiente. Se logró tener un modelo que predice el precio de un juego dadas ciertas caraceristicas. Y todo eso quedó disponibilizado en una API pronta para ser consumida. 

## **Trabajo futuro:**

+ **Mejorar Modelo:** Dado a que el modelo no es tan certero como se podria esperar para ponerlo en producción, se debería estudiar algunas otros modelos y/o ver si se puede mejorar el uso de los datos actuales para lograr mejores predicciones. Además se tendria que trabajar para no usar un modelo con tantas columnas para que sea mas eficiente a la hora de entrenar y predecir en el caso de que se vaya a usar muchas veces.

+ **Transformaciones en Pipeline:** Varias transformaciones se hicieron de forma "manual", para esta vez no fue tan grave pero en general si se quisiera trabajar con entrada continua de datos tendriamos que tener esas transformaciones en un Pipeline pronto para trabajar con los nuevos datos enseguida lleguen.

+ **Validaciones:** Por falta de tiempo no se realizaron muchas validaciones a las funciones, como por ejemplo tipo de datos, rango de años, etc. Esto es algo que se debe hacer si o si en un caso productivo.

# API Examples

[Root](https://pi-ml-ops-sebastian-besio.onrender.com/)

[Docs](https://pi-ml-ops-sebastian-besio.onrender.com/Docs)

[genero](https://pi-ml-ops-sebastian-besio.onrender.com/genero/2015)

[juegos](https://pi-ml-ops-sebastian-besio.onrender.com/juegos/2015)

[specs](https://pi-ml-ops-sebastian-besio.onrender.com/specs/2015)

[earlyaccess](https://pi-ml-ops-sebastian-besio.onrender.com/earlyaccess/2015)

[sentiment](https://pi-ml-ops-sebastian-besio.onrender.com/sentiment/2015)

[metascore](https://pi-ml-ops-sebastian-besio.onrender.com/metascore/2015)

[Prueba Prediccion](https://pi-ml-ops-sebastian-besio.onrender.com/prediccion/?earlyaccess=true&sentiment=%27Mostly%20Positive%27&year=2018&genre=Casual&genre=Indie&genre=Simulation&genre=Strategy)
