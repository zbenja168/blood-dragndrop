BRICK = {
    "brick_num": 14,
    "brick_title": "Autoimmune Hemolytic Anemias",
    "games": [
        {
            "slug": "aha_subtypes",
            "title": "Subtypes of Immune Hemolysis",
            "subtitle": "Match each hemolytic disorder to its antibody/defect, main hemolysis site, and key feature",
            "categories": ["Antibody or Defect", "Main Hemolysis Site", "Key Feature"],
            "data": {
                "Warm AHA": {
                    "Antibody or Defect": "IgG autoantibody, most active at 37 C",
                    "Main Hemolysis Site": "Extravascular, in the spleen",
                    "Key Feature": "Spherocytes on the blood smear"
                },
                "Cold AHA": {
                    "Antibody or Defect": "IgM cold agglutinin, active below 30 C",
                    "Main Hemolysis Site": "Mostly extravascular but more intravascular than warm",
                    "Key Feature": "RBC agglutinates and acrocyanosis in cold"
                },
                "Paroxysmal Cold Hemoglobinuria": {
                    "Antibody or Defect": "Biphasic IgG Donath-Landsteiner anti-P antibody",
                    "Main Hemolysis Site": "Intravascular",
                    "Key Feature": "Children after viral infection; self-limited"
                },
                "Paroxysmal Nocturnal Hemoglobinuria": {
                    "Antibody or Defect": "Acquired PIGA mutation; missing CD55 and CD59",
                    "Main Hemolysis Site": "Intravascular, complement-mediated",
                    "Key Feature": "Venous thrombosis and pancytopenia"
                }
            }
        },
        {
            "slug": "aha_labs",
            "title": "Working Up Hemolysis",
            "subtitle": "Match each test to what it detects, its result in disease, and its main clinical use",
            "categories": ["What It Detects", "Result in Disease", "Primary Use"],
            "data": {
                "Direct Antiglobulin Test": {
                    "What It Detects": "Antibody or complement coating the patient's RBCs",
                    "Result in Disease": "Positive in AHA, negative in nonimmune hemolysis",
                    "Primary Use": "Distinguishes AHA from other hemolytic anemias"
                },
                "Complete Blood Count": {
                    "What It Detects": "RBC indices and cell counts",
                    "Result in Disease": "Normocytic anemia with increased reticulocytes",
                    "Primary Use": "Shows anemia and marrow compensation"
                },
                "Serum Haptoglobin": {
                    "What It Detects": "Free plasma haptoglobin that binds released hemoglobin",
                    "Result in Disease": "Decreased, especially with intravascular hemolysis",
                    "Primary Use": "Confirms ongoing hemolysis"
                },
                "Flow Cytometry": {
                    "What It Detects": "GPI-anchored surface proteins on blood cells",
                    "Result in Disease": "Absence of CD55 and CD59 anchors",
                    "Primary Use": "Key diagnostic test for PNH"
                },
                "Peripheral Blood Smear": {
                    "What It Detects": "RBC morphology under the microscope",
                    "Result in Disease": "Spherocytes in warm, agglutinates in cold AHA",
                    "Primary Use": "Supports the diagnosis and type of hemolysis"
                }
            }
        },
        {
            "slug": "aha_treatments",
            "title": "Treating Autoimmune Hemolysis",
            "subtitle": "Match each therapy to its mechanism, best indication, and important caveat",
            "categories": ["Mechanism", "Best Indication", "Important Caveat"],
            "data": {
                "Glucocorticoids": {
                    "Mechanism": "Anti-inflammatory suppression of the immune response",
                    "Best Indication": "First-line therapy for warm AHA",
                    "Important Caveat": "Not clinically useful in cold AHA"
                },
                "Rituximab": {
                    "Mechanism": "Anti-CD20 antibody that destroys B lymphocytes",
                    "Best Indication": "Warm AHA and may help refractory cold AHA",
                    "Important Caveat": "Works by preventing autoantibody production"
                },
                "Splenectomy": {
                    "Mechanism": "Removes the main site of extravascular hemolysis",
                    "Best Indication": "Warm AHA refractory to other therapies",
                    "Important Caveat": "Raises risk of encapsulated bacterial infection"
                },
                "RBC Transfusion": {
                    "Mechanism": "Replaces lost red blood cells to raise hemoglobin",
                    "Best Indication": "Temporary support in severe anemia",
                    "Important Caveat": "Transfused cells are also coated by autoantibodies"
                },
                "Eculizumab": {
                    "Mechanism": "Recombinant antibody against complement component C5",
                    "Best Indication": "Paroxysmal nocturnal hemoglobinuria",
                    "Important Caveat": "Raises Neisseria risk; vaccinate before use"
                }
            }
        },
        {
            "slug": "aha_etiologies",
            "title": "Causes and Associations of AHA",
            "subtitle": "Match each cause category to a representative example and its link to AHA",
            "categories": ["Type of Cause", "Representative Example", "Association with AHA"],
            "data": {
                "Medications": {
                    "Type of Cause": "Drug-induced autoantibody formation",
                    "Representative Example": "Penicillins, cephalosporins, quinidine, NSAIDs",
                    "Association with AHA": "Major cause of warm AHA"
                },
                "Acute Infections": {
                    "Type of Cause": "Infection-triggered antibodies",
                    "Representative Example": "Mycoplasma pneumoniae and Epstein-Barr virus",
                    "Association with AHA": "Classic trigger of cold AHA"
                },
                "Autoimmune Disorders": {
                    "Type of Cause": "Systemic autoimmune disease",
                    "Representative Example": "Systemic lupus erythematosus and rheumatoid arthritis",
                    "Association with AHA": "Underlies both warm and cold secondary AHA"
                },
                "Malignancy": {
                    "Type of Cause": "Neoplastic disease",
                    "Representative Example": "Leukemias, lymphomas, lymphoproliferative disorders",
                    "Association with AHA": "Cause of secondary AHA"
                },
                "Idiopathic": {
                    "Type of Cause": "No identifiable underlying cause",
                    "Representative Example": "Primary disease with no associated condition",
                    "Association with AHA": "Most common classification of AHA"
                }
            }
        }
    ]
}
