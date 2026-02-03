---
title: Discriminerende effecten en ander ongewenst onderscheid bij het gebruik van algoritmes - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/onderwerpen/bias-en-non-discriminatie/
scraped_at: 2025-06-12T10:33:39.364323
---

# Discriminerende effecten en ander ongewenst onderscheid bij het gebruik van algoritmes - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/onderwerpen/bias-en-non-discriminatie/

---

[ ![Home Algoritmekader](../../assets/logo.svg) ](../.. "Algoritmekader 2.2") Algoritmekader 2.2

[ GitHub  ](https://github.com/MinBZK/Algoritmekader "Ga naar repository")

  * [ Soorten algoritmes en AI  ](../../soorten-algoritmes-en-ai/)
  * Onderwerpen  Onderwerpen
    * [ Onderwerpen  ](../)

Onderwerpen
      * Discriminerende effecten en ander ongewenst onderscheid bij het gebruik van algoritmes  [ Discriminerende effecten en ander ongewenst onderscheid bij het gebruik van algoritmes  ](./) Inhoudsopgave
        * Wat is ongewenst onderscheid?
          * Uitzondering
        * Belang van discriminerende effecten voorkomen
        * Profilering
        * Herken bias
          * Bias in statistiek en berekeningen
          * Bias in systemen en processen
          * Bias in menselijk denken
        * Let altijd op discriminerende effecten
        * Vereisten
        * Aanbevolen maatregelen
        * Aanbevolen hulpmiddelen
        * Help ons deze pagina te verbeteren
      * [ Verantwoord datagebruik  ](../data/)
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

  * Wat is ongewenst onderscheid?
    * Uitzondering
  * Belang van discriminerende effecten voorkomen
  * Profilering
  * Herken bias
    * Bias in statistiek en berekeningen
    * Bias in systemen en processen
    * Bias in menselijk denken
  * Let altijd op discriminerende effecten
  * Vereisten
  * Aanbevolen maatregelen
  * Aanbevolen hulpmiddelen
  * Help ons deze pagina te verbeteren

  1. [ Onderwerpen  ](../)
  2. [ Onderwerpen  ](../)

# Discriminerende effecten en ander ongewenst onderscheid bij het gebruik van algoritmes

Wie algoritmes ontwikkelt of gebruikt, moet ongewenst onderscheid en eventuele discriminerende effecten hiervan voorkomen. Want met algoritmes kun je makkelijk discrimineren, ook al is dat niet de bedoeling. Let daarom steeds op ‘bias’. Dit zijn vooroordelen of fouten in je algoritme of aanpak.

## Wat is ongewenst onderscheid?

Algoritmes kunnen leiden tot ongewenst onderscheid als je mensen of (andere) groepen ongelijk behandelt in gelijke situaties.

Een camera met gezichtsherkenning herkent bijvoorbeeld geen vrouwen van kleur. Of een computerprogramma selecteert vooral mensen met een laag inkomen als risicogroep voor fraude.

Dit onderscheid kan op twee manieren ontstaan:

  * Direct onderscheid: Het algoritme gebruikt een [discriminatiegrond](https://www.mensenrechten.nl/mensenrechten-voor-jou/discriminatie-en-gelijke-behandeling/wat-is-discriminatie) als variabele, zoals geloof, politieke voorkeur, ras, nationaliteit, geslacht, handicap, burgerlijke staat, vermogen of leeftijd.
  * Indirect onderscheid: Het algoritme lijkt neutraal of eerlijk. Maar later blijkt dat bepaalde mensen op een andere manier worden behandeld door hun geloof, politieke of seksuele voorkeur, ras, geslacht, of burgerlijke staat.

Direct en indirect onderscheid is in veel gevallen niet toegestaan. Ongewenst onderscheid kan leiden tot discrimerende effecten van een algoritme.

Tip

Maakt je algoritme een ongewenst onderscheid of is er sprake van discrimerende effecten van je algoritme? Dan moet je zo snel mogelijk [stoppen met het algoritme](../../levenscyclus/uitfaseren/). Gebruik bijvoorbeeld het [discriminatieprotocol](https://minbzk.github.io/discriminatieprotocol/) van het ministerie van Binnenlandse Zaken en Koninkrijksrelaties.

### Uitzondering

Een direct of indirect onderscheid is niet altijd verboden volgens [Artikel 2 Algemene wet gelijke behandeling](https://wetten.overheid.nl/jci1.3:c:BWBR0006502&hoofdstuk=1&paragraaf=1&artikel=1&z=2020-01-01&g=2020-01-01). In bepaalde situaties en onder bepaalde strenge voorwaarden mag je zo’n onderscheid wel maken.

Direct onderscheid maken mag bijvoorbeeld als hiervoor een uitzondering staat in de wet. Zo mag je in situaties waar het gaat om moederschap of zwangerschap onderscheid maken op basis van geslacht.

Indirect onderscheid maken mag niet, tenzij hiervoor een wettelijke uitzondering geldt. Of je hebt een goede reden (objectieve rechtvaardiging). Selecteert je algoritme bijvoorbeeld alleen vrouwen voor een vacature, dan moet je hier een objectieve rechtvaardiging voor hebben. En het algoritme moet passend en noodzakelijk zijn om een doel te bereiken dat wettelijk is toegestaan. Anders is het discriminatie.

## Belang van discriminerende effecten voorkomen

Discriminatie is verboden volgens [Artikel 1 van de Nederlandse Grondwet](https://wetten.overheid.nl/jci1.3:c:BWBR0001840&hoofdstuk=1&artikel=1&z=2023-02-22&g=2023-02-22). En algoritmes kunnen snel een discriminerend effect hebben op grote groepen mensen. Vooral [impactvolle algoritmes](../../soorten-algoritmes-en-ai/impact-van-algoritmes/) kunnen veel schade veroorzaken in de maatschappij door discriminatie.

Het is erg moeilijk om discriminerende effecten te voorkomen. Discriminatiegronden weglaten als variabele in je algoritme is niet genoeg. Want discriminatie ontstaat ook indirect, door bias.

## Profilering

Veel organisaties gebruiken risicoprofilering als hulpmiddel om regels te handhaven. Dit gebruik van risicoprofilering kan leiden tot discriminerende effecten. Het gebruik van risicoprofilering vraagt om een zorgvuldige aanpak om nadelige effecten te voorkomen. Om organisaties hier mee te helpen, heeft het College voor de Rechten van de Mens een gedetailleerd [toetsingskader voor risicoprofilering](https://publicaties.mensenrechten.nl/publicatie/4093c026-ae41-4c1d-aa78-4ce0e205b5de) ontwikkeld om discriminatie op grond van ras en nationaliteit te voorkomen.

Tip

Meer weten over dit onderwerp? Of wil je dat collega's meer weten over dit onderwerp? Volg de [e-learning non-discriminatie in algoritmes en data](https://www.it-academieoverheid.nl/actueel/nieuws/2024/10/29/nieuwe-radio-e-learning-non-discriminatie), ontwikkeld door het Ministerie van Binnenlandse Zaken en Koninkrijksrelaties.

## Herken bias

Bias herkennen is een belangrijke stap in het voorkomen van discriminerende effecten van algoritmes.

'Bias' is een Engels woord voor vooroordeel of vooringenomenheid. Algoritmes met een bias maken steeds een bepaald soort fout. Volgens de norm [ISO/IEC TR 24027](https://www.nen.nl/iso-iec-tr-24027-2021-en-289193) bevat een algoritme bias wanneer het bepaalde mensen, groepen of producten steeds (systematisch) op een verschillende manier behandelt. Dit verhoogt de kans op discriminatie.

Alle algoritmes hebben vooroordelen en maken fouten, net als de mens. Wil je dit aanpakken, zoek dan naar bias in het algoritme zelf en in de mensen en processen om het algoritme heen. Een bias-vrij algoritme is niet mogelijk.

Bias ontstaat bijvoorbeeld in:

  * statistiek en berekeningen (statistische bias)
  * systemen en processen in bijvoorbeeld de samenleving of je organisatie (systemische bias)
  * het menselijk denken (menselijke bias)

### Bias in statistiek en berekeningen

Dit zijn fouten in de:

  * kwaliteit van de data
  * manier waarop algoritmes data verwerken

Voorbeelden:

Meet-bias (measurement bias)

Je algoritme maakt een verkeerde schatting of benadering van kenmerken of labels. Dit komt doordat het de ene variabele gebruikt om een andere variabele te voorspellen of te benaderen (proxy). En hierbij laat het belangrijke informatie weg, of het voegt onbelangrijke informatie (ruis) toe.

Een algoritme maakt bijvoorbeeld een verkeerde schatting van het risico op overlijden aan longontsteking in het ziekenhuis. Het algoritme leert namelijk uit de data dat dit risico lager is voor astmapatiënten. Maar dit komt niet door hun astma. Het algoritme laat weg dat astmapatiënten met longontsteking direct naar de intensive care gaan. En mensen zonder astma niet.

Versterkingsbias (amplification bias)

Je algoritme versterkt een patroon uit de trainingsdata.

Een algoritme dat mensen en hun acties herkent, voorspelt bijvoorbeeld 5 keer zo vaak de combinatie ‘vrouw’ en ‘koken’. Terwijl deze combinatie in de trainingsdata maar 2 keer zo vaak voorkomt.

Evaluatie-bias (evaluation bias)

Je algoritme trekt verkeerde conclusies omdat de evaluatiedata niet kloppen, of niet compleet zijn.

Een algoritme voor gezichtsherkenning herkent bijvoorbeeld vrouwen van kleur niet goed, omdat deze vrouwen te weinig voorkomen in de dataset voor evaluatie.

Representatie-bias (representation bias)

Je algoritme doet voorspellingen over een grote groep, op basis van resultaten uit subgroepen met te weinig verschillende proefpersonen.

Een algoritme beoordeelt bijvoorbeeld de populariteit van treinstations onder reizigers op basis van hun smartphone-gebruik. Maar deze groep is niet representatief, omdat oudere reizigers vaak minder gebruik maken van smartphones.

### Bias in systemen en processen

Dit is vooringenomenheid die vaak in de loop der tijd is ontstaan in de samenleving of je organisatie. Deze vooringenomenheid werkt door in processen of systemen, of wordt soms versterkt door algoritmes. Dit gebeurt vaak niet bewust.

Systemische bias heet ook wel: institutionele vooringenomenheid. Dit betekent dat vooroordelen vaak horen bij de cultuur en samenleving. Die vooroordelen zitten daardoor ook in veel datasets, en kunnen zo versterkt worden door je algoritme.

Voorbeelden:

Historische bias

Je algoritme heeft vooroordelen die in de loop der tijd ontstonden in de samenleving.

Een algoritme gebruikt bijvoorbeeld data die gebaseerd is op oude belastingregels, terwijl er nieuwe wetten en regels zijn. Dan zit er een historische bias in je data. Of een algoritme voorspelt bijvoorbeeld de koopkracht van mensen, maar gebruikt hiervoor data uit een tijd waarin mannen meer verdienden dan vrouwen.

Activiteitenbias (activity bias)

Je algoritme geeft een verkeerd beeld over gebruikers van interactieve producten, zoals websites of apps. Dit komt omdat alleen de meest actieve gebruikers trainingsdata aanleveren.

Een algoritme onderzoekt bijvoorbeeld wat burgers van een bepaalde brief vinden op basis van kliks in een digitale vragenlijst. Het algoritme kan niet zeggen wat burgers écht vinden, omdat de meest actieve internetgebruikers vaker klikken en vaker de vragenlijst invullen.

Samenlevingsbias (societal bias)

Je algoritme maakt een fout op basis van stereotypes die voorkomen in de samenleving. Dit gebeurt vooral in AI-systemen die taal verwerken via Natural Language Processing (NLP).

Een algoritme dat teksten maakt, geeft bijvoorbeeld ‘verpleegster’ als vrouwelijke vorm van ‘dokter’. Dit komt omdat het stereotype dokter in die samenleving een man is.

### Bias in menselijk denken

Dit zijn vooroordelen in het menselijk denken die steeds (systematisch) invloed hebben op de manier waarop iemand iets ziet, hoort, ruikt, proeft of voelt.

Menselijke bias kan invloed hebben op de:

  * verzamelde data
  * manier waarop je het algoritme optimaliseert
  * besluiten die je neemt op basis van het algoritme

Voorbeelden:

Automatiseringsbias

Mensen maken een denkfout omdat zij de voorkeur geven aan adviezen van automatische besluitvormingssystemen. Zelfs als uit andere informatie blijkt dat deze adviezen niet kloppen.

Wanneer behandelaren handmatig controleren of een uitkering van een burger klopt, hebben zij vaak de neiging om de beslissing te volgen van het algoritme.

Cognitieve bias

Mensen maken een denkfout omdat zij volgens een vast patroon afwijken van logisch nadenken. Vaak gebeurt dit om complexe denktaken te versimpelen of versnellen.

Administratief medewerkers weigeren bijvoorbeeld een AI-systeem te gebruiken, omdat ze slechte ervaringen hebben met een ander AI-systeem. Zij willen het nieuwe AI-systeem dus niet gebruiken, terwijl ze dit nooit gebruikt hebben.

Bevestigingsbias

Mensen maken een denkfout omdat zij de voorkeur geven aan voorspellingen van algoritmes die hun eigen overtuigingen of gedachtes bevestigen.

Rechercheurs zoeken bijvoorbeeld direct naar bewijs om verdachte X te veroordelen, nadat een algoritme X voorspelt als dader. Terwijl de rechercheurs ook ander bewijs moeten zoeken.

Implementatie-bias

Een algoritme wordt op een andere manier gebruikt dan hoe het bedoeld is en waarvoor het ontwikkeld is. Dit komt vaak voor wanneer een algoritme wordt gebruikt als beslishulp voor mensen. Deze vorm van bias is een menselijke denkfout in de vorm dat gebruikers niet op dezelfde of goede manier omgaan met adviezen.

Een wet over bijvoorbeeld immigratie wordt ingevoerd en er wordt een algoritme ontwikkeld om te onderzoeken wat de gevolgen hiervan zijn. Dit algoritme is dan ook bedoeld om voor bepaalde groepen mensen te kijken wat de gevolgen zijn. Het algoritme wordt ook gebruikt bij het toekennen van staatsburgerschap aan de hand van de gevolgen. Dit is niet zoals het systeem bedoeld is en dus kunnen er incomplete antwoorden of resultaten uitkomen.

Overlevingsbias (survivorship bias)

Mensen hebben de neiging om voorkeur te geven aan dingen, mensen of observaties die door een bepaalde selectie zijn gekomen. Naar de gevallen die buiten de selecties vallen wordt vaak niet of minder gekeken. Dit kan leiden tot een zichzelf versterkend proces. Zo worden bijvoorbeeld modellen die werken verbeterd, maar wordt niet gekeken waarom de andere modellen niet werken.

Om fraudeherkenning te vergemakkelijken wordt bijvoorbeeld een model getraind op data van personen/huishoudens die eerder zijn gecontroleerd op mogelijke fraude. Hiermee wordt een groot gedeelte personen/huishoudens niet meegenomen in de trainingsdata, omdat deze groep niet eerder gecontroleerd is.

## Let altijd op discriminerende effecten

Het risico op bias en discriminatie blijft altijd bestaan. Je kunt dit niet in 1 keer wegnemen.

Houd daarom rekening met bias tijdens het ontwikkelen, inkopen en gebruiken van algoritmes. En controleer voortdurend of je algoritmes en je aanpak nog eerlijk en rechtvaardig zijn. Let hierop in alle fasen van de [levenscyclus](../../levenscyclus/) van het algoritme.

## Vereisten

id| Vereisten
---|---
[aia-04](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-04-risicobeoordeling-voor-jongeren-en-kwetsbaren/index.html)| [Hoog-risico-AI-systemen vormen geen risico voor kwetsbare groepen zoals kinderen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-04-risicobeoordeling-voor-jongeren-en-kwetsbaren/index.html)
[avg-08](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-08-wettelijke-verwerking-van-gevoelige-gegevens/index.html)| [Gevoelige persoonsgegevens worden alleen gebruikt als hiervoor een wettelijke uitzondering geldt](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-08-wettelijke-verwerking-van-gevoelige-gegevens/index.html)
[grw-02](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/grw-02-non-discriminatie/index.html)| [Algoritmes discrimineren niet](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/grw-02-non-discriminatie/index.html)

## Aanbevolen maatregelen

id| Maatregelen
---|---
[org-15](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/0-org-15-discriminatieprotocol/index.html)| [Stel een protocol vast voor de situatie dat er (een vermoeden van) discriminatie door een algoritme is geconstateerd en pas dit wanneer nodig toe](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/0-org-15-discriminatieprotocol/index.html)
[dat-02](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-02-toetsen-geschiktheid-variabelen/index.html)| [Toets en analyseer of de inputvariabelen of risicoindicatoren geschikt zijn voor het beoogde algoritme](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-02-toetsen-geschiktheid-variabelen/index.html)
[dat-07](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-07-training-validatie-en-testdata/index.html)| [Gebruik bij machine learning technieken gescheiden train-, test- en validatiedata en houd rekening met underfitting en overfitting](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-07-training-validatie-en-testdata/index.html)
[owk-08](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-08-feedbackloops/index.html)| [Bepaal welke feedbackloops van invloed zijn op het algoritme](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-08-feedbackloops/index.html)
[ver-01](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-01-functioneren-in-lijn-met-doeleinden/index.html)| [Controleer regelmatig of het algoritme werkt zoals het bedoeld is](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-01-functioneren-in-lijn-met-doeleinden/index.html)
[ver-02](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-02-evalueer-nauwkeurigheid/index.html)| [Evalueer de nauwkeurigheid van het algoritme](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-02-evalueer-nauwkeurigheid/index.html)
[ver-03](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-03-biasanalyse/index.html)| [Toets het algoritme op bias en voer een rechtvaardigingstoets uit](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-03-biasanalyse/index.html)
[imp-02](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-02-aselecte-steekproeven/index.html)| [Doe aselecte steekproeven om algoritmes met 'risicogestuurde selectie’ te controleren](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-02-aselecte-steekproeven/index.html)

## Aanbevolen hulpmiddelen
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
