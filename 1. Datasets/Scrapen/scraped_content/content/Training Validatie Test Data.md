---
title: Gebruik bij machine learning technieken gescheiden train-, test- en validatiedata en houd rekening met underfitting en overfitting - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-07-training-validatie-en-testdata/index.html
scraped_at: 2025-06-12T10:34:21.262969
---

# Gebruik bij machine learning technieken gescheiden train-, test- en validatiedata en houd rekening met underfitting en overfitting - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-07-training-validatie-en-testdata/index.html

---

[ ![Home Algoritmekader](../../../assets/logo.svg) ](../../.. "Algoritmekader 2.2") Algoritmekader 2.2

[ GitHub  ](https://github.com/MinBZK/Algoritmekader "Ga naar repository")

  * [ Soorten algoritmes en AI  ](../../../soorten-algoritmes-en-ai/)
  * [ Onderwerpen  ](../../../onderwerpen/)
  * [ Levenscyclus  ](../../../levenscyclus/)
  * [ Rollen  ](../../../rollen/)
  * [ Voldoen aan wetten en regels  ](../../)

Inhoudsopgave

  * Maatregel
  * Toelichting
    * Grootte van de drie datasets
    * K-fold cross validation
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Gebruik bij machine learning technieken gescheiden train-, test- en validatiedata en houd rekening met underfitting en overfitting

[]( "Vereiste ID")dat-07[](../../../levenscyclus/ "Levencyclus")[Dataverkenning en datapreparatie](../../../levenscyclus/dataverkenning-en-datapreparatie/)[](../../../levenscyclus/ "Levencyclus")[Ontwikkelen](../../../levenscyclus/ontwikkelen/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Data](../../../onderwerpen/data/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)[](../../../onderwerpen/ "Onderwerp")[Bias en non discriminatie](../../../onderwerpen/bias-en-non-discriminatie/)

## Maatregel

Indien je gebruik maakt van machine learning technieken, maak een passende keuze voor gescheiden train-, test- en validatiedata en houd hierbij rekening met underfitting en overfitting.

## Toelichting

Verdeel je dataset in drie delen:

  1. **De trainingset**

Deze dataset wordt gebruikt om het model te trainen. Uit deze dataset worden de onderliggende patronen of relaties geleerd die later gebruikt kunnen worden om voorspellingen mee te doen.

De [kwaliteit](../3-dat-01-datakwaliteit/) van deze dataset moet goed zijn en zo representatief mogelijk van de doelpopulatie. Eventuele [bias](../../../onderwerpen/bias-en-non-discriminatie/#herken-bias) of vooroordelen in deze dataset kunnen door het trainen in het model sluipen.

Let bij het samenstellen van de traningset op dat de data waarop het model gebaseerd is, niet beschikbaar is voordat de uitkomsten zijn geobserveerd. Met andere woorden, zorg ervoor de de voorspellingen geen onderdeel kunnen zijn van de inputvariabelen.

  2. **De validatieset**

De validatieset fungeert als een onafhankelijke, onbevooroordeelde dataset voor het vergelijken van de prestaties van verschillende algoritmes die zijn getraind op de trainingset.

Verschillende modellen kunnen getraind worden op de trainingset. Zo kan je bijvoorbeeld variëren in de (hyper)parameters of de inputvariabelen. Dit leidt tot verschillende varianten van het model. Om de prestaties van de verschillende modellen te vergelijken, moeten we een nieuwe dataset gebruiken: de validatieset. Zou je hiervoor de trainingset gebruiken, kan dat leiden tot [overfitting](https://www.statlearning.com), omdat het model te specifiek afgestemd is op 1 dataset. Het model kan dan niet voldoende generaliseren voor nieuwe situaties.

  3. **De testset**

Nadat er met behulp van de validatieset een keuze is gemaakt voor een passend model en bijbehorende (hyper)parameters, moet je het model nog testen op nieuwe data. Dit geeft een beeld van de werkelijke prestaties van het model in nieuwe omstandigheden.

Let op dat je pas naar deze resultaten kijkt als laatste stap. Inzichten uit deze testdataset mogen niet worden meegenomen in de ontwikkeling, omdat dit kan leiden tot overfitting. Het model zal dan in productie mogelijk minder goed presteren.

### Grootte van de drie datasets

Er is geen optimale verdeling van de drie datsets. Veelvoorkomende verhoudingen om data te splitten zijn:

  * 80% trainingsset, 10% validatieset, 10% testset
  * 70% trainingsset, 15% validatieset, 15% testset
  * 60% trainingsset, 20% validatieset, 20% testset

Afhankelijk van de hoeveelheid beschikbare data en de context maak je hierin een keuze. Houdt hierbij rekening met:

  * Hoe minder trainingdata, hoe groter de variatie van het model tijdens het trainen. De patronen en relaties die ontdekt zijn bevatten dan een grotere onzekerheid.
  * Hoe minder validatie- en testdata je gebruikt, hoe groter de variatie en de onzekerheid in de verwachte prestaties van het algoritme.
  * Hoe complexer het model en hoe meer (hyper)parameters er zijn om te optimaliseren, hoe groter de validatieset moet zijn om het model met optimale presetaties te vinden. Wanneer er weinig hyperparameters zijn, is een relatief kleine validatieset vaak voldoende.

### K-fold cross validation

Naast dat je de datasets willekeurig kan verdelen in drie delen (aselect), kan je ook meer geavanceerde technieken gebruiken. Een robuuste en veelgebruikte techniek is [k-fold cross validation](https://www.statlearning.com), waarbij het model _k_ keer wordt getraind op verschillende delen van de data.

## Risico

Door onjuiste training van het model presteert het model in de praktijk minder goed dan bij de tests. Als training-, validatie- en testdata door elkaar lopen ("data leakage"), kan dit leiden tot overfitting waardoor het model beter lijkt te presteren dan in werkelijkheid het geval is.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[aia-10 - Hoog-risico-AI-systemen zijn voldoende nauwkeurig, robuust en cyberveilig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-10-nauwkeurigheid-robuustheid-cyberbeveiliging/)

## Bronnen

  * [Onderzoekskader algoritmes, Auditdienst Rijk, DM.5 en DM.6](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/hulpmiddelen/onderzoekskader-adr/)
  * [Toetsingskader Algoritmes Algemene Rekenkamer, 2.15, 2.21](https://www.rekenkamer.nl/onderwerpen/algoritmes/documenten/publicaties/2024/05/15/het-toetsingskader-aan-de-slag)

## Voorbeelden

Gemeente Amsterdam: Lokaliseren van lantaarnpalen

Gemeente Amsterdam heeft een systeem voor het herkennen van lantaarnpalen. Hiervoor is een subset van de data gebruikt uit Amsterdam-Oost om te trainen. Het testen is onder andere gebeurd in Weesp wat in het Zuid-Oosten van de gemeente ligt. Het uiteindelijke doel is het gehele gebied gemeente Amsterdam. Het grootste punt van verbetering zou zijn om de trainingdata en validatiedata expliciet te benoemen. Daarnaast zou de trainingdata het beste uit verschillende delen van het gebied gemeente Amsterdam gehaald kunnen worden om zo overfitting op Amsterdam-Oost te voorkomen.

Bron: [Lokaliseren lantaarnpalen - Algoritmeregister](https://algoritmes.overheid.nl/nl/algoritme/lokaliseren-van-lantaarnpalen-gemeente-amsterdam/17364371)

Gemeente Ede – WOZ-taxatiemodellen

De gemeente Ede heeft een algoritme in gebruik als ondersteuning bij het bepalen (en controleren) van de WOZ-waarde van woningen. Dit wordt gedaan aan de hand van Machine Learning modellen die op basis van onder andere woning- en locatiekenmerken gecombineerd met markt- en verkoop condities de WOZ-waarde kan bepalen. Hierbij wordt bepaald welke kenmerken het meeste gewicht hebben voor deze bepaling. Dit algoritme is getraind op 80% van de data om vanuit daar verbanden tussen transactieprijzen en kenmerken te leren. Voor de testset is 20% van de data gebruik om te valideren of nieuwe (onbekende) data ook correct gewaardeerd wordt.

Bron: [WOZ-taxatiemodellen - Gemeente Ede](https://algoritmes.overheid.nl/nl/algoritme/woztaxatiemodellen-gemeente-ede/39323486)

Heb je een voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

22 april 2025 12 november 2024

Terug naar boven
  *norm: een norm is een vrijwillige afspraak tussen partijen over een product, dienst of proces. Normen zijn geen wetten, maar ’best practices’. Iedereen kan - op vrijwillige basis - hier zijn voordeel mee doen. In zakelijke overeenkomsten hebben normen een belangrijke functie. Ze bieden marktpartijen duidelijkheid over en vertrouwen in producten, diensten of organisaties en dagen de maatschappij uit te innoveren. NEN-normen worden ontwikkeld door inhoudsexperts en specialisten op het gebied van normontwikkeling.
  *aanbieder: Een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem of een AI-model voor algemene doeleinden ontwikkelt of laat ontwikkelen en dat systeem of model in de handel brengt of het AI-systeem in gebruik stelt onder de eigen naam of merk, al dan niet tegen betaling.
  *AI-geletterdheid: vaardigheden, kennis en begrip die aanbieders, gebruiksverantwoordelijken en betrokken personen, rekening houdend met hun respectieve rechten en plichten in het kader van de de AI-verordening, in staat stellen met kennis van zaken AI-systemen in te zetten en zich bewuster te worden van de kansen en risico’s van AI en de mogelijke schade die zij kan veroorzaken
  *geharmoniseerde norm: Een Europese norm die op verzoek van de Commissie is vastgesteld met het oog op de toepassing van harmonisatiewetgeving van de Unie
  *conformiteitsbeoordeling: Het proces waarbij de naleving wordt aangetoond van de voorschriften van hoofdstuk III, afdeling 2 van de AI-Verordening in verband met een AI-systeem met een hoog risico
  *gebruiksverantwoordelijke: Een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem onder eigen verantwoordelijkheid gebruikt, tenzij het AI-systeem wordt gebruikt in het kader van een persoonlijke niet- beroepsactiviteit.
  *AI-bureau: De taak van de Commissie waarbij zij bijdraagt aan de uitvoering van, de monitoring van en het toezicht op AI-systemen en AI-modellen voor algemene doeleinden, en AI-governance, als bepaald in het besluit van de Commissie van 24 januari 2024; verwijzingen in deze verordening naar het AI-bureau worden begrepen als verwijzingen naar de Commissie
  *proceseigenaar: De proceseigenaar is verantwoordelijk voor de kwaliteit van het proces en de vastlegging daarvan in een processchema
  *testdata: data die worden gebruikt voor het verrichten van een onafhankelijke evaluatie van het AI-systeem om de verwachte prestaties van dat systeem te bevestigen voordat het in de handel wordt gebracht of in gebruik wordt gesteld
  *verwerker: Een .. rechtspersoon, een overheidsinstantie, een dienst of een ander orgaan die/dat ten behoeve van de verwerkingsverantwoordelijke persoonsgegevens verwerkt.
  *trainingsdata: data die worden gebruikt voor het trainen van een AI-systeem door de leerbare parameters hiervan aan te passen
  *AI-model voor algemene doeleinden: Een AI-model, ook wanneer het is getraind met een grote hoeveelheid data met behulp van self-supervision op grote schaal, dat een aanzienlijk algemeen karakter vertoont en in staat is op competente wijze een breed scala aan verschillende taken uit te voeren, ongeacht de wijze waarop het model in de handel wordt gebracht, en dat kan worden geïntegreerd in een verscheidenheid aan systemen verder in de AI-waardeketen of toepassingen verder in de AI-waardeketen, met uitzondering van AI-modellen die worden gebruikt voor onderzoek, ontwikkeling of prototypingactiviteiten alvorens zij in de handel worden gebracht.
  *AI-systeem voor algemene doeleinden: Een AI-systeem dat is gebaseerd op een AI- model voor algemene doeleinden en dat verschillende doeleinden kan dienen, zowel voor direct gebruik als voor integratie in andere AI-systemen
  *importeur: Een natuurlijke of rechtspersoon die zich bevindt of gevestigd is in de Unie die een AI-systeem in de handel brengt dat de naam of merknaam van een in een derde land gevestigde natuurlijke of rechtspersoon draagt
  *distributeur: Een andere natuurlijke persoon of rechtspersoon in de toeleveringsketen dan de aanbieder of de importeur, die een AI-systeem in de Unie op de markt aanbiedt
  *gemachtigde: een natuurlijke of rechtspersoon die zich bevindt of gevestigd is in de Unie die een schriftelijke machtiging heeft gekregen en aanvaard van een aanbieder van een AI-systeem of een AI-model voor algemene doeleinden om namens die aanbieder de verplichtingen en procedures van deze verordening respectievelijk na te komen en uit te voeren;
  *discriminatiegrond: Beschermde persoonskenmerken op basis waarvan het maken van onderscheid tussen personen verboden is. Bijvoorbeeld: ras, nationaliteit, religie, geslacht, seksuele gerichtheid, handicap of chronische ziekte.
  *indirect onderscheid: Indien een ogenschijnlijk neutrale bepaling, maatstaf of handelwijze personen met een bepaalde godsdienst, levensovertuiging, politieke gezindheid, ras, geslacht, nationaliteit, hetero- of homoseksuele gerichtheid of burgerlijke staat in vergelijking met andere personen bijzonder treft.
  *objectieve rechtvaardiging: Van een objectieve rechtvaardiging voor onderscheid is sprake wanneer onderscheid een legitiem doel nastreeft en er een redelijke relatie van evenredigheid bestaat tussen het gemaakte onderscheid en het nagestreefde doel.
  *inputdata: data die in een AI-systeem worden ingevoerd of direct door een AI-systeem worden verworven en op basis waarvan het systeem een output genereert
  *gebruiksinstructies: de door de aanbieder verstrekte informatie om de gebruiksverantwoordelijke te informeren over met name het beoogde doel en juiste gebruik van een AI-systeem
  *validatiedata: data die worden gebruikt voor het verrichten van een evaluatie van het getrainde AI-systeem en voor het afstemmen van onder andere de niet-leerbare parameters en het leerproces ervan, om underfitting of overfitting te voorkomen
