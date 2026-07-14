BRICK = {
    "brick_num": 26,
    "brick_title": "Thrombocytopenia",
    "games": [
        {
            "slug": "severity_presentation",
            "title": "Platelet Count and Clinical Severity",
            "subtitle": "Match each platelet count range to its severity category and the clinical presentation expected",
            "categories": ["Severity Category", "Clinical Presentation"],
            "data": {
                "150,000-400,000 cells/uL": {
                    "Severity Category": "Normal platelet count",
                    "Clinical Presentation": "Normal hemostasis with no bleeding symptoms"
                },
                "Below 150,000 cells/uL": {
                    "Severity Category": "Mild thrombocytopenia",
                    "Clinical Presentation": "Often asymptomatic; may have easy bruising"
                },
                "30,000-50,000 cells/uL": {
                    "Severity Category": "Moderate thrombocytopenia",
                    "Clinical Presentation": "Easy bruising, petechiae, and purpura"
                },
                "Below 30,000 cells/uL": {
                    "Severity Category": "Severe thrombocytopenia",
                    "Clinical Presentation": "Increased bleeding following minor trauma"
                },
                "Below 10,000 cells/uL": {
                    "Severity Category": "Hematologic emergency",
                    "Clinical Presentation": "Risk of spontaneous bleeding"
                }
            }
        },
        {
            "slug": "mechanisms",
            "title": "How Thrombocytopenia Develops",
            "subtitle": "Match each condition to its underlying mechanism and a distinctive feature",
            "categories": ["Mechanism", "Distinctive Feature"],
            "data": {
                "Acute leukemia": {
                    "Mechanism": "Decreased production from bone marrow infiltration",
                    "Distinctive Feature": "Pancytopenia with abnormal cells on smear"
                },
                "Hypersplenism": {
                    "Mechanism": "Increased splenic sequestration",
                    "Distinctive Feature": "Enlarged spleen traps circulating platelets"
                },
                "Immune thrombocytopenia (ITP)": {
                    "Mechanism": "Immune-mediated platelet destruction",
                    "Distinctive Feature": "Autoantibodies against platelet surface proteins"
                },
                "Disseminated intravascular coagulation": {
                    "Mechanism": "Increased consumption within microthrombi",
                    "Distinctive Feature": "Schistocytes with prolonged PT and PTT"
                },
                "Liver failure": {
                    "Mechanism": "Decreased hepatic thrombopoietin production",
                    "Distinctive Feature": "Commonly from chronic alcohol use"
                },
                "Vitamin B12 or folate deficiency": {
                    "Mechanism": "Decreased production from nutritional deficiency",
                    "Distinctive Feature": "Correctable with nutritional repletion"
                }
            }
        },
        {
            "slug": "increased_destruction",
            "title": "Causes of Increased Platelet Destruction",
            "subtitle": "Match each cause to its category and its hallmark feature",
            "categories": ["Category", "Hallmark Feature"],
            "data": {
                "Heparin-induced thrombocytopenia (HIT)": {
                    "Category": "Immunologic, drug-induced",
                    "Hallmark Feature": "Antibody to heparin-PF4 complex causing thrombosis"
                },
                "Immune thrombocytopenia (ITP)": {
                    "Category": "Immunologic, autoimmune",
                    "Hallmark Feature": "Idiopathic or linked to SLE, HIV, or H. pylori"
                },
                "Thrombotic microangiopathy (TTP/HUS)": {
                    "Category": "Nonimmunologic, microangiopathic",
                    "Hallmark Feature": "Small-vessel damage with schistocytes"
                },
                "HELLP syndrome": {
                    "Category": "Nonimmunologic, pregnancy-related",
                    "Hallmark Feature": "Hemolysis, elevated liver enzymes, low platelets"
                },
                "Post-transfusion reaction": {
                    "Category": "Immunologic, alloimmune",
                    "Hallmark Feature": "Foreign antigens in transfused blood product"
                },
                "Ethanol": {
                    "Category": "Multifactorial",
                    "Hallmark Feature": "Both lowers marrow production and destroys platelets"
                }
            }
        },
        {
            "slug": "workup_management",
            "title": "Diagnostic Workup and Management",
            "subtitle": "Match each test or intervention to its purpose and a key clinical point",
            "categories": ["Purpose", "Key Point"],
            "data": {
                "Complete blood count (CBC)": {
                    "Purpose": "Initial test used to detect a low platelet count",
                    "Key Point": "Concurrent anemia and leukopenia suggest pancytopenia"
                },
                "Peripheral blood smear": {
                    "Purpose": "Evaluate platelet size and cell-line morphology",
                    "Key Point": "Schistocytes suggest microangiopathic hemolytic anemia"
                },
                "Bone marrow biopsy": {
                    "Purpose": "Assess the marrow when pancytopenia is present",
                    "Key Point": "Distinguishes marrow failure from hematopoietic neoplasia"
                },
                "Citrate-tube CBC recount": {
                    "Purpose": "Confirm the count when platelet clumping is suspected",
                    "Key Point": "Excludes pseudothrombocytopenia, an EDTA-tube artifact"
                },
                "Platelet transfusion": {
                    "Purpose": "Treat severe or actively bleeding thrombocytopenia",
                    "Key Point": "Given below 10,000; goal above 50,000 (100,000 for CNS bleeds)"
                }
            }
        }
    ]
}
