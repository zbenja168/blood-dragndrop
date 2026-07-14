BRICK = {
    "brick_num": 9,
    "brick_title": "Red Blood Cell Laboratory Tests",
    "games": [
        {
            "slug": "rbc_indices",
            "title": "RBC Indices on the CBC",
            "subtitle": "Match each red cell index to what it measures, its reference range, and a key interpretive point",
            "categories": ["What It Measures", "Typical Reference Range", "Key Interpretive Point"],
            "data": {
                "RBC count": {
                    "What It Measures": "Number of red blood cells per volume of blood",
                    "Typical Reference Range": "Males 4.3-5.9 x10^12/L; females 3.5-5.5 x10^12/L",
                    "Key Interpretive Point": "Decreased in anemia, increased in polycythemia"
                },
                "Hemoglobin (Hgb)": {
                    "What It Measures": "Concentration of hemoglobin in the blood",
                    "Typical Reference Range": "Males 14-18 g/dL; females 12-16 g/dL",
                    "Key Interpretive Point": "Primary value used to define anemia"
                },
                "Hematocrit (Hct)": {
                    "What It Measures": "Percentage of blood volume occupied by RBCs",
                    "Typical Reference Range": "Males 40%-54%; females 36%-48%",
                    "Key Interpretive Point": "Runs roughly three times the hemoglobin value"
                },
                "Mean cell volume (MCV)": {
                    "What It Measures": "Average volume (size) of the red cells",
                    "Typical Reference Range": "80-100 fL",
                    "Key Interpretive Point": "Sorts anemia into microcytic, normocytic, macrocytic"
                },
                "Mean cell hemoglobin concentration (MCHC)": {
                    "What It Measures": "Average concentration of hemoglobin within each RBC",
                    "Typical Reference Range": "32-36 g/dL",
                    "Key Interpretive Point": "A low value defines hypochromia"
                },
                "Red cell distribution width (RDW)": {
                    "What It Measures": "Variability in red cell size (variation of the MCV)",
                    "Typical Reference Range": "12%-15%",
                    "Key Interpretive Point": "Elevated when there is anisocytosis"
                }
            }
        },
        {
            "slug": "rbc_shapes",
            "title": "Abnormal RBC Shapes on the Smear",
            "subtitle": "Match each abnormal red cell to its alternate name, distinguishing feature, and classic disease association",
            "categories": ["Alternate Name", "Distinguishing Feature", "Associated Disease"],
            "data": {
                "Acanthocyte": {
                    "Alternate Name": "Spur cell",
                    "Distinguishing Feature": "Irregular spiny projections of varying length and spacing",
                    "Associated Disease": "Liver disease"
                },
                "Codocyte": {
                    "Alternate Name": "Target cell",
                    "Distinguishing Feature": "Central dot of hemoglobin within the pallor (bullseye)",
                    "Associated Disease": "Thalassemia, iron deficiency, liver disease"
                },
                "Dacryocyte": {
                    "Alternate Name": "Teardrop cell",
                    "Distinguishing Feature": "Single elongated teardrop-shaped tail",
                    "Associated Disease": "Chronic myelofibrosis or marrow-infiltrating lesions"
                },
                "Schistocyte": {
                    "Alternate Name": "Helmet or fragmented cell",
                    "Distinguishing Feature": "Sharp jagged fragments from mechanical shearing",
                    "Associated Disease": "Microangiopathic hemolytic anemia"
                },
                "Spherocyte": {
                    "Alternate Name": "Sphere-shaped cell",
                    "Distinguishing Feature": "Round dense cell lacking central pallor",
                    "Associated Disease": "Hereditary spherocytosis and warm autoimmune hemolytic anemia"
                },
                "Echinocyte": {
                    "Alternate Name": "Burr cell",
                    "Distinguishing Feature": "Short, uniform, evenly spaced blunt projections",
                    "Associated Disease": "Kidney disease or blood smear artifact"
                }
            }
        },
        {
            "slug": "rbc_inclusions",
            "title": "Red Cell Inclusions",
            "subtitle": "Match each RBC inclusion to its composition and the condition in which it appears",
            "categories": ["Composition", "Special Stain / Clue", "Associated Condition"],
            "data": {
                "Basophilic stippling": {
                    "Composition": "Aggregated ribosomes / RNA",
                    "Special Stain / Clue": "Fine to coarse blue granules dispersed through the cell",
                    "Associated Condition": "Lead poisoning and thalassemia"
                },
                "Howell-Jolly body": {
                    "Composition": "Residual nuclear DNA remnant",
                    "Special Stain / Clue": "Single small round dark inclusion normally removed by spleen",
                    "Associated Condition": "Post-splenectomy or functional asplenia"
                },
                "Pappenheimer bodies": {
                    "Composition": "Iron-containing (siderotic) granules",
                    "Special Stain / Clue": "Clusters of granules that also stain with Prussian blue",
                    "Associated Condition": "Sideroblastic anemia"
                },
                "Plasmodium organisms": {
                    "Composition": "Intracellular malarial parasites",
                    "Special Stain / Clue": "Ring forms and other parasite stages within RBCs",
                    "Associated Condition": "Malaria"
                }
            }
        },
        {
            "slug": "ancillary_rbc_tests",
            "title": "Specialized Red Cell Tests",
            "subtitle": "Match each ancillary RBC test to what it detects and its classic abnormal finding",
            "categories": ["What It Detects", "Method / Reagent", "Classic Abnormal Finding"],
            "data": {
                "Hemoglobin electrophoresis": {
                    "What It Detects": "The types and relative amounts of hemoglobin present",
                    "Method / Reagent": "Charged gel separates Hb by migration (order A, F, S, C)",
                    "Classic Abnormal Finding": "Detects HbS in sickle cell disease/trait and abnormal Hb in thalassemia"
                },
                "Osmotic fragility test": {
                    "What It Detects": "How readily RBCs lyse in progressively hypotonic saline",
                    "Method / Reagent": "Blood added to solutions of decreasing NaCl concentration",
                    "Classic Abnormal Finding": "Increased fragility (lysis at higher NaCl) in hereditary spherocytosis"
                },
                "Direct antiglobulin test (Coombs)": {
                    "What It Detects": "Antibody or complement coating the patient's RBCs",
                    "Method / Reagent": "Anti-immunoglobulin (Coombs) reagent added to patient RBCs",
                    "Classic Abnormal Finding": "Agglutination (positive) in autoimmune hemolytic anemia"
                },
                "Reticulocyte count": {
                    "What It Detects": "Proportion of immature red cells reflecting marrow output",
                    "Method / Reagent": "Supravital stain (new methylene blue) shows ribosomal RNA network",
                    "Classic Abnormal Finding": "Value >2% indicates marrow response to hemolysis or blood loss"
                }
            }
        }
    ]
}
