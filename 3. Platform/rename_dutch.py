#!/usr/bin/env python3
"""
Script to rename markdown files to Dutch names with spaces
"""

import os
import shutil
import sys
from pathlib import Path

# Add the enhanced_rag.py to path
sys.path.append('/home/tr17711/Dev/Hackathon II/Hackathon_II-C-III/3. Platform')

def get_dutch_renaming_mapping():
    """Return comprehensive file renaming mapping to Dutch names with spaces"""
    return {
        # Algorithm & AI Governance
        'algorithm_governance_framework.md': 'Algoritme Governance Kader.md',
        'ai_bias_prevention.md': 'AI Bias Preventie.md',
        'ai_transparency_requirements.md': 'AI Transparantie Eisen.md',
        'eu_ai_act_compliance.md': 'EU AI Act Naleving.md',
        'ai_impact_assessment_tool.md': 'AI Impact Assessment Tool.md',
        'ethics_ai_assessment.md': 'Ethiek AI Beoordeling.md',
        'algorithm_registry_guide.md': 'Algoritme Register Handleiding.md',
        'generative_ai_guidance.md': 'Generatieve AI Richtlijnen.md',
        'algorithm_definition_guide.md': 'Wat Is Een Algoritme.md',
        'ai_risk_assessment.md': 'AI Risico Beoordeling.md',
        
        # Privacy & Data Protection (GDPR/AVG)
        'gdpr_basics_dutch.md': 'AVG Basis Nederlandse.md',
        'gdpr_basics_english.md': 'GDPR Basis Engels.md',
        'gdpr_lawful_processing.md': 'AVG Rechtmatige Verwerking.md',
        'gdpr_data_retention.md': 'AVG Data Bewaring.md',
        'gdpr_data_minimization.md': 'AVG Data Minimalisatie.md',
        'gdpr_dpia_mandatory.md': 'DPIA Verplicht AVG.md',
        'gdpr_request_handling.md': 'AVG Verzoeken Afhandelen.md',
        'gdpr_comprehensive_guide.md': 'AVG Uitgebreide Handleiding.md',
        
        # Common Ground Architecture
        'common_ground_principles.md': 'Common Ground Principes.md',
        'common_ground_overview.md': 'Common Ground Overzicht.md',
        'common_ground_quick_guide.md': 'Common Ground Snelgids.md',
        'common_ground_solutions.md': 'Common Ground Oplossingen.md',
        'common_ground_platform.md': 'Common Ground Platform.md',
        'common_ground_collaboration.md': 'Common Ground Samenwerking.md',
        'common_ground_showcase.md': 'Common Ground Etalage.md',
        'common_ground_explained.md': 'Common Ground Uitleg.md',
        'common_ground_benefits.md': 'Common Ground Voordelen.md',
        'common_ground_transition_explained.md': 'Common Ground Transitie.md',
        
        # Municipal Architecture (GEMMA/NORA) 
        'gemma_process_architecture.md': 'GEMMA Proces Architectuur.md',
        'gemma_model_architecture.md': 'GEMMA Model Architectuur.md',
        'gemma_common_ground_theme.md': 'GEMMA Common Ground.md',
        'gemma_architect_training.md': 'GEMMA Architect Training.md',
        'nora_reference_architecture.md': 'NORA Referentie Architectuur.md',
        'nora_wikipedia_overview.md': 'NORA Wikipedia Overzicht.md',
        'nora_derived_architectures.md': 'NORA Afgeleide Architecturen.md',
        'nora_online_platform.md': 'NORA Online Platform.md',
        'nora_strategy_supplement.md': 'NORA Strategie Supplement.md',
        'eif_nora_crossreference.md': 'EIF NORA Kruisverwijzing.md',
        'digital_gov_nora_overview.md': 'Digitale Overheid NORA.md',
        
        # Smart Cities & Innovation
        'smart_city_deal_program.md': 'Smart City Deal.md',
        'amsterdam_ai_assistant.md': 'Amsterdam AI Assistent.md',
        'smart_city_innovation_urgency.md': 'Smart City Innovatie.md',
        'innovation_funding_digital_areas.md': 'Innovatiegeld Digitale Gebieden.md',
        'amsterdam_civil_servant_ai.md': 'Amsterdam Ambtenaren AI.md',
        
        # Digital Government Services
        'digital_gov_public_values.md': 'Digitale Overheid Publieke Waarden.md',
        'user_centered_design.md': 'Gebruiker Centraal Ontwerp.md',
        'user_centered_themes.md': 'Gebruiker Centraal Themas.md',
        'digital_accessibility_guide.md': 'Digitale Toegankelijkheid Gids.md',
        'values_driven_digital_transition.md': 'Waarden Gedreven Digitale Transitie.md',
        'vng_digital_agenda_2028.md': 'VNG Digitale Agenda.md',
        'digital_transformation_leadership.md': 'Digitale Transformatie Leiderschap.md',
        'digital_government_page7.md': 'Digitale Overheid Pagina.md',
        'digital_ambassadors_final_report.md': 'Digitale Ambassadeurs Rapport.md',
        'digital_work_agenda_progress.md': 'Digitale Werkagenda Voortgang.md',
        
        # Legal & Compliance Frameworks
        'government_legislation_portal.md': 'Overheid Wetgeving Portaal.md',
        'open_government_act.md': 'Wet Open Overheid.md',
        'freedom_information_act.md': 'Wet Openbaarheid Bestuur.md',
        'freedom_info_act_outline.md': 'WOO Hoofdlijnen Wet.md',
        'wob_to_woo_transition_guide.md': 'WOB Naar WOO.md',
        'new_archive_act_adopted.md': 'Nieuwe Archiefwet Aangenomen.md',
        'archive_act_news.md': 'Archiefwet Nieuws Artikel.md',
        'electronic_admin_traffic_act.md': 'Elektronisch Bestuurlijk Verkeer.md',
        'legislation_calendar_entry.md': 'Wetgevingskalender Entry.md',
        'national_archive_legitimacy.md': 'Nationaal Archief Legitimiteit.md',
        'national_archive_legislation.md': 'Nationaal Archief Wetgeving.md',
        'environment_act_content.md': 'Omgevingswet Inhoud.md',
        'local_regulation_cvdr.md': 'Lokale Regelgeving CVDR.md',
        
        # Standards & Procurement
        'standards_forum_main.md': 'Forum Standaardisatie Hoofdpagina.md',
        'standards_forum_intro.md': 'Forum Standaardisatie Introductie.md',
        'standards_comply_explain_policy.md': 'Pas Toe Leg Uit.md',
        'mandatory_open_standards_list.md': 'Verplichte Open Standaarden.md',
        'standards_what_to_do.md': 'Standaarden Wat Doen.md',
        'why_standardization_matters.md': 'Waarom Standaardisatie Belangrijk.md',
        'procurement_obligation_rules.md': 'Aanbestedingsplicht Regels.md',
        'procurement_assignment_design.md': 'Opdracht Vormgeven Aanbesteding.md',
        'procurement_requirements_specs.md': 'Programma Van Eisen.md',
        'digital_procurement_guide.md': 'Digitaal Aanbesteden Gids.md',
        'european_procurement_guide.md': 'Europees Aanbesteden Gids.md',
        'project_requirements_content.md': 'Project Eisen Inhoud.md',
        'requirements_specification_checklist.md': 'Eisen Specificatie Checklist.md',
        
        # Security & Information Management
        'digital_resilience_project.md': 'Digitale Weerbaarheid Project.md',
        'information_security_baseline.md': 'Informatie Beveiliging Baseline.md',
        'proactive_disclosure_project.md': 'Actieve Openbaarmaking Project.md',
        'government_cybersecurity_violations.md': 'Overheid Cyberveiligheid Overtredingen.md',
        'digital_autonomy_sovereignty.md': 'Digitale Autonomie Soevereiniteit.md',
        
        # GitHub Organizations & Development
        'amsterdam_github_repos.md': 'Amsterdam GitHub Repositories.md',
        'vng_github_development.md': 'VNG GitHub Ontwikkeling.md',
        'utrecht_github_repos.md': 'Utrecht GitHub Repositories.md',
        'public_sector_nl_github.md': 'Publieke Sector GitHub.md',
        'amsterdam_github_pages.md': 'Amsterdam GitHub Pages.md',
        
        # Training & Capacity Building
        'gov_it_academy_projects.md': 'IT Academie Overheid.md',
        'government_organization_odi.md': 'Rijksorganisatie ODI.md',
        'cio_assessment_process.md': 'CIO Oordeel Proces.md',
        'ict_advisory_college.md': 'ICT Toetsing Adviescollege.md',
        'government_cio_system_ineffective.md': 'CIO Stelsel Ineffectief.md',
        
        # Innovation & Funding
        'innovation_budget_rules_2024.md': 'Innovatiebudget Reglement 2024.md',
        'innovation_budget_recipients.md': 'Innovatiebudget Ontvangers.md',
        'innovation_budget_new_round.md': 'Innovatiebudget Nieuwe Ronde.md',
        'subsidy_financing_wis.md': 'Subsidie Financiering WIS.md',
        'europe_digital_ambitions.md': 'Europa Digitale Ambities.md',
        'european_digital_commons.md': 'Europese Digitale Gemeenschapsgoederen.md',
        'new_european_digital_cooperation.md': 'Nieuwe Europese Digitale Samenwerking.md',
        'digital_decade_initiative.md': 'Digital Decade Initiatief.md',
        'digital_decade_multiyear_approach.md': 'Digital Decade Meerjarige Aanpak.md',
        
        # AI Ethics & Implementation
        'ai_civil_servant_satisfaction.md': 'AI Ambtenaar Werkplezier.md',
        'civil_servants_ai_application_space.md': 'Ambtenaren AI Toepassing.md',
        'government_ai_implementation_pace.md': 'Overheid AI Implementatie.md',
        'parliament_algorithm_transparency.md': 'Kamer Algoritme Transparantie.md',
        'dutch_ai_coalition_impact.md': 'Nederlandse AI Coalitie.md',
        'tno_ai_government_deployment.md': 'TNO AI Overheid.md',
        'future_proof_ai_society.md': 'Toekomstbestendige AI Maatschappij.md',
        'agentic_ai_explanation.md': 'Agentic AI Uitleg.md',
        
        # Logius & Standards
        'logius_main_services.md': 'Logius Hoofddiensten.md',
        'digid_saml_authentication_spec.md': 'DigiD SAML Authenticatie.md',
        'logius_standards_services.md': 'Logius Standaarden Diensten.md',
        'logius_api_adr_standards.md': 'Logius API ADR.md',
        
        # VNG Projects & Initiatives
        'vng_digital_brochure.md': 'VNG Digitale Brochure.md',
        'vng_municipal_implementation.md': 'VNG Gemeentelijke Uitvoering.md',
        'vng_digital_security_privacy.md': 'VNG Digitale Veiligheid.md',
        'vng_gibit_project.md': 'VNG GIBIT Project.md',
        'vng_microsoft_collaboration.md': 'VNG Microsoft Samenwerking.md',
        'vng_signalen_project.md': 'VNG Signalen Project.md',
        'vng_wmebv_regulation.md': 'VNG WMEBV Regelgeving.md',
        'signalen_platform_main.md': 'Signalen Platform Hoofdpagina.md',
        'vrij_brp_platform.md': 'VrijBRP Platform.md',
        'vng_information_management.md': 'VNG Informatie Management.md',
        
        # Project Management & Evaluation
        'evaluation_five_steps_guide.md': 'Evaluatie Vijf Stappen.md',
        'large_ict_projects_report_2021.md': 'Grote ICT Projecten.md',
        'government_finances_chapter7.md': 'Rijksfinancien Hoofdstuk 7.md',
        'government_finances_section.md': 'Rijksfinancien Onderdeel.md',
        'ethical_innovation_toolbox.md': 'Ethische Innovatie Toolbox.md',
        'social_government_nora.md': 'Social Overheid NORA.md',
        'italian_government_software.md': 'Italiaanse Overheid Software.md',
        'digital_accessibility_project.md': 'Digitale Toegankelijkheid Project.md',
        'cabinet_change_admin_guide.md': 'Kabinetswissel Ambtenaren Gids.md',
        'open_pdd_environment.md': 'Open PDD Omgeving.md',
        'architecture_design_requirements.md': 'Architectuur Ontwerp Eisen.md',
        'proactive_disclosure_implementation.md': 'Actieve Openbaarmaking Implementatie.md',
        'woensdrecht_administrative_info.md': 'Woensdrecht Bestuurlijke Informatie.md',
        
        # MinBZK Algorithm Framework Files (detailed mapping for key files)
        'algorithm_inventory_process.md': 'Algoritmes Inventariseren.md',
        'algorithm_expertise_capacity.md': 'Algoritme Expertise Capaciteit.md',
        'algorithm_policy_development.md': 'Algoritme Beleid Opstellen.md',
        'algorithm_risk_management.md': 'Algoritme Risicobeheer.md',
        'algorithm_political_responsibility.md': 'Politiek Bestuurlijke Verantwoordelijkheid.md',
        'algorithm_existing_governance.md': 'Bestaande Algoritme Governance.md',
        'algorithm_maturity_model.md': 'Algoritme Volwassenheidsmodel.md',
        'algorithm_internal_oversight.md': 'Intern Toezicht Algoritmes.md',
        'algorithm_lifecycle_decisions.md': 'Algoritme Levenscyclus Besluiten.md',
        'algorithm_risk_category_governance.md': 'Algoritme Governance Risicocategorie.md',
        'algorithm_governance_responsibilities.md': 'Algoritme Governance Verantwoordelijkheden.md',
        'algorithm_user_management.md': 'Algoritme Gebruikersbeheer.md',
        'algorithm_quality_evaluation.md': 'Algoritme Kwaliteit Evaluatie.md',
        'algorithm_password_management.md': 'Algoritme Wachtwoordbeheer.md',
        'algorithm_change_process.md': 'Algoritme Wijzigingenproces.md',
        'algorithm_discrimination_protocol.md': 'Algoritme Discriminatie Protocol.md',
        'algorithm_awareness_training.md': 'Algoritme Bewustwording Training.md',
        
        # Continue with remaining MinBZK files
        'problem_definition_formulation.md': 'Probleemdefinitie Formuleren.md',
        'objective_formulation.md': 'Doelstelling Formuleren.md',
        'algorithm_use_justification.md': 'Algoritme Gebruik Onderbouwen.md',
        'stakeholder_involvement.md': 'Belanghebbenden Betrekken.md',
        'legal_basis_requirement.md': 'Wettelijke Grondslag.md',
        'multidisciplinary_procurement_team.md': 'Multidisciplinair Inkoopteam.md',
        
        # Data management files
        'data_quality_management.md': 'Data Kwaliteit Management.md',
        'variable_suitability_testing.md': 'Variabelen Geschiktheid Toetsen.md',
        'personal_data_retention.md': 'Persoonsgegevens Bewaartermijnen.md',
        'pseudonymization_anonymization.md': 'Pseudonimiseren Anonimiseren.md',
        'data_minimization_principle.md': 'Data Minimalisatie Principe.md',
        'fair_data_principles.md': 'FAIR Data Principes.md',
        
        # Development & technical files
        'security_by_design.md': 'Security By Design.md',
        'system_logging_requirements.md': 'Systeem Logging Eisen.md',
        'system_reproducibility.md': 'Systeem Reproduceerbaarheid.md',
        'parameter_documentation.md': 'Parameter Documentatie.md',
        
        # Verification files
        'system_objective_alignment.md': 'Systeem Doelen Afstemming.md',
        'accuracy_evaluation.md': 'Nauwkeurigheid Evaluatie.md',
        'bias_analysis_process.md': 'Bias Analyse Proces.md',
        'reliability_evaluation.md': 'Betrouwbaarheid Evaluatie.md',
        
        # Implementation files
        'user_work_instructions.md': 'Gebruiker Werkinstructies.md',
        'human_intervention_requirement.md': 'Menselijke Tussenkomst Vereiste.md',
        'algorithm_registry_publication.md': 'Algoritmeregister Publicatie.md',
        'complaint_objection_appeal.md': 'Klacht Bezwaar Beroep.md',
        
        # Monitoring files
        'backup_procedures.md': 'Backup Procedures.md',
        'evaluation_plan_monitoring.md': 'Evaluatieplan Monitoring.md',
        'continuous_monitoring_plan.md': 'Continue Monitoring Plan.md',
        
        # AI Act specific files
        'ai_literacy_requirement.md': 'AI Geletterdheid Vereiste.md',
        'ai_risk_management_system.md': 'AI Risicobeheersysteem.md',
        'ai_human_oversight.md': 'AI Menselijk Toezicht.md',
        'ai_decision_explanation_right.md': 'AI Besluit Uitleg.md',
        'ai_fundamental_rights_impact.md': 'AI Grondrechten Impact.md',
        
        # Framework and guidance files
        'algorithm_framework_legal_compliance.md': 'Algoritme Kader Wetgeving.md',
        'dpia_guidance_framework.md': 'DPIA Richtlijnen Kader.md',
        'iama_impact_assessment.md': 'IAMA Impact Assessment.md',
        'non_discrimination_guidance.md': 'Non Discriminatie Richtlijnen.md',
        'audit_office_assessment_framework.md': 'Rekenkamer Toetsingskader.md'
    }

