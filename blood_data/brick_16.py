BRICK = {
    "brick_num": 16,
    "brick_title": "Coagulation Assays",
    "games": [
        {
            "slug": "coag_tests",
            "title": "The Common Coagulation Tests",
            "subtitle": "Match each assay to the pathways it assesses, what is added to the plasma, and its normal range",
            "categories": ["Pathways Assessed", "Added to Plasma", "Normal Range"],
            "data": {
                "Prothrombin Time (PT)": {
                    "Pathways Assessed": "Extrinsic and common pathways",
                    "Added to Plasma": "Thromboplastin (tissue factor + phospholipid) and calcium",
                    "Normal Range": "11 to 15 seconds"
                },
                "International Normalized Ratio (INR)": {
                    "Pathways Assessed": "Extrinsic and common (standardized PT)",
                    "Added to Plasma": "Derived from ratio of patient PT to normal PT",
                    "Normal Range": "0.8 to 1.2"
                },
                "Activated PTT (aPTT)": {
                    "Pathways Assessed": "Intrinsic and common pathways",
                    "Added to Plasma": "Phospholipid, calcium, and an activator (silica or kaolin)",
                    "Normal Range": "25 to 40 seconds"
                },
                "Thrombin Time (TT)": {
                    "Pathways Assessed": "Fibrinogen-to-fibrin conversion (end of common pathway)",
                    "Added to Plasma": "Thrombin",
                    "Normal Range": "12 to 14 seconds"
                }
            }
        },
        {
            "slug": "prolonged_ptt",
            "title": "Working Up a Prolonged PTT",
            "subtitle": "Match each cause of a prolonged PTT to its mixing-study behavior and its clinical significance",
            "categories": ["Mixing Study Behavior", "In Vivo Effect", "Example"],
            "data": {
                "Clotting factor deficiency": {
                    "Mixing Study Behavior": "PTT corrects when mixed with normal plasma",
                    "In Vivo Effect": "Causes abnormal bleeding",
                    "Example": "Hemophilia (factor VIII or IX deficiency)"
                },
                "Anticoagulant drug": {
                    "Mixing Study Behavior": "PTT does not correct with normal plasma",
                    "In Vivo Effect": "Therapeutic anticoagulation",
                    "Example": "Heparin"
                },
                "Specific factor inhibitor": {
                    "Mixing Study Behavior": "Corrects immediately, then prolongs after incubation",
                    "In Vivo Effect": "Antibody neutralizes a single factor over time",
                    "Example": "Acquired factor VIII inhibitor"
                },
                "Lupus anticoagulant": {
                    "Mixing Study Behavior": "Does not correct, immediately or after incubation",
                    "In Vivo Effect": "Causes thrombosis (DVT/PE), not bleeding",
                    "Example": "Antiphospholipid antibody in systemic lupus"
                },
                "Factor XII deficiency": {
                    "Mixing Study Behavior": "PTT corrects when mixed with normal plasma",
                    "In Vivo Effect": "Prolonged aPTT in vitro but no clinical bleeding",
                    "Example": "Isolated preoperative aPTT prolongation"
                }
            }
        },
        {
            "slug": "fibrinolysis",
            "title": "Fibrinolysis and Thrombosis Markers",
            "subtitle": "Match each component of the fibrinolytic pathway to its role and the product or clinical meaning",
            "categories": ["Role in Fibrinolysis", "Product / Significance", "Class"],
            "data": {
                "Thrombin": {
                    "Role in Fibrinolysis": "Cleaves fibrinogen to fibrin",
                    "Product / Significance": "Fibrin monomers that form the clot",
                    "Class": "Coagulation enzyme"
                },
                "Factor XIII (XIIIa)": {
                    "Role in Fibrinolysis": "Cross-links fibrin strands",
                    "Product / Significance": "Stabilized cross-linked fibrin",
                    "Class": "Transglutaminase"
                },
                "tPA": {
                    "Role in Fibrinolysis": "Converts plasminogen to plasmin",
                    "Product / Significance": "Active plasmin that dissolves clots",
                    "Class": "Plasminogen activator"
                },
                "Plasmin": {
                    "Role in Fibrinolysis": "Degrades fibrin and fibrinogen",
                    "Product / Significance": "Fibrin degradation products (FDPs)",
                    "Class": "Fibrinolytic protease"
                },
                "D-dimer": {
                    "Role in Fibrinolysis": "Formed when plasmin degrades cross-linked fibrin",
                    "Product / Significance": "Specific marker of clot breakdown; elevated in DVT/PE/DIC",
                    "Class": "Fibrin degradation product"
                }
            }
        },
        {
            "slug": "assay_patterns",
            "title": "Assay Patterns in Disease",
            "subtitle": "Match each condition to its coagulation assay findings and the underlying mechanism",
            "categories": ["Assay Findings", "Key Mechanism", "Monitoring / Note"],
            "data": {
                "Cirrhosis (liver disease)": {
                    "Assay Findings": "All prolonged: PT, PTT, and TT",
                    "Key Mechanism": "Liver produces all coagulation factors, which become decreased",
                    "Monitoring / Note": "Most common acquired coagulation disorder"
                },
                "Disseminated intravascular coagulation": {
                    "Assay Findings": "Prolonged PT/INR and aPTT, low platelets, high D-dimer/FDP",
                    "Key Mechanism": "Widespread activation consumes factors, fibrin, and platelets",
                    "Monitoring / Note": "Bleeding and thrombosis occur simultaneously"
                },
                "Hemophilia A": {
                    "Assay Findings": "Prolonged aPTT with normal PT",
                    "Key Mechanism": "Intrinsic pathway factor VIII deficiency",
                    "Monitoring / Note": "Corrects on mixing study"
                },
                "Warfarin therapy": {
                    "Assay Findings": "Elevated INR / prolonged PT",
                    "Key Mechanism": "Blocks gamma-carboxylation of factors II, VII, IX, X",
                    "Monitoring / Note": "Monitored with the INR"
                },
                "Heparin therapy": {
                    "Assay Findings": "Prolonged aPTT",
                    "Key Mechanism": "Activates antithrombin, inhibiting IIa and Xa",
                    "Monitoring / Note": "Monitored with aPTT (or anti-Xa assay)"
                }
            }
        }
    ]
}
