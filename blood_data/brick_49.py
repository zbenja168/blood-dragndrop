BRICK = {
    "brick_num": 49,
    "brick_title": "Primary Myelofibrosis",
    "games": [
        {
            "slug": "pmf_genetics",
            "title": "Genetic Mutations in Primary Myelofibrosis",
            "subtitle": "Match each gene to how often it drives PMF, what it normally encodes, and its testing role",
            "categories": ["Frequency in PMF", "Normal Product or Function", "Testing Note"],
            "data": {
                "JAK2": {
                    "Frequency in PMF": "About 50% to 60% of cases",
                    "Normal Product or Function": "Janus kinase 2 tyrosine kinase driving JAK-STAT growth signaling",
                    "Testing Note": "Most useful mutation to test; target of the inhibitor ruxolitinib"
                },
                "CALR (calreticulin)": {
                    "Frequency in PMF": "About 20% to 30% of cases",
                    "Normal Product or Function": "Calreticulin protein",
                    "Testing Note": "Found in JAK2-negative cases"
                },
                "MPL": {
                    "Frequency in PMF": "About 5% to 10% of cases",
                    "Normal Product or Function": "Thrombopoietin receptor",
                    "Testing Note": "Found in a minority of JAK2-negative cases"
                },
                "BCR::ABL1": {
                    "Frequency in PMF": "Absent in PMF",
                    "Normal Product or Function": "Philadelphia-chromosome fusion tyrosine kinase",
                    "Testing Note": "Its presence points to chronic myeloid leukemia instead"
                }
            }
        },
        {
            "slug": "pmf_diagnosis",
            "title": "Diagnosing Primary Myelofibrosis",
            "subtitle": "Match each study to its finding in PMF and its diagnostic role",
            "categories": ["Result in PMF", "Diagnostic Role"],
            "data": {
                "Complete blood count": {
                    "Result in PMF": "Elevated white blood cell count with a left shift and anemia",
                    "Diagnostic Role": "Screening study; picture resembles chronic myeloid leukemia"
                },
                "Peripheral blood smear": {
                    "Result in PMF": "Teardrop-shaped RBCs (dacryocytes) and nucleated RBCs",
                    "Diagnostic Role": "Leukoerythroblastic reaction that suggests a fibrotic marrow"
                },
                "Bone marrow biopsy": {
                    "Result in PMF": "Dry tap on aspiration; core shows fibrosis with early hypercellularity or late few cells",
                    "Diagnostic Role": "Needed to confirm the diagnosis"
                },
                "Genetic testing": {
                    "Result in PMF": "Activating JAK2 mutation in roughly half of patients",
                    "Diagnostic Role": "Supports a clonal neoplasm and guides targeted therapy"
                },
                "Physical exam": {
                    "Result in PMF": "Massively enlarged spleen with tip reaching the pelvis",
                    "Diagnostic Role": "Reflects extramedullary hematopoiesis compensating for marrow failure"
                }
            }
        },
        {
            "slug": "pmf_treatment",
            "title": "Treating Primary Myelofibrosis",
            "subtitle": "Match each therapy to the patient it fits, its purpose, and a key note",
            "categories": ["Indicated Patient or Setting", "Mechanism or Purpose", "Key Adverse Effect or Note"],
            "data": {
                "Observation": {
                    "Indicated Patient or Setting": "Low-risk, asymptomatic patient",
                    "Mechanism or Purpose": "Monitor counts and replace platelets or RBCs only if needed",
                    "Key Adverse Effect or Note": "Avoids drug toxicity while disease is stable"
                },
                "Allogeneic stem cell transplant": {
                    "Indicated Patient or Setting": "High- or intermediate-risk patient healthy enough for the procedure",
                    "Mechanism or Purpose": "Replaces nonfunctional marrow; the only therapy with curative potential",
                    "Key Adverse Effect or Note": "Graft-versus-host disease and immunosuppression with infections"
                },
                "Ruxolitinib": {
                    "Indicated Patient or Setting": "High-risk patient not eligible for transplant",
                    "Mechanism or Purpose": "Selectively inhibits JAK1 and JAK2 to counter dysregulated JAK-STAT signaling",
                    "Key Adverse Effect or Note": "Pancytopenia, bruising, and hypercholesterolemia"
                },
                "Hydroxyurea": {
                    "Indicated Patient or Setting": "High-risk patient needing cytoreduction",
                    "Mechanism or Purpose": "Antimetabolite that inhibits ribonucleotide reductase, halting the cell cycle at G1/S",
                    "Key Adverse Effect or Note": "Teratogenic; live vaccines are contraindicated"
                },
                "Momelotinib": {
                    "Indicated Patient or Setting": "Newly approved option for PMF",
                    "Mechanism or Purpose": "JAK inhibitor that is an effective treatment",
                    "Key Adverse Effect or Note": "May provide better anemia-related benefits than ruxolitinib"
                }
            }
        },
        {
            "slug": "pmf_clinical_features",
            "title": "Clinical Consequences of Marrow Fibrosis",
            "subtitle": "Match each PMF feature to its underlying mechanism and how it shows up",
            "categories": ["Underlying Mechanism", "Clinical Manifestation"],
            "data": {
                "Massive splenomegaly": {
                    "Underlying Mechanism": "Extramedullary hematopoiesis as the spleen compensates for the failing marrow",
                    "Clinical Manifestation": "Left upper quadrant fullness, early satiety, spleen tip near the pelvis"
                },
                "Anemia": {
                    "Underlying Mechanism": "Marrow failure lowers red blood cell production",
                    "Clinical Manifestation": "Fatigue and breathlessness"
                },
                "Infections": {
                    "Underlying Mechanism": "Marrow failure lowers the white blood cell count",
                    "Clinical Manifestation": "Recurrent or severe infections"
                },
                "Bleeding episodes": {
                    "Underlying Mechanism": "Marrow failure lowers the platelet count",
                    "Clinical Manifestation": "Easy bruising and bleeding"
                },
                "Teardrop red blood cells": {
                    "Underlying Mechanism": "RBCs elongate while squeezing through the fibrous marrow",
                    "Clinical Manifestation": "Dacryocytes visible on the peripheral smear"
                },
                "Leukemic transformation": {
                    "Underlying Mechanism": "Progression to acute myeloid leukemia in about 3% to 4% of cases",
                    "Clinical Manifestation": "A usually fatal outcome"
                }
            }
        }
    ]
}
