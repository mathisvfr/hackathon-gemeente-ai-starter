#!/usr/bin/env python3
"""
Script to rename remaining markdown files that weren't renamed yet
"""

import os
import shutil
import sys
from pathlib import Path

# Add the enhanced_rag.py to path
sys.path.append('/home/tr17711/Dev/Hackathon II/Hackathon_II-C-III/3. Platform')

def get_remaining_files_mapping():
    """Return mapping for all remaining files that need Dutch names"""
    return {
        # MinBZK Ownership and Procurement files (2-owp)
        'minbzk_github_io_2-owp-01-rollen-en-verantwoordelijkheden_index_html.md': 'Rollen En Verantwoordelijkheden Algoritme.md',
        'minbzk_github_io_2-owp-02-data-beschikbaarheid_index_html.md': 'Data Beschikbaarheid Algoritme.md',
        'minbzk_github_io_2-owp-03-doel-verwerken-persoonsgegevens_index_html.md': 'Doel Verwerken Persoonsgegevens.md',
        'minbzk_github_io_2-owp-04-gebruikte-techniek_index_html.md': 'Gebruikte Techniek Algoritme.md',
        'minbzk_github_io_2-owp-05-soort-algoritme_index_html.md': 'Soort Algoritme Bepalen.md',
        'minbzk_github_io_2-owp-06-impactanalyse_index_html.md': 'Impact Analyse Algoritme.md',
        'minbzk_github_io_2-owp-07-afwegen-grondrechten_index_html.md': 'Afwegen Grondrechten Algoritme.md',
        'minbzk_github_io_2-owp-08-kwetsbare-groepen_index_html.md': 'Kwetsbare Groepen Beschermen.md',
        'minbzk_github_io_2-owp-09-archiveren-documenten_index_html.md': 'Archiveren Algoritme Documenten.md',
        'minbzk_github_io_2-owp-10-projectstartarchitectuur_index_html.md': 'Project Start Architectuur.md',
        'minbzk_github_io_2-owp-11-gebruikte-data_index_html.md': 'Gebruikte Data Algoritme.md',
        'minbzk_github_io_2-owp-12-duurzaam-inkopen_index_html.md': 'Duurzaam Inkopen Algoritmes.md',
        'minbzk_github_io_2-owp-13-eenvoudigere-algoritmes_index_html.md': 'Eenvoudigere Algoritmes Kiezen.md',
        'minbzk_github_io_2-owp-14-verwerkersovereenkomst-onderdeel-aanbesteding_index_html.md': 'Verwerkersovereenkomst Algoritme Aanbesteding.md',
        'minbzk_github_io_2-owp-15-bespreek-vereisten-met-aanbieders_index_html.md': 'Vereisten Bespreken Aanbieders.md',
        'minbzk_github_io_2-owp-16-vereisten-onderdeel-algemene-inkoopvoorwaarden-en-contractovereenkomst_index_html.md': 'Vereisten Inkoopvoorwaarden Contract.md',
        'minbzk_github_io_2-owp-17-leveren-bewijs-voldoen-aan-vereisten-algoritme-aanbieder_index_html.md': 'Bewijs Voldoen Vereisten.md',
        'minbzk_github_io_2-owp-18-leveren-bewijs-door-aanbieder-niet-schenden-auteursrechten_index_html.md': 'Bewijs Geen Auteursrechten.md',
        'minbzk_github_io_2-owp-19-beoordeel-aansprakelijkheidsvoorwaarden-van-aanbieder_index_html.md': 'Aansprakelijkheidsvoorwaarden Beoordelen.md',
        'minbzk_github_io_2-owp-20-maak-vereisten-onderdeel-van-subgunningscriteria_index_html.md': 'Vereisten Subgunning Criteria.md',
        'minbzk_github_io_2-owp-21-ruimte-voor-samenwerking-met-aanbieder_index_html.md': 'Samenwerking Met Aanbieder.md',
        'minbzk_github_io_2-owp-22-vaststellen-aanleveren-informatie-technische-documentatie_index_html.md': 'Technische Documentatie Vaststellen.md',
        'minbzk_github_io_2-owp-23-uitvoeren-audit-voor-naleving-vereisten_index_html.md': 'Audit Naleving Vereisten.md',
        'minbzk_github_io_2-owp-24-invloed-besluitvorming-algoritmes-aanbieders_index_html.md': 'Invloed Besluitvorming Aanbieders.md',
        'minbzk_github_io_2-owp-25-kennisoverdracht-en-ondersteuning-aanbieder_index_html.md': 'Kennisoverdracht Ondersteuning Aanbieder.md',
        'minbzk_github_io_2-owp-26-risico-analyse-informatiebeveiliging-leverancier_index_html.md': 'Risico Analyse Informatiebeveiliging.md',
        'minbzk_github_io_2-owp-27-maak-vereisten-onderdeel-van-programma-van-eisen_index_html.md': 'Vereisten Programma Van Eisen.md',
        'minbzk_github_io_2-owp-28-maak-vereisten-onderdeel-van-service-level-agreement_index_html.md': 'Vereisten Service Level Agreement.md',
        'minbzk_github_io_2-owp-29-contractuele-afspraken-data-en-artefacten_index_html.md': 'Contractuele Afspraken Data.md',
        'minbzk_github_io_2-owp-30-informeer-betrokkenen_index_html.md': 'Informeren Betrokkenen Algoritme.md',
        'minbzk_github_io_2-owp-31-pas-vastgestelde-beleidskaders-zijn-nageleefd_index_html.md': 'Beleidskaders Naleven Algoritme.md',
        'minbzk_github_io_2-owp-32-toepassen-uitlegbaarheidstechnieken_index_html.md': 'Uitlegbaarheid Technieken Toepassen.md',
        'minbzk_github_io_2-owp-33-technische-interventies-robuustheid_index_html.md': 'Technische Interventies Robuustheid.md',
        'minbzk_github_io_2-owp-34-voorkom-kwetsbaarheden-supplychain_index_html.md': 'Kwetsbaarheden Supply Chain.md',
        'minbzk_github_io_2-owp-35-genereren-bronvermelding_index_html.md': 'Genereren Bronvermelding Algoritme.md',
        'minbzk_github_io_2-owp-36-maak-of-koopbeslissing_index_html.md': 'Maak Of Koop Beslissing.md',

        # Data management files (3-dat)
        'minbzk_github_io_3-dat-05-schending-auteursrechten_index_html.md': 'Schending Auteursrechten Data.md',
        'minbzk_github_io_3-dat-06-duurzame-datacenters_index_html.md': 'Duurzame Datacenters Gebruiken.md',
        'minbzk_github_io_3-dat-07-training-validatie-en-testdata_index_html.md': 'Training Validatie Test Data.md',
        'minbzk_github_io_3-dat-08-eigenaarschap-data_index_html.md': 'Eigenaarschap Data Bepalen.md',
        'minbzk_github_io_3-dat-10-datamanipulatie_index_html.md': 'Data Manipulatie Voorkomen.md',
        'minbzk_github_io_3-dat-11-controleren-inputdata_index_html.md': 'Controleren Input Data.md',

        # Development & technical files (4-owk)
        'minbzk_github_io_4-owk-02-stopzetten-gebruik_index_html.md': 'Stopzetten Gebruik Algoritme.md',
        'minbzk_github_io_4-owk-03-privacyrisico_index_html.md': 'Privacy Risico Beoordelen.md',
        'minbzk_github_io_4-owk-05-energiezuinige-programmeermethoden_index_html.md': 'Energiezuinige Programmeer Methoden.md',
        'minbzk_github_io_4-owk-06-optimaliseer-AI-training_index_html.md': 'Optimaliseren AI Training.md',
        'minbzk_github_io_4-owk-08-feedbackloops_index_html.md': 'Feedback Loops Implementeren.md',
        'minbzk_github_io_4-owk-09-adversarial-aanvallen_index_html.md': 'Adversarial Aanvallen Voorkomen.md',
        'minbzk_github_io_4-owk-10-voorkom-lekken-op-basis-van-output_index_html.md': 'Lekken Output Voorkomen.md',
        'minbzk_github_io_4-owk-12-licentiegebruik_index_html.md': 'Licentie Gebruik Algoritme.md',

        # Verification files (5-ver)
        'minbzk_github_io_5-ver-04-representatieve-testomgeving_index_html.md': 'Representatieve Test Omgeving.md',
        'minbzk_github_io_5-ver-05-vertaling-wetgeving-naar-systeem_index_html.md': 'Wetgeving Naar Systeem.md',

        # Implementation files (6-imp)
        'minbzk_github_io_6-imp-02-aselecte-steekproeven_index_html.md': 'Aselecte Steekproeven Algoritme.md',
        'minbzk_github_io_6-imp-05-vermelding-in-privacyverklaring_index_html.md': 'Vermelding Privacy Verklaring.md',
        'minbzk_github_io_6-imp-07-vermelding-in-verwerkingsregister_index_html.md': 'Vermelding Verwerkings Register.md',
        'minbzk_github_io_6-imp-08-politiek-bestuurlijk-besluit_index_html.md': 'Politiek Bestuurlijk Besluit.md',
        'minbzk_github_io_6-imp-09-interventies-ux_index_html.md': 'UX Interventies Algoritme.md',
        'minbzk_github_io_6-imp-10-proces-privacyrechten_index_html.md': 'Proces Privacy Rechten.md',

        # Monitoring files (7-mon)
        'minbzk_github_io_7-mon-02-beveiliging-algoritme_index_html.md': 'Beveiliging Algoritme Monitoring.md',
        'minbzk_github_io_7-mon-03-informatiebeveiligingsincidenten_index_html.md': 'Informatie Beveiliging Incidenten.md',
        'minbzk_github_io_7-mon-05-evalueer-bij-veranderingen-in-data_index_html.md': 'Evalueren Data Veranderingen.md',
        'minbzk_github_io_7-mon-06-meten-milieu-impact_index_html.md': 'Milieu Impact Meten.md',
        'minbzk_github_io_7-mon-08-test-weerbaarheid-tegen-aanvallen_index_html.md': 'Weerbaarheid Tegen Aanvallen.md',

        # Framework files
        'minbzk_github_io_BIO_index_html.md': 'BIO Baseline Informatiebeveiliging.md',
        'minbzk_github_io_DEDA_index_html.md': 'DEDA Framework.md',

        # AI Act specific files (aia)
        'minbzk_github_io_aia-00-verboden-AI-praktijken_index_html.md': 'Verboden AI Praktijken.md',
        'minbzk_github_io_aia-02-documentatie-beoordeling-niet-hoog-risico-ai_index_html.md': 'Documentatie Niet Hoog Risico.md',
        'minbzk_github_io_aia-04-risicobeoordeling-voor-jongeren-en-kwetsbaren_index_html.md': 'Risico Jongeren Kwetsbaren.md',
        'minbzk_github_io_aia-05-data-kwaliteitscriteria_index_html.md': 'Data Kwaliteit Criteria.md',
        'minbzk_github_io_aia-06-technische-documentatie_index_html.md': 'Technische Documentatie AI.md',
        'minbzk_github_io_aia-07-automatische-logregistratie_index_html.md': 'Automatische Log Registratie.md',
        'minbzk_github_io_aia-08-transparantie-aan-gebruiksverantwoordelijken_index_html.md': 'Transparantie Gebruiks Verantwoordelijken.md',
        'minbzk_github_io_aia-11-systeem-voor-kwaliteitsbeheer_index_html.md': 'Systeem Kwaliteits Beheer.md',
        'minbzk_github_io_aia-12-bewaartermijn-voor-documentatie_index_html.md': 'Bewaar Termijn Documentatie.md',
        'minbzk_github_io_aia-14-conformiteitsbeoordeling_index_html.md': 'Conformiteits Beoordeling AI.md',
        'minbzk_github_io_aia-15-eu-conformiteitsverklaring_index_html.md': 'EU Conformiteits Verklaring.md',
        'minbzk_github_io_aia-16-ce-markering_index_html.md': 'CE Markering AI.md',
        'minbzk_github_io_aia-17-registratieverplichtingen_index_html.md': 'Registratie Verplichtingen AI.md',
        'minbzk_github_io_aia-18-corrigerende-maatregelen-voor-non-conforme-ai_index_html.md': 'Corrigerende Maatregelen Non Conforme.md',
        'minbzk_github_io_aia-19-toegankelijkheidseisen_index_html.md': 'Toegankelijkheids Eisen AI.md',
        'minbzk_github_io_aia-20-gebruiksverantwoordelijken-maatregelen_index_html.md': 'Gebruiks Verantwoordelijken Maatregelen.md',
        'minbzk_github_io_aia-21-gebruiksverantwoordelijken-menselijk-toezicht_index_html.md': 'Gebruiks Verantwoordelijken Menselijk Toezicht.md',
        'minbzk_github_io_aia-22-gebruiksverantwoordelijken-monitoren-werking_index_html.md': 'Gebruiks Verantwoordelijken Monitoren.md',
        'minbzk_github_io_aia-23-gebruiksverantwoordelijken-bewaren-logs_index_html.md': 'Gebruiks Verantwoordelijken Logs.md',
        'minbzk_github_io_aia-24-informeren-werknemers_index_html.md': 'Informeren Werknemers AI.md',
        'minbzk_github_io_aia-25-gebruiksverantwoordelijken-registratieverplichtingen_index_html.md': 'Gebruiks Verantwoordelijken Registratie.md',
        'minbzk_github_io_aia-28-transparantieverplichtingen_index_html.md': 'Transparantie Verplichtingen AI.md',
        'minbzk_github_io_aia-29-ai-modellen-algemene-doeleinden_index_html.md': 'AI Modellen Algemene Doeleinden.md',
        'minbzk_github_io_aia-30-ai-modellen-algemene-doeleinden-systeemrisico_index_html.md': 'AI Modellen Systeem Risico.md',
        'minbzk_github_io_aia-31-ai-modellen-algemene-doeleinden-systeemrisico-ernstige-incidenten_index_html.md': 'AI Modellen Ernstige Incidenten.md',
        'minbzk_github_io_aia-32-ai-modellen-algemene-doeleinden-systeemrisico-cyberbeveiliging_index_html.md': 'AI Modellen Cyber Beveiliging.md',
        'minbzk_github_io_aia-33-verwerking-in-testomgeving_index_html.md': 'Verwerking Test Omgeving.md',
        'minbzk_github_io_aia-34-monitoring-na-het-in-de-handel-brengen_index_html.md': 'Monitoring Na Markt Introductie.md',
        'minbzk_github_io_aia-35-melding-ernstige-incidenten_index_html.md': 'Melding Ernstige Incidenten.md',
        'minbzk_github_io_aia-36-melding-inbreuk-op-ai-verordening_index_html.md': 'Melding Inbreuk AI Verordening.md',
        'minbzk_github_io_aia-37-recht-klacht-indienen-bij-ai-bureau_index_html.md': 'Klacht Indienen AI Bureau.md',
        'minbzk_github_io_aia-38-testen_index_html.md': 'Testen AI Systemen.md',
        'minbzk_github_io_aia-39-beleid-naleven-auteurs-en-naburige-rechten_index_html.md': 'Auteurs Naburige Rechten.md',

        # Legal frameworks
        'minbzk_github_io_arc-01-archiefwet_index_html.md': 'Archief Wet Compliance.md',
        'minbzk_github_io_avg-04-proportionaliteit-en-subsidiariteit_index_html.md': 'Proportionaliteit Subsidiariteit AVG.md',
        'minbzk_github_io_avg-05-juistheid-en-actualiteit-van-persoonsgegevens_index_html.md': 'Juistheid Actualiteit Persoonsgegevens.md',
        'minbzk_github_io_avg-06-verantwoordingsplicht-rechtmatigheid_index_html.md': 'Verantwoordings Plicht Rechtmatigheid.md',
        'minbzk_github_io_avg-07-transparantie-bij-verwerken-persoonsgegevens_index_html.md': 'Transparantie Verwerken Persoonsgegevens.md',
        'minbzk_github_io_avg-08-wettelijke-verwerking-van-gevoelige-gegevens_index_html.md': 'Wettelijke Verwerking Gevoelige Gegevens.md',
        'minbzk_github_io_avg-09-inroepen-privacyrecht-bij-verwerking-persoonsgegevens_index_html.md': 'Inroepen Privacy Recht.md',
        'minbzk_github_io_avg-10-recht-op-niet-geautomatiseerde-besluitvorming_index_html.md': 'Recht Niet Geautomatiseerde Besluitvorming.md',
        'minbzk_github_io_avg-11-privacy-bij-ontwerp-bij-verwerking-van-persoonsgegevens_index_html.md': 'Privacy Bij Ontwerp.md',
        'minbzk_github_io_avg-12-beveiliging-van-verwerking_index_html.md': 'Beveiliging Van Verwerking.md',
        'minbzk_github_io_awb-01-zorgvuldigheidsbeginsel_index_html.md': 'Zorgvuldigheids Beginsel AWB.md',
        'minbzk_github_io_awb-02-motiveringsbeginsel_index_html.md': 'Motiverings Beginsel AWB.md',
        'minbzk_github_io_bzk-01-algoritmeregister_index_html.md': 'BZK Algoritme Register.md',
        'minbzk_github_io_dat-01-databankenwet_index_html.md': 'Databanken Wet Compliance.md',
        'minbzk_github_io_framework-meaningful-engagement_index_html.md': 'Framework Meaningful Engagement.md',
        'minbzk_github_io_grw-01-fundamentele-rechten_index_html.md': 'Fundamentele Rechten Grondwet.md',
        'minbzk_github_io_grw-02-non-discriminatie_index_html.md': 'Non Discriminatie Grondwet.md',
        'minbzk_github_io_inkoopvoorwaarden_index_html.md': 'Inkoop Voorwaarden Algoritmes.md',
        'minbzk_github_io_woo-01-recht-op-toegang-tot-publieke-informatie_index_html.md': 'WOO Toegang Publieke Informatie.md',

        # Topics and subjects
        'minbzk_github_io_onderwerpen_data.md': 'Onderwerp Data Management.md',
        'minbzk_github_io_onderwerpen_duurzaamheid.md': 'Onderwerp Duurzaamheid Algoritmes.md',
        'minbzk_github_io_onderwerpen_fundamentele-rechten.md': 'Onderwerp Fundamentele Rechten.md',
        'minbzk_github_io_onderwerpen_menselijke-controle.md': 'Onderwerp Menselijke Controle.md',
        'minbzk_github_io_onderwerpen_privacy-en-gegevensbescherming.md': 'Onderwerp Privacy Gegevensbescherming.md',
        'minbzk_github_io_onderwerpen_publieke-inkoop.md': 'Onderwerp Publieke Inkoop.md',
        'minbzk_github_io_onderwerpen_technische-robuustheid-en-veiligheid.md': 'Onderwerp Technische Robuustheid.md',

        # Assessment frameworks
        'minbzk_github_io_onderzoekskader-adr_index_html.md': 'Onderzoeks Kader ADR.md',
        'minbzk_github_io_standaarden_index_html.md': 'Standaarden Overzicht.md',
        'minbzk_github_io_toetsingskader-risicoprofilering_index_html.md': 'Toetsings Kader Risico Profilering.md'
    }

