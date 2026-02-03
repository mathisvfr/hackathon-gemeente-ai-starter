---
title: Doe aselecte steekproeven om algoritmes met 'risicogestuurde selectie’ te controleren - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-02-aselecte-steekproeven/index.html
scraped_at: 2025-06-12T10:34:51.403277
---

# Doe aselecte steekproeven om algoritmes met 'risicogestuurde selectie’ te controleren - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-02-aselecte-steekproeven/index.html

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

# Doe aselecte steekproeven om algoritmes met 'risicogestuurde selectie’ te controleren

[]( "Vereiste ID")imp-02[](../../../levenscyclus/ "Levencyclus")[Dataverkenning en datapreparatie](../../../levenscyclus/dataverkenning-en-datapreparatie/)[](../../../levenscyclus/ "Levencyclus")[Implementatie](../../../levenscyclus/implementatie/)[](../../../levenscyclus/ "Levencyclus")[Monitoring en beheer](../../../levenscyclus/monitoring-en-beheer/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Bias en non discriminatie](../../../onderwerpen/bias-en-non-discriminatie/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)

## Maatregel

Uitvoeren van aselecte steekproeven als aanvulling wanneer gebruik gemaakt wordt van risicogestuurde selectie.

## Toelichting

Aselecte steekproeven kunnen een waardevolle toevoeging zijn bij risicogestuurde selectie.

Het toevoegen van aselecte steekproeven maakt het mogelijk om over tijd te beoordelen of het algoritme nog voldoende effectief is. Populaties veranderen immers over tijd. Een selectie die het meest effectief was bij ingebruikname kan over tijd dat niet meer zijn. Door alleen risicogestuurd te selecteren wordt dit niet inzichtelijk, omdat bepaalde groepen zelden tot nooit gecontroleerd worden. Door de aanvullende mogelijkheid van monitoring, kan over tijd beoordeeld worden of er nog steeds sprake is van de meest proportionele vorm. Als dat niet zo is, kan bijvoorbeeld gekozen worden voor aanpassing van de risicogestuurde selectie of overgaan op volledig aselect.

De maatregel gaat daarmee niet direct discriminatie tegen, omdat er sprake kan zijn van discriminatie ongeacht de effectiviteit van de risicogestuurde selectie. Een lagere effectiviteit maakt het echter lastiger het gemaakte onderscheid te rechtvaardigen.

Het gebruik van een aselecte steekproef is in veel gevallen essentieel om het systeem te kunnen toetsen op vooringenomenheid. Een aselecte steekproef geeft ook inzicht in een deel van de populatie dat doorgaans niet geselecteerd en behandeld wordt door het betreffende risicogestuurde algoritme. Dit maakt het mogelijk om te toetsen of er sprake is van een over- of ondervertegenwoordiging van bepaalde groepen, of om te bepalen of bepaalde typen fouten vaker gemaakt worden in bepaalde groepen.

Bij AI-systemen die verder leren op basis van verkregen data kan daarnaast sprake zijn van een reinforcing feedbackloop, omdat zij geen representatieve data krijgen. Het toevoegen van aselecte steekproeven kan deze feedbackloop doorbreken.

Het is aan te bevelen om, waar mogelijk, behandelaars niet in te lichten of een casus toegewezen is op basis van een risicogestuurd of aselecte selectie. Daardoor wordt beperkt dat een behandelaar met tunnelvisie een zaak bekijkt. De behandelaar weet immers dat er tussen de selecties zaken zitten waar niet sprake is van verhoogd risico. Op die manier kan automation bias beperkt te worden. Niet in alle gevallen zal dit mogelijk zijn, omdat de behandelaar ook uit andere aangeleverde gegevens kan halen op basis waarvan een casus geselecteerd is. Het is dan van belang om op andere wijze de tunnelvisie tegen te gaan.

