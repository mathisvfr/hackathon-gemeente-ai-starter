---
title: Evalueer de betrouwbaarheid van het algoritme - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-06-evalueer-betrouwbaarheid/index.html
scraped_at: 2025-06-12T10:34:49.003530
---

# Evalueer de betrouwbaarheid van het algoritme - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-06-evalueer-betrouwbaarheid/index.html

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
    * Bepaal methodes en metrieken
    * Zorg voor een representatieve testset
    * Bepaal welke mate van betrouwbaarheid noodzakelijk is
    * Bepaal interventies voor als het restrisico hoger is dan acceptabel
    * Zorg en controleer of de betrouwbaarheid van een uitkomst wordt meegegeven in de output
    * Zorg voor continue monitoring op betrouwbaarheid
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Evalueer de betrouwbaarheid van het algoritme

[]( "Vereiste ID")ver-06[](../../../levenscyclus/ "Levencyclus")[Ontwikkelen](../../../levenscyclus/ontwikkelen/)[](../../../levenscyclus/ "Levencyclus")[Verificatie en validatie](../../../levenscyclus/verificatie-en-validatie/)[](../../../levenscyclus/ "Levencyclus")[Monitoring en beheer](../../../levenscyclus/monitoring-en-beheer/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)

## Maatregel

Evalueer de betrouwbaarheid van het algoritme door het algoritme te testen op verschillende input en in verschillende situaties.

## Toelichting

De betrouwbaarheid van een algoritme omschrijft of het algoritme in staat is om onder verschillende omstandigheden en met alle mogelijke input tot een correcte uitkomst te komen. In sommige gevallen is het wenselijk om duidelijk aan te geven wat de onzekerheid is van een uitkomst, dat het juiste antwoord niet bepaald kan worden of dat er kans is op fouten.

Om de betrouwbaarheid te evalueren kan je de volgende stappen doorlopen:

  1. Bepaal methodes en metrieken.
  2. Zorg voor een representatieve testset.
  3. Bepaal welke mate van betrouwbaarheid noodzakelijk is.
  4. Bepaal interventies voor als het restrisico hoger is dan acceptabel.
  5. Zorg en controleer of de betrouwbaarheid van een uitkomst wordt meegegeven in de output.

### Bepaal methodes en metrieken

