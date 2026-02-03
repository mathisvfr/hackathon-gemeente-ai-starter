---
title: Datasets voor hoog-risico-AI-systemen voldoen aan kwaliteitscriteria - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-05-data-kwaliteitscriteria/index.html
scraped_at: 2025-06-11T13:47:18.464279
---

# Datasets voor hoog-risico-AI-systemen voldoen aan kwaliteitscriteria - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-05-data-kwaliteitscriteria/index.html

---

[ ![Home Algoritmekader](../../../assets/logo.svg) ](../../.. "Algoritmekader 2.2") Algoritmekader 2.2

[ GitHub  ](https://github.com/MinBZK/Algoritmekader "Ga naar repository")

  * [ Soorten algoritmes en AI  ](../../../soorten-algoritmes-en-ai/)
  * [ Onderwerpen  ](../../../onderwerpen/)
  * [ Levenscyclus  ](../../../levenscyclus/)
  * [ Rollen  ](../../../rollen/)
  * [ Voldoen aan wetten en regels  ](../../)

Inhoudsopgave

  * Vereiste
  * Toelichting
  * Bronnen
  * Van toepassing op
  * Risico
  * Maatregelen

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Vereisten  ](../)

# Datasets voor hoog-risico-AI-systemen voldoen aan kwaliteitscriteria

[]( "Vereiste ID")aia-05[](../../../levenscyclus/ "Levencyclus")[Dataverkenning en datapreparatie](../../../levenscyclus/dataverkenning-en-datapreparatie/)[](../../../levenscyclus/ "Levencyclus")[Verificatie en validatie](../../../levenscyclus/verificatie-en-validatie/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Data](../../../onderwerpen/data/)

## Vereiste

AI-systemen met een hoog risico die technieken gebruiken die het trainen van AI-modellen met data omvatten, worden ontwikkeld op basis van datasets voor training, validatie en tests die voldoen aan de kwaliteitscriteria telkens wanneer dergelijke datasets worden gebruikt.

## Toelichting

AI-systemen met een hoog risico die data gebruiken voor het trainen van AI-modellen, moeten gebaseerd zijn op datasets die voldoen aan specifieke [kwaliteitscriteria](../../maatregelen/3-dat-01-datakwaliteit/).

Deze criteria zorgen ervoor dat de data geschikt zijn voor [training, validatie en tests](../../maatregelen/3-dat-07-training-validatie-en-testdata/), wat de betrouwbaarheid en nauwkeurigheid van het AI-systeem waarborgt. De kwaliteitscriteria zijn te vinden in leden 2 t/m 5 van artikel 10 van de AI-verordening. Bijvoorbeeld datasets moeten aan praktijken voor databeheer voldoen en moeten relevant, representatief, accuraat en volledig zijn.

Deze vereiste houdt in dat de gebruikte datasets onder meer moeten voldoen aan:

  * datasets voor training, validatie en tests worden onderworpen aan praktijken op het gebied van databeheer die stroken met het beoogde doel van het AI-systeem met een hoog risico. Dit heeft in het bijzonder betrekking op relevante ontwerpkeuzes, processen voor dataverzameling, verwerkingsactiviteiten voor datavoorbereiding, het opstellen van aannames met name betrekking tot de informatie die de data moeten meten en vertegenwoordigen, beschikbaarheid, kwantiteit en geschiktheid van de datasets en een beoordeling op mogelijke vooringenomenheid en passende maatregelen om deze vooringenomenheid op te sporen, te voorkomen en te beperken.
  * datasets voor training, validatie en tests zijn relevant, voldoende representatief en zoveel mogelijk foutenvrij en volledig met het oog op het beoogde doel.
  * Er wordt rekening gehouden met de eigenschappen of elementen die specifiek zijn voor een bepaalde geografische, contextuele, functionele of gedragsomgeving waarin het AI-systeem wordt gebruikt.

## Bronnen

