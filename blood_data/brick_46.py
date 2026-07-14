BRICK = {
    "brick_num": 46,
    "brick_title": "Chronic Myeloid Leukemia",
    "games": [
        {
            "slug": "cml_diagnostic_tests",
            "title": "Diagnosing CML",
            "subtitle": "Match each diagnostic test to what it detects, a distinguishing detail, and its role in care",
            "categories": ["What It Detects", "Distinguishing Detail", "Role in Care"],
            "data": {
                "Complete Blood Count": {
                    "What It Detects": "Elevated myeloid WBCs with left-shifted maturation",
                    "Distinguishing Detail": "Mean WBC near 100,000/mm3 with increased basophils and eosinophils",
                    "Role in Care": "First test that raises suspicion of CML"
                },
                "Peripheral Smear": {
                    "What It Detects": "Different WBC subtypes and their cell maturity",
                    "Distinguishing Detail": "Blast counts rise noticeably during the blast crisis phase",
                    "Role in Care": "Discerns cell types seen on the CBC"
                },
                "Bone Marrow Biopsy": {
                    "What It Detects": "Percentage of blasts, marrow fibrosis, and mutated cell lines",
                    "Distinguishing Detail": "Marrow is hypercellular with small hypolobated megakaryocytes",
                    "Role in Care": "Establishes disease phase and monitors progression"
                },
                "FISH for t(9;22)": {
                    "What It Detects": "Presence or absence of the t(9;22) translocation only",
                    "Distinguishing Detail": "Fast test that does not examine any other chromosomes",
                    "Role in Care": "Rapid confirmation of the driver translocation"
                },
                "Karyotype": {
                    "What It Detects": "All chromosomes, including additional abnormalities",
                    "Distinguishing Detail": "Extra abnormalities can signal a worse prognosis; takes 1-2 weeks",
                    "Role in Care": "Risk stratification beyond the single translocation"
                },
                "RT-PCR for BCR::ABL": {
                    "What It Detects": "Quantitative baseline level of the BCR::ABL transcript",
                    "Distinguishing Detail": "Level is followed serially over the course of therapy",
                    "Role in Care": "Monitors treatment response and residual disease"
                }
            }
        },
        {
            "slug": "cml_treatments",
            "title": "Treating CML",
            "subtitle": "Match each therapy to its role, its signature adverse effect, and a mechanism note",
            "categories": ["Role in Therapy", "Signature Adverse Effect", "Mechanism / Note"],
            "data": {
                "Imatinib": {
                    "Role in Therapy": "Most common first choice for chronic-phase CML",
                    "Signature Adverse Effect": "GI upset: nausea, vomiting, diarrhea, abdominal pain",
                    "Mechanism / Note": "Competitively binds the kinase site of BCR::ABL"
                },
                "Dasatinib": {
                    "Role in Therapy": "Switched to after imatinib resistance or intolerance",
                    "Signature Adverse Effect": "Pleural effusion and prolonged QTc",
                    "Mechanism / Note": "Binds both active and inactive ABL kinase conformations"
                },
                "Ponatinib": {
                    "Role in Therapy": "Used to overcome imatinib-resistance mutations",
                    "Signature Adverse Effect": "Thrombosis and liver toxicity",
                    "Mechanism / Note": "Active against resistant BCR::ABL kinase mutations"
                },
                "Hydroxyurea / Interferon alpha": {
                    "Role in Therapy": "Later-stage option when TKIs fail or are ineffective",
                    "Signature Adverse Effect": "Nonspecific cytoreductive chemotherapy effects",
                    "Mechanism / Note": "Less-specific chemotherapy, not targeted to BCR::ABL"
                },
                "Allogeneic stem cell transplant": {
                    "Role in Therapy": "Considered for younger patients with advanced disease",
                    "Signature Adverse Effect": "Transplant-related morbidity",
                    "Mechanism / Note": "Replaces neoplastic marrow with donor hematopoiesis"
                }
            }
        },
        {
            "slug": "cml_phases",
            "title": "Chronic Phase vs Blast Crisis",
            "subtitle": "Sort each feature into how it appears in the chronic phase versus the blast crisis",
            "categories": ["Chronic Phase", "Blast Crisis"],
            "data": {
                "Blast count": {
                    "Chronic Phase": "Low, usually 2%-3% and not more than 10%",
                    "Blast Crisis": "Greater than 20% of cells"
                },
                "Typical symptoms": {
                    "Chronic Phase": "Often asymptomatic; fatigue or splenomegaly-related fullness",
                    "Blast Crisis": "Fever, night sweats, weight loss, and bone pain"
                },
                "WBC behavior": {
                    "Chronic Phase": "Slowly rising leukocytosis over time",
                    "Blast Crisis": "WBC count rises rapidly"
                },
                "Untreated survival": {
                    "Chronic Phase": "Approximately 3 to 4 years",
                    "Blast Crisis": "Weeks to a few months"
                },
                "Clinical resemblance": {
                    "Chronic Phase": "Stable, slowly progressive myeloproliferative state",
                    "Blast Crisis": "Behaves essentially like an acute leukemia"
                },
                "Share of patients at presentation": {
                    "Chronic Phase": "Most patients present here (85%-90%)",
                    "Blast Crisis": "End-stage phase most untreated patients eventually develop"
                }
            }
        },
        {
            "slug": "cml_complications",
            "title": "Complications of CML",
            "subtitle": "Match each complication to its underlying mechanism and its clinical clue",
            "categories": ["Underlying Mechanism", "Clinical Clue"],
            "data": {
                "Gouty arthritis": {
                    "Underlying Mechanism": "High uric acid from rapid turnover and lysis of many WBCs",
                    "Clinical Clue": "Joint pain with hyperuricemia"
                },
                "Splenomegaly": {
                    "Underlying Mechanism": "Extramedullary hematopoiesis in the spleen",
                    "Clinical Clue": "Left upper quadrant fullness, dragging sensation, early satiety"
                },
                "Retrosternal pain": {
                    "Underlying Mechanism": "Expansion of the hypercellular bone marrow",
                    "Clinical Clue": "Chest or sternal discomfort"
                },
                "Normocytic anemia": {
                    "Underlying Mechanism": "Neoplastic cells crowd out normal red cell precursors",
                    "Clinical Clue": "Fatigue and weakness; develops in about half of patients"
                },
                "Bleeding tendency": {
                    "Underlying Mechanism": "Falling platelet counts as the disease advances",
                    "Clinical Clue": "Easy bruising or bleeding"
                }
            }
        }
    ]
}
