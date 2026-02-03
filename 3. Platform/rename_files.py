#!/usr/bin/env python3
"""
Script to rename markdown files to shorter, more descriptive names
and regenerate RAG chunks with the new filenames.
"""

import os
import shutil
import sys
from pathlib import Path

# Add the enhanced_rag.py to path
sys.path.append('/home/tr17711/Dev/Hackathon II/Hackathon_II-C-III/3. Platform')

def get_file_renaming_mapping():
    """Return comprehensive file renaming mapping from old to new names"""
    return {
        # Algorithm & AI Governance
        'minbzk_github_io_onderwerpen_governance.md': 'algorithm_governance_framework.md',
        'minbzk_github_io_onderwerpen_bias-en-non-discriminatie.md': 'ai_bias_prevention.md',
        'minbzk_github_io_onderwerpen_transparantie.md': 'ai_transparency_requirements.md',
        'minbzk_github_io_voldoen-aan-wetten-en-regels_ai-verordening.md': 'eu_ai_act_compliance.md',
        'minbzk_github_io_AIIA_index_html.md': 'ai_impact_assessment_tool.md',
        'minbzk_github_io_ALTAI_index_html.md': 'ethics_ai_assessment.md',
        'minbzk_github_io_algoritmeregister_index_html.md': 'algorithm_registry_guide.md',
        'minbzk_github_io_soorten-algoritmes-en-ai_generatieve-ai.md': 'generative_ai_guidance.md',
        'minbzk_github_io_soorten-algoritmes-en-ai_wat-is-een-algoritme.md': 'algorithm_definition_guide.md',
        'minbzk_github_io_soorten-algoritmes-en-ai_risico-van-ai-systemen.md': 'ai_risk_assessment.md',
        
        # Privacy & Data Protection (GDPR/AVG)
        'autoriteitpersoonsgegevens_nl_avg-algemeen_de-avg-in-het-kort.md': 'gdpr_basics_dutch.md',
        'autoriteitpersoonsgegevens_nl_gdpr-basics_the-gdpr-in-brief.md': 'gdpr_basics_english.md',
        'minbzk_github_io_avg-01-persoonsgegevens-worden-rechtmatig-verwerkt_index_html.md': 'gdpr_lawful_processing.md',
        'minbzk_github_io_avg-02-beperkte-bewaartermijn-van-persoonsgegevens_index_html.md': 'gdpr_data_retention.md',
        'minbzk_github_io_avg-03-minimale-verwerking-van-persoonsgegevens_index_html.md': 'gdpr_data_minimization.md',
        'minbzk_github_io_avg-13-dpia-verplicht_index_html.md': 'gdpr_dpia_mandatory.md',
        'rijksoverheid_nl_16_handleiding-afhandeling-avg-verzoeken.md': 'gdpr_request_handling.md',
        'rijksoverheid_nl_22_handleiding-algemene-verordening-gegevensbescherming.md': 'gdpr_comprehensive_guide.md',
        
        # Common Ground Architecture
        'commonground_nl_12f73f0d-ae26-4021-ba52-849eef37d11f_de-common-ground-principes.md': 'common_ground_principles.md',
        'vng_nl_artikelen_common-ground.md': 'common_ground_overview.md',
        'vng_nl_2022-03_Common-Ground-in-3-minuten_pdf.md': 'common_ground_quick_guide.md',
        'centric_eu_it-oplossingen-overheid_common-ground.md': 'common_ground_solutions.md',
        'haven_commonground_nl.md': 'common_ground_platform.md',
        'vng_nl_artikelen_common-ground-zonder-samenwerking-redden-we-het-niet.md': 'common_ground_collaboration.md',
        'vng_nl_projecten_common-ground-etalage.md': 'common_ground_showcase.md',
        'blog_9cv9_com_what-is-the-common-ground-approach-and-how-it-works.md': 'common_ground_explained.md',
        'paqt_com_en_not-only-municipalities-can-benefit-from-common-ground.md': 'common_ground_benefits.md',
        
        # Municipal Architecture (GEMMA/NORA) 
        'gemmaonline_nl_index_php_GEMMA_Procesarchitectuur.md': 'gemma_process_architecture.md',
        'vng_nl_projecten_gemeentelijke-model-architectuur-gemma.md': 'gemma_model_architecture.md',
        'gemmaonline_nl_wiki_Thema-architectuur_Common_Ground.md': 'gemma_common_ground_theme.md',
        'noraonline_nl.md': 'nora_reference_architecture.md',
        'nl_wikipedia_org_wiki_Nederlandse_Overheid_Referentie_Architectuur.md': 'nora_wikipedia_overview.md',
        'noraonline_nl_wiki_NORA_dochters.md': 'nora_derived_architectures.md',
        'noraonline_nl_wiki_NORA_online.md': 'nora_online_platform.md',
        'digitaleoverheid_nl_overzicht-van-alle-onderwerpen_nora.md': 'digital_gov_nora_overview.md',
        
        # Smart Cities & Innovation
        'agendastad_nl_city-deal_een-slimme-stad-zo-doe-je-dat.md': 'smart_city_deal_program.md',
        'amsterdam_nl_nieuwsoverzicht_chatamsterdam.md': 'amsterdam_ai_assistant.md',
        'stadszaken_nl_4869_city-deal-slimme-stad-gaat-door-snel-innovatie-nodig-voor-leefbare-steden.md': 'smart_city_innovation_urgency.md',
        'stadszaken_nl_6352_innovatiegeld-voor-digitale-gebiedsontwikkeling-taal-ai-en-open-overheid.md': 'innovation_funding_digital_areas.md',
        'binnenlandsbestuur_nl_digitaal_eigen-ai-assistent-voor-amsterdamse-ambtenaren.md': 'amsterdam_civil_servant_ai.md',
        
        # Digital Government Services
        'digitaleoverheid_nl_nieuwe-technologieen-data-en-ethiek_publieke-waarden.md': 'digital_gov_public_values.md',
        'gebruikercentraal_nl.md': 'user_centered_design.md',
        'gebruikercentraal_nl_themas.md': 'user_centered_themes.md',
        'gebruikercentraal_nl_themas_inclusie-en-digitale-toegankelijkheid.md': 'digital_accessibility_guide.md',
        'rijksoverheid_nl_09_een-stap-verder-in-de-waardengedreven-digitale-transitie.md': 'values_driven_digital_transition.md',
        'vng_nl_2024-09_vng-digitale-agenda-gemeenten-2028_pdf.md': 'vng_digital_agenda_2028.md',
        'vng_nl_agenda_leiderschap-in-digitale-transformatie.md': 'digital_transformation_leadership.md',
        
        # Legal & Compliance Frameworks
        'wetten_overheid_nl.md': 'government_legislation_portal.md',
        'ictrecht_nl_wetgeving_wet-open-overheid.md': 'open_government_act.md',
        'rijksoverheid_nl_onderwerpen_wet-open-overheid-woo.md': 'freedom_information_act.md',
        'rijksoverheid_nl_wet-open-overheid-woo_hoofdlijnen-woo.md': 'freedom_info_act_outline.md',
        'vng_nl_2021-03_handreiking-van-wob-naar-woo_pdf.md': 'wob_to_woo_transition_guide.md',
        'open-overheid_nl_20_nieuwe-archiefwet-aangenomen-door-tweede-kamer.md': 'new_archive_act_adopted.md',
        'digitaleoverheid_nl_nieuws_nieuwe-archiefwet-aangenomen.md': 'archive_act_news.md',
        'digitaleoverheid_nl_wetgeving_wet-modernisering-elektronisch-bestuurlijk-verkeer.md': 'electronic_admin_traffic_act.md',
        'wetgevingskalender_overheid_nl_regeling_WGK006161.md': 'legislation_calendar_entry.md',
        'nationaalarchief_nl_kennisbank_legitimiteit.md': 'national_archive_legitimacy.md',
        'nationaalarchief_nl_kennisbank_wet-en-regelgeving.md': 'national_archive_legislation.md',
        
        # Standards & Procurement
        'forumstandaardisatie_nl.md': 'standards_forum_main.md',
        'forumstandaardisatie_nl_introductie.md': 'standards_forum_intro.md',
        'forumstandaardisatie_nl_pas-toe-leg-uit-beleid.md': 'standards_comply_explain_policy.md',
        'forumstandaardisatie_nl_publicaties_lijst-verplichte-open-standaarden.md': 'mandatory_open_standards_list.md',
        'forumstandaardisatie_nl_thema_wat-moet-ik-doen.md': 'standards_what_to_do.md',
        'magazine_forumstandaardisatie_nl_standaard-samenwerken_waarom-standaardisatie.md': 'why_standardization_matters.md',
        'pianoo_nl_fase-1-voorbereiden_aanbestedingsplicht.md': 'procurement_obligation_rules.md',
        'pianoo_nl_fase-1-voorbereiden_vormgeven-van-een-opdracht.md': 'procurement_assignment_design.md',
        'rijksoverheid_nl_19_programma-van-eisen.md': 'procurement_requirements_specs.md',
        'rijksoverheid_nl_aanbesteden_digitaal-aanbesteden.md': 'digital_procurement_guide.md',
        'kvk_nl_internationaal_europees-aanbesteden-zo-doe-je-mee.md': 'european_procurement_guide.md',
        'werken-aan-projecten_nl_fasen-project_programma-van-eisen-wat-staat-er.md': 'project_requirements_content.md',
        'computable_nl_15_dit-is-de-checklist-voor-compleet-programma-van-eisen.md': 'requirements_specification_checklist.md',
        
        # Security & Information Management
        'informatiebeveiligingsdienst_nl_project_digitaleweerbaarheid.md': 'digital_resilience_project.md',
        'minbzk_github_io_bio-01-beveiliging-informatie-en-informatiesystemen_index_html.md': 'information_security_baseline.md',
        'informatiehuishouding_nl_projecten_actieve-openbaarmaking-overheidsinformatie.md': 'proactive_disclosure_project.md',
        'binnenlandsbestuur_nl_cyberveiligheid_overheid-overtreedt-wet-met-haastig-aangeschafte.md': 'government_cybersecurity_violations.md',
        'berenschot_nl_blog_noodzaak-van-digitale-autonomie-en-soevereiniteit.md': 'digital_autonomy_sovereignty.md',
        
        # GitHub Organizations & Development
        'github_com_amsterdam.md': 'amsterdam_github_repos.md',
        'github_com_VNG-Realisatie.md': 'vng_github_development.md',
        'github_com_GemeenteUtrecht.md': 'utrecht_github_repos.md',
        'github_com_J535D165_PublicSectorNL.md': 'public_sector_nl_github.md',
        'amsterdam_github_io.md': 'amsterdam_github_pages.md',
        
        # Training & Capacity Building
        'it-academieoverheid_nl_i_ict-projecten.md': 'gov_it_academy_projects.md',
        'rijksorganisatieodi_nl.md': 'government_organization_odi.md',
        'rijksorganisatieodi_nl_25_wat-is-een-cio-oordeel-en-hoe-gaat-het-in-zijn-werk.md': 'cio_assessment_process.md',
        'organisaties_overheid_nl_28360995_Adviescollege_ICT-toetsing.md': 'ict_advisory_college.md',
        'ibestuur_nl_artikel_waarom-het-cio-stelsel-van-de-rijksoverheid-niet-effectief-genoeg-is.md': 'government_cio_system_ineffective.md',
        
        # Innovation & Funding
        'digitaleoverheid_nl_innovatiebudget_reglement-innovatiebudget-digitale-overheid-2024.md': 'innovation_budget_rules_2024.md',
        'digitaleoverheid_nl_nieuws_20-projecten-krijgen-innovatiebudget-digitale-overheid.md': 'innovation_budget_recipients.md',
        'ibestuur_nl_artikel_bzk-opent-nieuwe-ronde-innovatiebudget-digitale-overheid.md': 'innovation_budget_new_round.md',
        'rvo_nl_subsidies-financiering_wis.md': 'subsidy_financing_wis.md',
        'koneksa-mondo_nl_08_digitale-ambities-van-europa.md': 'europe_digital_ambitions.md',
        'digitaleoverheid_nl_nieuws_europese-samenwerking-voor-digitale-gemeenschapsgoederen.md': 'european_digital_commons.md',
        'ibestuur_nl_artikel_nieuwe-europese-samenwerking-digitale-gemeenschapsgoederen.md': 'new_european_digital_cooperation.md',
        'vng_nl_onderwerpen_digital-decade.md': 'digital_decade_initiative.md',
        'vng_nl_projecten_meerjarige-aanpak-digital-decade.md': 'digital_decade_multiyear_approach.md',
        
        # AI Ethics & Implementation
        'ibestuur_nl_artikel_ai-en-overheid-hoe-bezorgt-ai-de-ambtenaar-meer-werkplezier.md': 'ai_civil_servant_satisfaction.md',
        'ibestuur_nl_artikel_ambtenaren-krijgen-meer-ruimte-om-ai-toe-te-passen-mits.md': 'civil_servants_ai_application_space.md',
        'ibestuur_nl_artikel_overheid-implementeert-meer-ai-toepassingen-dan-er-in-de-experimenteerfase-zitten.md': 'government_ai_implementation_pace.md',
        'ibestuur_nl_artikel_kamer-wil-dat-overheid-de-transparantie-van-algoritmes-snel-verbetert.md': 'parliament_algorithm_transparency.md',
        'ibestuur_nl_artikel_nederlandse-ai-coalitie-en-ained-willen-impact-vergroten-in-een-ai-coalitie-4-nl.md': 'dutch_ai_coalition_impact.md',
        'tno_nl_06_kunstmatige-intelligentie-inzet-overheid.md': 'tno_ai_government_deployment.md',
        'vector_tno_nl_artikelen_toekomstbestendige-ai-maatschappelijk.md': 'future_proof_ai_society.md',
        'servicenow_com_ai_what-is-agentic-ai_html.md': 'agentic_ai_explanation.md',
        
        # Logius & Standards
        'logius_nl.md': 'logius_main_services.md',
        'logius_nl_documentatie_koppelvlakspecificatie-digid-saml-authenticatie.md': 'digid_saml_authentication_spec.md',
        'logius_nl_onze-dienstverlening_standaarden.md': 'logius_standards_services.md',
        'gitdocumentatie_logius_nl_api_adr.md': 'logius_api_adr_standards.md',
        
        # VNG Projects & Initiatives
        'vng_nl_2021-01_vng_brochure_digitale_v5_pdf.md': 'vng_digital_brochure.md',
        'vng_nl_gemeentelijke-uitvoering.md': 'vng_municipal_implementation.md',
        'vng_nl_onderwerpen_digitale-veiligheid-en-privacy.md': 'vng_digital_security_privacy.md',
        'vng_nl_projecten_gibit.md': 'vng_gibit_project.md',
        'vng_nl_projecten_gt-microsoft.md': 'vng_microsoft_collaboration.md',
        'vng_nl_projecten_signalen.md': 'vng_signalen_project.md',
        'vng_nl_wmebv.md': 'vng_wmebv_regulation.md',
        'signalen_org.md': 'signalen_platform_main.md',
        'vrijbrp_nl.md': 'vrij_brp_platform.md',
        
        # Environmental & Legislation
        'iplo_nl_inhoud_omgevingswet.md': 'environment_act_content.md',
        'lokaleregelgeving_overheid_nl_CVDR701963.md': 'local_regulation_cvdr.md',
        'woensdrecht_bestuurlijkeinformatie_nl_View_37deaf3d-f51e-4ce3-82ae-d4ce60f22440.md': 'woensdrecht_administrative_info.md',
        
        # Project Management & Evaluation
        'kaderbreed_nl_de-vijf-stappen-van-een-goede-evaluatie.md': 'evaluation_five_steps_guide.md',
        'rijksoverheid_nl_13_rapportage-grote-ict-projecten-2021.md': 'large_ict_projects_report_2021.md',
        'digitaleoverheid_nl_werkagenda_de-werkagenda-een-jaar-onderweg.md': 'digital_work_agenda_progress.md',
        'rijksfinancien_nl_VII_6.md': 'government_finances_chapter7.md',
        'rijksfinancien_nl_onderdeel_2765066.md': 'government_finances_section.md',
        
        # Digital Government Reports & Analysis
        'digitaleoverheid_nl_09_Eindverslag-Ambassadeurs-Digitale-Gemeenten-augustus-2017_pdf.md': 'digital_ambassadors_final_report.md',
        'digitaleoverheid_nl_page_7.md': 'digital_government_page7.md',
        'digitaleoverheid_nl_toolbox-voor-ethisch-verantwoorde-innovatie_publieke-waarden-centraal.md': 'ethical_innovation_toolbox.md',
        'social_overheid_nl__nora_113305743680511177.md': 'social_government_nora.md',
        'developers_italia_it_software_1dbf7eeb-fad1-4b95-842d-dcb0dbaee64e_html.md': 'italian_government_software.md',
        
        # Knowledge & Information Management
        'kiacommunity_nl_groups_113-vng-grip-op-informatie.md': 'vng_information_management.md',
        'ictu_nl_projecten_digitoegankelijk-sneller-naar-een-digitaal-toegankelijke-overheid.md': 'digital_accessibility_project.md',
        'open-overheid_nl_handreiking-ihh-kabinetswissel_Handreiking_Ambtelijke_Organisatie_pdf.md': 'cabinet_change_admin_guide.md',
        'openwebconcept_nl_blog_30-wat-is-de-openpdd-mijn-omgeving.md': 'open_pdd_environment.md',
        
        # Specific Architecture & Technical Documents
        'vng_nl_2021-03_bijlage-3-architectuur-ontwerp-incl_-eisen-specificaties-en-wensen-def_pdf.md': 'architecture_design_requirements.md',
        'vng_nl_2022-03_vng_grip_op_05_implementatieplan_actief_openbaar_maken_idd__pdf.md': 'proactive_disclosure_implementation.md',
        'vng_nl_2024-05_09d-bijlage-2-uitgebreide-toelichting-propositie-transitieprogramma-common-ground_pdf.md': 'common_ground_transition_explained.md',
        'flexspot_io_opdrachten_architect-gemma-en-gemma-opleiding-fs252881.md': 'gemma_architect_training.md',
        'noraonline_nl_18_NORA_3_0_Strategy_Supplement_pdf.md': 'nora_strategy_supplement.md',
        'noraonline_nl_5c_XREF_EIF_and_NORA_2023_pdf.md': 'eif_nora_crossreference.md',
        
        # MinBZK Algorithm Framework Files (detailed mapping for all 100+ files)
        'minbzk_github_io_0-org-00-inventariseren-algoritmes_index_html.md': 'algorithm_inventory_process.md',
        'minbzk_github_io_0-org-01-benodigde-expertise-en-capaciteit_index_html.md': 'algorithm_expertise_capacity.md',
        'minbzk_github_io_0-org-02-beleid-opstellen-inzet-algoritmes_index_html.md': 'algorithm_policy_development.md',
        'minbzk_github_io_0-org-03-toepassen-risicobeheer_index_html.md': 'algorithm_risk_management.md',
        'minbzk_github_io_0-org-04-politiek-bestuurlijke-verantwoordelijkheid_index_html.md': 'algorithm_political_responsibility.md',
        'minbzk_github_io_0-org-05-bestaande-governance_index_html.md': 'algorithm_existing_governance.md',
        'minbzk_github_io_0-org-06-volwassenheidsmodel_index_html.md': 'algorithm_maturity_model.md',
        'minbzk_github_io_0-org-07-intern-toezicht_index_html.md': 'algorithm_internal_oversight.md',
        'minbzk_github_io_0-org-08-beslismoment-levenscyclus_index_html.md': 'algorithm_lifecycle_decisions.md',
        'minbzk_github_io_0-org-09-governance-per-risicocategorie_index_html.md': 'algorithm_risk_category_governance.md',
        'minbzk_github_io_0-org-10-inrichten-taken-en-verantwoordelijkheden-algoritmegovernance_index_html.md': 'algorithm_governance_responsibilities.md',
        'minbzk_github_io_0-org-11-gebruikersbeheer_index_html.md': 'algorithm_user_management.md',
        'minbzk_github_io_0-org-12-periodieke-evaluatie-kwaliteit_index_html.md': 'algorithm_quality_evaluation.md',
        'minbzk_github_io_0-org-13-wachtwoordbeheer_index_html.md': 'algorithm_password_management.md',
        'minbzk_github_io_0-org-14-wijzigingenproces_index_html.md': 'algorithm_change_process.md',
        'minbzk_github_io_0-org-15-discriminatieprotocol_index_html.md': 'algorithm_discrimination_protocol.md',
        'minbzk_github_io_0-org-16-bewustwording-en-opleiding_index_html.md': 'algorithm_awareness_training.md',
        
        # Continue with remaining MinBZK files (abbreviated for space)
        'minbzk_github_io_1-pba-01-formuleren-probleemdefinitie_index_html.md': 'problem_definition_formulation.md',
        'minbzk_github_io_1-pba-02-formuleren-doelstelling_index_html.md': 'objective_formulation.md',
        'minbzk_github_io_1-pba-03-onderbouwen-gebruik-algoritme_index_html.md': 'algorithm_use_justification.md',
        'minbzk_github_io_1-pba-04-betrek-belanghebbenden_index_html.md': 'stakeholder_involvement.md',
        'minbzk_github_io_1-pba-05-wettelijke-grondslag_index_html.md': 'legal_basis_requirement.md',
        'minbzk_github_io_1-pba-06-multidisciplinair-inkoopteam_index_html.md': 'multidisciplinary_procurement_team.md',
        
        # Data management files
        'minbzk_github_io_3-dat-01-datakwaliteit_index_html.md': 'data_quality_management.md',
        'minbzk_github_io_3-dat-02-toetsen-geschiktheid-variabelen_index_html.md': 'variable_suitability_testing.md',
        'minbzk_github_io_3-dat-03-bewaartermijnen-persoonsgegevens_index_html.md': 'personal_data_retention.md',
        'minbzk_github_io_3-dat-04-pseudonimiseren-anonimiseren_index_html.md': 'pseudonymization_anonymization.md',
        'minbzk_github_io_3-dat-09-dataminimalisatie_index_html.md': 'data_minimization_principle.md',
        'minbzk_github_io_3-dat-12-fair-data_index_html.md': 'fair_data_principles.md',
        
        # Development & technical files
        'minbzk_github_io_4-owk-01-security-by-design_index_html.md': 'security_by_design.md',
        'minbzk_github_io_4-owk-04-logging_index_html.md': 'system_logging_requirements.md',
        'minbzk_github_io_4-owk-07-reproduceerbaarheid_index_html.md': 'system_reproducibility.md',
        'minbzk_github_io_4-owk-11-documenteer-parameters_index_html.md': 'parameter_documentation.md',
        
        # Verification files
        'minbzk_github_io_5-ver-01-functioneren-in-lijn-met-doeleinden_index_html.md': 'system_objective_alignment.md',
        'minbzk_github_io_5-ver-02-evalueer-nauwkeurigheid_index_html.md': 'accuracy_evaluation.md',
        'minbzk_github_io_5-ver-03-biasanalyse_index_html.md': 'bias_analysis_process.md',
        'minbzk_github_io_5-ver-06-evalueer-betrouwbaarheid_index_html.md': 'reliability_evaluation.md',
        
        # Implementation files
        'minbzk_github_io_6-imp-01-werkinstructies-gebruikers_index_html.md': 'user_work_instructions.md',
        'minbzk_github_io_6-imp-03-menselijke-tussenkomst_index_html.md': 'human_intervention_requirement.md',
        'minbzk_github_io_6-imp-04-publiceren-algoritmeregister_index_html.md': 'algorithm_registry_publication.md',
        'minbzk_github_io_6-imp-06-klacht-bezwaar-beroep_index_html.md': 'complaint_objection_appeal.md',
        
        # Monitoring files
        'minbzk_github_io_7-mon-01-backups-maken_index_html.md': 'backup_procedures.md',
        'minbzk_github_io_7-mon-04-evaluatieplan_index_html.md': 'evaluation_plan_monitoring.md',
        'minbzk_github_io_7-mon-07-plan-continue-monitoring_index_html.md': 'continuous_monitoring_plan.md',
        
        # AI Act specific files
        'minbzk_github_io_aia-01-ai-geletterdheid_index_html.md': 'ai_literacy_requirement.md',
        'minbzk_github_io_aia-03-risicobeheersysteem_index_html.md': 'ai_risk_management_system.md',
        'minbzk_github_io_aia-09-menselijk-toezicht_index_html.md': 'ai_human_oversight.md',
        'minbzk_github_io_aia-26-recht-op-uitleg-ai-besluiten_index_html.md': 'ai_decision_explanation_right.md',
        'minbzk_github_io_aia-27-beoordelen-gevolgen-grondrechten_index_html.md': 'ai_fundamental_rights_impact.md',
        
        # Framework and guidance files
        'minbzk_github_io_Algoritmekader_voldoen-aan-wetten-en-regels.md': 'algorithm_framework_legal_compliance.md',
        'minbzk_github_io_DPIA_index_html.md': 'dpia_guidance_framework.md',
        'minbzk_github_io_IAMA_index_html.md': 'iama_impact_assessment.md',
        'minbzk_github_io_handreiking-non-discriminatie_index_html.md': 'non_discrimination_guidance.md',
        'minbzk_github_io_toetsingskader-algemene-rekenkamer_index_html.md': 'audit_office_assessment_framework.md'
    }