[Artikel 10(1) Verordening Artificiële Intelligentie](https://eur-lex.europa.eu/legal-content/NL/TXT/HTML/?uri=OJ:L_202401689#d1e3348-1-1)

## Van toepassing op

Deze vereiste is van toepassing voor onderstaande (combinatie van) labels. Gebruik de [beslishulp](https://ai-act-decisiontree.apps.digilab.network) voor hulp bij wat er in jouw situatie van toepassing is.

[](../../../soorten-algoritmes-en-ai/wat-is-een-algoritme/ "Soort toepassing")[AI-systeem](../../ai-verordening/#ai-systeem)[](../../../soorten-algoritmes-en-ai/wat-is-een-algoritme/ "Soort toepassing")[AI-systeem voor algemene doeleinden](../../ai-verordening/#ai-model-voor-algemene-doeleinden)[](../../ai-verordening/#risicogroepen "Risicogroep")[Hoog risico AI-systeem](../../../soorten-algoritmes-en-ai/risico-van-ai-systemen/#hoog-risico-ai-systeem)[](../../ai-verordening/#rollen-uit-de-ai-verordening "Rol AI-verordening")[Aanbieder](../../ai-verordening/#aanbieder)[](../../../soorten-algoritmes-en-ai/risico-van-ai-systemen/#risico-op-misleiding "Transparantieverplichting AI-verordening")[Geen transparantieverplichting](../../../soorten-algoritmes-en-ai/risico-van-ai-systemen/#risico-op-misleiding)[](../../../soorten-algoritmes-en-ai/risico-van-ai-systemen/#risico-op-misleiding "Transparantieverplichting AI-verordening")[Transparantieverplichting](../../../soorten-algoritmes-en-ai/risico-van-ai-systemen/#risico-op-misleiding)

## Risico

Gebruik van laagkwalitatieve of bevooroordeelde datasets kan leiden tot onbetrouwbare en oneerlijke AI-besluitvorming. Onvoldoende kwaliteitsborging van testdata kan leiden tot vertekende resultaten en gebrekkige prestaties van het AI-systeem bij gebruik in de praktijk.

## Maatregelen

id| Maatregelen
---|---
[owp-02](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-02-data-beschikbaarheid/index.html)| [Voer voorafgaand aan een project een data beschikbaarheid, kwaliteit- en toegankelijkheidsanalayse uit](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-02-data-beschikbaarheid/index.html)
[owp-11](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-11-gebruikte-data/index.html)| [Beschrijf welke data gebruikt wordt voor de beoogde toepassing](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-11-gebruikte-data/index.html)
[owp-15](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-15-bespreek-vereisten-met-aanbieders/index.html)| [Bespreek de vereisten die gelden voor een verantwoorde inzet van algoritmes met aanbieders](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-15-bespreek-vereisten-met-aanbieders/index.html)
[owp-16](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-16-vereisten-onderdeel-algemene-inkoopvoorwaarden-en-contractovereenkomst/index.html)| [Maak vereisten voor algoritmes onderdeel van algemene inkoopvoorwaarden en de contractovereenkomst](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-16-vereisten-onderdeel-algemene-inkoopvoorwaarden-en-contractovereenkomst/index.html)
[owp-20](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-20-maak-vereisten-onderdeel-van-subgunningscriteria/index.html)| [Maak vereisten onderdeel van (sub)gunningscriteria bij een aanbesteding](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-20-maak-vereisten-onderdeel-van-subgunningscriteria/index.html)
[owp-21](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-21-ruimte-voor-samenwerking-met-aanbieder/index.html)| [Creëer ruimte om met een aanbieder samen te gaan werken om specifieke vereisten te realiseren](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-21-ruimte-voor-samenwerking-met-aanbieder/index.html)
[owp-23](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-23-uitvoeren-audit-voor-naleving-vereisten/index.html)| [Neem het kunnen uitvoeren van een audit over de vereiste op in contractvoorwaarden en de contractovereenkomst](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-23-uitvoeren-audit-voor-naleving-vereisten/index.html)
[owp-27](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-27-maak-vereisten-onderdeel-van-programma-van-eisen/index.html)| [Maak vereisten onderdeel van het programma van eisen bij een aanbesteding](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-27-maak-vereisten-onderdeel-van-programma-van-eisen/index.html)
[owp-28](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-28-maak-vereisten-onderdeel-van-service-level-agreement/index.html)| [Maak vereisten voor algoritmes onderdeel van de Service Level Agreement](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-28-maak-vereisten-onderdeel-van-service-level-agreement/index.html)
[owp-29](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-29-contractuele-afspraken-data-en-artefacten/index.html)| [Maak (contractuele) afspraken over data en artefacten met een aanbieder](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-29-contractuele-afspraken-data-en-artefacten/index.html)
[owp-31](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-31-pas-vastgestelde-beleidskaders-zijn-nageleefd/index.html)| [Pas vastgestelde interne beleidskaders toe en maak aantoonbaar dat deze zijn nageleefd bij het ontwikkelen, inkopen en gebruiken van algoritmes](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/2-owp-31-pas-vastgestelde-beleidskaders-zijn-nageleefd/index.html)
[dat-01](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-01-datakwaliteit/index.html)| [Controleer de datakwaliteit](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-01-datakwaliteit/index.html)
[dat-08](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-08-eigenaarschap-data/index.html)| [Zorg dat je controle of eigenaarschap hebt over de data](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-08-eigenaarschap-data/index.html)
[owk-12](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-12-licentiegebruik/index.html)| [Gebruik een passende licentie bij publicatie of gebruik van (open) data](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/4-owk-12-licentiegebruik/index.html)
[ver-03](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-03-biasanalyse/index.html)| [Toets het algoritme op bias en voer een rechtvaardigingstoets uit](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-03-biasanalyse/index.html)
[ver-05](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-05-vertaling-wetgeving-naar-systeem/index.html)| [Controleer regelmatig of het algoritme voldoet aan alle wetten en regels en het eigen beleid](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-05-vertaling-wetgeving-naar-systeem/index.html)
[mon-05](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-05-evalueer-bij-veranderingen-in-data/index.html)| [Monitor regelmatig op veranderingen in de data. Bij veranderingen evalueer je de prestaties en output van het algoritme.](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/7-mon-05-evalueer-bij-veranderingen-in-data/index.html)
19 februari 2025 11 april 2024
  *AI-modellen voor algemene doeleinden: Een AI-model, ook wanneer het is getraind met een grote hoeveelheid data met behulp van self-supervision op grote schaal, dat een aanzienlijk algemeen karakter vertoont en in staat is op competente wijze een breed scala aan verschillende taken uit te voeren, ongeacht de wijze waarop het model in de handel wordt gebracht, en dat kan worden geïntegreerd in een verscheidenheid aan systemen verder in de AI-waardeketen of toepassingen verder in de AI-waardeketen, met uitzondering van AI-modellen die worden gebruikt voor onderzoek, ontwikkeling of prototypingactiviteiten alvorens zij in de handel worden gebracht.
  *AI-geletterdheid: vaardigheden, kennis en begrip die aanbieders, gebruiksverantwoordelijken en betrokken personen, rekening houdend met hun respectieve rechten en plichten in het kader van de de AI-verordening, in staat stellen met kennis van zaken AI-systemen in te zetten en zich bewuster te worden van de kansen en risico’s van AI en de mogelijke schade die zij kan veroorzaken
  *AI-model voor algemene doeleinden: Een AI-model, ook wanneer het is getraind met een grote hoeveelheid data met behulp van self-supervision op grote schaal, dat een aanzienlijk algemeen karakter vertoont en in staat is op competente wijze een breed scala aan verschillende taken uit te voeren, ongeacht de wijze waarop het model in de handel wordt gebracht, en dat kan worden geïntegreerd in een verscheidenheid aan systemen verder in de AI-waardeketen of toepassingen verder in de AI-waardeketen, met uitzondering van AI-modellen die worden gebruikt voor onderzoek, ontwikkeling of prototypingactiviteiten alvorens zij in de handel worden gebracht.
  *biometrische gegevens: persoonsgegevens die het resultaat zijn van een specifieke technische verwerking met betrekking tot de fysieke, fysiologische of gedragsgerelateerde kenmerken van een natuurlijk persoon, zoals gezichtsafbeeldingen of vingerafdrukgegevens
  *AI-systeem voor algemene doeleinden: Een AI-systeem dat is gebaseerd op een AI- model voor algemene doeleinden en dat verschillende doeleinden kan dienen, zowel voor direct gebruik als voor integratie in andere AI-systemen
  *systeemrisico: een risico dat specifiek is voor de capaciteiten met een grote impact van AI-modellen voor algemene doeleinden, die aanzienlijke gevolgen hebben voor de markt van de Unie vanwege hun bereik, of vanwege feitelijke of redelijkerwijs te voorziene negatieve gevolgen voor de gezondheid, de veiligheid, de openbare veiligheid, de grondrechten of de samenleving als geheel, en dat op grote schaal in de hele waardeketen kan worden verspreid
  *AI-bureau: De taak van de Commissie waarbij zij bijdraagt aan de uitvoering van, de monitoring van en het toezicht op AI-systemen en AI-modellen voor algemene doeleinden, en AI-governance, als bepaald in het besluit van de Commissie van 24 januari 2024; verwijzingen in deze verordening naar het AI-bureau worden begrepen als verwijzingen naar de Commissie
  *aanbieder: Een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem of een AI-model voor algemene doeleinden ontwikkelt of laat ontwikkelen en dat systeem of model in de handel brengt of het AI-systeem in gebruik stelt onder de eigen naam of merk, al dan niet tegen betaling.
  *kritieke infrastructuur: kritieke infrastructuur zoals gedefinieerd in artikel 2, punt 4, van Richtlijn (EU) 2022/2557
  *redelijkerwijs te voorzien misbruik: Het gebruik van een AI-systeem op een wijze die niet in overeenstemming is met het beoogde doel, maar die kan voortvloeien uit redelijkerwijs te voorzien menselijk gedrag of redelijkerwijs te voorziene interactie met andere systemen, waaronder andere AI-systemen
  *gebruiksinstructies: de door de aanbieder verstrekte informatie om de gebruiksverantwoordelijke te informeren over met name het beoogde doel en juiste gebruik van een AI-systeem
  *testdata: data die worden gebruikt voor het verrichten van een onafhankelijke evaluatie van het AI-systeem om de verwachte prestaties van dat systeem te bevestigen voordat het in de handel wordt gebracht of in gebruik wordt gesteld