def rename_files_dutch(content_dir, mapping):
    """Rename files according to the Dutch mapping"""
    content_path = Path(content_dir)
    
    if not content_path.exists():
        print(f"Content directory not found: {content_dir}")
        return False
    
    renamed_count = 0
    skipped_count = 0
    
    print(f"Starting Dutch file renaming in: {content_dir}")
    print(f"Total files to rename: {len(mapping)}")
    
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
    
    print(f"\nDutch renaming complete:")
    print(f"  Successfully renamed: {renamed_count} files")
    print(f"  Skipped: {skipped_count} files")
    
    return renamed_count > 0

def regenerate_chunks():
    """Regenerate RAG chunks with new Dutch filenames"""
    print("\nRegenerating RAG chunks with Dutch filenames...")
    
    try:
        # Import and initialize the RAG system
        from enhanced_rag import EnhancedRAGSystem
        
        # Initialize with the content directory
        content_dir = '../1. Datasets/Scrapen/scraped_content/content'
        rag_system = EnhancedRAGSystem(content_dir)
        
        print("✓ RAG system reinitialized with Dutch filenames")
        print(f"✓ Total chunks generated: {len(rag_system.chunks)}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error regenerating chunks: {e}")
        return False

def main():
    """Main execution function"""
    print("=== Dutch File Renaming and Chunk Regeneration Script ===\n")
    
    # Define paths
    content_dir = '/home/tr17711/Dev/Hackathon II/Hackathon_II-C-III/1. Datasets/Scrapen/scraped_content/content'
    
    # Get Dutch renaming mapping
    mapping = get_dutch_renaming_mapping()
    
    # Rename files to Dutch
    if rename_files_dutch(content_dir, mapping):
        print("\n" + "="*50)
        
        # Regenerate chunks
        if regenerate_chunks():
            print("\n✅ All operations completed successfully!")
            print("\nThe knowledge base now has:")
            print("- Dutch filenames with spaces")
            print("- 3-5 word descriptive names")
            print("- Updated RAG chunks with new filenames")
            print("- Better search and discovery capabilities")
        else:
            print("\n⚠️  File renaming succeeded but chunk regeneration failed")
            print("You may need to manually restart the backend to refresh the RAG system")
    else:
        print("\n❌ Dutch file renaming failed - skipping chunk regeneration")

if __name__ == "__main__":
    main()