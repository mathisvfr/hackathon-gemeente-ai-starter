---
title: Evalueer de nauwkeurigheid van het algoritme - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-02-evalueer-nauwkeurigheid/index.html
scraped_at: 2025-06-12T10:34:44.047523
---

# Evalueer de nauwkeurigheid van het algoritme - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-02-evalueer-nauwkeurigheid/index.html

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
    * Metrieken
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Evalueer de nauwkeurigheid van het algoritme

[]( "Vereiste ID")ver-02[](../../../levenscyclus/ "Levencyclus")[Ontwikkelen](../../../levenscyclus/ontwikkelen/)[](../../../levenscyclus/ "Levencyclus")[Verificatie en validatie](../../../levenscyclus/verificatie-en-validatie/)[](../../../levenscyclus/ "Levencyclus")[Monitoring en beheer](../../../levenscyclus/monitoring-en-beheer/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)[](../../../onderwerpen/ "Onderwerp")[Bias en non discriminatie](../../../onderwerpen/bias-en-non-discriminatie/)

## Maatregel

Test en evalueer de nauwkeurigheid van het algoritme om te zorgen dat deze accurate uitkomsten geeft.

## Toelichting

De nauwkeurigheid van het algoritme wil zeggen: geeft het algoritme de juiste uitkomst voor [het gewenste doel](../1-pba-02-formuleren-doelstelling/); maakt het correcte berekeningen, voorspellingen, aanbevelingen, beslissingen of classificeringen.

Voor het evalueren van de nauwkeurigheid zijn de volgende stappen essentieel:

  * Bepaal met welke methoden en metriek(en) je de nauwkeurigheid wilt gaan meten. Pas dit aan op de [ontwerpkeuzes](../../../levenscyclus/ontwerp/), [het beoogde doel](../1-pba-02-formuleren-doelstelling/) en [de bepaalde risico’s](../2-owp-06-impactanalyse/).
  * [Controleer of de data volledig en actueel is](../3-dat-01-datakwaliteit/) om de metrieken te kunnen meten.
  * Bepaal welke foutmarge acceptabel is:

    * Bepaal hoe vaak het algoritme een bepaalde fout maakt. Houd rekening met verschillende fouten die gemaakt kunnen worden, zoals _false positives_ en _false negatives_. Welke fouten zijn erger om te maken?
    * De foutmarge is afhankelijk van [welke schade wordt veroorzaakt](../2-owp-06-impactanalyse/) bij onnauwkeurige of foutieve voorspellingen.
    * Heb hierbij aandacht voor de afweging tussen nauwkeurigheid en [betrouwbaarheid](../5-ver-06-evalueer-betrouwbaarheid/). Een model met hoge nauwkeurigheid op de testset kan vaak slechter generaliseren naar situaties net buiten de test set (overfitting).
    * Bepaal interventies voor als het restrisico hoger is dan acceptabel.

    * Wanneer de nauwkeurigheid niet voldoende is tijdens de ontwikkelfase kan er besloten worden door te ontwikkelen, andere maatregelen te treffen (bijvoorbeeld in [menselijke interventies](../../../onderwerpen/menselijke-controle/)) om het restrisico acceptabel te maken of door [te stoppen met de ontwikkeling van het systeem](../../../levenscyclus/uitfaseren/).

    * Wanneer monitoring aangeeft dat de nauwkeurigheid onvoldoende is, moet er een passende afweging worden gemaakt om het systeem te verbeteren dan wel over te gaan op het [stoppen van het systeem](../4-owk-02-stopzetten-gebruik/).

### Metrieken

Afhankelijk van het type algoritme zijn er verschillende metrieken waarmee je de nauwkeurigheid kan meten. Veelgebruikte metrieken/methoden zijn:

  * accuraatheid _(accuracy)_
  * precisie _(precision)_
  * _recall_
  * _F1-score_
  * _mean-squared-error_
  * _mean-absolute-error_
  * _ROC-curve_

