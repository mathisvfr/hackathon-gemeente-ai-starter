---
title: Beperk de omvang van datasets voor energie-efficiëntie - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-09-dataminimalisatie/index.html
scraped_at: 2025-06-12T10:34:23.691012
---

# Beperk de omvang van datasets voor energie-efficiëntie - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-09-dataminimalisatie/index.html

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
    * Technieken voor dataminimalisatie
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Beperk de omvang van datasets voor energie-efficiëntie

[]( "Vereiste ID")dat-09[](../../../levenscyclus/ "Levencyclus")[Dataverkenning en datapreparatie](../../../levenscyclus/dataverkenning-en-datapreparatie/)[](../../../levenscyclus/ "Levencyclus")[Ontwikkelen](../../../levenscyclus/ontwikkelen/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../onderwerpen/ "Onderwerp")[Data](../../../onderwerpen/data/)[](../../../onderwerpen/ "Onderwerp")[Duurzaamheid](../../../onderwerpen/duurzaamheid/)

## Maatregel

Houd datasets beperkt tot het noodzakelijke en voldoende specifiek om onnodige energieconsumptie te voorkomen tijdens de verwerking en opslag van data voor algoritmes. We noemen dit ook wel dataminimalisatie.

## Toelichting

Hoe meer je bewaart, hoe meer ruimte dat kost om op te slaan. Bovendien verbruikt elk apparaat dat nodig is om data op te slaan stroom. Dat heeft grote invloed op de CO₂-uitstoot van een datacentrum. Grote datasets brengen daarom hoge energie- en opslagkosten met zich mee. Door de dataset bewust te beperken tot relevante gegevens, kun je ook de energie-efficiëntie van algoritmes aanzienlijk verbeteren. Vooral bij de ontwikkeling van AI-systemen kan het verminderen van data bijdragen aan lagere energiebehoeften en CO₂-uitstoot.

### Technieken voor dataminimalisatie

  * **Slimme selectie van trainingdata** : Gebruik methoden die irrelevante data uit de dataset filteren, zoals dataselectie-algoritmes en sampling-technieken. Door te focussen op relevante data, beperk je de omvang zonder de prestaties van het model te beïnvloeden.
  * **Verwijderen van redundante en dubbele data** : Deduplicatie van data minimaliseert onnodige verwerkingskracht. Door alleen unieke en relevante gegevens op te slaan, wordt de opslagbehoefte verder beperkt.
  * **Opschonen en archiveren van verouderde data** : [Regelmatige archivering](../2-owp-09-archiveren-documenten/) of verwijdering van verouderde data in je dataset zorgt voor een verminderde voetafdruk en verhoogt ook de efficiëntie.

## Risico

Zonder dataminimalisatie loopt je organisatie het risico op onnodig hoge energie- en opslagkosten, en een grotere ecologische impact.

## Bijbehorende vereiste(n)

Bekijk alle vereisten

Geen vereisten beschikbaar voor deze maatregel.

## Bronnen

  * [Onderzoekskader Auditdienst Rijk, PRI.5](https://www.rijksoverheid.nl/documenten/rapporten/2023/07/11/onderzoekskader-algoritmes-adr-2023)
  * [Toetsingskader Algoritmes Algemene Rekenkamer, 2.20](https://www.rekenkamer.nl/onderwerpen/algoritmes/documenten/publicaties/2024/05/15/het-toetsingskader-aan-de-slag)
  * [Rijks ICT-dashboard](https://www.rijksictdashboard.nl/duurzaamheid)
  * [Sustainable artificial intelligence – TU Delft](https://www.tudelft.nl/en/stories/articles/sustainable-artificial-intelligence-from-chatgpt-to-green-ai)

## Voorbeelden

Basisregistratie Personen: Dataminimalisatie

De Basisregistratie Personen (BRP) heeft in 2023 een experiment uitgevoerd rondom dataminimalisatie. BRP-gegevens zoals naam en geslacht werden vertaald naar direct bruikbare informatie zoals aanschrijfnaam. Op deze manier werd informatie op een efficiëntere manier doorgegeven. Het experiment van BRP is een indirecte vorm van energie-efficiëntie omdat er minder (onnodige) data verstrekt wordt aan de aanvrager. Hierdoor hoeft de aanvrager minder data op te slaan en te verwerken.

Bron: [Experimentbesluit BRP dataminimalisatie](https://www.internetconsultatie.nl/experimentbesluitbrp/b1)

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

18 februari 2025 12 november 2024

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
