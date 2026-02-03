---
title: Maak afspraken over het beheer van gebruikers - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/0-org-11-gebruikersbeheer/index.html
scraped_at: 2025-06-12T10:33:02.018756
---

# Maak afspraken over het beheer van gebruikers - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/0-org-11-gebruikersbeheer/index.html

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

# Maak afspraken over het beheer van gebruikers

[]( "Vereiste ID")org-11[](../../../levenscyclus/ "Levencyclus")[Organisatieverantwoordelijkheden](../../../levenscyclus/organisatieverantwoordelijkheden/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../rollen/ "Rollen")[Beleid en advies](../../../rollen/beleid-en-advies/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)[](../../../onderwerpen/ "Onderwerp")[Governance](../../../onderwerpen/governance/)

## Maatregel

Richt gebruikersbeheer in, waarmee bepaald wordt wie toegang heeft tot wat, en wat er bijvoorbeeld gebeurt bij indiensttreding, functiewijziging en uitdiensttreding.

## Toelichting

Gebruikersbeheer zorgt ervoor dat accounts en autorisaties beheerst worden aangevraagd, geautoriseerd, gewijzigd en ingetrokken bij indiensttreding, functiewijziging en uitdiensttreding. Ook wordt functievermenging voorkomen bij toegang en gebruik van het algoritme, de data of de uitkomsten van een algoritme.

Bij het inrichten van gebruikersbeheer moeten aan de volgende elementen worden gedacht:

  * Gebruikers en beheerders krijgen slechts toegang tot functionaliteit die zij uit hoofde van hun functie nodig hebben (need to know, need to use). Daartoe is een beschrijving beschikbaar welke rollen en rechten per applicatie bij een functie horen (BIO 6.1.2, 9.2.2 en 9.4).
  * Het verlenen en muteren van accounts en toegangsrechten vindt plaats na goedkeuring door een bevoegde functionaris. Dit aan de hand van een actueel mandaatregister waaruit blijkt welke personen beslissende bevoegdheden hebben voor het verlenen van een bepaald type (niveau) toegangsrechten danwel functieprofielen (BIO 9.2.1.2, 9.2.2.1, 9.4).
  * Er bestaat functiescheiding tussen het aanvragen, autoriseren en doorvoeren van wijzigingen in gebruikersaccounts en toegangsrechten (BIO 9.2.1.2, 9.2.2.1, 9.2.3).
  * Functiewijzigingen en uitdiensttredingen worden bewaakt voor aanpassen van de toegangsrechten en voor intrekken van de identiteits- en authenticatiemiddelen (BIO 9.2.2, 9.2.6).
  * Het aantal accounts met verhoogde rechten is beperkt en verklaard, en staat in logische verhouding tot de beheerders en of ICT-afdeling (BIO 9.1.2.(1), 9.2.3, 9.2.4).
  * Gebruikersaccounts en beheeraccounts dienen altijd persoonsgebonden en verklaard te zijn, zodat handelingen altijd te herleiden zijn naar één verantwoordelijke (BIO 9.1, 9.4.2).
  * Eindgebruikers hebben geen directe toegang tot de onderliggende componenten (zoals de database) (BIO 9.2.3, 13.1.3).
  * Toegangsrechten op onderliggende componenten dienen periodiek, minimaal jaarlijks, geëvalueerd te worden. Dit interval dient te zijn beschreven in het toegangsbeleid en zijn bepaald op basis van het risiconiveau. De uitkomsten van de evaluatie en de opvolging daarvan worden vastgelegd (BIO 9.2.5).

Voor deze maatregelen is het van belang om aandacht te hebben voor de volgende zaken:

  * Autorisatiematrix en beschrijving rollen/rechten per systeem(laag)
  * Lijst met wijzigingen rollen en bijbehorende goedkeuringen
  * Overzicht aantallen en rechten per (systeem)laag

## Risico

Er bestaan meerdere risico's wanneer er geen gebruikersbeheer is:

  * Toegangsrechten kunnen niet meer up-to-date zijn, bijvoorbeeld wanneer er geen rekening wordt gehouden met het IDU-proces. Er bestaat dan het risico dat gebruikers toegang tot de omgeving van het algoritme, de data of de uitkomsten van het algoritme hebben die zij niet zouden mogen hebben.
  * Wanneer functievermenging niet wordt voorkomen bij toegang en gebruik van het algoritme, bestaat het risico dat er ongeautoriseerde wijzigingen worden doorgevoerd aan het algoritme, de data of de uitkomsten van het algoritme.
  * Wanneer gebruik wordt gemaakt van generieke-, groeps- of onpersoonlijke accounts, bestaat het risico dat handelingen niet te herleiden zijn naar een verantwoordelijke persoon.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[bio-01 - Computersystemen zijn voldoende beveiligd tegen ongelukken en cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/bio-01-beveiliging-informatie-en-informatiesystemen/)

## Bronnen

  * [Baseline Informatiebeveiliging Overheid](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cybersecurity/bio-en-ensia/baseline-informatiebeveiliging-overheid/)
  * [Onderzoekskader Algoritmes Auditdienst Rijk, IB.10 t/m IB.17](https://www.rijksoverheid.nl/documenten/rapporten/2023/07/11/onderzoekskader-algoritmes-adr-2023)
  * [Toetsingskader Algoritmes Algemene Rekenkamer, 4.01, 4.02, 4.04, 4.05](https://www.rekenkamer.nl/onderwerpen/algoritmes/documenten/publicaties/2024/05/15/het-toetsingskader-aan-de-slag)

## Voorbeelden

Heb je een ander voorbeeld of best practice, laat het ons weten via [algoritmes@minbzk.nl](mailto:algoritmes@minbzk.nl)

11 februari 2025 14 augustus 2024

Terug naar boven
  *norm: een norm is een vrijwillige afspraak tussen partijen over een product, dienst of proces. Normen zijn geen wetten, maar ’best practices’. Iedereen kan - op vrijwillige basis - hier zijn voordeel mee doen. In zakelijke overeenkomsten hebben normen een belangrijke functie. Ze bieden marktpartijen duidelijkheid over en vertrouwen in producten, diensten of organisaties en dagen de maatschappij uit te innoveren. NEN-normen worden ontwikkeld door inhoudsexperts en specialisten op het gebied van normontwikkeling.
  *aanbieder: Een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem of een AI-model voor algemene doeleinden ontwikkelt of laat ontwikkelen en dat systeem of model in de handel brengt of het AI-systeem in gebruik stelt onder de eigen naam of merk, al dan niet tegen betaling.
  *AI-geletterdheid: vaardigheden, kennis en begrip die aanbieders, gebruiksverantwoordelijken en betrokken personen, rekening houdend met hun respectieve rechten en plichten in het kader van de de AI-verordening, in staat stellen met kennis van zaken AI-systemen in te zetten en zich bewuster te worden van de kansen en risico’s van AI en de mogelijke schade die zij kan veroorzaken
  *geharmoniseerde norm: Een Europese norm die op verzoek van de Commissie is vastgesteld met het oog op de toepassing van harmonisatiewetgeving van de Unie
  *conformiteitsbeoordeling: Het proces waarbij de naleving wordt aangetoond van de voorschriften van hoofdstuk III, afdeling 2 van de AI-Verordening in verband met een AI-systeem met een hoog risico
  *gebruiksverantwoordelijke: Een natuurlijke of rechtspersoon, overheidsinstantie, agentschap of ander orgaan die/dat een AI-systeem onder eigen verantwoordelijkheid gebruikt, tenzij het AI-systeem wordt gebruikt in het kader van een persoonlijke niet- beroepsactiviteit.
