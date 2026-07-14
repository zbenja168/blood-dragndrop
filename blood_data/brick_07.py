BRICK = {
    "brick_num": 7,
    "brick_title": "Anemia of Chronic Disease/Inflammation",
    "games": [
        {
            "slug": "acd_iron_studies",
            "title": "Iron Studies in Anemia of Chronic Disease",
            "subtitle": "Match each lab test to its level in ACD, the mechanism, and its acute-phase reactant type",
            "categories": ["Level in ACD", "Mechanism", "Acute-phase reactant type"],
            "data": {
                "Serum ferritin": {
                    "Level in ACD": "Normal or high",
                    "Mechanism": "Liver makes more of it during inflammation",
                    "Acute-phase reactant type": "Positive acute-phase reactant"
                },
                "Serum iron": {
                    "Level in ACD": "Low",
                    "Mechanism": "Iron sequestered in macrophages and hepatocytes",
                    "Acute-phase reactant type": "Not an acute-phase reactant"
                },
                "TIBC (transferrin)": {
                    "Level in ACD": "Low",
                    "Mechanism": "Liver makes less transferrin during inflammation",
                    "Acute-phase reactant type": "Negative acute-phase reactant"
                },
                "Transferrin saturation": {
                    "Level in ACD": "Low, sometimes normal",
                    "Mechanism": "Both circulating iron and transferrin are reduced",
                    "Acute-phase reactant type": "Ratio of serum iron to transferrin"
                },
                "Hemoglobin": {
                    "Level in ACD": "Low",
                    "Mechanism": "Decreased RBC production plus shortened RBC lifespan",
                    "Acute-phase reactant type": "Measured on the complete blood count"
                }
            }
        },
        {
            "slug": "acd_hepcidin_pathway",
            "title": "Hepcidin and Iron Sequestration",
            "subtitle": "Match each player in ACD pathophysiology to what it is, its action, and its effect on iron",
            "categories": ["What it is", "Action in ACD", "Effect on iron"],
            "data": {
                "Interleukin-6 (IL-6)": {
                    "What it is": "Inflammatory cytokine",
                    "Action in ACD": "Increases production of hepcidin",
                    "Effect on iron": "Lowers circulating plasma iron"
                },
                "Hepcidin": {
                    "What it is": "Iron-regulatory hormone",
                    "Action in ACD": "Causes internalization and degradation of ferroportin-1",
                    "Effect on iron": "Traps iron inside storage cells"
                },
                "Ferroportin-1": {
                    "What it is": "Cellular iron export channel",
                    "Action in ACD": "Decreased when degraded by hepcidin",
                    "Effect on iron": "Blocks iron release from enterocytes, macrophages, and hepatocytes"
                },
                "Macrophages and hepatocytes": {
                    "What it is": "Main iron storage cells",
                    "Action in ACD": "Cannot release their stored iron",
                    "Effect on iron": "Iron is retained, so less reaches the bone marrow"
                },
                "Interleukin-1 (IL-1)": {
                    "What it is": "Inflammatory cytokine",
                    "Action in ACD": "Prompts macrophages to prematurely ingest RBCs",
                    "Effect on iron": "Shortens RBC lifespan, worsening anemia"
                }
            }
        },
        {
            "slug": "acd_underlying_causes",
            "title": "Underlying Causes of ACD",
            "subtitle": "Match each underlying condition to its category, a clinical clue, and any added mechanism of anemia",
            "categories": ["Category", "Clinical clue", "Added mechanism of anemia"],
            "data": {
                "Rheumatoid arthritis": {
                    "Category": "Autoimmune disorder",
                    "Clinical clue": "Joint pain and swelling",
                    "Added mechanism of anemia": "Inflammation only (hepcidin-mediated)"
                },
                "Systemic lupus erythematosus": {
                    "Category": "Autoimmune disorder",
                    "Clinical clue": "Positive antinuclear antibody (ANA) test",
                    "Added mechanism of anemia": "Inflammation only (hepcidin-mediated)"
                },
                "Ulcerative colitis / Crohn disease": {
                    "Category": "Inflammatory bowel disease",
                    "Clinical clue": "Chronic gastrointestinal blood loss",
                    "Added mechanism of anemia": "Concurrent iron deficiency"
                },
                "Colon cancer": {
                    "Category": "Malignancy",
                    "Clinical clue": "GI blood loss",
                    "Added mechanism of anemia": "Concurrent iron deficiency"
                },
                "Leukemia": {
                    "Category": "Malignancy",
                    "Clinical clue": "Bone marrow infiltration",
                    "Added mechanism of anemia": "Marrow replacement lowers production"
                }
            }
        },
        {
            "slug": "acd_management",
            "title": "Managing Anemia of Chronic Disease",
            "subtitle": "Match each intervention to when it is indicated, the rationale, and a key caveat",
            "categories": ["When indicated", "Rationale", "Key caveat"],
            "data": {
                "Treat the underlying disorder": {
                    "When indicated": "First step for every ACD patient",
                    "Rationale": "Removes the inflammatory driver of the anemia",
                    "Key caveat": "Anemia often resolves once the disease is controlled"
                },
                "Oral iron supplementation": {
                    "When indicated": "Only with documented concurrent iron deficiency",
                    "Rationale": "Replaces genuinely depleted iron stores",
                    "Key caveat": "Confirm with serum ferritin before giving"
                },
                "RBC transfusion": {
                    "When indicated": "Profound anemia, typically below 7 g/dL",
                    "Rationale": "Rapidly restores oxygen-carrying capacity",
                    "Key caveat": "Generally not needed if the cause is treatable"
                },
                "Erythropoietin injections": {
                    "When indicated": "Severe cases; also anemia of chronic kidney disease",
                    "Rationale": "Stimulates marrow production of RBCs",
                    "Key caveat": "Not required for mild ACD"
                },
                "ESR and CRP testing": {
                    "When indicated": "When an inflammatory cause is suspected",
                    "Rationale": "Nonspecific markers that flag inflammation",
                    "Key caveat": "Do not identify the specific disease"
                }
            }
        }
    ]
}