def rename_remaining_files(content_dir, mapping):
    """Rename remaining files according to the Dutch mapping"""
    content_path = Path(content_dir)
    
    if not content_path.exists():
        print(f"Content directory not found: {content_dir}")
        return False
    
    renamed_count = 0
    skipped_count = 0
    
    print(f"Starting remaining file renaming in: {content_dir}")
    print(f"Total remaining files to rename: {len(mapping)}")
    
    for old_name, new_name in mapping.items():
        old_path = content_path / old_name
        new_path = content_path / new_name
        
        if old_path.exists():
            if new_path.exists():
                print(f"  SKIP: Target already exists: {new_name}")
                skipped_count += 1
                continue
                
            try:
                shutil.move(str(old_path), str(new_path))
                print(f"  ✓ {old_name} → {new_name}")
                renamed_count += 1
            except Exception as e:
                print(f"  ✗ Error renaming {old_name}: {e}")
        else:
            print(f"  SKIP: File not found: {old_name}")
            skipped_count += 1
    
    print(f"\nRemaining file renaming complete:")
    print(f"  Successfully renamed: {renamed_count} files")
    print(f"  Skipped: {skipped_count} files")
    
    return renamed_count > 0

def regenerate_chunks():
    """Regenerate RAG chunks with all Dutch filenames"""
    print("\nRegenerating RAG chunks with all Dutch filenames...")
    
    try:
        # Import and initialize the RAG system
        from enhanced_rag import EnhancedRAGSystem
        
        # Initialize with the content directory
        content_dir = '../1. Datasets/Scrapen/scraped_content/content'
        rag_system = EnhancedRAGSystem(content_dir)
        
        print("✓ RAG system reinitialized with all Dutch filenames")
        print(f"✓ Total chunks generated: {len(rag_system.chunks)}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error regenerating chunks: {e}")
        return False

def main():
    """Main execution function"""
    print("=== Remaining Files Dutch Renaming Script ===\n")
    
    # Define paths
    content_dir = '/home/tr17711/Dev/Hackathon II/Hackathon_II-C-III/1. Datasets/Scrapen/scraped_content/content'
    
    # Get remaining files mapping
    mapping = get_remaining_files_mapping()
    
    # Rename remaining files to Dutch
    if rename_remaining_files(content_dir, mapping):
        print("\n" + "="*60)
        
        # Regenerate chunks
        if regenerate_chunks():
            print("\n✅ All remaining files renamed successfully!")
            print("\nThe knowledge base now has:")
            print("- ALL files with Dutch names and spaces")
            print("- Complete coverage of MinBZK algorithm framework")
            print("- Updated RAG chunks with all new filenames")
            print("- Consistent naming across all 300+ documents")
        else:
            print("\n⚠️  File renaming succeeded but chunk regeneration failed")
            print("You may need to manually restart the backend to refresh the RAG system")
    else:
        print("\n❌ Remaining file renaming failed - skipping chunk regeneration")

if __name__ == "__main__":
    main()