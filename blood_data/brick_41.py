BRICK = {
    "brick_num": 41,
    "brick_title": "B-Cell Non-Hodgkin Lymphomas (Part 2)",
    "games": [
        {
            "slug": "nhl_presentations",
            "title": "Clinical Presentations Across B-Cell NHL",
            "subtitle": "Match each lymphoma (or Burkitt form) to its typical patient, classic presentation, and key association",
            "categories": ["Typical patient / population", "Classic presentation", "Key association"],
            "data": {
                "Diffuse large B-cell lymphoma": {
                    "Typical patient / population": "Older adults, or immunosuppressed patients such as those with HIV/AIDS",
                    "Classic presentation": "Rapidly enlarging lymphadenopathy or extranodal mass with B symptoms",
                    "Key association": "Most common NHL; can arise from CLL/SLL via Richter transformation"
                },
                "Endemic Burkitt lymphoma": {
                    "Typical patient / population": "Children in equatorial Africa",
                    "Classic presentation": "Rapidly growing tumors of the jaw and facial bones",
                    "Key association": "Strong Epstein-Barr virus link; possible malaria co-factor"
                },
                "Sporadic Burkitt lymphoma": {
                    "Typical patient / population": "Patients in the United States (most common form there)",
                    "Classic presentation": "Abdominal mass involving the ileocecum, mimicking appendicitis, with ascites",
                    "Key association": "Tumor can cause intestinal obstruction"
                },
                "Immunodeficiency-associated Burkitt lymphoma": {
                    "Typical patient / population": "People with HIV/AIDS or other immunodeficiency",
                    "Classic presentation": "Lymph node involvement; ~15% CNS and 20-30% bone marrow at diagnosis",
                    "Key association": "Strong Epstein-Barr virus association like the endemic form"
                },
                "Mantle cell lymphoma": {
                    "Typical patient / population": "Middle-aged to older adults with male predominance (median age 60)",
                    "Classic presentation": "High-stage lymphadenopathy, hepatosplenomegaly, and bone marrow involvement",
                    "Key association": "Usually presents at advanced stage"
                }
            }
        },
        {
            "slug": "genes_proteins",
            "title": "Key Genes and Proteins in B-Cell NHL",
            "subtitle": "Match each gene/protein to its normal role, the abnormality seen, and its lymphoma association",
            "categories": ["Normal role", "Abnormality in NHL", "Lymphoma association"],
            "data": {
                "MYC": {
                    "Normal role": "Transcriptional regulator that boosts genes making building blocks for cell growth and division",
                    "Abnormality in NHL": "Overexpression leading to uncontrolled cell division",
                    "Lymphoma association": "Burkitt lymphoma via t(8;14); also part of the DLBCL panel"
                },
                "BCL2": {
                    "Normal role": "Regulates apoptosis (programmed cell death)",
                    "Abnormality in NHL": "Overexpression, also connected to a t(14;18) translocation",
                    "Lymphoma association": "Tested in the DLBCL MYC/BCL2/BCL6 FISH panel"
                },
                "BCL6": {
                    "Normal role": "Prevents apoptosis and drives T cells to become T helper cells",
                    "Abnormality in NHL": "Down-regulation",
                    "Lymphoma association": "Tested in the DLBCL MYC/BCL2/BCL6 FISH panel"
                },
                "Cyclin D1 (CCND1)": {
                    "Normal role": "Drives cell cycle progression",
                    "Abnormality in NHL": "Overexpression from t(11;14) placing CCND1 next to IGH",
                    "Lymphoma association": "Mantle cell lymphoma; immunohistochemistry is a surrogate for the translocation"
                }
            }
        },
        {
            "slug": "chemo_agents",
            "title": "Chemotherapy Agents for High-Grade B-Cell NHL",
            "subtitle": "Match each drug to its mechanism, a characteristic adverse effect, and a regimen that uses it",
            "categories": ["Mechanism of action", "Characteristic adverse effect", "Used in regimen"],
            "data": {
                "Cyclophosphamide": {
                    "Mechanism of action": "Alkylating agent that interferes with DNA/RNA replication",
                    "Characteristic adverse effect": "Hemorrhagic cystitis (reduce risk with Mesna) and SIADH",
                    "Used in regimen": "R-CHOP for DLBCL and CODOX-M for Burkitt lymphoma"
                },
                "Doxorubicin": {
                    "Mechanism of action": "Inhibits DNA/RNA synthesis",
                    "Characteristic adverse effect": "Cumulative dose-related cardiomyopathy leading to heart failure",
                    "Used in regimen": "R-CHOP for DLBCL and CODOX-M for Burkitt lymphoma"
                },
                "Vincristine": {
                    "Mechanism of action": "Inhibits microtubule function",
                    "Characteristic adverse effect": "Dose-related peripheral neuropathy and autonomic (vocal cord) paralysis",
                    "Used in regimen": "R-CHOP for DLBCL and CODOX-M for Burkitt lymphoma"
                },
                "Methotrexate": {
                    "Mechanism of action": "Competitive inhibitor of dihydrofolate reductase, blocking DNA synthesis",
                    "Characteristic adverse effect": "Nephrotoxicity, hepatotoxicity, and mucositis",
                    "Used in regimen": "High-dose in adult CODOX-M; given intrathecally for CNS disease"
                },
                "Cytarabine": {
                    "Mechanism of action": "Pyrimidine analog that inhibits DNA polymerase",
                    "Characteristic adverse effect": "Myelosuppression and megaloblastic anemia",
                    "Used in regimen": "High-dose cytarabine (HiDAc) with rituximab for mantle cell lymphoma"
                },
                "Polatuzumab vedotin": {
                    "Mechanism of action": "CD79b-directed antibody-drug conjugate delivering an anti-mitotic agent",
                    "Characteristic adverse effect": "Neutropenia (>60%), thrombocytopenia, and peripheral neuropathy",
                    "Used in regimen": "R-pola-CHP for advanced-stage DLBCL"
                }
            }
        },
        {
            "slug": "treatment_regimens",
            "title": "Treatment Regimens for B-Cell NHL",
            "subtitle": "Match each regimen to its component drugs, primary indication, and a notable feature",
            "categories": ["Component drugs", "Primary indication", "Notable feature"],
            "data": {
                "R-CHOP": {
                    "Component drugs": "Rituximab, cyclophosphamide, doxorubicin, vincristine, prednisone",
                    "Primary indication": "DLBCL (standard first-line)",
                    "Notable feature": "Usually 3-5 cycles followed by response assessment"
                },
                "R-pola-CHP": {
                    "Component drugs": "Rituximab, polatuzumab vedotin, cyclophosphamide, doxorubicin, prednisone",
                    "Primary indication": "Advanced-stage DLBCL (stage III or IV)",
                    "Notable feature": "Adds a CD79b-directed antibody-drug conjugate"
                },
                "CODOX-M": {
                    "Component drugs": "Cyclophosphamide, doxorubicin, methotrexate (with vincristine)",
                    "Primary indication": "Burkitt lymphoma",
                    "Notable feature": "Rituximab is often added to minimize tumor lysis syndrome"
                },
                "R-B (bendamustine)": {
                    "Component drugs": "Rituximab plus bendamustine, an alkylating agent",
                    "Primary indication": "Mantle cell lymphoma",
                    "Notable feature": "Preferred for its balance of toxicity and long-term survival"
                },
                "HiDAc": {
                    "Component drugs": "Rituximab with high-dose cytarabine",
                    "Primary indication": "Mantle cell lymphoma (alternative regimen)",
                    "Notable feature": "Cytarabine is a pyrimidine analog that inhibits DNA polymerase"
                }
            }
        }
    ]
}
