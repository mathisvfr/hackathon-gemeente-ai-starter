---
title: Controleer regelmatig of het algoritme voldoet aan alle wetten en regels en het eigen beleid - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-05-vertaling-wetgeving-naar-systeem/index.html
scraped_at: 2025-06-12T10:34:47.726082
---

# Controleer regelmatig of het algoritme voldoet aan alle wetten en regels en het eigen beleid - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-05-vertaling-wetgeving-naar-systeem/index.html

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

# Controleer regelmatig of het algoritme voldoet aan alle wetten en regels en het eigen beleid

[]( "Vereiste ID")ver-05[](../../../levenscyclus/ "Levencyclus")[Verificatie en validatie](../../../levenscyclus/verificatie-en-validatie/)[](../../../levenscyclus/ "Levencyclus")[Monitoring en beheer](../../../levenscyclus/monitoring-en-beheer/)[](../../../rollen/ "Rollen")[Jurist](../../../rollen/jurist/)[](../../../onderwerpen/ "Onderwerp")[Governance](../../../onderwerpen/governance/)[](../../../onderwerpen/ "Onderwerp")[Transparantie](../../../onderwerpen/transparantie/)

## Maatregel

Stel regelmatig vast dat wetgeving en (lokaal) beleid correct is vertaald naar de uitvoering van het te ondersteunen werkproces en de onderliggende systemen.

## Toelichting

  * Systemen die overheidsorganisaties inzetten voor bijvoorbeeld het verlenen van subsidies, vergunningen of bijstandsuitkeringen moeten de regels en processtappen volgen die in wetgeving zijn voorgeschreven.
  * Er is een vertaling nodig van deze regels en processtappen naar de uitvoering van het werkproces, het datagebruik en onderliggende systemen.
  * Algoritmes moeten ook voldoen aan deze regels en processtappen.
  * Als algoritmes worden ontwikkeld, moet worden onderzocht wat deze regels zijn en hoe deze moeten worden toegepast bij het ontwikkelen van algoritmes.
  * Het moeten voldoen aan wetgeving en beleid kan dus in zekere zin 'begrenzend' werken op wat mag worden gedaan met algoritmes. Dit is mede afhankelijk van de risico classificatie van de specifieke toepassing.
  * Voor algoritmes, bijvoorbeeld regelgebaseerde rekenregels, moet bijvoorbeeld nauwkeurig worden geprogrammeerd in welke gevallen welke bedragen moeten worden uitgekeerd voor een bijstandsuitkering.
  * Voor machine learning algoritmes moet bijvoorbeeld worden vastgesteld of de trainingsdata wel tot stand is gekomen in lijn met wetgeving en vastgesteld beleid (datakwaliteit) en welke verbanden en patronen (inputvariabelen) al dan niet passend zijn bij het ondersteunen van wettelijke taken.

  * Er is een multidisciplinaire samenwerking nodig tussen de proceseigenaar, gebruikers, juristen, informatieanalisten en ontwikkelaar om deze vertaling zorgvuldig en doorlopend te maken.

  * Voorafgaand aan het (laten) ontwikkelen van een algoritme moet dit zijn uitgevoerd.
  * De toegepaste 'business rules' en de verwerkte data voor de uitvoering van het te ondersteunen werkproces met algoritmes moeten worden onderzocht en beoordeeld.
  * Diepgaande procesanalyses (bijv. BPMN niveau Analytisch) en procesbeschrijvingen kunnen hierbij ondersteunen.
  * Als blijkt dat een werkproces niet (meer) conform (gewijzigde) wetgeving of beleid wordt uitgevoerd, dan moet worden beoordeeld of de verworven data of welke deel van de data geschikt is voor het ontwikkelen een algoritme.
  * Het is dan raadzaam om de uitvoering van het betreffende werkproces en de werking van onderliggende systemen eerst te 'herstellen' en om hiermee een nieuw datafundament te creëeren (eerst een groot aantal zaken behandelen) die later als trainingsdata kan worden gebruikt.

## Risico

Een beslissing of besluit wordt niet conform wetgeving genomen en is daarmee onrechtmatig als er geen goede vertaling wordt gemaakt van wetgeving naar het algoritme.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[awb-01 - Organisaties die algoritmes gebruiken voor publieke taken nemen besluiten zorgvuldig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/awb-01-zorgvuldigheidsbeginsel/)
[aia-08 - Hoog-risico-AI-systemen zijn op een transparante manier ontwikkeld en ontworpen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-08-transparantie-aan-gebruiksverantwoordelijken/)
[awb-02 - Organisaties kunnen duidelijk uitleggen waarom en hoe algoritmes leiden tot een besluit](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/awb-02-motiveringsbeginsel/)
[aia-05 - Datasets voor hoog-risico-AI-systemen voldoen aan kwaliteitscriteria](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-05-data-kwaliteitscriteria/)

## Bronnen

  * [Wetsanalyse](https://wendbarewetsuitvoering.pleio.nl/page/view/918f9a63-4383-410e-b526-4b8fb67b1c40/het-boek-wetsanalyse)
  * [Onderzoekskader Auditdienst Rijk, DM.15](https://www.rijksoverheid.nl/documenten/rapporten/2023/07/11/onderzoekskader-algoritmes-adr-2023)
  * [Toetsingskader Algoritmes Algemene Rekenkamer, 2.05](https://www.rekenkamer.nl/onderwerpen/algoritmes/documenten/publicaties/2024/05/15/het-toetsingskader-aan-de-slag)

## Voorbeelden

Belastingdienst – Handleiding Wetsanalyse in de praktijk

Bij de Belastingdienst is een team dat zich focust op de verdere ontwikkeling van Wendbare Wetsuitvoering. Hieronder valt onder andere de handleiding "Wetsanalyse in de praktijk". In dit document staat hoe de vertaling van wetgeving naar inrichting van de uitvoeringspraktijk gedaan kan worden. Hierin wordt ook tastbaar gemaakt waarom dit nodig is aan de hand van een aantal voorbeelden.

In het eerste inhoudelijke hoofdstuk wordt toegelicht wat wetsanalyse inhoudt aan de hand van karakteristieken. In het tweede hoofdstuk worden de daadwerkelijke handelingen verder uitgelegd.

Bron: [Handleiding Wetsanalyse in de praktijk - Wendbare wetsuitvoering](https://wendbarewetsuitvoering.pleio.nl/page/view/41f08520-3910-4691-a982-f355e199f011/handleiding-wetsanalyse-in-de-praktijk)

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

19 februari 2025 14 augustus 2024

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
