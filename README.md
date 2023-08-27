# Stream Video 

## Task (czech)
Backend aplikace v Pythonu (framework Django)
Aplikace by měla periodicky stahovat seznam filmů z API (https://gist.githubusercontent.com/nextsux/f6e0327857c88caedd2dab13affb72c1/raw/04441487d90a0a05831835413f5942d58026d321/videos.json)
Tento seznam by si měla lokálně udržovat v DB vlastního výběru z důvodu možného "výpadku dodavatele"
Uživateli by měla poskytnout JEDNODUCHÝ front-end psaný jakoukoliv technologií, může jednoduše renderovat na straně serveru obyčejné HTML, kde uživateli zobrazí "karty" s jednotlivými videi a umožní mezi nimi filtrovat a řadit je.
Přehrávání !NENÍ! potřeba řešit, ale obrázek z iconUri by byl hezký
Nejde o grafickou podobu a jestli budou barvičky ladit - to není úplně práce backendisty, tzn. nikdo neřešíme design. Důležité je, jak se zhostíte práce s parametry, filtrovanim a řazením.
Vysledek bych rád viděl jako git repozitář s historií např. na githubu

## Solution description
The solution contains a Django-based project with an app for managing the video database. A Celery task
is set up to periodically fetch video metadata from a remote source and store them in a local database.
A simple frontend has been set up to display videos from the database. The list of videos can be searched
through and the results can be sorted.

## How to run
* Have a docker engine set up and running
* Use the following command to run:
> docker-compose build
> docker-compose up
* Use a browser to navigate to http://localhost:8000/ to browse the interface
