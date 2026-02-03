---
title: Maak afspraken over het beheer van wachtwoorden - Algoritmekader 2.2
url: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/0-org-13-wachtwoordbeheer/index.html
scraped_at: 2025-06-12T10:33:04.425675
---

# Maak afspraken over het beheer van wachtwoorden - Algoritmekader 2.2

Source: https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/maatregelen/0-org-13-wachtwoordbeheer/index.html

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

# Maak afspraken over het beheer van wachtwoorden

[]( "Vereiste ID")org-13[](../../../levenscyclus/ "Levencyclus")[Organisatieverantwoordelijkheden](../../../levenscyclus/organisatieverantwoordelijkheden/)[](../../../rollen/ "Rollen")[Projectleider](../../../rollen/projectleider/)[](../../../rollen/ "Rollen")[Ontwikkelaar](../../../rollen/ontwikkelaar/)[](../../../onderwerpen/ "Onderwerp")[Technische robuustheid en veiligheid](../../../onderwerpen/technische-robuustheid-en-veiligheid/)[](../../../onderwerpen/ "Onderwerp")[Governance](../../../onderwerpen/governance/)

## Maatregel

Richt wachtwoordbeheer in, waarmee bepaald wordt hoe wachtwoorden worden opgeslagen, wanneer wijzigingen moeten plaatsvinden en waaraan wachtwoorden moeten voldoen. Hiermee wordt de toegang tot bijvoorbeeld ontwikkelomgevingen geregeld op een veilige manier.

## Toelichting

Bij het inrichten van wachtwoordbeheer moeten de volgende zaken worden toegepast:

  * Alle wachtwoorden van gebruikers en beheerders dienen periodiek te worden gewijzigd, met een maximum van 1 jaar (BIO 9.4.3). Initiële wachtwoorden en wachtwoorden die gereset zijn, hebben een maximale geldigheidsduur van 24 uur en moeten bij het eerste gebruik worden gewijzigd.
  * Voor toegang vanuit een onvertrouwde omgeving dient twee-factor authenticatie te worden gebruikt (BIO 9.4.2.1). Als er geen gebruik wordt gemaakt van twee-factor authenticatie, is de wachtwoordlengte minimaal 8 posities en complex van samenstelling. In situaties waar geen twee-factor authenticatie mogelijk is, wordt minimaal halfjaarlijks het wachtwoord vernieuwd.
  * Na een periode van maximaal 15 minuten inactiviteit dient de toegang tot de applicatie te worden vergrendeld en na 10 foutieve inlogpogingen dient het account geblokkeerd te worden (BIO 11.2.9, BIO 9.4.3). De tijdsduur dat een account wordt geblokkeerd na overschrijding van het aantal keer foutief inloggen is vastgelegd.
  * Wachtwoorden mogen niet in originele vorm (plaintext) worden opgeslagen, maar dienen versleuteld te worden (NIST 5.1.1.2).
  * De eisen aan wachtwoorden moeten geautomatiseerd worden afgedwongen.

## Risico

Als het wachtwoordbeheer van onvoldoende kwaliteit is, kan oneigenlijke toegang plaatsvinden tot het algoritme of uitkomsten van het algoritme, bijvoorbeeld doordat het wachtwoord te eenvoudig is.

## Bijbehorende vereiste(n)

Bekijk alle vereisten Vereiste
---
[bio-01 - Computersystemen zijn voldoende beveiligd tegen ongelukken en cyberaanvallen](https://minbzk.github.io/Algoritmekader/voldoen-aan-wetten-en-regels/vereisten/bio-01-beveiliging-informatie-en-informatiesystemen/)

## Bronnen

  * [Baseline Informatiebeveiliging Overheid](https://www.digitaleoverheid.nl/overzicht-van-alle-onderwerpen/cybersecurity/bio-en-ensia/baseline-informatiebeveiliging-overheid/)
  * [Onderzoekskader Algoritmes Auditdienst Rijk, IB.6 t/m IB.9](https://www.rijksoverheid.nl/documenten/rapporten/2023/07/11/onderzoekskader-algoritmes-adr-2023)
  * [Toetsingskader Algoritmes Algemene Rekenkamer, 4.03](https://www.rekenkamer.nl/onderwerpen/algoritmes/documenten/publicaties/2024/05/15/het-toetsingskader-aan-de-slag)
  * [NIST 5.1.1.2](https://pages.nist.gov/800-63-3/sp800-63b.html#sec5)

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