Leg vast welke keuze je maakt voor bepaalde metrieken en waarom. In verschillende omgevingen en onder verschillende datasets moeten de relevante metrieken voor jouw toepassing worden geëvalueerd.

## Risico

Een onnauwkeurig algoritme geeft de verkeerde uitkomsten waardoor situaties of mogelijk personen verkeerd beoordeeld kunnen worden.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[aia-06 - Hoog-risico-AI-systemen zijn voorzien van voldoende technische documentatie](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-06-technische-documentatie/)
[aia-10 - Hoog-risico-AI-systemen zijn voldoende nauwkeurig, robuust en cyberveilig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-10-nauwkeurigheid-robuustheid-cyberbeveiliging/)
[awb-01 - Organisaties die algoritmes gebruiken voor publieke taken nemen besluiten zorgvuldig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/awb-01-zorgvuldigheidsbeginsel/)

## Bronnen

  * [Europese Commissie, Ethische richtsnoeren voor betrouwbare KI](https://digital-strategy.ec.europa.eu/nl/library/ethics-guidelines-trustworthy-ai)
  * [Toetingskader Algemene Rekenkamer, 2.03](https://www.rekenkamer.nl/onderwerpen/algoritmes/documenten/publicaties/2024/05/15/het-toetsingskader-aan-de-slag)
  * [Onderzoekskader algoritmes, Auditdienst Rijk, DM.1 en DM.4](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/hulpmiddelen/onderzoekskader-adr/)

## Voorbeelden

Gemeente Amsterdam – Public Eye

De gemeente Amsterdam maakt gebruik van een algoritme – Public Eye – om te bepalen hoeveel mensen er op een afbeelding staan. Public Eye wordt gebruikt om te kunnen monitoren hoeveel voetgangers er op plekken in de stad zijn, om zo onveilige situaties en drukte goed te kunnen begeleiden.

De gemeente geeft aan dat zij een minimum nauwkeurigheid van 70% hanteert om relevante inzichten te krijgen. In de praktijk levert Public Eye een hogere nauwkeurigheid van 90%, afgeleid van trainingsbeelden. Deze data is handmatig geannoteerd door een selecte groep werknemers die dit periodiek doet.

Bron: [Public Eye-Amsterdam Algoritmeregister](https://algoritmeregister.amsterdam.nl/ai-system/public-eye/231/)

Gemeente Ede – WOZ-taxatiemodellen

De gemeente Ede heeft een algoritme in gebruik als ondersteuning bij het bepalen (en controleren) van de WOZ-waarde van woningen. Dit wordt gedaan aan de hand van machine-learning modellen die op basis van onder andere woning- en locatiekenmerken, gecombineerd met markt- en verkoopconditites, de WOZ-waarde kunnen bepalen. Hierbij wordt bepaald welke kenmerken het meeste gewicht hebben voor deze bepaling.

Om deze uitkomsten te kunnen controleren wordt er aan de hand van ratio's bekeken of het algoritme nauwkeurig werkt (zie afbeelding hieronder). Aan de hand van deze ratio's wordt gecontroleerd of het algoritme aansluit bij het marktniveau. Als de waarden van de ratio's buiten de bandbreedte liggen, wordt de WOZ-waarde aangepast of wordt deze afwijking verder verklaard.

[![image](https://github.com/user-attachments/assets/8230f572-8836-40ef-9f91-ca8b1143c17a)](https://github.com/user-attachments/assets/8230f572-8836-40ef-9f91-ca8b1143c17a)

Bron: [WOZ-taxatiemodellen - Gemeente Ede](https://algoritmes.overheid.nl/nl/algoritme/woztaxatiemodellen-gemeente-ede/39323486#werking)

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

10 april 2025 19 december 2024

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
  *open-source: Open source is een manier van werken waarbij de makers de broncode, documentatie en ontwerp openbaar beschikbaar stellen onder een opensourcelicentie. Hierdoor kan iedereen de software bekijken, kopiëren, aanpassen of delen. Mensen kunnen voorstellen doen voor verbeteringen of toevoegingen.
