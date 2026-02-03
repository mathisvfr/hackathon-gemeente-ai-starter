---
title: Pas uitlegbaarheidstechnieken toe en evalueer en valideer deze - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-32-toepassen-uitlegbaarheidstechnieken/index.html
scraped_at: 2025-06-12T10:34:06.966192
---

# Pas uitlegbaarheidstechnieken toe en evalueer en valideer deze - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-32-toepassen-uitlegbaarheidstechnieken/index.html

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
    * Gebruik uitlegbaarheid bij besluiten
    * Generatieve AI
    * Beperkingen en veiligheid
    * Evaluatie en validatie
  * Risico
  * Bijbehorende vereiste(n)
  * Bronnen
  * Voorbeelden

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Maatregelen  ](../)

# Pas uitlegbaarheidstechnieken toe en evalueer en valideer deze

[]( "Vereiste ID")owp-32[](../../../levenscyclus/ "Levencyclus")[Ontwerp](../../../levenscyclus/ontwerp/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../rollen/ "Rollen")[Beleid en advies](../../../rollen/beleid-en-advies/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Transparantie](../../../onderwerpen/transparantie/)

## Maatregel

Pas uitlegbaarheidstechnieken toe en evalueer en valideer deze.

## Toelichting

Uitlegbaarheidstechnieken helpen om de werking van een algoritme transparant te maken. De keuze voor het type algoritme bepaalt hoe transparant je kunt zijn. Van rekenregels kun je namelijk precies uitleggen hoe deze tot een beslissing komen. Aan de andere kant kunnen complexe AI-systemen een black box zijn. Het is dan onduidelijk hoe deze systemen beslissingen maken.

Afhankelijk van het type algoritme zijn er uitlegbaarheidstechnieken beschikbaar om de werking en keuzes van een algoritme bloot te leggen. Er moet eerst een keuze worden gemaakt welk type algoritme geschikt is gezien de [informatiebehoefte](../2-owp-30-informeer-betrokkenen/). Het is belangrijk om samen met de betrokken partijen vast te leggen welke uitlegbaarheidstechnieken moeten worden toegepast. Bij bronnen kan informatie worden geraadpleegd die helpen bij het vinden van de juiste methodiek.

### Gebruik uitlegbaarheid bij besluiten

Onderzoek hoe uitlegbaarheidstechnieken kunnen bijdragen aan het motiveren van besluiten. Dit kan bijvoorbeeld door:

  * De output van het algoritme te koppelen aan het zaakdossier, met een toelichting op de interpretatie van die output.
  * De output of een samenvatting hiervan op te nemen in de beschikking.

### Generatieve AI

Bij gebruik van generatieve AI is het haast onmogelijk om direct uitlegbaar te maken hoe een uitkomst tot stand is gekomen. Om toch (deels) uitleg te kunnen geven over de werking van een generatief AI-model kun je uitleg verschaffen over de capaciteiten, beperkingen en trainingsdata van het AI-model. Daarnaast is het verstanding om te onderzoeken wat de risico's zijn als de uitkomsten van een generatief AI-systeem niet uitgelegd kunnen worden.

### Beperkingen en veiligheid

Vanuit veiligheidsoverwegingen kan bij specifieke algoritmes besloten worden om bepaalde informatie over de werking van een algoritme niet aan iedereen vrij te geven. Denk hierbij aan de beperkingen die de [Wet Open Overheid](../../vereisten/woo-01-recht-op-toegang-tot-publieke-informatie/) oplegt. Houd ook rekening met mogelijke risico’s op aanvallen die kunnen ontstaan door het gebruik van uitlegbaarheidstechnieken, zoals omschreven in: A Survey of Privacy-Preserving Model Explanations: Privacy Risks, Attacks, and Countermeasures.

### Evaluatie en validatie

Evalueer de uitlegbaarheid van het systeem op functionele, operationele, bruikbaarheids- en veiligheidsvereisten in samenwerking met betrokkenen zoals gebruikers. Valideer of de uitkomst van het algoritme begrijpelijk genoeg is voor een gebruiker om hier op een verantwoorde wijze mee te werken.

## Risico

Als er geen rekening wordt gehouden met de uitlegbaarheid van een algoritme binnen een bepaalde context ontstaat het risico dat de output van het algoritme niet wordt begrepen of verkeerd wordt geïnterpreteerd, wat kan leiden tot onjuist gebruik.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[aia-08 - Hoog-risico-AI-systemen zijn op een transparante manier ontwikkeld en ontworpen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-08-transparantie-aan-gebruiksverantwoordelijken/)
[aia-26 - Mensen over wie besluiten worden genomen door een hoog-risico-AI-systemen, krijgen op verzoek informatie over deze besluiten](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-26-recht-op-uitleg-ai-besluiten/)
[awb-02 - Organisaties kunnen duidelijk uitleggen waarom en hoe algoritmes leiden tot een besluit](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/awb-02-motiveringsbeginsel/)

## Bronnen

  * [Onderzoekskader Auditdienst Rijk, DM.11](https://www.rijksoverheid.nl/documenten/rapporten/2023/07/11/onderzoekskader-algoritmes-adr-2023)
  * [Toetsingskader Algoritmes, Algemene Rekenkamder, 2.04](https://www.rekenkamer.nl/onderwerpen/algoritmes/documenten/publicaties/2024/05/15/het-toetsingskader-aan-de-slag)
  * [Toolkit voor implementatie](https://xaitk.org/)
  * [An introduction to explainable AI with Shapley values](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html)
  * [Benchmarking eXplainable AI - A Survey on Available Toolkits and Open Challenges](https://www.ijcai.org/proceedings/2023/747)
  * [UXAI: Design Strategy](https://www.uxai.design/design-strategy)
  * [Overzicht (evaluatie van) metrieken XAI](https://dl.acm.org/doi/pdf/10.1145/3583558)
  * [Part 2: Explaining AI in practice | ICO](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/explaining-decisions-made-with-artificial-intelligence/part-2-explaining-ai-in-practice/)
  * [A Survey of Privacy-Preserving Model Explanations: Privacy Risks, Attacks, and Countermeasures](https://arxiv.org/abs/2404.00673)
  * [Towards Transparency by Design for Artificial Intelligence, Science and Engineering Ethics](https://link.springer.com/article/10.1007/s11948-020-00276-4)
  * [From Anecdotal Evidence to Quantitative Evaluation Methods: A Systematic Review on Evaluating Explainable AI](https://dl.acm.org/doi/pdf/10.1145/3583558)

## Voorbeelden

Gemeente Amsterdam - Slimme check levensonderhoud

Gemeente Amsterdam heeft in een pilot gebruik gemaakt van een algoritme dat medewerkers helpt om te bepalen of een aanvraag levensonderhoud onderzoekswaardig is. De gemeente heeft ook een document waarin wordt toegelicht hoe verwerkte data gebruikt wordt. Dit is gedaan aan de hand van bijvoorbeeld een belangrijkheids-score per kenmerk. Op deze manier wordt inzichtelijk en uitlegbaar wat de invloed is van individuele kenmerken.

Bron: [Overzicht Verwerkte Data en Features](https://algoritmeregister.amsterdam.nl/onderzoekswaardigheid-slimme-check-levensonderhoud/#:~:text=Overzicht%20Verwerkte%20Data%20en%20Features.pdf)

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl).

22 april 2025 3 december 2024

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
