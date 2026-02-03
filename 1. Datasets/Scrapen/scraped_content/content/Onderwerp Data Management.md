---
title: Verantwoord datagebruik - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/onderwerpen/data/
scraped_at: 2025-06-12T10:33:40.565096
---

# Verantwoord datagebruik - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/onderwerpen/data/

---

[ ![Home Algoritmekader](../../assets/logo.svg) ](../.. "Algoritmekader 2.2") Algoritmekader 2.2

[ GitHub  ](https://github.com/MinBZK/Algoritmekader "Ga naar repository")

  * [ Soorten algoritmes en AI  ](../../soorten-algoritmes-en-ai/)
  * Onderwerpen  Onderwerpen
    * [ Onderwerpen  ](../)

Onderwerpen
      * [ Discriminerende effecten en ander ongewenst onderscheid bij het gebruik van algoritmes  ](../bias-en-non-discriminatie/)
      * Verantwoord datagebruik  [ Verantwoord datagebruik  ](./) Inhoudsopgave
        * Wat is verantwoord datagebruik?
          * Rechtmatig gebruik van data
          * Goede datakwaliteit
          * Goed databeheer: datagovernance en datamanagement
        * Belang van verantwoord datagebruik
          * Bescherming van cruciale infrastructuurdata
        * Vereisten
        * Aanbevolen maatregelen
        * Hulpmiddelen
      * [ Duurzaam werken met algoritmes  ](../duurzaamheid/)
      * [ Grondrechten beschermen in algoritmes  ](../fundamentele-rechten/)
      * [ Governance van algoritmes binnen je organisatie  ](../governance/)
      * [ Menselijke controle over algoritmes  ](../menselijke-controle/)
      * [ Privacy en persoonsgegevens beschermen in algoritmes  ](../privacy-en-gegevensbescherming/)
      * [ Inkoop van verantwoorde algoritmes  ](../publieke-inkoop/)
      * [ Technische robuustheid en veiligheid  ](../technische-robuustheid-en-veiligheid/)
      * [ Transparant zijn over algoritmes  ](../transparantie/)
  * [ Levenscyclus  ](../../levenscyclus/)
  * [ Rollen  ](../../rollen/)
  * [ Voldoen aan wetten en regels  ](../../voldoen-aan-wetten-en-regels/)

Inhoudsopgave

  * Wat is verantwoord datagebruik?
    * Rechtmatig gebruik van data
    * Goede datakwaliteit
    * Goed databeheer: datagovernance en datamanagement
  * Belang van verantwoord datagebruik
    * Bescherming van cruciale infrastructuurdata
  * Vereisten
  * Aanbevolen maatregelen
  * Hulpmiddelen

  1. [ Onderwerpen  ](../)
  2. [ Onderwerpen  ](../)

# Verantwoord datagebruik

Overheden moeten verantwoord omgaan met de data die hun algoritmes gebruiken. De data moet voldoen aan regels voor bijvoorbeeld privacy. De kwaliteit van de data moet goed zijn. En overheden moeten deze gegevens goed beheren. Anders is het algoritme niet betrouwbaar.

## Wat is verantwoord datagebruik?

Verantwoord datagebruik betekent:

  * Rechtmatig gebruik van gegevens
  * Goede datakwaliteit
  * Goed databeheer

### Rechtmatig gebruik van data

Net als organisaties mogen algoritmes niet zomaar gegevens verzamelen en gebruiken. Dit moet rechtmatig gebeuren: volgens de wettelijke regels. Zo moet je rekening houden met auteursrechten. Ook vóórdat het algoritme in gebruik is, moet je rechtmatig omgaan met data. Dus tijdens het trainen, valideren en testen.

Andere belangrijke regels gaan over privacy. Zo mag je algoritme alleen de minimale persoonsgegevens gebruiken die nodig zijn om het doel te bereiken. Technieken om dit te doen zijn:

  * Anonimiseren: data zoveel mogelijk anoniem maken
  * [Pseudonimiseren](https://www.autoriteitpersoonsgegevens.nl/themas/beveiliging/beveiliging-van-persoonsgegevens/gegevens-pseudonimiseren): data moeilijker herleidbaar maken naar personen
  * Aggregeren: data zoveel mogelijk combineren of samenvoegen tot 1 waarde, zoals een totaal of gemiddelde

### Goede datakwaliteit

Hoe slechter de datakwaliteit, hoe onbetrouwbaarder de uitkomsten van je algoritme.

Je bepaalt en controleert zelf de [kwaliteit van je dataset](../../voldoen-aan-wetten-en-regels/maatregelen/3-dat-01-datakwaliteit/). Check bijvoorbeeld of alle gegevens juist, compleet en actueel zijn. En herken [bias in je data](../bias-en-non-discriminatie/).

### Goed databeheer: datagovernance en datamanagement

Goed databeheer betekent dat je organisatie duidelijke afspraken maakt over het:

  * opslaan en verwerken van data
  * gebruik van data: welke data mag je waarvoor gebruiken?
  * beveiligen van data
  * bewaken van de datakwaliteit, zoals het actueel houden van de gegevens
  * eigenaarschap van data, bijvoorbeeld de partij die het algoritme ontwikkelt
  * documenteren en labelen van data (metadata)

Leg de processen en afspraken hierover vast in de [datagovernance](https://realisatieibds.nl/page/view/f51c90d3-c33d-4826-83d2-7381c0b14aba/8-data-governance) van je organisatie. In een datamanagementstrategie beschrijf je hoe je organisatie data verzamelt, ordent en gebruikt. Zo kan je organisatie optimaal gebruikmaken van data.

Hoe goed je organisatie data beheert, check je met [datavolwassenheidsmodellen](https://realisatieibds.nl/page/view/ad94d97c-4d48-443c-aedd-235b2d0ca8b6/wegwijzer-volwassenheidsmodellen) uit de Toolbox verantwoord datagebruik van de Interbestuurlijke Datastrategie (IBDS). Of gebruik de [beslishulp datavolwassenheid](https://realisatieibds.nl/groups/view/c23ab74c-adb4-424e-917d-773a37968efe/kenniscentrum-van-de-ibds).

## Belang van verantwoord datagebruik

Algoritmes kunnen veel schade veroorzaken in de maatschappij als ze de verkeerde gegevens gebruiken.

Met verantwoord datagebruik voorkom je:

  * verkeerde beslissingen doordat je algoritme resultaten baseert op data van slechte kwaliteit
  * discriminerende effecten van algoritmes doordat je data bias bevat
  * lekken van privacygevoelige informatie, zoals persoonsgegevens
  * gebruik van data die niet rechtenvrij zijn, zoals teksten met auteursrechten
  * dat resultaten niet te reproduceren zijn, doordat de data niet goed is opgeslagen

### Bescherming van cruciale infrastructuurdata

Niet alleen persoonsgegevens, maar ook gegevens over de Nederlandse infrastructuur vragen om verantwoord datagebruik. Dit omvat zowel fysieke infrastructuur, zoals wegen, bruggen, tunnels en energievoorzieningen, als digitale infrastructuur, zoals datakabels en datacentra.

Het ongecontroleerd delen of gebruiken van deze gegevens, bijvoorbeeld voor het trainen van buitenlandse AI-toepassingen, kan risico’s opleveren voor de nationale veiligheid en de continuïteit van vitale systemen. Overheden en organisaties moeten deze data goed [beveiligen](../technische-robuustheid-en-veiligheid/) en duidelijke [kaders opstellen](../../voldoen-aan-wetten-en-regels/maatregelen/0-org-02-beleid-opstellen-inzet-algoritmes/) om verantwoord gebruik te waarborgen.

## Vereisten

id| Vereisten
---|---
[aia-05](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-05-data-kwaliteitscriteria/index.html)| [Datasets voor hoog-risico-AI-systemen voldoen aan kwaliteitscriteria](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-05-data-kwaliteitscriteria/index.html)
[aia-33](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-33-verwerking-in-testomgeving/index.html)| [AI-testomgevingen die persoonsgegevens verwerken, voldoen aan strenge voorwaarden](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-33-verwerking-in-testomgeving/index.html)
[arc-01](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/arc-01-archiefwet/index.html)| [Informatie over algoritmes wordt in goede, geordende en toegankelijke staat gebracht, bewaard en vernietigd wanneer nodig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/arc-01-archiefwet/index.html)
[aut-01](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aut-01-auteursrechten/index.html)| [Auteursrechten zijn beschermd](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aut-01-auteursrechten/index.html)
[avg-09](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-09-inroepen-privacyrecht-bij-verwerking-persoonsgegevens/index.html)| [Betrokkenen kunnen een beroep doen op hun privacyrechten](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-09-inroepen-privacyrecht-bij-verwerking-persoonsgegevens/index.html)
[dat-01](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/dat-01-databankenwet/index.html)| [Databanken worden alleen gebruikt met toestemming van de databank-producent](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/dat-01-databankenwet/index.html)

## Aanbevolen maatregelen

id| Maatregelen
---|---
[owp-02](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-02-data-beschikbaarheid/index.html)| [Voer voorafgaand aan een project een data beschikbaarheid, kwaliteit- en toegankelijkheidsanalayse uit](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-02-data-beschikbaarheid/index.html)
[owp-11](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-11-gebruikte-data/index.html)| [Beschrijf welke data gebruikt wordt voor de beoogde toepassing](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-11-gebruikte-data/index.html)
[owp-18](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-18-leveren-bewijs-door-aanbieder-niet-schenden-auteursrechten/index.html)| [Laat aanbieder(s) bewijs leveren dat de door hen ontwikkelde algoritmes geen inbreuk maken op de auteursrechten van derden met de trainingsdata en de output](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-18-leveren-bewijs-door-aanbieder-niet-schenden-auteursrechten/index.html)
[owp-34](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-34-voorkom-kwetsbaarheden-supplychain/index.html)| [Voorkom kwetsbaarheden die geïntroduceerd worden in de supply-chain van het algoritme](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-34-voorkom-kwetsbaarheden-supplychain/index.html)
[dat-01](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-01-datakwaliteit/index.html)| [Controleer de datakwaliteit](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-01-datakwaliteit/index.html)
[dat-02](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-02-toetsen-geschiktheid-variabelen/index.html)| [Toets en analyseer of de inputvariabelen of risicoindicatoren geschikt zijn voor het beoogde algoritme](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-02-toetsen-geschiktheid-variabelen/index.html)
[dat-05](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-05-schending-auteursrechten/index.html)| [Controleer de auteursrechten van eigen data](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-05-schending-auteursrechten/index.html)
[dat-07](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-07-training-validatie-en-testdata/index.html)| [Gebruik bij machine learning technieken gescheiden train-, test- en validatiedata en houd rekening met underfitting en overfitting](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-07-training-validatie-en-testdata/index.html)
[dat-08](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-08-eigenaarschap-data/index.html)| [Zorg dat je controle of eigenaarschap hebt over de data](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-08-eigenaarschap-data/index.html)
[dat-09](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-09-dataminimalisatie/index.html)| [Beperk de omvang van datasets voor energie-efficiëntie](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-09-dataminimalisatie/index.html)
[dat-10](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-10-datamanipulatie/index.html)| [Controleer de data op manipulatie en ongewenste afhankelijkheden](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-10-datamanipulatie/index.html)
[dat-11](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-11-controleren-inputdata/index.html)| [Controleer de input van gebruikers op misleiding](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-11-controleren-inputdata/index.html)
[dat-12](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-12-fair-data/index.html)| [Maak waardevolle data vindbaar, toegankelijk, interoperabel en herbruikbaar (FAIR) binnen en buiten de eigen organisatie](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-12-fair-data/index.html)
[owk-12](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-12-licentiegebruik/index.html)| [Gebruik een passende licentie bij publicatie of gebruik van (open) data](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-12-licentiegebruik/index.html)
[imp-10](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-10-proces-privacyrechten/index.html)| [Spreek af hoe de organisatie omgaat met privacy-verzoeken](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-10-proces-privacyrechten/index.html)
[mon-05](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-05-evalueer-bij-veranderingen-in-data/index.html)| [Monitor regelmatig op veranderingen in de data. Bij veranderingen evalueer je de prestaties en output van het algoritme.](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-05-evalueer-bij-veranderingen-in-data/index.html)

## Hulpmiddelen

  * [Toolbox verantwoord datagebruik](https://realisatieibds.nl/page/view/628d59dd-0755-4c20-8217-d3f26d9d8a5c/toolbox-voor-verantwoord-datagebruik), Interbestuurlijke Datastrategie (IBDS)
  * [Richtlijnen voor ‘FAIR’ data](https://www.gofair.foundation/), GO FAIR Foundation

19 december 2024 9 januari 2024
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
