---
title: Identificeer en implementeer technische interventies die robuustheid vergroten - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-33-technische-interventies-robuustheid/index.html
scraped_at: 2025-06-12T10:34:08.166816
---

# Identificeer en implementeer technische interventies die robuustheid vergroten - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-33-technische-interventies-robuustheid/index.html

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

# Identificeer en implementeer technische interventies die robuustheid vergroten

[]( "Vereiste ID")owp-33[](../../../levenscyclus/ "Levencyclus")[Ontwerp](../../../levenscyclus/ontwerp/)[](../../../levenscyclus/ "Levencyclus")[Ontwikkelen](../../../levenscyclus/ontwikkelen/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)

## Maatregel

Bepaal in het ontwerp welke technische interventies bijdragen aan de [robuustheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/#wat-is-technisch-robuust-en-veilig) van het algoritme. Deze keuzes moeten in lijn zijn met het [beoogde doel](../1-pba-02-formuleren-doelstelling/) en de context.

## Toelichting

Maak in de ontwerpfase de volgende afwegingen:

  * **Identificeer en implementeer technische interventies die de robuustheid vergroten**

In het ontwerp en in de training kunnen extra interventies worden genomen die de robuustheid vergroten. Dit kan op verschillende niveaus. Denk bijvoorbeeld aan:

    * _Data Augmentation_ : op data niveau kan de dataset uitgebreid worden met variaties op de oorspronkelijke data, bijvoorbeeld door het toevoegen van extra ruis aan de dataset;
    * _Regularisatie_ : tijdens training kunnen interventies worden gebruikt die overfitting voorkomen zoals _dropout_ of _weight decay_.
    * _[Cross-validation](../3-dat-07-training-validatie-en-testdata/#k-fold-cross-validation)_ : tijdens training kunnen meerdere combinaties van train- en testsets gebruikt worden om generalisatie te waarborgen.
    * _Model ensembles_ : er kunnen meerdere modellen gecombineerd worden om samen een beslissing te maken, dit minimaliseert de impact van een fout van één model.
    * _Adversarial training_ : het trainen met speciale voorbeelden die bedoeld zijn om het model te misleiden.
    * Ook zijn er andere methoden die generalisatie kunnen verbeteren, zoals _invariant risk minimization_ , _robust optimization_ , _transfer learning_ en _causal learning_.
  * **Bepaal de factoren waarop je interventies voor robuustheid beoordeelt** Afhankelijk van de context, verschillen de factoren waarop je deze afwegingen maakt. Denk aan complexiteit van de data, invoerdata en resultaten, [risico en impact als het fout gaat](../2-owp-06-impactanalyse/), belang van [betrouwbaarheid versus nauwkeurigheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/#wat-is-technisch-robuust-en-veilig), of belang van robuustheid versus transparantie.

  * **Leg de beargumenteerde keuze vast** Leg vast welke keuzes er gemaakt zijn en waarom deze keuzes zijn gemaakt.

## Risico

Wanneer robuustheid niet in het ontwerp wordt meegenomen, kan er voor een model worden gekozen waar het niet mogelijk is robuustheid voldoende te waarborgen. Het model wordt dan ofwel ingezet met de risico’s van dien of de innovatie moet later stop gezet worden.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[aia-06 - Hoog-risico-AI-systemen zijn voorzien van voldoende technische documentatie](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-06-technische-documentatie/)

## Bronnen

  * [Kenniscentrum Data & Maatschappij, Ethisch principe 2: technische robuustheid en veiligheid](https://data-en-maatschappij.ai/publicaties/ethisch-principe-2-technische-robuustheid-en-veiligheid)
  * [Europese Commissie, Ethische richtsnoeren voor betrouwbare KI](https://digital-strategy.ec.europa.eu/nl/library/ethics-guidelines-trustworthy-ai)
  * [A. Tocchetti et al., A.I. Robustness: a Human-Centered Perspective on Technological Challenges and Opportunities](https://arxiv.org/abs/2210.08906)

## Voorbeelden

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

17 februari 2025 19 december 2024

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