De precieze inzet van aselecte steekproeven zal afhangen van de context. Zo verschilt het per context hoeveel zaken aselect geselecteerd moeten worden. Bepaal welke groepen er precies vergeleken dienen te worden en bepaal aan de hand daarvan een passende steekproefgrootte zodanig dat er gesproken kan worden over statistische significantie.

In sommige gevallen zal de impact van een selectie ook dusdanig zijn dat het zich niet leent voor aselecte steekproef. Zo kan een aselecte steekproef wel de basis zijn voor bureauonderzoek, maar mogelijk niet als enige basis voor een huisbezoek. Deze belangenenafweging moet per context gemaakt worden.

## Risico

  * Historical bias
  * Representation bias
  * Automation bias en Reinforcing Feedback Loop

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[aia-27 - Hoog-risico-AI-systemen voor publieke taken worden beoordeeld op gevolgen voor grondrechten](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-27-beoordelen-gevolgen-grondrechten/)
[grw-02 - Algoritmes discrimineren niet](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/grw-02-non-discriminatie/)
[aia-10 - Hoog-risico-AI-systemen zijn voldoende nauwkeurig, robuust en cyberveilig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-10-nauwkeurigheid-robuustheid-cyberbeveiliging/)

## Bronnen

[Rapportage Algoritmerisico's Nederland voorjaar 2024 (pp. 36-41)](https://www.autoriteitpersoonsgegevens.nl/documenten/rapportage-ai-algoritmerisicos-nederland-ran-voorjaar-2024)

## Voorbeelden

Algorithm Audit: analyse Controle Uitwonendenbeurs

Stichting Algorithm Audit heeft de risicoprofilering in het Controle Uitwonendenbeurs-proces (CUB-proces) onderzocht op verzoek van Dienst Uitvoering Onderwijs (DUO). DUO heeft tussen 2010 en 2023 gebruik gemaakt van een risicoprofiel voor het tegengaan van onrechtmatig gebruik van de uitwonendenbeurs. Dit is in 2023 in opspraak geraakt en DUO heeft Algorithm Audit verzocht hier verder onderzoek naar te doen. Tijdens de kwantitatieve analyse heeft Algorithm Audit gewerkt aan de hand van aselecte steekproeven. Aan de hand van deze data hebben ze verschillende deelvragen beantwoord en blijkt dat tussen een aantal selectiecriteria onvoldoende statistisch verband gebleken is. Door middel van de aselecte steekproef blijkt hierdoor dat de selectie(criteria) aangepast moet(en) worden.

Bron: [Algorithm Audit: analyse Controle Uitwonendenbeurs](https://algorithmaudit.eu/nl/algoprudence/cases/aa202401_preventing-prejudice/)

Rijksdienst voor Ondernemend Nederland: Risicocontrole Subsidieaanvragen

De Rijksdienst voor Ondernemend Nederland (RVO) maakt gebruik van een algoritme bij het behandelen van subsidieaanvragen. Hierbij wordt bij iedere aanvraag een risico-indicatie gemaakt op basis van een aantal regels. Als er volgens het algoritme geen risico’s zijn wordt de aanvraag automatisch aangemaakt, zo niet wordt de aanvraag nog beoordeeld door een adviseur.

Daarnaast wordt het algoritme gecontroleerd aan de hand van een steekproef. Op deze manier wordt getest of het algoritme tot de juiste conclusie is gekomen of aangescherpt moet worden. Mocht door de steekproef blijken dat het algoritme niet goed werkt geeft de RVO ook aan dat de keuze gemaakt kan worden om het algoritme niet te gebruiken. Op deze manier wordt aan de hand van steekproeven gecontroleerd dat het algoritme naar behoren werkt.

Bron: [Rijksdienst voor Ondernemend Nederland: Risicocontrole Subsidieaanvragen](https://algoritmes.overheid.nl/nl/algoritme/risicocontrole-sde-subsidieaanvragen-rijksdienst-voor-ondernemend-nederland/51892728#verantwoordGebruik)

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl).

20 februari 2025 13 augustus 2024

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
