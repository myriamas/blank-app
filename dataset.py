import pandas as pd

# I build here the master requirement table for the Digital Regulatory Twin
data_requirements = [
    {
        "Nom": "Traçabilité complète des données de sécurité en Phase I",
        "Type_element": "Exigence",
        "Phase": "Phase I",
        "Type_exigence": "Sécurité",
        "Description": "Toutes les données d'innocuité doivent être tracées, horodatées et documentées selon GCP.",
        "Statut": "Conforme",
        "Impact_AMM": "Critique",
        "Documents_lies": "Protocole clinique Phase I",
        "Preuves_liees": "CRF, base eCRF, listings de sécurité",
        "IoT": "",
        "Frequence": "",
        "Certificat_etalonnage": "",
        "Process_qualite": "Gestion des données cliniques GCP",
        "Fiche_protocole": "VIH_VAX_P1_PROTOCOL.pdf"
    },
    {
        "Nom": "Sécurité long terme (24 mois)",
        "Type_element": "Exigence",
        "Phase": "Phase I–III",
        "Type_exigence": "Sécurité",
        "Description": "Surveillance sécurité des volontaires pendant au moins 24 mois après vaccination.",
        "Statut": "Conforme",
        "Impact_AMM": "Critique",
        "Documents_lies": "Rapport de sécurité longue durée (24 mois)",
        "Preuves_liees": "Base de PV, rapports périodiques",
        "IoT": "",
        "Frequence": "",
        "Certificat_etalonnage": "",
        "Process_qualite": "Plan de pharmacovigilance VIH",
        "Fiche_protocole": "PV_PLAN_VIH.pdf"
    },
    {
        "Nom": "Stérilité des lots cliniques",
        "Type_element": "Exigence",
        "Phase": "Phase I",
        "Type_exigence": "Qualité",
        "Description": "Tous les lots cliniques doivent être testés et certifiés stériles.",
        "Statut": "Conforme",
        "Impact_AMM": "Modéré",
        "Documents_lies": "Certificat de stérilité du lot clinique",
        "Preuves_liees": "Rapports de stérilité CL-0001",
        "IoT": "Température chambre stérile",
        "Frequence": "En continu",
        "Certificat_etalonnage": "Certificat étalonnage incubateur",
        "Process_qualite": "Contrôle de stérilité GMP",
        "Fiche_protocole": "STERILITY_SOP.pdf"
    },
    {
        "Nom": "Validation analytique des méthodes ELISA/neutralisation VIH",
        "Type_element": "Exigence",
        "Phase": "Préclinique",
        "Type_exigence": "Qualité",
        "Description": "Méthodes analytiques validées (spécificité, sensibilité, répétabilité).",
        "Statut": "Non conforme",
        "Impact_AMM": "Modéré",
        "Documents_lies": "Qualification méthodes analytiques",
        "Preuves_liees": "Capture ELISA, rapports de validation",
        "IoT": "",
        "Frequence": "",
        "Certificat_etalonnage": "Certificat étalonnage lecteurs ELISA",
        "Process_qualite": "Validation de méthode selon ICH Q2",
        "Fiche_protocole": "ELISA_VALIDATION_REPORT.pdf"
    },
    {
        "Nom": "Stabilité 2–8°C sur 24 mois",
        "Type_element": "Exigence",
        "Phase": "AMM",
        "Type_exigence": "Qualité",
        "Description": "Démontrer la stabilité du vaccin à 2–8°C sur au moins 24 mois.",
        "Statut": "Non conforme",
        "Impact_AMM": "Critique",
        "Documents_lies": "Étude de stabilité 24 mois",
        "Preuves_liees": "Tableau stabilité 24 mois",
        "IoT": "Température frigos QC",
        "Frequence": "Quotidienne",
        "Certificat_etalonnage": "Certificats sondes de température",
        "Process_qualite": "Programme de stabilité ICH",
        "Fiche_protocole": "STABILITY_PROTOCOL_2_8C.pdf"
    },
    {
        "Nom": "Réponse immunitaire humorale (anticorps neutralisants)",
        "Type_element": "Exigence",
        "Phase": "Phase II",
        "Type_exigence": "Efficacité",
        "Description": "Mesure des anticorps neutralisants VIH au-dessus d'un seuil minimal d'immunogénicité.",
        "Statut": "Partiel",
        "Impact_AMM": "Critique",
        "Documents_lies": "Rapport immunogénicité Phase II",
        "Preuves_liees": "Courbes de neutralisation virale",
        "IoT": "",
        "Frequence": "",
        "Certificat_etalonnage": "",
        "Process_qualite": "Plan d'analyse statistique ICH E9",
        "Fiche_protocole": "IMMUNO_P2_ANALYSIS_PLAN.pdf"
    },
    {
        "Nom": "Réponse immunitaire cellulaire CD4+/CD8+",
        "Type_element": "Exigence",
        "Phase": "Phase II",
        "Type_exigence": "Efficacité",
        "Description": "Quantification des lymphocytes CD4+/CD8+ activés (ELISpot/ICS validés).",
        "Statut": "Partiel",
        "Impact_AMM": "Modéré",
        "Documents_lies": "Rapport immunogénicité Phase II",
        "Preuves_liees": "Résultats ELISpot et cytométrie",
        "IoT": "",
        "Frequence": "",
        "Certificat_etalonnage": "",
        "Process_qualite": "Contrôles de qualité de cytométrie",
        "Fiche_protocole": "CELLULAR_IMMUNO_SOP.pdf"
    },
    {
        "Nom": "Documentation complète GxP (préclinique → clinique → production)",
        "Type_element": "Exigence",
        "Phase": "Production",
        "Type_exigence": "Production",
        "Description": "Dossiers qualité, préclinique et production conformes aux standards GxP.",
        "Statut": "Partiel",
        "Impact_AMM": "Important",
        "Documents_lies": "Dossier CMC, rapports GxP",
        "Preuves_liees": "Audit trail, change control, CAPA",
        "IoT": "",
        "Frequence": "",
        "Certificat_etalonnage": "",
        "Process_qualite": "Système qualité pharmaceutique (GMP)",
        "Fiche_protocole": "QMS_MANUAL_VAX_HIV.pdf"
    },
    {
        "Nom": "Conformité Directive 2001/83/CE et Règlement (CE) 726/2004",
        "Type_element": "Règlementation",
        "Phase": "AMM",
        "Type_exigence": "Réglementaire",
        "Description": "Respect du cadre communautaire des médicaments, procédure centralisée EMA et pharmacovigilance.",
        "Statut": "Conforme",
        "Impact_AMM": "Critique",
        "Documents_lies": "Dossier AMM complet (CTD Modules 1–5)",
        "Preuves_liees": "Décision EMA, avis Commission Européenne",
        "IoT": "",
        "Frequence": "",
        "Certificat_etalonnage": "",
        "Process_qualite": "Processus AMM centralisée",
        "Fiche_protocole": "CTD_OVERVIEW_VAX_HIV.pdf"
    },
    {
        "Nom": "Archivage GxP 25 ans (PDF/A + signature + hash SHA-256)",
        "Type_element": "Exigence",
        "Phase": "Tout le cycle de vie",
        "Type_exigence": "PV",
        "Description": "Conserver l'ensemble des documents GxP au minimum 25 ans avec intégrité prouvée (PDF/A, signature qualifiée, SHA-256).",
        "Statut": "Partiel",
        "Impact_AMM": "Important",
        "Documents_lies": "Politique d'archivage VIH",
        "Preuves_liees": "Registre d'archives, métadonnées, checksums",
        "IoT": "",
        "Frequence": "Revue annuelle des archives",
        "Certificat_etalonnage": "",
        "Process_qualite": "Processus d'archivage sécurisé",
        "Fiche_protocole": "ARCHIVING_POLICY_VAX_HIV.pdf"
    },
]

