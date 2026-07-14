BRICK = {
    "brick_num": 5,
    "brick_title": "Iron-Deficiency Anemia",
    "games": [
        {
            "slug": "iron_handling_molecules",
            "title": "Iron-Handling Molecules",
            "subtitle": "Match each molecule to its location, function, and key regulatory feature",
            "categories": ["Location / Source", "Primary Function", "Key Regulatory Feature"],
            "data": {
                "HCP1 (heme carrier protein 1)": {
                    "Location / Source": "Duodenal enterocyte apical membrane (heme pathway)",
                    "Primary Function": "Absorbs heme-bound ferrous iron from the gut lumen",
                    "Key Regulatory Feature": "Imports the heme-bound form of iron directly"
                },
                "DMT-1": {
                    "Location / Source": "Duodenal enterocyte apical membrane (nonheme pathway)",
                    "Primary Function": "Imports nonheme ferrous iron into the enterocyte",
                    "Key Regulatory Feature": "Requires ferric iron to first be reduced to ferrous"
                },
                "Ferroportin": {
                    "Location / Source": "Basolateral membrane of enterocytes and macrophages",
                    "Primary Function": "Transports iron across the cell membrane into the blood",
                    "Key Regulatory Feature": "Internalized and degraded when hepcidin is high"
                },
                "Ferritin": {
                    "Location / Source": "Intracellular; the liver stores the bulk of body iron",
                    "Primary Function": "Stores iron and neutralizes iron's free radicals",
                    "Key Regulatory Feature": "Positive acute-phase reactant that rises in inflammation"
                },
                "Transferrin": {
                    "Location / Source": "Blood plasma",
                    "Primary Function": "Transports iron through the bloodstream",
                    "Key Regulatory Feature": "Liver makes more of it when iron is low, raising TIBC"
                },
                "Hepcidin": {
                    "Location / Source": "Secreted by liver hepatocytes",
                    "Primary Function": "Blocks iron release by degrading ferroportin",
                    "Key Regulatory Feature": "Inhibited by erythropoietin; increased by inflammation"
                }
            }
        },
        {
            "slug": "causes_of_ida",
            "title": "Causes of Iron-Deficiency Anemia",
            "subtitle": "Match each cause to its mechanism category, example, and key detail",
            "categories": ["Mechanism Category", "Representative Example", "Key Detail"],
            "data": {
                "Heavy menses": {
                    "Mechanism Category": "Chronic blood loss",
                    "Representative Example": "Premenopausal woman with menorrhagia",
                    "Key Detail": "Most common overall cause; menses loses about 1 mg iron per day"
                },
                "Colon cancer": {
                    "Mechanism Category": "Chronic gastrointestinal blood loss",
                    "Representative Example": "Occult slow bleeding from a GI tumor",
                    "Key Detail": "In an older man or postmenopausal woman, assume GI malignancy until proven otherwise"
                },
                "Hookworm infection": {
                    "Mechanism Category": "Parasitic gastrointestinal blood loss",
                    "Representative Example": "Ancylostoma infection in tropical regions",
                    "Key Detail": "A leading cause of GI iron loss in tropical and subtropical areas"
                },
                "Pregnancy": {
                    "Mechanism Category": "Increased iron demand",
                    "Representative Example": "Iron needs of the growing fetus",
                    "Key Detail": "Placenta strips iron from the mother even if she is deficient"
                },
                "Vegan diet / cow's-milk infant": {
                    "Mechanism Category": "Insufficient dietary iron intake",
                    "Representative Example": "Plant-based diet or cow's-milk-fed infant",
                    "Key Detail": "Nonheme plant iron is poorly absorbed; cow's milk iron absorbs poorly"
                },
                "Bariatric surgery / antacids": {
                    "Mechanism Category": "Impaired iron absorption",
                    "Representative Example": "Post-gastric-bypass patient or chronic antacid user",
                    "Key Detail": "Tetracyclines and antacids also reduce GI iron absorption"
                }
            }
        },
        {
            "slug": "lab_findings_ida",
            "title": "Laboratory Findings in Iron-Deficiency Anemia",
            "subtitle": "Match each test to its direction, what it reflects, and the reason for the change",
            "categories": ["Direction in IDA", "What the Test Reflects", "Reason for the Change"],
            "data": {
                "Serum ferritin": {
                    "Direction in IDA": "Low",
                    "What the Test Reflects": "Total body iron stores",
                    "Reason for the Change": "Stores are depleted; a level <15 ng/mL is virtually diagnostic"
                },
                "Total iron-binding capacity (TIBC)": {
                    "Direction in IDA": "High",
                    "What the Test Reflects": "Number of open transferrin binding sites",
                    "Reason for the Change": "Liver makes more transferrin to capture the scarce iron"
                },
                "Transferrin saturation": {
                    "Direction in IDA": "Low",
                    "What the Test Reflects": "Percent of transferrin binding sites occupied by iron",
                    "Reason for the Change": "Little iron combined with increased transferrin lowers the ratio"
                },
                "Mean corpuscular volume (MCV)": {
                    "Direction in IDA": "Low (microcytic)",
                    "What the Test Reflects": "Average red blood cell size",
                    "Reason for the Change": "Decreased hemoglobin per cell yields smaller red cells"
                },
                "Red cell distribution width (RDW)": {
                    "Direction in IDA": "High",
                    "What the Test Reflects": "Variation in red blood cell size",
                    "Reason for the Change": "Anisocytosis develops as iron availability varies"
                },
                "Reticulocyte count": {
                    "Direction in IDA": "Low (less than 0.5%)",
                    "What the Test Reflects": "Bone marrow red cell production",
                    "Reason for the Change": "Too little iron for the marrow to make new red cells"
                }
            }
        },
        {
            "slug": "clinical_signs_ida",
            "title": "Clinical Signs of Iron Deficiency",
            "subtitle": "Match each finding to its body site, description, and clinical significance",
            "categories": ["Body Site", "Clinical Description", "Clinical Significance"],
            "data": {
                "Koilonychia": {
                    "Body Site": "Fingernails",
                    "Clinical Description": "Nails curve upward into a concave, spoon-like shape",
                    "Clinical Significance": "A relatively specific chronic sign of iron deficiency"
                },
                "Angular cheilitis": {
                    "Body Site": "Corners of the mouth",
                    "Clinical Description": "Cracks and fissures with redness, swelling, or crusting",
                    "Clinical Significance": "A mucocutaneous manifestation of iron deficiency"
                },
                "Atrophic glossitis": {
                    "Body Site": "Tongue",
                    "Clinical Description": "Papillae shrink, leaving a shiny, smooth, flattened surface",
                    "Clinical Significance": "Also seen in B-vitamin deficiency and malnutrition"
                },
                "Pica": {
                    "Body Site": "Appetite / behavior",
                    "Clinical Description": "Persistent craving and ingestion of ice, dirt, clay, or paint chips",
                    "Clinical Significance": "A symptom specifically related to iron deficiency"
                },
                "Plummer-Vinson syndrome": {
                    "Body Site": "Esophagus and tongue",
                    "Clinical Description": "Atrophic glossitis, esophageal webs, and dysphagia",
                    "Clinical Significance": "Carries a risk of esophageal squamous cell carcinoma"
                },
                "Conjunctival pallor": {
                    "Body Site": "Conjunctivae and skin",
                    "Clinical Description": "Pale mucous membranes, skin, and conjunctivae",
                    "Clinical Significance": "A general sign common to any anemia"
                }
            }
        }
    ]
}
