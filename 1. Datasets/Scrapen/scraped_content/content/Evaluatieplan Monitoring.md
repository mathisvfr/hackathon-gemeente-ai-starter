---
title: Maak een evaluatieplan voor tijdens het gebruik van het algoritme - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-04-evaluatieplan/index.html
scraped_at: 2025-06-12T10:35:05.802998
---

# Maak een evaluatieplan voor tijdens het gebruik van het algoritme - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-04-evaluatieplan/index.html

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
    * Bepaal of periodieke controle noodzakelijk is
    * Bepaal bij welke gebeurtenissen het algoritme geëvalueerd moet worden
    * Bepaal wat er geëvalueerd moet worden
    * Documenteer voor en tijdens iedere evaluatie
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Maak een evaluatieplan voor tijdens het gebruik van het algoritme

[]( "Vereiste ID")mon-04[](../../../levenscyclus/ "Levencyclus")[Monitoring en beheer](../../../levenscyclus/monitoring-en-beheer/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)

## Maatregel

Maak een evaluatieplan voor wanneer het algoritme in gebruik is. Dit plan bevat wanneer, wat en hoe er geëvalueerd dient te worden om te valideren of het model nog in lijn is met de [vastgestelde doelstelling](../1-pba-02-formuleren-doelstelling/).

## Toelichting

Het evaluatieplan moet aangeven op welke momenten er wordt geëvalueerd, wat er opnieuw wordt geëvalueerd en hoe dat wordt gedaan.

Voor het opstellen van het evaluatieplan zijn de volgende stappen nodig:

  1. Bepaal of periodieke controle noodzakelijk is
  2. Bepaal bij welke gebeurtenissen het algoritme geëvalueerd moet worden
  3. Bepaal wat er geëvalueerd moet worden

### Bepaal of periodieke controle noodzakelijk is

Stel vast of er periodieke momenten zijn vanuit bijvoorbeeld wetgeving, organisatiebeleid of risicomanagement waarop het wenselijk is dat het algoritme geëvalueerd wordt.

### Bepaal bij welke gebeurtenissen het algoritme geëvalueerd moet worden

Wat zijn gebeurtenissen die om een nieuwe evaluatie vragen? Denk bijvoorbeeld aan momenten waarop het bijtrainen van het model noodzakelijk is, zoals:

  * Een wijziging in de data of het algoritme.
  * Aangepaste wetgeving.
  * Andere context of tijd waarin het algoritme gebruikt wordt.
  * Een nieuwe werkwijze.
  * Het optreden van een incident.
  * Gebruikersfeedback.
  * Een verandering in de gebruikscontext (bijv. een situatie als COVID-19).

### Bepaal wat er geëvalueerd moet worden

Bepaal welke onderdelen van het algoritme geëvalueerd dienen te worden bij een periodieke controle of wanneer er een gebeurtenis plaatsvindt waardoor evaluatie wenselijk is.

Wat minimaal periodiek geëvalueerd moet worden is:

  * [nauwkeurigheid](../5-ver-02-evalueer-nauwkeurigheid/)
  * [betrouwbaarheid](../5-ver-06-evalueer-betrouwbaarheid/)
  * [reproduceerbaarheid](../4-owk-07-reproduceerbaarheid/)
  * [bias](../5-ver-03-biasanalyse/)
  * [veiligheid](../7-mon-08-test-weerbaarheid-tegen-aanvallen/)
  * [grondrechten](../2-owp-07-afwegen-grondrechten/)
  * [privacy](../4-owk-03-privacyrisico/).

Bij een evaluatie hoeft niet altijd alles weer geëvalueerd te worden. Dit hangt af van het type wijzigingen die er zijn geweest en van de aspecten die continu worden gemonitored. Leg vast wat er wanneer geëvalueerd dient te worden.

### Documenteer voor en tijdens iedere evaluatie

Zorg dat de benodigde informatie voor de evaluatie wordt opgeslagen en beschikbaar is voor de evaluatiemomenten. Denk aan invoerwaarden, resultaten en gebruikersstatistieken.

Betrek bij het opstellen van dit plan een [diverse groep van belanghebbenden](../1-pba-04-betrek-belanghebbenden/) met o.a. ontwikkelaars, gebruikers en ethisch adviseurs. Zorg dat het evaluatieplan periodiek wordt herzien of deze nog voldoet.

## Risico

Er zullen veranderingen plaatsvinden in de gebruikscontext, de data en in het algoritme zelf (bijv. door bijtrainen). Wanneer niet wordt geëvalueerd tijdens het gebruik is het onbekend of het algoritme nog steeds werkt zoals beoogd en voldoet aan de acceptatiecriteria.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[aia-03 - Hoog-risico-AI-systemen zijn voorzien van een risicobeheersysteem](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-03-risicobeheersysteem/)
[aia-18 - Als een hoog-risico-AI-systeem niet voldoet aan de AI-verordening, grijpt de aanbieder in](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-18-corrigerende-maatregelen-voor-non-conforme-ai/)
[aia-22 - De werking van hoog-risico-AI-systemen wordt gemonitord](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-22-gebruiksverantwoordelijken-monitoren-werking/)
[aia-34 - Hoog-risico-AI-systemen zijn voorzien van een monitoringsysteem](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-34-monitoring-na-het-in-de-handel-brengen/)

## Bronnen

  * [Toetsingskader Algemene Rekenkamer, 2.14](https://www.rekenkamer.nl/onderwerpen/algoritmes/documenten/publicaties/2024/05/15/het-toetsingskader-aan-de-slag)

## Voorbeelden

UWV - Claim beoordelings- en borgingsysteem

Om te bepalen of iemand nog kan werken en hoeveel maakt het UWV gebruik van een 'Claim beoordelings- en borgingsysteem' (CBBS). Dit systeem bepaalt aan de hand van onder andere de beoordeling van de verzekeringsarts en de UWV-polisadministratie het arbeidsongeschiktheidspercentage. Deze waarde wordt gebruikt als basis om een geschikte baan te vinden voor het individu dat beoordeeld wordt. Het UWV geeft aan CBBS iedere dag te testen om zo te kijken of het goed werkt. Daarnaast wordt er specifiek gecontroleerd na wijzigingen in bijvoorbeeld wet- en regelgeving, bij functieveranderingen of als de zwaarte van een functie veranderd. Dit evaluatiebeleid geeft dus aan wat er gecontroleerd wordt en wanneer.

Bron: [Claim Beoordelings- en Borgingsysteem](https://algoritmes.overheid.nl/nl/algoritme/claim-beoordelings-en-borgingsysteem-cbbs-uitvoeringsinstituut-werknemersverzekeringen/21447945)

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

19 februari 2025 19 december 2024

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
  *direct onderscheid: Indien een persoon op een andere wijze wordt behandeld dan een ander in een vergelijkbare situatie wordt, is of zou worden behandeld, op grond van godsdienst, levensovertuiging, politieke gezindheid, ras, geslacht, nationaliteit, hetero- of homoseksuele gerichtheid of burgerlijke staat;
  *bijzondere categorieën persoonsgegevens: de categorieën persoonsgegevens als bedoeld in artikel 9, lid 1, van Verordening (EU) 2016/679, artikel 10 van Richtlijn (EU) 2016/680 en artikel 10, lid 1, van Verordening (EU) 2018/1725
  *operator: een aanbieder, productfabrikant, gebruiksverantwoordelijke, gemachtigde, importeur of distributeur
