BRICK = {
    "brick_num": 51,
    "brick_title": "Acute Myeloid Leukemia",
    "games": [
        {
            "slug": "aml_complications",
            "title": "Complications of Acute Myeloid Leukemia",
            "subtitle": "Match each complication to its underlying cause, its key feature, and its management or note",
            "categories": ["Underlying Cause", "Key Feature", "Management or Note"],
            "data": {
                "Sepsis": {
                    "Underlying Cause": "Circulating blasts lack normal immunologic protective function",
                    "Key Feature": "Atypical bacterial or fungal infection in an immunocompromised host",
                    "Management or Note": "The leading cause of death in AML"
                },
                "Disseminated intravascular coagulation": {
                    "Underlying Cause": "Blast granules and tissue factor trigger the coagulation cascade",
                    "Key Feature": "Widespread clotting that consumes clotting factors and platelets",
                    "Management or Note": "Most common in APL and worsened by chemotherapy"
                },
                "Tumor lysis syndrome": {
                    "Underlying Cause": "Massive release of intracellular contents as tumor cells die",
                    "Key Feature": "Hyperuricemia, hyperkalemia, hyperphosphatemia, and hypocalcemia",
                    "Management or Note": "Prevented with IV hydration and allopurinol; rasburicase if uric acid is high"
                },
                "Leukostasis": {
                    "Underlying Cause": "Increased blood viscosity from a large population of blasts",
                    "Key Feature": "Neurologic and pulmonary symptoms with hyperleukocytosis",
                    "Management or Note": "Treated with cytoreductive chemotherapy or leukapheresis plus hydroxyurea"
                }
            }
        },
        {
            "slug": "aml_genetics",
            "title": "Genetic Alterations in AML",
            "subtitle": "Match each genetic alteration to its molecular change, its prognosis, and an associated note or therapy",
            "categories": ["Molecular Change", "Prognosis", "Associated Note or Therapy"],
            "data": {
                "Acute promyelocytic leukemia": {
                    "Molecular Change": "t(15;17) creating the PML-RARalpha fusion gene",
                    "Prognosis": "Excellent long-term survival once early DIC is survived",
                    "Associated Note or Therapy": "Responds to all-trans retinoic acid and arsenic trioxide"
                },
                "Core binding factor leukemia": {
                    "Molecular Change": "t(8;21) or inv(16)",
                    "Prognosis": "Relatively favorable",
                    "Associated Note or Therapy": "Two abnormalities grouped by their shared molecular target"
                },
                "NPM1 mutation": {
                    "Molecular Change": "Mutation in the NPM1 gene",
                    "Prognosis": "Relatively favorable in the absence of other mutations",
                    "Associated Note or Therapy": "Prognostic value depends on co-existing mutations"
                },
                "FLT3 mutation": {
                    "Molecular Change": "Mutation in the FLT3 gene",
                    "Prognosis": "Generally unfavorable",
                    "Associated Note or Therapy": "Targetable with FLT3 inhibitors such as midostaurin"
                }
            }
        },
        {
            "slug": "aml_treatments",
            "title": "Medications and Therapies in AML",
            "subtitle": "Match each therapy to its class or mechanism, its role in AML, and a key note",
            "categories": ["Class or Mechanism", "Role in AML", "Key Note"],
            "data": {
                "Cytarabine": {
                    "Class or Mechanism": "Pyrimidine nucleoside analog",
                    "Role in AML": "Backbone of induction chemotherapy for most forms of AML",
                    "Key Note": "Given as a continuous IV infusion over 7 days in the 7+3 regimen"
                },
                "Daunorubicin": {
                    "Class or Mechanism": "Anthracycline",
                    "Role in AML": "Paired with cytarabine to induce remission",
                    "Key Note": "Given as a single daily IV dose for 3 days in the 7+3 regimen"
                },
                "All-trans retinoic acid": {
                    "Class or Mechanism": "Vitamin A derivative that binds nuclear receptors",
                    "Role in AML": "Induces differentiation of malignant promyelocytes in APL",
                    "Key Note": "Boxed warnings for fetal toxicity and differentiation syndrome"
                },
                "Arsenic trioxide": {
                    "Class or Mechanism": "Vitamin A derivative that induces apoptosis",
                    "Role in AML": "Combined with ATRA to treat APL",
                    "Key Note": "Degrades the PML-RARalpha protein; risks cardiac conduction abnormalities"
                },
                "Hematopoietic stem cell transplant": {
                    "Class or Mechanism": "Replacement of marrow with donor stem cells",
                    "Role in AML": "Consolidation after chemotherapy-induced remission",
                    "Key Note": "Reduces relapse and is the only way to fully cure the disease"
                }
            }
        },
        {
            "slug": "aml_diagnosis",
            "title": "Diagnostic Workup of AML",
            "subtitle": "Match each study to its purpose and its characteristic finding in AML",
            "categories": ["Purpose", "Finding in AML"],
            "data": {
                "Complete blood count": {
                    "Purpose": "Screens the peripheral blood cell counts",
                    "Finding in AML": "Leukocytosis from circulating blasts with decreased RBCs, platelets, and neutrophils"
                },
                "Peripheral blood smear": {
                    "Purpose": "Examines circulating cell morphology",
                    "Finding in AML": "Myeloblasts with a high N:C ratio, fine chromatin, nucleoli, and Auer rods"
                },
                "Bone marrow biopsy": {
                    "Purpose": "Quantifies the marrow blast percentage",
                    "Finding in AML": "20% or more myeloblasts confirms the diagnosis"
                },
                "Flow cytometry": {
                    "Purpose": "Determines blast lineage",
                    "Finding in AML": "Immaturity marker CD34 with myeloid markers CD13, CD33, and MPO"
                },
                "Genetic testing": {
                    "Purpose": "FISH, karyotype, and molecular studies",
                    "Finding in AML": "Diagnostic translocations such as t(15;17), t(8;21), and inv(16)"
                }
            }
        }
    ]
}
