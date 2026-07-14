BRICK = {
    "brick_num": 29,
    "brick_title": "Thrombotic Microangiopathies",
    "games": [
        {
            "slug": "types_and_causes",
            "title": "Types and Causes of Thrombotic Microangiopathy",
            "subtitle": "Match each disorder to its classification, underlying cause, and key distinguishing feature",
            "categories": ["Classification", "Underlying Cause", "Distinguishing Feature"],
            "data": {
                "Thrombotic thrombocytopenic purpura (TTP)": {
                    "Classification": "Primary thrombotic microangiopathy",
                    "Underlying Cause": "Deficiency of the enzyme ADAMTS13",
                    "Distinguishing Feature": "Neurologic findings; seen mostly in young adults"
                },
                "Hemolytic-uremic syndrome (HUS)": {
                    "Classification": "Primary thrombotic microangiopathy",
                    "Underlying Cause": "Shiga toxin from Escherichia coli O157:H7",
                    "Distinguishing Feature": "Follows bloody diarrhea; seen mostly in young children"
                },
                "Disseminated intravascular coagulation (DIC)": {
                    "Classification": "Secondary thrombotic microangiopathy",
                    "Underlying Cause": "Diffuse activation of the coagulation cascade",
                    "Distinguishing Feature": "Prolonged PT and aPTT from consumed clotting factors"
                },
                "HELLP syndrome": {
                    "Classification": "Secondary thrombotic microangiopathy",
                    "Underlying Cause": "Pregnancy-related hemolysis and elevated liver enzymes",
                    "Distinguishing Feature": "Abdominal pain and hypertension in a pregnant patient"
                },
                "Malignant hypertension": {
                    "Classification": "Secondary thrombotic microangiopathy",
                    "Underlying Cause": "Vessel injury from blood pressure above 220/100 mm Hg",
                    "Distinguishing Feature": "MAHA, low platelets, and rising serum creatinine"
                },
                "Drug-induced microangiopathy": {
                    "Classification": "Secondary thrombotic microangiopathy",
                    "Underlying Cause": "Endothelial injury from calcineurin inhibitors or quinine",
                    "Distinguishing Feature": "Improves after the causative drug is removed"
                }
            }
        },
        {
            "slug": "ttp_pathophysiology",
            "title": "Molecular Players in TTP Pathophysiology",
            "subtitle": "Match each factor to its role, its normal function, and its consequence in TTP",
            "categories": ["Role", "Normal Function", "Consequence in TTP"],
            "data": {
                "ADAMTS13": {
                    "Role": "Plasma metalloproteinase enzyme",
                    "Normal Function": "Cleaves ultra-large vWF multimers into smaller ones",
                    "Consequence in TTP": "Deficient, so ultra-large vWF is not cleaved"
                },
                "von Willebrand factor (vWF)": {
                    "Role": "Platelet adhesion protein",
                    "Normal Function": "Helps platelets adhere to injured vessel walls",
                    "Consequence in TTP": "Ultra-large multimers accumulate and bind platelets"
                },
                "Anti-ADAMTS13 autoantibody": {
                    "Role": "Cause of acquired TTP",
                    "Normal Function": "Absent in healthy people",
                    "Consequence in TTP": "Inhibits ADAMTS13, the most common acquired mechanism"
                },
                "Inherited ADAMTS13 mutation": {
                    "Role": "Cause of inherited TTP",
                    "Normal Function": "Gene normally encodes a functional enzyme",
                    "Consequence in TTP": "Inactivating mutation causes the less common inherited form"
                },
                "Platelets": {
                    "Role": "Cells consumed within microthrombi",
                    "Normal Function": "Circulate freely and form plugs when needed",
                    "Consequence in TTP": "Adhere to uncleaved vWF, forming clots and falling in number"
                }
            }
        },
        {
            "slug": "smear_and_labs",
            "title": "Peripheral Smear and Laboratory Findings",
            "subtitle": "Match each finding to why it occurs and its diagnostic significance",
            "categories": ["Finding", "Why It Occurs", "Diagnostic Significance"],
            "data": {
                "Schistocytes": {
                    "Finding": "Fragmented RBCs with pointy edges and no central pallor",
                    "Why It Occurs": "RBCs sheared by microthrombi in small vessels",
                    "Diagnostic Significance": "Specific for MAHA; never seen on a normal smear"
                },
                "Reticulocytes": {
                    "Finding": "Immature red blood cells released into the blood",
                    "Why It Occurs": "Bone marrow makes more RBCs to correct hemolysis",
                    "Diagnostic Significance": "Seen in all hemolytic anemias with a healthy marrow"
                },
                "High LDH and indirect bilirubin": {
                    "Finding": "Increased LDH and unconjugated bilirubin",
                    "Why It Occurs": "Contents released from lysed red blood cells",
                    "Diagnostic Significance": "Typical of intravascular hemolysis"
                },
                "Low haptoglobin": {
                    "Finding": "Reduced serum haptoglobin level",
                    "Why It Occurs": "Consumed while binding free hemoglobin",
                    "Diagnostic Significance": "Supports a diagnosis of intravascular hemolysis"
                },
                "Thrombocytopenia": {
                    "Finding": "Low platelet count",
                    "Why It Occurs": "Platelets consumed forming multiple thrombi",
                    "Diagnostic Significance": "Present in essentially all forms of TM"
                },
                "Normal PT and aPTT": {
                    "Finding": "Coagulation assays that are not prolonged",
                    "Why It Occurs": "Thrombi are platelet-rich with minimal fibrin",
                    "Diagnostic Significance": "Normal in TTP and HUS but elevated in DIC"
                }
            }
        },
        {
            "slug": "diagnosis_and_management",
            "title": "Diagnosis and Management of Primary TMs",
            "subtitle": "Match each clinical situation to its approach and a key detail",
            "categories": ["Situation", "Approach", "Key Detail"],
            "data": {
                "Thrombotic thrombocytopenic purpura": {
                    "Situation": "Adult with neurologic signs and thrombocytopenia",
                    "Approach": "Urgent plasmapheresis (plasma exchange)",
                    "Key Detail": "Clears and replaces defective ADAMTS13; a medical emergency"
                },
                "Hemolytic-uremic syndrome": {
                    "Situation": "Child with bloody diarrhea and acute kidney injury",
                    "Approach": "Supportive care with IV fluids and electrolytes",
                    "Key Detail": "Antibiotics are not useful in most cases"
                },
                "Secondary thrombotic microangiopathy": {
                    "Situation": "TM caused by a drug or underlying disease",
                    "Approach": "Remove the causative drug or treat the condition",
                    "Key Detail": "Correcting the cause resolves the process"
                },
                "Confirming immune TTP": {
                    "Situation": "Cause remains unclear after routine testing",
                    "Approach": "Measure ADAMTS13 activity and check for an inhibitor",
                    "Key Detail": "Activity under 10% suggests immune TTP"
                },
                "Distinguishing TTP from HUS": {
                    "Situation": "Deciding between the two primary TMs",
                    "Approach": "Rely on the clinical history and physical exam",
                    "Key Detail": "Lab tests and smear cannot separate them"
                }
            }
        }
    ]
}
