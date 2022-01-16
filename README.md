# APC-MD3Kaggle Online News Popularity

## Nom: Javier Alejandro Camacho Machaca  
## NIU: 1566088
## Correu electronic: javieralejandr.camacho@e-campus.uab.cat o javier.cm.060@gmail.com
## Cas Kagggle:
_El meu objectiu amb aquesta base de dades es predir el nombre de vegades que es comparteixen els articles de la página wev Mashable, peró al final vig redirigir el objectiu 
d'altre manera_
[Base de Dades de Kaggle: Online News Popularity](https://www.kaggle.com/srikaranelakurthy/online-news-popularity)

## Resum

La base de dades del cas Kaggle **Online News Popularity** conté 61 variables, un es el **target**, que s'anomena **Shares** i la resta son característiques i contingut d'un article de la pàgina web Mashable.


### Objectius del dataset

Utilitzar varis models d’aprenentatge per saber quin es el millor per la nostra base de dades i en les característiques que te. I analitzar les dades per optimitzar aquest procés.


## Experiments 

Per entendre millor la base de dades primer es van analitzar i visualitzar les dades, després es van veure les correlacions i les distribucions de les variables per prendre una decisió de que fer amb la base de dades per trobar una solució.

### Preprocessat

Primer es va fer un anàlisi de les dades per veure si hi ha dades amb valors nuls i repetits per depurar-ho i així tenir menys treball en un futur. 

Després amb un **Heatmap** es va veure les correlacions de les variables, però com mostraré casi no hi ha correlacions: 

![Primer Heatmap](https://github.com/j4v1t0/APC-MD3Kaggle/blob/main/Images/heatmap.png)

Al veure que hi havien variables que estaven directament correlacionades, els vaig suprimir ja que no serien molt valuoses a l’hora de fer l’aprenentatge amb els futurs algorismes. 

Al veure que això seria complicat, vaig decidir convertir el meu target en unes dades binaries. 
Si es un **1** l’article seria viral o popular, i si es **0** no ho seria, i per definir això vaig decidir utilitzar un Umbral, que seria el valor mínim d’un valor anòmal, per calcular això fa falta calcular el primer i el tercer Quartil, després calcular el valor de Q3 – Q1 , utilitzar aquesta resta i multiplicar-lo per 1.5 per després sumar-ho al tercer Quartil, i aquest resultat final donaria el Umbral de valor atípic superior.
Vaig utilitzar aquest Umbral en la variable **Shares** per passar les seves dades a uns i ceros. 

Fet això, vaig prendre la decisió d'utilitzar els models que millor s'adaptin a les característiques de la base de dades, que com te moltes coses a tenir en compte, i casi ninguna variables depèn d’altre o te molt de pes, el primer algorisme en el que vaig pensar va ser el **Random Forest Classifier** i altres similars.

I per poder mesurar la seva efectivitat vaig utilitzar el mètode de **Cross-Validation Score**.

### Model

|  | CV Score |
| ------------- | ------------- |
| Random Forest  | 88.5%  |
| Decision Tree  | 79.7%  |
| Ada Boost  | 88.4%  |


## Conclusions 

He fet varies probes utilitzant varis mides de la base de dades i modificant els models d’aprenentatge, i en tots el **Random Forest** sempre donava els millors resultats. I no es de estranyar, ja que com hem dit en un principi, la base de dades te moltes variables sense molta importància.


## Idees per treballar en un futur

Per millorar el meu treball, es podria depurar més les dades, i utilitzant el **target** sense modificar, però això donaria a treball i processos més complexos per trobar un valor que pugui calcular un valor exacte o un rang petit per poder predir el nombre de **Shares**.

## Llicencia

Llicencia **Altre** sense especificar.


