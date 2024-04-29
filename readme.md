Blackjack
Målsättningen för dig som spelare är att din hand efter spelets slut ska ha ett värde som är närmare 21 än bankens hand. Kortens värde får dock inte vara över 21.

Mål
  1. Ett deck med 6 kortlekar, fyra 1:or, 2:or,...
  2. Blanda kortlkeken
  3. Kenkt, dam och kung e värda 10
  4. Ess e värt 1 ELLER 11
  5. Ge spelaren och dealern kort tills båda har två kort var, dealerns andra kort skall vara gömt
  6. Ge spelaren möjlighet att hit eller stand
  7. Ge spelaren möjligheten att bli "tjock"
  8. Datorn får möjlighet att hit eller stand beroende på hans hands värde
  9. Vem vinner?
  10. Låt spelaren fortsätta spela utan att avbryta koden
  11. Spela om pengar/valuta
  12. Spara valutan genom alla rundor tills man tappat allt

Bonus
  Spelfunktioner
    1. Kunna dubbla och splitta din hand 
    2. Side bets, PP och 21+3
  Grafik:
    1. Skapa en spelbräda
    2. Visa upp kort 
    3. Visa värdet av spelaren och dealerns hand 
    4. Skapa knappar som låter dig ta eller stanna
    5. Visa det nya kort som dras från kortleken 
    6. "Spelaren vann" eller "Dealern vann" skärm
    7. Lägg till valuta
    8. Visa hur mycket spelaren vinner (I form av valutan) Ex: "Du vann 100$"
    9. Skapa en animation när korten dras ur högen
    10. Njut av en snyggare version av spelet :)


Dokumentation

Blackjack:

