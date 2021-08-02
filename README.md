# tusdatos
Prueba tecnica

En este repositorio se encuentra la prueba técnica realizada para continuar con el proceso de selección, donde se pueden encontrar los archivos utilizados para los puntos 1 y 2 de la prueba.

- Para el punto 1 se utilizó el framework "flask" con el fin de incorporar html con css y js, se utiliza css para el formato de las clases del archivo html, y js para la configuración de las búsquedas dentro del sitio. Ademas de esto se consume la api "https://www.scorebat.com/video-api/v1/" con python (main.py) donde se encuentran datos de partidos de fútbol, los cuales son usados en el sitio web. Adicionalmente se configuró un hosting free con "Heroku" para subir el proyecto y ser visualizado facilmente: https://prueba-football-highlights.herokuapp.com
- Para hacer uso de la webapp, basta con dar click en la lupa de búsqueda de la parte superior derecha, esto desplegará una barra donde podrá filtrar el equipo que desee y luego podrá seleccionar el partido. Este se abrirá en una ventana nueva.

- En el punto 2 se realizó el proceso de web scraping utlizando la libreria "BeautifulSoup" de python (web-scraping.py) donde se obtienen datos de productos en venta haciendo peticiones a "https://webscraper.io/test-sites/e-commerce/scroll/" y se escriben dichos datos en un archivo .json.