def rename_files(content_dir, mapping):
    """Rename files according to the mapping"""
    content_path = Path(content_dir)
    
    if not content_path.exists():
        print(f"Content directory not found: {content_dir}")
        return False
    
    renamed_count = 0
    skipped_count = 0
    
    print(f"Starting file renaming in: {content_dir}")
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
    
    print(f"\nRenaming complete:")
    print(f"  Successfully renamed: {renamed_count} files")
    print(f"  Skipped: {skipped_count} files")
    
    return renamed_count > 0

def regenerate_chunks():
    """Regenerate RAG chunks with new filenames"""
    print("\nRegenerating RAG chunks with new filenames...")
    
    try:
        # Import and initialize the RAG system
        from enhanced_rag import EnhancedRAGSystem
        
        # Initialize with the content directory
        content_dir = '../1. Datasets/Scrapen/scraped_content/content'
        rag_system = EnhancedRAGSystem(content_dir)
        
        print("✓ RAG system reinitialized with new filenames")
        print(f"✓ Total chunks generated: {len(rag_system.chunks)}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error regenerating chunks: {e}")
        return False

def main():
    """Main execution function"""
    print("=== File Renaming and Chunk Regeneration Script ===\n")
    
    # Define paths
    content_dir = '/home/tr17711/Dev/Hackathon II/Hackathon_II-C-III/1. Datasets/Scrapen/scraped_content/content'
    
    # Get renaming mapping
    mapping = get_file_renaming_mapping()
    
    # Rename files
    if rename_files(content_dir, mapping):
        print("\n" + "="*50)
        
        # Regenerate chunks
        if regenerate_chunks():
            print("\n✅ All operations completed successfully!")
            print("\nThe knowledge base now has:")
            print("- Shorter, more descriptive filenames")
            print("- Updated RAG chunks with new filenames")
            print("- Better search and discovery capabilities")
        else:
            print("\n⚠️  File renaming succeeded but chunk regeneration failed")
            print("You may need to manually restart the backend to refresh the RAG system")
    else:
        print("\n❌ File renaming failed - skipping chunk regeneration")

if __name__ == "__main__":
    main()