Jag började allt med att lära mig mer om grunderna samt lite svårare delar av python med hjälp av olika youtube videor (https://www.youtube.com/watch?v=rfscVS0vtbw&t=1931s). Jag skrev kod medans jag följde med i videon och testade hur det olika funktionerna i python funkade med egna exempel, vilket gav mig lite bättre känsla för hur det skulle användas i ett Blackjack. 

Målet med min första dag av att faktiskt skriva kod var att skapa en fungerande kortlek med 52 kort där varje värde hade 4 olika "suits" (färger). Jag började med att skapa 3 olika listor, en för själva kortleken och två för färgern och värde. Jag använde mig sedan av for looper för att skapa varje kort, för att sedan lägga till dom i min kortlek. Jag var inte helt säker på hur for loopen fungerade med listor så jag använde mig av denna video för att lära mig mer (https://www.youtube.com/watch?v=rmaaKvh94Vs).
Googlade sedan lite på hur man kan blanda en lista för att det ska bli helt slumpmässigt och hittade snabbt random.shuffle() vilket var perfekt. Skapade då en funktion med uppgiften att blanda min kortlek.

Nästa mål var nu att att kunna dela ut kort till spelaren och datorn. Detta ville jag göra med hjälp av en funtion och det var relativt simpelt då jag skapade en lista där korten i handen ska samlas (cards). Sedan drar man valfritt antal kort ur kortleken med hjälp av pop(), korten läggs sedan in i listan och funktionen returnerar sedan handen. Ex: player_hand = deal(2) spelarens hand är nu en lista med två slumpmässiga kort.
 
Nu är det dags att ge korten ett värde. Detta gjorde jag med hjälp av en funktion som kan räkna ut värdet av ett kort beroende på vilken valör den har. Funktionen fungerar på det sätt att man skickar med valören du har på kortet och så beroende på vad det är så får man tillbaks ett värde i form av en siffra. Ex player_score = value_f(player_hand[0][1] + player_hand[1][1]) kommer ge spelaren ett värde av både korten tillsammans, skulle korten vara en K och 7 så blir värdet alltså 17.

Man kan nu få en hand och räkna ut vad värdet av handen är. Nästa mål är nu att låta spelaren och datorn ta mer kort om det behövs. Jag gör detta med hjälp av en "hit" funktion. Jag gjorde detta genom att man skickar med vilken hand som ska ta (spelaren eller datorn) och värdet av handen. Funktionen tar sedan ett kort från kortleken och lägger till det i handen, ett nytt värde räknas sedan ut genom att lägga ihop det tidare värdet med det senaste tillagda kortet (player_hand[-1][1]). Funktionen visar även den nya handen och dess värde. 
Men just nu så kunde man ta hur många kort som helst utan att bli tjock, jag skapade sedan en bust funktion som testade ifall värdet var över 21, jag kör sedan denna funktionen i hit funktionen för att testa ifall det nya värdet är giltigt. 

Nu funkar egentligen allt och det är dags att utse vinnare. Detta genom en funktion som kollar vilken hand som har bäst värde och uster sedan en vinnare utifrån detta. Vinner du med 21 så får du Blackjack. 

Alla funktioner i spelet finns nu och det är dags att skapa själva spelet. Det gjorde jag genom att använda det olika funktioner jag redan hade för att ge spelaren och datorn varsinn hand med ett värde. Endast datorn första kort är synligt och utifrån det så frågar spelet om du vill ta eller stå. Jag skapade sedan en variabel som får ett värde utifrån om du vill ta (h) eller stå (s). Om du väljer att ta så startas en while loop som håller på tills variabeln inte har värdet h (ta kort). Spelaren får chans att ta fler kort så länge värdet av handen är under 21, annars blir variabels värde s och programmet fortsätter och visar att spelaren förlorat. Om spelaren inte blivit tjock så visas datorns andra kort och ifall värdet är under 17 så kommer datorn ta nya kort tills den antingen har en giltig hand eller blivit tjock. Ifall både spelaren och datorn har en giltig hand så körs win funtionen och en vinnare utses. 

Nu ville jag lägga till en valuta i spelet. Det var inte överdrivet svårt, Jag löste det genom att skapa en variable som skall vara din bank. Man väljer valfri summa att starta med och spelet kommer att fortsätta spelas så länge du har mer än 0 på din bank. Innan varje runda så frågar spelet även dig hur mycket du vill betta och beroende på hur handen spelas ut så kommer du vinna eller förlora pengar. Det räknas ut genom att antingen värdet antingen dubblas eller försvinner. Värdet läggs sedan till på din bank och du får frågan om vad du vill satsa inför nästa runda.

En hemsida som hjälp speciellt mycket under tiden har varit Stackoverflow.com vilket är en sida där man delar kod med andra där man kan få kommentarer om sin kod. Jag hittade många som gjort liknande projekt och stött på problem och kunde då lära mig från deras kod. Jag testade även vid vissa tillfällen att publicera min egna kod och frågade personer ifall dom såg problem i koden eller ifall jag skulle kunna skriva något på ett nytt enklare sätt. Vilket var väldigt lärorikt då några faktiskt skrev svar på min kod och jag kunde ställa frågor om saker jag inte riktigt förstått.
Jag änvände även detta när jag gjorde ett tärningsspel där man spelare mot varann och jag hade problem med att lägga till stege kombinationen.

Blackjack spelet funkar nu och alla mina mål är uppnådda med egna lösningar jag kommit på med hjälp av internet och dig :)



Grafik:


24-04-18
Idag så löste jag problemet med att dra kort, för att göra det så skapade jag en variabel som skulle känna av när knappen tryckdes och när man släpper den. Programmet kommer alltså bara köra koden en gång fram på grund av att värder på mouse_down kommer ändras. 

Jag löste även ett problemet att alla kort som dras placeras direkt på varann genom att ändra x kordinaten på korten med en variabel som ökar i värde efter varje gång man klickat på knappen. 

Jag fick därefter att nytt problem med att det första två korten skrivs ut fler gånger vilket gör att det nya korten inte är lika synliga. Lösningen till detta är då att jag ska ha en for loop i main() som printar ut alla kort i handen samtidigt istället. Vilket får bli ett uppdrag till nästa lektion.

24-04-20 (Hemma)
Idag ville jag lösa problemet med for loopen och det gjorde jag genom att för varje kort i loopen så får variabeln card_image ett värde som senare används för att kalla efter bilden. Jag har även en x och y variabel för postionen för varje kort, dessa ändrar värde efter varje gång loopen körs vilket resulterar i korten flyttar på sig och placeras fint ovanpå varann i den ordning som jag vill. 

24-04-24 (Skola (Inte lektion))
Idag hade vi presentationer och blev lite uttråkad, så istället för att kolla på mobilen så började jag programmera.
p_value fixad.
"Stand" nästan helt färdig. 
d_value fixad.
Orkar inte skriva dokumentationen nu (ligger i sängen och ska sova).

24-04-25
Win()
bust()
value bug fix

24-05-29
d_stand > 16

(Skriver mer dokumentation om nån dag)
