---
title: Controleer de datakwaliteit - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-01-datakwaliteit/index.html
scraped_at: 2025-06-12T10:34:14.092692
---

# Controleer de datakwaliteit - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-01-datakwaliteit/index.html

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
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Controleer de datakwaliteit

[]( "Vereiste ID")dat-01[](../../../levenscyclus/ "Levencyclus")[Dataverkenning en datapreparatie](../../../levenscyclus/dataverkenning-en-datapreparatie/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Data](../../../onderwerpen/data/)

## Maatregel

Stel vast of de gebruikte data van voldoende kwaliteit is voor de beoogde toepassing.

## Toelichting

  * Stel functionele eisen voor de datakwaliteit vast en [analyseer structureel of er aan deze eisen wordt voldaan](../7-mon-05-evalueer-bij-veranderingen-in-data/).
  * De kwaliteit van de data die als input voor het algoritme wordt gebruikt is bepalend voor de uitkomsten van het algoritme. Hier wordt soms ook naar gerefereerd als _garbage in = garbage out_.
  * Een vraag die gesteld dient te worden: beschrijft de data het fenomeen dat onderzocht dient te worden? Oftewel: is de data _representatief_ voor de [doelpopulatie](../1-pba-02-formuleren-doelstelling/)?
  * Het [Raamwerk gegevenskwaliteit](https://www.noraonline.nl) bevat een breed toepasbare set van kwaliteitsdimensies:

    * juistheid
    * compleetheid
    * validiteit
    * consistentie
    * actualiteit
    * precisie
    * plausibiliteit
    * traceerbaarheid
    * begrijpelijkheid

Deze dimensies zijn aangevuld met [kwaliteitsattributen](https://www.noraonline.nl) welke gebruikt kunnen worden om de verschillende dimensies meetbaar te maken.

  * De vraag of de data kwaliteit voldoende is, hangt sterk samen met de vraag of er bias in de onderliggende data zit. Analyseer daarom ook welke bias en aannames er besloten zijn in de onderliggende data. Denk hierbij onder andere aan de volgende vormen van bias:

    * [historische bias](../../../onderwerpen/bias-en-non-discriminatie/#herken-bias)
    * [meetbias](../../../onderwerpen/bias-en-non-discriminatie/#herken-bias)
    * [representatie bias](../../../onderwerpen/bias-en-non-discriminatie/#herken-bias)
  * Zorg dat je data [vindbaar, toegankelijk, interoperabel en herbruikbaar (FAIR)](../3-dat-12-fair-data/) is.

  * Bepaal of de data voldoende representatief is voor de doelpopulatie en of de data voldoende representatief is voor eventuele relevante subgroepen uit de productiedata.

Let op!

Wanneer je een algoritme inkoopt en de ontwikkeling van het algoritme uitbesteedt aan een derde partij, houdt er dan dan rekening mee dat data traceerbaar en reproduceerbaar moet zijn. Maak hier heldere afspraken over met de aanbieder.

## Risico

  * Door onjuiste beslissingen van gegevens kunnen verkeerde beslissingen genomen worden.
  * Het model creëert onwenselijke systematische afwijking voor specifieke personen, groepen of andere eenheden. Dit kan leiden tot ongelijke behandeling en discriminerende effecten met eventuele schade voor betrokkenen.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[avg-05 - Persoonsgegevens zijn juist en actueel](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-05-juistheid-en-actualiteit-van-persoonsgegevens/)
[aia-05 - Datasets voor hoog-risico-AI-systemen voldoen aan kwaliteitscriteria](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-05-data-kwaliteitscriteria/)

## Bronnen

  * [Onderzoekskader Algoritmes Auditdienst Rijk, DM.7, DM.9, DM.19](https://www.rijksoverheid.nl/documenten/rapporten/2023/07/11/onderzoekskader-algoritmes-adr-2023)
  * [Toetsingskader Algoritmes, Algemene Rekenkamder, 2.18](https://www.rekenkamer.nl/onderwerpen/algoritmes/documenten/publicaties/2024/05/15/het-toetsingskader-aan-de-slag)
  * [NORA, Raamwerk gegevenskwaliteit](https://www.noraonline.nl)
  * [Impact Assessment Mensenrechten en Algoritmes, 2A.2.2](../../hulpmiddelen/IAMA/)
  * [Handreiking non-discriminatie by design](https://www.rijksoverheid.nl/documenten/rapporten/2021/06/10/handreiking-non-discriminatie-by-design)
  * Norm: ["Artificial intelligence - Data quality for analytics and machine learning (ML) - Part 2: Data quality measures"](https://www.nen.nl/iso-iec-5259-2-2024-en-331171)

## Voorbeelden

Voorbeeld: Gemeente Rotterdam - Avola

In de Gemeente Rotterdam wordt gebruik gemaakt van een ondersteunend advies algoritme voor een toetsing voor recht op een uitkering, Avola. Dit algoritme maakt gebruik van beslisregels gebaseerd op wet- en regelgeving waarmee een advies aan een consulent van Werk en Inkomen gegeven wordt. De data waarop dit advies gebaseerd is, wordt gedeeltelijk door de burger zelf aangeleverd.

In het rapport van de Rekenkamer Rotterdam “Kleur bekennen” wordt aangegeven dat er bij het gebruik van Avola ook aandacht is voor de kwaliteit van de gebruikte data. Deze data wordt tijdens het aanvraagproces gecontroleerd door zowel de burger als consulent. Hierbij wordt op onjuistheden getoetst voordat de data gebruikt wordt. Dit zou verder verbeterd kunnen worden door duidelijk aan te geven hoe de gegevens worden gecontroleerd.

Bron: [Kleur bekennen](https://rekenkamer.rotterdam.nl/onderzoeken/kleur-bekennen/)

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

20 februari 2025 23 september 2024

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
