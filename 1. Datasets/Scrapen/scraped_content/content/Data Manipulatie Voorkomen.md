---
title: Controleer de data op manipulatie en ongewenste afhankelijkheden - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-10-datamanipulatie/index.html
scraped_at: 2025-06-12T10:34:24.887307
---

# Controleer de data op manipulatie en ongewenste afhankelijkheden - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-10-datamanipulatie/index.html

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
    * Adversarial training
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Controleer de data op manipulatie en ongewenste afhankelijkheden

[]( "Vereiste ID")dat-10[](../../../levenscyclus/ "Levencyclus")[Dataverkenning en datapreparatie](../../../levenscyclus/dataverkenning-en-datapreparatie/)[](../../../levenscyclus/ "Levencyclus")[Monitoring en beheer](../../../levenscyclus/monitoring-en-beheer/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../rollen/ "Rollen")[Beleid en advies](../../../rollen/beleid-en-advies/)[](../../../onderwerpen/ "Onderwerp")[Data](../../../onderwerpen/data/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)

## Maatregel

De dataset die gebruikt wordt om een model te (her)trainen moet periodiek gecontroleerd worden op manipulatie (data poisoning). Voorkom ongewenste afhankelijkheden.

## Toelichting

Manipulatie van data wordt een “data poisoning” aanval genoemd 1 2 3. Een kwaadwillende kan op verschillende manieren te werk gaan:

  * Bewust verkeerde informatie aan de dataset toevoegen. Dit is bijvoorbeeld mogelijk door als aanvaller zelf een foutieve dataset beschikbaar te stellen. Controleer daarom goed of een afgenomen dataset de kenmerken heeft die je verwacht. Daarnaast kun je ook nog verifiëren of bijvoorbeeld het proces waarmee de dataset vergaard is op de juiste manier is uitgevoerd. Tot slot is het verstandig om te voorkomen dat de dataset afhankelijk is van een enkele bron.
  * Een aanvaller kan een bestaande dataset aanpassen, door bijvoorbeeld labels om te draaien. In dit geval moet een aanvaller toegang krijgen tot de locatie van de dataset. Bescherming hiertegen begint met algemene beveiligingsmaatregelen, bijvoorbeeld zoals beschreven in de [BIO](../../hulpmiddelen/BIO/). Daarnaast moet er ook gekeken worden naar het voorkomen van een insider aanval. Dit kan door selectief te zijn in het verlenen van toegang tot de locatie van de data en bijvoorbeeld het toepassen van een vier-ogen principe.
  * In lijn met het aanpassen van de dataset kan een aanvaller ook een deel van de dataset verwijderen. Dit is naar verwachting makkelijker te realiseren dan het selectief aanpassen van de data. Door bijvoorbeeld alle data over een bepaalde groep personen uit de dataset te verwijderen functioneert het model minder goed voor die groep. Controleer daarom of de dataset waarmee uiteindelijk getraind wordt precies hetzelfde is als de origineel bedoelde data. Dit kan bijvoorbeeld door middel van een handtekening die geverifieerd moet worden.

Op deze manieren kan een aanvaller een model slecht laten functioneren, of alleen fouten laten maken op specifiek gekozen invoerwaarden. Een aanvaller kan de trainingsdata zo beïnvloeden dat nummerborden met een stip altijd foutief gelezen worden, waardoor criminelen kentekencontroles kunnen ontwijken. In dit geval wordt ook wel gesproken over een [“backdoor” aanval](../4-owk-09-adversarial-aanvallen/#backdoor).

### Adversarial training

Daarnaast kan het principe van [adversarial training](https://arxiv.org/abs/1611.01236) worden toegepast door zelf bewust foutieve invoerwaarden aan de trainingsdata toe te voegen. Door een algoritme hierop te laten trainen kan deze beter bestand gemaakt worden tegen aanvallen tijdens het gebruik.

## Risico

Een aanvaller kan proberen om de trainingset te manipuleren om het uiteindelijke model doelbewust fouten te laten maken. Dit kan leiden tot verkeerde antwoorden, vooroordelen of zelfs kwetsbaarheden in het model.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[aia-10 - Hoog-risico-AI-systemen zijn voldoende nauwkeurig, robuust en cyberveilig](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-10-nauwkeurigheid-robuustheid-cyberbeveiliging/)
[aia-22 - De werking van hoog-risico-AI-systemen wordt gemonitord](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-22-gebruiksverantwoordelijken-monitoren-werking/)
[aia-32 - AI-modellen voor algemene doeleinden met systeemrisico’s zijn voldoende beveiligd tegen cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-32-ai-modellen-algemene-doeleinden-systeemrisico-cyberbeveiliging/)
[bio-01 - Computersystemen zijn voldoende beveiligd tegen ongelukken en cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/bio-01-beveiliging-informatie-en-informatiesystemen/)
[avg-12 - Data zoals persoonsgegevens zijn voldoende beveiligd tegen ongelukken en cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/avg-12-beveiliging-van-verwerking/)

## Bronnen

  * [Crowdstrike, Data Poisoning: The Exploitation of Generative AI](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/data-poisoning/)
  * [TNO, Ministerie van Justitie en Veiligheid, Verkenning van het raakvlak van cybersecurity en AI](https://www.rijksoverheid.nl/onderwerpen/terrorismebestrijding/documenten/rapporten/2024/10/28/tk-bijlage-4-tno-2024-r10768-verkenning-van-het-raakvlak-van-cybersecurity-en-ai)
  * [AIVD, AI-systemen: ontwikkel ze veilig](https://www.aivd.nl/documenten/publicaties/2023/02/15/ai-systemen-ontwikkel-ze-veilig#:~:text=Steeds%20meer%20computersystemen%20maken%20gebruik,organisaties%20zich%20hiertegen%20kunnen%20verdedigen)
  * [Kurakin, et al., Adversarial Machine Learning at Scale](https://arxiv.org/abs/1611.01236)

## Voorbeelden

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

* * *

  1. [Crowdstrike, Data Poisoning: The Exploitation of Generative AI](https://www.crowdstrike.com/en-us/cybersecurity-101/cyberattacks/data-poisoning/) ↩

  2. [Ministerie van Justitie en Veiligheid, Verkenning van het raakvlak van cybersecurity en AI](https://www.rijksoverheid.nl/onderwerpen/terrorismebestrijding/documenten/rapporten/2024/10/28/tk-bijlage-4-tno-2024-r10768-verkenning-van-het-raakvlak-van-cybersecurity-en-ai) ↩

  3. [AIVD, AI-systemen: ontwikkel ze veilig](https://www.aivd.nl/documenten/publicaties/2023/02/15/ai-systemen-ontwikkel-ze-veilig#:~:text=Steeds%20meer%20computersystemen%20maken%20gebruik,organisaties%20zich%20hiertegen%20kunnen%20verdedigen) ↩

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
  *validatiedata: data die worden gebruikt voor het verrichten van een evaluatie van het getrainde AI-systeem en voor het afstemmen van onder andere de niet-leerbare parameters en het leerproces ervan, om underfitting of overfitting te voorkomen
