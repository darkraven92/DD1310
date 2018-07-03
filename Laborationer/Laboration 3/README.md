Laboration 3
Nyckelord: For-satser och listor

Mål: Att du efter laborationen ska kunna behärska listor, for-satser, nästlade slingor

Gör följande uppgifter, kraven måste uppfyllas.
Uppgift 1: For-satser och range
Skriv ett program som visar en tabell över temperaturer i Celsius från 0 till 20 och deras motsvarigheter i Fahrenheit. Formeln för att omvandla en temperatur från Celsius till Fahrenheit är :

C × 9 + 160 
F =	                             
5
Ditt program måste använda en for-slinga för att visa tabellen.

Krav: En for-slinga och den inbyggda funktionen range ska användas

 


 

Uppgift 2: Nästlade slingor
Skriv ett program som frågar efter två tal mellan 1 och 9 och skriver sedan ut multiplikationstabellen av de två talen.
Scenario:
Ange antal rader: 3 
Ange antal kolumner: 7 


 1	 2	 3	 4 	 5	 6	 7
1	 1	 2	 3	 4  	 5  	 6	 7
2	 2	 4	 6	 8  	 10	 12	 14
3	 3	 6	 9	 12	 15	 18	 21
Krav: man ska använda sig av nästlade while-slingor. 
Dessutom ska tabellen se fint ut precis som ovanstående exempel och alltså INTE som nedanstående exempel där tal med två siffror hamnat under fel (läs filen med exempel från föreläsning 3)

kolumn: 
   1 2 3 4 5 6 7
1 1 2 3 4 5 6 7
2 2 4 6 8 10 12 14
3 3 6 9 12 15 18 21

Uppgift 3: Slingor och listor
Skriv ett tärnings-program som ska kunna användas till diverse olika spel. Programmet böjar fråga efter antal tärningar som ska användas i spelet. Till exempel för Yatzy 5 tärningar används och för backgammon 2 tärningar. Sedan ska programmet fråga efter max antal kast per spelare per tur. För backgammon är alltså 1 och för yatzy är 3. Efter att programmet har fått svar på de två frågorna kan programmet börja slumpa värden till tärningarna. En exempelkörning av programmet skulle kunna se ut som nedan, studera exemplet noga:

Hur många tärningar behövs i spelet? 3
Hur många kast en spelare får? 2
Genom att trycka på enter kan du börja kasta, om du vill avsluta spelet skriv A:
Tärning 1: 5
Tärning 2: 4
Tärning 3: 2
Är du inte nöjd kan du kansta igen, vill du kasta igen?(j/n)j
Tärning 1: 3
Tärning 2: 1
Tärning 3: 6
Du fick 3, 1, 6.
Genom att trycka på enter kan du börja kasta, om du vill avsluta spelet skriv A:
Tärning 1: 4
Tärning 2: 3
Tärning 3: 2
Är du inte nöjd kan du kansta igen, vill du kasta igen?(j/n)n
Du fick 4, 3, 2.
Genom att trycka på enter kan du börja kasta, om du vill avsluta spelet skriv A:
osv...
En annan körning för ett annat spel där antal kast per spelare är 1 och därmed frågan om om spelaren är nöjd med kastet ställs inte, ser ut som nedan:

Hur många tärningar behövs i spelet? 2
Hur många kast en spelare får? 1
Genom att trycka på enter kan du börja kasta, om du vill avsluta spelet skriv A:
Tärning 1: 6
Tärning 2: 6
Du fick 6, 6.
Genom att trycka på enter kan du börja kasta, om du vill avsluta spelet skriv A:
Tärning 1: 4
Tärning 2: 3
Du fick 4, 3.
Genom att trycka på enter kan du börja kasta, om du vill avsluta spelet skriv A:
osv...
Krav:

En lista ska användas för att lagra alla kast för aktuell spelare.
Både while- och for-loop ska användas där de passar bättre, du ska kunna resonera kring ditt val av loop.
