BRICK = {
    "brick_num": 21,
    "brick_title": "Disseminated Intravascular Coagulation",
    "games": [
        {
            "slug": "dic_triggers",
            "title": "What Triggers DIC?",
            "subtitle": "Sort each underlying cause of DIC by how it sets off the clotting cascade",
            "categories": ["Mechanism Class", "How It Triggers DIC", "Classic Example"],
            "data": {
                "Obstetric complications": {
                    "Mechanism Class": "Dumper (adds procoagulants to blood)",
                    "How It Triggers DIC": "Placental/amniotic material dumps procoagulants into circulation",
                    "Classic Example": "Placental abruption or amniotic fluid embolism"
                },
                "Mucinous adenocarcinoma": {
                    "Mechanism Class": "Dumper (adds procoagulants to blood)",
                    "How It Triggers DIC": "Tumor releases procoagulant substances into the blood",
                    "Classic Example": "Pancreatic adenocarcinoma"
                },
                "Acute promyelocytic leukemia": {
                    "Mechanism Class": "Dumper (adds procoagulants to blood)",
                    "How It Triggers DIC": "Leukemic promyelocyte granules release procoagulants",
                    "Classic Example": "APL (a subtype of acute myeloid leukemia)"
                },
                "Gram-negative sepsis": {
                    "Mechanism Class": "Ripper (damages endothelium)",
                    "How It Triggers DIC": "Bacterial toxins injure endothelium and expose tissue factor",
                    "Classic Example": "Severe toxin-producing bacterial infection"
                },
                "Thermal burns or trauma": {
                    "Mechanism Class": "Ripper (damages endothelium)",
                    "How It Triggers DIC": "Extensive tissue and endothelial injury",
                    "Classic Example": "Severe burns"
                },
                "Vasculitis": {
                    "Mechanism Class": "Ripper (damages endothelium)",
                    "How It Triggers DIC": "Inflammatory damage to blood vessel walls",
                    "Classic Example": "Systemic lupus erythematosus"
                }
            }
        },
        {
            "slug": "dic_labs",
            "title": "DIC Laboratory Workup",
            "subtitle": "Match each lab marker to how it changes in DIC and why",
            "categories": ["Change in DIC", "Underlying Reason", "Clinical Utility"],
            "data": {
                "Platelet count": {
                    "Change in DIC": "Decreased",
                    "Underlying Reason": "Platelets consumed during widespread clotting",
                    "Clinical Utility": "Low count is a characteristic blood smear finding"
                },
                "Fibrinogen": {
                    "Change in DIC": "Decreased",
                    "Underlying Reason": "Used up as it is converted into fibrin",
                    "Clinical Utility": "Falls as the coagulopathy worsens"
                },
                "PT and aPTT": {
                    "Change in DIC": "Prolonged",
                    "Underlying Reason": "Coagulation factors depleted by rampant clotting",
                    "Clinical Utility": "Distinguishes DIC from other thrombotic microangiopathies"
                },
                "D-dimer / fibrin degradation products": {
                    "Change in DIC": "Increased",
                    "Underlying Reason": "Clots are being broken down by fibrinolysis",
                    "Clinical Utility": "Sensitive but nonspecific; good for ruling out clotting"
                },
                "Indirect bilirubin": {
                    "Change in DIC": "Increased",
                    "Underlying Reason": "Released during ongoing hemolysis of red blood cells",
                    "Clinical Utility": "Reflects the microangiopathic hemolysis"
                },
                "Schistocytes": {
                    "Change in DIC": "Present on smear",
                    "Underlying Reason": "RBCs sliced by sharp fibrin strands in small vessels",
                    "Clinical Utility": "Hallmark of microangiopathic hemolytic anemia"
                }
            }
        },
        {
            "slug": "dic_clinical",
            "title": "Clinical Manifestations of DIC",
            "subtitle": "Place each sign by the organ system it affects and its mechanism",
            "categories": ["Organ System", "Mechanism", "Process Type"],
            "data": {
                "Petechiae and oozing from IV lines": {
                    "Organ System": "Skin",
                    "Mechanism": "Low platelets cause microvascular hemorrhage",
                    "Process Type": "Bleeding-predominant"
                },
                "Gangrene of fingers and toes": {
                    "Organ System": "Extremities and skin",
                    "Mechanism": "Occlusive thrombi cause tissue necrosis",
                    "Process Type": "Clotting-predominant"
                },
                "Seizures and coma": {
                    "Organ System": "Nervous system",
                    "Mechanism": "Cerebral microthrombi cause ischemia",
                    "Process Type": "Clotting-predominant"
                },
                "Oliguria and acute renal failure": {
                    "Organ System": "Renal system",
                    "Mechanism": "Glomerular microthrombi reduce perfusion",
                    "Process Type": "Clotting-predominant"
                },
                "Cyanosis and respiratory failure": {
                    "Organ System": "Respiratory system",
                    "Mechanism": "Pulmonary microthrombi impair gas exchange",
                    "Process Type": "Clotting-predominant"
                },
                "Circulatory failure and shock": {
                    "Organ System": "Cardiovascular system",
                    "Mechanism": "Widespread microvascular thrombosis and bleeding",
                    "Process Type": "Mixed clotting and bleeding"
                }
            }
        },
        {
            "slug": "dic_treatment",
            "title": "Managing DIC",
            "subtitle": "Match each intervention to its indication and what it provides",
            "categories": ["Indication", "What It Provides or Does", "When Used"],
            "data": {
                "Treat the underlying condition": {
                    "Indication": "First and most important goal in every case",
                    "What It Provides or Does": "Removes the DIC trigger (e.g., antibiotics for sepsis)",
                    "When Used": "Always the foundation of DIC management"
                },
                "Platelet transfusion": {
                    "Indication": "Significant bleeding with thrombocytopenia",
                    "What It Provides or Does": "Replaces consumed platelets",
                    "When Used": "When the patient is actively bleeding"
                },
                "Cryoprecipitate": {
                    "Indication": "Bleeding with low fibrinogen",
                    "What It Provides or Does": "Replaces fibrinogen and factor VIII",
                    "When Used": "To correct hypofibrinogenemia"
                },
                "Fresh frozen plasma (FFP)": {
                    "Indication": "Bleeding with prolonged PT and aPTT",
                    "What It Provides or Does": "Replaces depleted coagulation factors",
                    "When Used": "To correct a prolonged PT and aPTT"
                },
                "Heparin": {
                    "Indication": "Thrombosis-predominant DIC",
                    "What It Provides or Does": "Anticoagulation to limit further clotting",
                    "When Used": "For large thrombi or tissue necrosis"
                },
                "Packed red blood cells": {
                    "Indication": "Symptomatic anemia from hemolysis or bleeding",
                    "What It Provides or Does": "Restores oxygen-carrying capacity",
                    "When Used": "When the patient is anemic or bleeding"
                }
            }
        }
    ]
}