df_master = pd.DataFrame(data_requirements)

# I also build small helper tables for RFLP, lifecycle, IVV, archiving and audit trail

data_rflp = [
    {"Pilier": "Sécurité", "Exigences_clefs": "Evaluer le risque d'ADE, sécurité long terme, tolérance clinique."},
    {"Pilier": "Qualité", "Exigences_clefs": "Contrôle de stérilité, validation des tests VIH, stabilité 24 mois."},
    {"Pilier": "Efficacité", "Exigences_clefs": "Immunité humorale et cellulaire complètes, tests multi-variants, corrélats de protection."},
    {"Pilier": "Production", "Exigences_clefs": "Règles GMP, process robuste, traçabilité complète des lots."}
]

df_rflp = pd.DataFrame(data_rflp)

data_lifecycle = [
    {"Étape": "Concept", "Description": "Plateforme vaccinale, exigences VIH, stratégie réglementaire initiale."},
    {"Étape": "Préclinique", "Description": "Études in vitro / in vivo, immunogénicité, toxicologie, risque ADE."},
    {"Étape": "Phase I", "Description": "Sécurité sur petits groupes, première preuve d'immunité."},
    {"Étape": "Phase II", "Description": "Dose optimale, immunogénicité détaillée, premières données d'efficacité."},
    {"Étape": "Phase III", "Description": "Preuve statistique d'efficacité, profil bénéfice/risque complet."},
    {"Étape": "Dossier AMM", "Description": "Soumission CTD EMA/ANSM, évaluation centralisée, décisions HAS."},
    {"Étape": "Production GMP", "Description": "Fabrication industrielle, libération lots, chaîne du froid."},
    {"Étape": "Pharmacovigilance", "Description": "Suivi post-AMM, signaux de sécurité, mises à jour produit."}
]

df_lifecycle = pd.DataFrame(data_lifecycle)

data_archiving = [
    {"Aspect": "Durée", "Détail": "Conservation minimale 25 ans, jusqu'à 30 ans pour documents critiques."},
    {"Aspect": "Formats", "Détail": "PDF/A et XML comme formats pérennes pour les documents réglementaires."},
    {"Aspect": "Sécurisation", "Détail": "Signature numérique qualifiée, hashing SHA-256, stockage WORM."},
    {"Aspect": "Traçabilité", "Détail": "Métadonnées complètes, ID document, version, statut, checksum."}
]

df_archiving = pd.DataFrame(data_archiving)

data_audit_trail = [
    {
        "Qui": "Clinical QA",
        "Quoi": "Change control sur protocole Phase II",
        "Quand": "2025-10-12 09:32",
        "Pourquoi": "Mise à jour guidance EMA VIH 2025",
        "Livrables_impactes": "Protocole Phase II, plan d'analyse, formulaire consentement"
    },
    {
        "Qui": "Regulatory Affairs",
        "Quoi": "Mise à jour section Module 1 CTD",
        "Quand": "2025-11-03 14:08",
        "Pourquoi": "Ajout nouvelle Référence Directive 2001/83/CE consolidée",
        "Livrables_impactes": "Dossier AMM, annexes locales France"
    },
    {
        "Qui": "QA Release",
        "Quoi": "CAPA sur déviation stabilité 2–8°C",
        "Quand": "2025-11-20 16:45",
        "Pourquoi": "Excursion de température détectée sur frigo clinique",
        "Livrables_impactes": "Rapport de stabilité, enregistrements IoT, plan d'action CAPA"
    }
]

df_audit_trail = pd.DataFrame(data_audit_trail)
