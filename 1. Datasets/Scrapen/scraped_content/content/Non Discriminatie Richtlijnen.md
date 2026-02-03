---
title: Handreiking non-discriminatie by design - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/hulpmiddelen/handreiking-non-discriminatie/index.html
scraped_at: 2025-06-12T10:32:41.617094
---

# Handreiking non-discriminatie by design - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/hulpmiddelen/handreiking-non-discriminatie/index.html

---

[ ![Home Algoritmekader](../../../assets/logo.svg) ](../../.. "Algoritmekader 2.2") Algoritmekader 2.2

[ GitHub  ](https://github.com/MinBZK/Algoritmekader "Ga naar repository")

  * [ Soorten algoritmes en AI  ](../../../soorten-algoritmes-en-ai/)
  * [ Onderwerpen  ](../../../onderwerpen/)
  * [ Levenscyclus  ](../../../levenscyclus/)
  * [ Rollen  ](../../../rollen/)
  * [ Voldoen aan wetten en regels  ](../../)

Inhoudsopgave

  * Hulpmiddel
  * Relevantie
  * Wanneer toepassen?
    * Relatie tot IAMA
    * Relatie tot het Fairness Handbook
    * Relatie tot Toetsingskader Risicoprofilering van het College voor de Rechten van de Mens
  * Bijbehorende vereisten
  * Bijbehorende maatregelen
  * Bronnen
  * Voorbeeld

  1. [ Voldoen aan wetten en regels  ](../../)
  2. [ Hulpmiddelen  ](../)

# Handreiking non-discriminatie by design

[](../../../levenscyclus/ "Levencyclus")[Ontwikkelen](../../../levenscyclus/ontwikkelen/)[](../../../levenscyclus/ "Levencyclus")[Implementatie](../../../levenscyclus/implementatie/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Bias en non discriminatie](../../../onderwerpen/bias-en-non-discriminatie/)[](../../../onderwerpen/ "Onderwerp")[Fundamentele rechten](../../../onderwerpen/fundamentele-rechten/)

[Direct naar de Handreiking non-discriminatie by design](https://www.rijksoverheid.nl/documenten/rapporten/2021/06/10/handreiking-non-discriminatie-by-design)

## Hulpmiddel

Deze handreiking legt uit welke vragen en principes leidend zijn bij het ontwikkelen en implementeren van een AI-systeem met het oog op het discriminatieverbod, vanuit zowel juridisch, technisch, als organisatorisch perspectief. De handreiking is een praktisch toepasbaar ontwerpkader dat ontwikkelaars helpt om al in de ontwikkelfase van een AI-systeem discriminerende patronen zoveel mogelijk te identificeren, te voorkomen en te bestrijden.

Er zijn 4 uitgangspunten die leidend zijn in de handreiking:

  1. Diversiteit
  2. Context
  3. Controleerbaarheid
  4. Evaluatie.

## Relevantie

Stuk over relevantie voor het AK volgt nog. Net als bij het [IAMA](../IAMA/), is dit document een manier om een multidisciplinaire discussie te faciliteren en stimuleren. Hierbij kunnen verschillende rollen betrokken worden door de [projectleider](../../../rollen/projectleider/): [data-scientists](../../../rollen/ontwikkelaar/), [juristen](../../../rollen/jurist/), de functionaris gegevensbescherming (FG), aangevuld met domeinspecialisten.

## Wanneer toepassen?

De handreiking is primair geschreven voor teams die zelf AI-systemen bouwen. Het gaat in op verschillende fases van ontwikkeling: [probleemanalyse](../../../levenscyclus/probleemanalyse/), [dataverkenning en datapreparatie](../../../levenscyclus/dataverkenning-en-datapreparatie/), [ontwikkeling](../../../levenscyclus/ontwikkelen/), [implementatie](../../../levenscyclus/implementatie/) en [evaluatie](../../../levenscyclus/verificatie-en-validatie/). Daarnaast kan deze handreiking dienen voor opdrachtgevers van AI-systemen, ofwel om vooraf offrerende partijen te vragen aan te geven hoe zij rekening zullen houden met de diverse punten uit de handreiking, ofwel om tijdens het proces mee te kijken en op relevante punten aanwijzingen te geven, ofwel om achteraf te controleren of een opgeleverd product aan alle relevante voorwaarden voldoet.

### Relatie tot IAMA

Gebruikers van zowel de Handreiking non-discriminatie by design als het [IAMA](../IAMA/) geven enkele verschillen tussen de twee instrumenten. Deze bevindingen zijn te vinden in het rapport [Bekendheid, toepasbaarheid en toegevoegde waarde handreiking 'non-discriminatie by design'](https://www.rijksoverheid.nl/documenten/rapporten/2023/06/26/onderzoeksrapport-bekendheid-en-toepasbaarheid-en-toegevoegde-waarde-handreiking-non-discriminatie-by-design) van de Auditdienst Rijk.

Zij geven aan dat het IAMA wordt gezien als instrument voor het nagaan van de impact van grondrechten in algemenere zin, waar de Handreiking zich specifiek richt op discriminatie. De handreiking bevat dan weer meer praktische voorbeelden die kunnen helpen bij begrip en afwegingen, waar de IAMA wat abstracter is.

### Relatie tot het Fairness Handbook

Over het [Fairness Handbook](../fairness-handbook/) werd in het rapport aangegeven dat het een technischere uitwerking bevat dan de Handreiking. Het Handbook biedt wellicht meer houvast voor iemand die analyses maakt om inzicht te geven in de prestaties van het algoritme met het oog op ‘fairness’ en ‘bias’. Dit komt doordat het Handbook meer details geeft over de technische stappen die nodig zijn om te komen tot bepaalde analyses.

### Relatie tot Toetsingskader Risicoprofilering van het College voor de Rechten van de Mens

Ook het [toetsingskader Risicoprofilering College voor de Rechten van de Mens](../toetsingskader-risicoprofilering/) kan worden gebruikt om te bepalen of er discriminatie plaatsvindt. De verschillende stappen die daarin gebruikt worden om te bepalen of een risicoprofiel leidt tot onderscheid op grond van ras of nationaliteit, zijn zeer relevant.

## Bijbehorende vereisten

Vereiste
---
[grw-01 - Algoritmes schenden geen grondrechten of mensenrechten](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/grw-01-fundamentele-rechten/)
[grw-02 - Algoritmes discrimineren niet](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/grw-02-non-discriminatie/)
[aia-04 - Hoog-risico-AI-systemen vormen geen risico voor kwetsbare groepen zoals kinderen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/aia-04-risicobeoordeling-voor-jongeren-en-kwetsbaren/)

## Bijbehorende maatregelen

Maatregel
---
[dat-01 - Controleer de datakwaliteit](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/3-dat-01-datakwaliteit/)
[ver-03 - Toets het algoritme op bias en voer een rechtvaardigingstoets uit](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/5-ver-03-biasanalyse/)
[imp-02 - Doe aselecte steekproeven om algoritmes met 'risicogestuurde selectie’ te controleren](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/6-imp-02-aselecte-steekproeven/)

## Bronnen

  * [Handreiking non-discriminatie by design](https://www.rijksoverheid.nl/documenten/rapporten/2021/06/10/handreiking-non-discriminatie-by-design)
  * [Onderzoeksrapport Bekendheid, toepasbaarheid en toegevoegde waarde handreiking 'non-discriminatie by design'](https://www.rijksoverheid.nl/documenten/rapporten/2023/06/26/onderzoeksrapport-bekendheid-en-toepasbaarheid-en-toegevoegde-waarde-handreiking-non-discriminatie-by-design)
  * [Toetsingskader Risicoprofilering, College voor de Rechten van de Mens](https://publicaties.mensenrechten.nl/publicatie/4093c026-ae41-4c1d-aa78-4ce0e205b5de)

## Voorbeeld

Heb jij een goed voorbeeld van het gebruik van de Handreiking non-discriminatie by design op het gebied van algoritmen? Laat het ons weten!

10 april 2025 25 september 2024

Terug naar boven
  *norm: een norm is een vrijwillige afspraak tussen partijen over een product, dienst of proces. Normen zijn geen wetten, maar ’best practices’. Iedereen kan - op vrijwillige basis - hier zijn voordeel mee doen. In zakelijke overeenkomsten hebben normen een belangrijke functie. Ze bieden marktpartijen duidelijkheid over en vertrouwen in producten, diensten of organisaties en dagen de maatschappij uit te innoveren. NEN-normen worden ontwikkeld door inhoudsexperts en specialisten op het gebied van normontwikkeling.
