# VAX-PLM — Digital Regulatory Twin (VAX-HIV-2030)

## Overview
VAX-PLM is an interactive digital regulatory twin designed to model the complete Product Lifecycle Management (PLM) flow of a fictional vaccine: **VAX-HIV-2030**.

The application centralizes all regulatory components — requirements, documents, evidence, quality, IoT monitoring, lifecycle, audit trail, and submission — to provide a unified and traceable view of regulatory compliance aligned with EMA and ANSM expectations.

This project illustrates how a full regulatory ecosystem can be organized, visualized, and navigated using a modern data application.

---

## Objectives

- Model a realistic regulatory workflow used in vaccine development  
- Provide end-to-end traceability between:  
  - Requirements  
  - Documents  
  - Evidence  
- Deliver a multi-view dashboard covering:  
  - Quality and GMP aspects  
  - Cold chain and IoT monitoring  
  - Lifecycle stages (R&D to pharmacovigilance)  
  - Archiving and audit trail  
  - Regulatory submission pathways  
- Allow CSV import and automatic relational fusion using PLM-style mappings  
- Present an intuitive UX suitable for training and demonstration  

---

## Main Features

### 1. Requirements – Documents – Evidence Mapping
Users can upload CSV files and automatically visualize the connections between:
- Requirement ↔ Document  
- Document ↔ Evidence  
- Requirement ↔ Evidence  

The system merges and standardizes datasets to rebuild traceability matrices used in real validation dossiers.

---

### 2. Multi-Page Interactive Application
The application is structured into dedicated modules, each representing a key regulatory activity:

- Requirements  
- Documents  
- Evidence  
- Regulatory Dashboard  
- Quality Control  
- IoT Monitoring  
- Lifecycle Management  
- Regulatory Submission  
- Secure Archiving  
- Audit Trail  

---

### 3. Pharmaceutical Lifecycle Modeling
A complete lifecycle representation is included:

1. Fundamental Research  
2. Preclinical Development  
3. Clinical Development (Phases I–III)  
4. Industrial Production (GMP)  
5. Marketing Authorization Application  
6. Commercialization and Distribution  
7. Pharmacovigilance and Post-Market Surveillance  

---

### 4. IoT Monitoring (Cold Chain)
Simulates temperature monitoring (fridges, freezers, labs, transport) to illustrate:
- chain-of-custody  
- temperature excursions  
- stability  
- quality risk assessment  

---

### 5. Regulatory Submission Simulation
Summarizes the key deliverables required for EMA/ANSM submissions, including:
- validation packages  
- consistency checks  
- data completeness  
- documentation structure  

---

## Project Structure

Pages/
Documents.py
Evidence.py
IoT_Monitor.py
Lifecycle_Management.py
Quality_Control.py
Regulatory_Dashboard.py
Regulatory_Submission.py
Requirements.py

streamlit_app.py
dataset.py
requirements.txt
README.md


---

## Technology Stack

- Python 3  
- Streamlit  
- Pandas  
- Plotly / Matplotlib  
- CSV datasets  
- GitHub Codespaces  
- Streamlit Cloud  

---

## Running Locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
