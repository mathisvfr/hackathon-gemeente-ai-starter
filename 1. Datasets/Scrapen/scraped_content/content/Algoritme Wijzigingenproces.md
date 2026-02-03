---
title: Maak afspraken over het wijzigen van de code - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/0-org-14-wijzigingenproces/index.html
scraped_at: 2025-06-12T10:33:05.623595
---

# Maak afspraken over het wijzigen van de code - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/0-org-14-wijzigingenproces/index.html

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

# Maak afspraken over het wijzigen van de code

[]( "Vereiste ID")org-14[](../../../levenscyclus/ "Levencyclus")[Organisatieverantwoordelijkheden](../../../levenscyclus/organisatieverantwoordelijkheden/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)[](../../../onderwerpen/ "Onderwerp")[Governance](../../../onderwerpen/governance/)

## Maatregel

Richt een wijzigingenproces in, waarmee bepaald wordt hoe codewijzigingen plaatsvinden.

## Toelichting

Bij het inrichten van een proces om wijzigingen aan de code te mogen aanbrengen, kunnen aan de volgende elementen worden gedacht:

  * Wijzigingen dienen van te voren te worden geautoriseerd door de systeemeigenaar of product owner. (BIO 12.1.2)
  * Wijzigingen worden getest in een andere omgeving dan de productieomgeving. (BIO 12.1.4, 14.2.3, 14.2.9, 14.3.1)
  * Wijzigingen worden door de systeemeigenaar of product owner goedgekeurd op basis van gedocumenteerde testresultaten en pas daarna doorgevoerd in de productieomgeving. (BIO 12.1.2, 14.2.2, 14.2.9)
  * Er dient functiescheiding te zijn ingericht tussen het aanvragen, goedkeuren en doorvoeren van wijzigingen om onbevoegde en onbedoelde wijzigingen te beperken. (BIO 6.1.2, 14.2.2)
  * Er dient periodiek controle plaats te vinden op wijzigingen aan het systeem, zodanig dat oneigenlijke wijzigingen worden gesignaleerd. (BIO 9.4.4, 12.4.1)

## Risico

Als een formeel wijzigingenproces ontbreekt bestaat het risico van ongeautoriseerde toegang, wijziging of beschadiging van de code van het algoritme, of de uitkomsten van het algoritme.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[bio-01 - Computersystemen zijn voldoende beveiligd tegen ongelukken en cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/bio-01-beveiliging-informatie-en-informatiesystemen/)

## Bronnen

  * [Baseline Informatiebeveiliging Overheid](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cybersecurity/bio-en-ensia/baseline-informatiebeveiliging-overheid/)
  * [Onderzoekskader Algoritmes Auditdienst Rijk, IB.1 t/m IB.5](https://www.rijksoverheid.nl/documenten/rapporten/2023/07/11/onderzoekskader-algoritmes-adr-2023)
  * [Toetsingskader Algoritmes Algemene Rekenkamer, 4.07](https://www.rekenkamer.nl/onderwerpen/algoritmes/documenten/publicaties/2024/05/15/het-toetsingskader-aan-de-slag)

## Voorbeelden

Informatie Beveiligingsdienst - Aanwijzing Logging

De informatie beveiligingsdienst (IBD) heeft een handreiking gepubliceerd rondom logging-beleid en -procedures. Hierin wordt onder andere uitgelegd wat voor soorten logbestanden er zijn, voor wie deze belangrijk zijn en wat er in een log moet staan. Daarnaast wordt toegelicht hoe logging gecontroleerd kan/moet worden.

Dit document kan een goede basis vormen voor het beginnen met log bestanden maken. Zo staan er in dit document verschillende bijlagen zoals een template voor logging-beleid en verschillende infographics die het logging-proces en de controles visualiseren voor de lezer.

Bron: [Handreiking Logging](https://www.informatiebeveiligingsdienst.nl/product/aanwijzing-logging/)

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

14 februari 2025 14 augustus 2024

Terug naar boven
  *norm: een norm is een vrijwillige afspraak tussen partijen over een product, dienst of proces. Normen zijn geen wetten, maar ’best practices’. Iedereen kan - op vrijwillige basis - hier zijn voordeel mee doen. In zakelijke overeenkomsten hebben normen een belangrijke functie. Ze bieden marktpartijen duidelijkheid over en vertrouwen in producten, diensten of organisaties en dagen de maatschappij uit te innoveren. NEN-normen worden ontwikkeld door inhoudsexperts en specialisten op het gebied van normontwikkeling.
  *aanbieder: Een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem of een AI-model voor algemene doeleinden ontwikkelt of laat ontwikkelen en dat systeem of model in de handel brengt of het AI-systeem in gebruik stelt onder de eigen naam of merk, al dan niet tegen betaling.
  *AI-geletterdheid: vaardigheden, kennis en begrip die aanbieders, gebruiksverantwoordelijken en betrokken personen, rekening houdend met hun respectieve rechten en plichten in het kader van de de AI-verordening, in staat stellen met kennis van zaken AI-systemen in te zetten en zich bewuster te worden van de kansen en risico’s van AI en de mogelijke schade die zij kan veroorzaken
  *geharmoniseerde norm: Een Europese norm die op verzoek van de Commissie is vastgesteld met het oog op de toepassing van harmonisatiewetgeving van de Unie
  *conformiteitsbeoordeling: Het proces waarbij de naleving wordt aangetoond van de voorschriften van hoofdstuk III, afdeling 2 van de AI-Verordening in verband met een AI-systeem met een hoog risico
  *gebruiksverantwoordelijke: Een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem onder eigen verantwoordelijkheid gebruikt, tenzij het AI-systeem wordt gebruikt in het kader van een persoonlijke niet- beroepsactiviteit.