Bepaal met welke methodes je betrouwbaarheid wil evalueren en welke metrieken je daarvoor wilt gebruiken. De metrieken voor prestatie kunnen gelijk zijn aan die van [nauwkeurigheid](../5-ver-02-evalueer-nauwkeurigheid/#metrieken), alleen gaat het om de score hierop in een onbekende situatie. Het testen van betrouwbaarheid kan bijvoorbeeld door precisie of recall te meten onder extreme omstandigheden of met ruis in de data.

Methodes om te testen op betrouwbaarheid

Afhankelijk van het type algoritme zijn er verschillende methodes om betrouwbaarheid te testen. In de literatuur gaat het ook over generalisatie wanneer we spreken over het correct presteren op nieuwe of minder voorkomende inputs en omstandigheden. Hieronder enkele voorbeelden van methoden die gebruikt kunnen worden:

  * De _monkey test_ is een manier om voor willekeurige, invalide of onverwachte inputs de werking van het algoritme te testen. Het idee is om een onvoorspelbare gebruiker (of een script) willekeurige acties te laten uitvoeren om te kijken hoe het systeem erop reageert.
  * Door een _out-of-sample test_ kan worden getest hoe een machine-learning algoritme presteert bij een dataset verdeling die niet in de training is meegegeven.
  * Door _stresstesten_ test je de prestatie van het algoritme onder extreme omstandigheden of ruis in de data.
  * Met synthetische data kunnen goed uitlegbare en controleerbare distributieshifts worden gesimuleerd om te testen of het algoritme in een onbekende situatie, waar geen data van bruikbaar of beschikbaar is, presteert.
  * De [AI Blindspots kaartenset](https://data-en-maatschappij.ai/tools/ai-blindspots-2.0) kan helpen om risico’s voor betrouwbaarheid (en specifiek [bias](../../../onderwerpen/bias-en-non-discriminatie/)) te identificeren.

Pas de methodes en metrieken aan op de ontwerpkeuzes, zoals de context waarin het algoritme gebruikt wordt en het [soort algoritme](../2-owp-05-soort-algoritme/). Onderzoek of er specifieke situaties of omstandigheden zijn waarvan bekend is dat deze kunnen variëren.

Voorbeeld

Analyseer welke veranderingen of wisselingen in de [inputdata](../2-owp-11-gebruikte-data/) er kunnen plaatsvinden. Bijvoorbeeld door economische schommelingen of door veranderingen in gebruikersgedrag. Test of het algoritme goed blijft presteren onder deze omstandigheden.

Voorbeeld

De verdeling van de inputdata kan invloed hebben op de prestaties van een machine-learning algoritme (distributieshift). Test hoe het algoritme presteert onder andere verdelingen van de inputdata.

### Zorg voor een representatieve testset

Zorg dat er een [representatieve testset](../5-ver-04-representatieve-testomgeving/) beschikbaar is waarin het algoritme kan worden getest in verschillende scenario's. Test het algoritme in verschillende omstandigheden:

  * gebruikers
  * omgeving
  * interface
  * verschillende datasets

Test je algoritme op generaliseerbaarheid van de uitkomsten buiten de standaard omgeving.

### Bepaal welke mate van betrouwbaarheid noodzakelijk is

  * Bedenk onder welke variaties het systeem betrouwbaar moet werken en hoe goed het moet kunnen werken onder rand- of uitzonderlijke gevallen.
  * Afhankelijk van de toepassing moeten resultaten altijd dezelfde uitkomst geven of niet ([reproduceerbaarheid](../4-owk-07-reproduceerbaarheid/)). In het geval van generatieve AI hoeft het antwoord bijvoorbeeld niet altijd exact hetzelfde te zijn.
  * Houd hierbij aandacht voor de afweging tussen [nauwkeurigheid](../5-ver-02-evalueer-nauwkeurigheid/) en betrouwbaarheid. Een model met hoge nauwkeurigheid op de testset kan vaak slechter generaliseren naar situaties net buiten de test set (overfitting).

### Bepaal interventies voor als het restrisico hoger is dan acceptabel

Bepaal wat er moet gebeuren wanneer de betrouwbaarheid niet voldoende is. Hiervoor zijn verschillende mogelijkheden:

  * Verder ontwikkelen aan het algoritme en andere maatregelen treffen om het restrisico acceptabel te maken. Bijvoorbeeld door:

    * meer [menselijke controle](../../../onderwerpen/menselijke-controle/) toe te voegen
    * een ander [soort algoritme](../2-owp-05-soort-algoritme/) of [techniek](../2-owp-04-gebruikte-techniek/) te gebruiken.
    * bij machinelearning algoritmes kan je overfitting voorkomen door [verschillende trainingsdatasets en testdatasets te gebruiken](../3-dat-07-training-validatie-en-testdata/), zoals bij [k-fold-cross-validation](../3-dat-07-training-validatie-en-testdata/#k-fold-cross-validation).
    * door (hyper)parameters aan te passen kan het algoritme worden aangepast zodat het beter presteert in verschillende testsituaties.
  * [Te stoppen met de ontwikkeling en/of het gebruik van het systeem](../../../levenscyclus/uitfaseren/).

### Zorg en controleer of de betrouwbaarheid van een uitkomst wordt meegegeven in de output

Voorspellingen of uitkomsten van een algoritme kunnen onzeker zijn. Zorg dat de (on)zekerheid van een uitkomst wordt meegegeven in de output van een algoritme. Dat kan bijvoorbeeld door een foutmarge mee te geven. In veel gevallen kan het wenselijk zijn dat het systeem aangeeft wanneer een uitkomst te onzeker is of soms zelfs geen antwoord geeft vanwege de onzekerheid. Dit kan bijdragen aan het vertrouwen in het algoritme.

### Zorg voor continue monitoring op betrouwbaarheid

Zorg dat het algoritme continu wordt [gemonitored](../../../levenscyclus/monitoring-en-beheer/) op de betrouwbaarheid en de prestaties van het systeem. Maak gebruik van periodieke updates en [valideer regelmatig de kwaliteit van de gebruikte data](../3-dat-01-datakwaliteit/).

## Risico

Een onbetrouwbaar algoritme kan in een nieuwe of onverwachte situatie de verkeerde uitkomsten geven.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[aia-10 - Hoog-risico-AI-systemen zijn voldoende nauwkeurig, robuust en cyberveilig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-10-nauwkeurigheid-robuustheid-cyberbeveiliging/)

## Bronnen

  * [Bo Li, et al., Trustworthy AI: From Principles to Practices](https://arxiv.org/abs/2110.01167)
  * [Pablo Soldati, et al., Design Principles for Model Generalization and Scalable AI Integration in Radio Access Networks](https://arxiv.org/abs/2306.06251v2)
  * [Jiashuo Liu, et al., Towards Out-Of-Distribution Generalization: A Survey](https://arxiv.org/abs/2108.13624)
  * [Kenniscentrum Data & Maatschappij - Tool: AI Blindspots 2.0](https://data-en-maatschappij.ai/tools/ai-blindspots-2.0)
  * [Kaiyang Zhou, et al., Domain Generalization: A Survey](https://ieeexplore.ieee.org/abstract/document/9847099)

## Voorbeelden

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl).

20 februari 2025 19 december 2024

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
