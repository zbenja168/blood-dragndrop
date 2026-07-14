BRICK = {
    "brick_num": 12,
    "brick_title": "Sickle Cell Disease",
    "games": [
        {
            "slug": "hemoglobin_variants",
            "title": "Hemoglobin Variants",
            "subtitle": "Match each hemoglobin variant to its beta-globin change, genotype, and clinical picture",
            "categories": ["Beta-globin change", "Genotype", "Clinical presentation"],
            "data": {
                "Normal hemoglobin (HbA)": {
                    "Beta-globin change": "Wild-type beta chain (glutamate at codon 6)",
                    "Genotype": "Two normal beta-globin genes",
                    "Clinical presentation": "Healthy, no hemolytic anemia"
                },
                "Sickle cell disease (HbSS)": {
                    "Beta-globin change": "Glutamate replaced by valine at position 6",
                    "Genotype": "Two mutated (sickle) beta genes, homozygous",
                    "Clinical presentation": "Hemolytic anemia and vaso-occlusive crises"
                },
                "Sickle cell trait (HbAS)": {
                    "Beta-globin change": "One valine-substituted beta chain",
                    "Genotype": "One normal and one sickle beta gene, heterozygous",
                    "Clinical presentation": "Usually asymptomatic; hematuria at high altitude"
                },
                "Hemoglobin C disease (HbCC)": {
                    "Beta-globin change": "Glutamate replaced by lysine at position 6",
                    "Genotype": "Two mutated (C) beta genes, homozygous",
                    "Clinical presentation": "Mild hemolytic anemia with Hb C crystals"
                },
                "Hemoglobin SC disease": {
                    "Beta-globin change": "One valine-substituted and one lysine-substituted beta chain",
                    "Genotype": "One sickle and one C beta gene",
                    "Clinical presentation": "Sickling disease milder than homozygous HbSS"
                }
            }
        },
        {
            "slug": "vasoocclusive_complications",
            "title": "Vaso-Occlusive Complications",
            "subtitle": "Match each complication to its site, mechanism, and clinical consequence",
            "categories": ["Site or organ", "Mechanism", "Clinical consequence"],
            "data": {
                "Acute chest syndrome": {
                    "Site or organ": "Pulmonary blood vessels",
                    "Mechanism": "Clogging of blood vessels of the lungs",
                    "Clinical consequence": "Chest pain, fever, hypoxia; a leading cause of mortality"
                },
                "Functional asplenia": {
                    "Site or organ": "Spleen",
                    "Mechanism": "Repeated splenic ischemia, infarction, and fibrosis",
                    "Clinical consequence": "Infection risk from encapsulated bacteria"
                },
                "Dactylitis": {
                    "Site or organ": "Bones of the hands and feet",
                    "Mechanism": "Small-vessel occlusion in the digits",
                    "Clinical consequence": "Painful swelling of hands and feet"
                },
                "Avascular necrosis": {
                    "Site or organ": "Head of the femur and hip",
                    "Mechanism": "Infarction of large weight-bearing bones",
                    "Clinical consequence": "Bone death with groin pain on bearing weight"
                },
                "Priapism": {
                    "Site or organ": "Penile venules",
                    "Mechanism": "Occlusion of penile venous outflow",
                    "Clinical consequence": "Painful and prolonged erection in men"
                },
                "Renal papillary necrosis": {
                    "Site or organ": "Innermost renal papilla",
                    "Mechanism": "Ischemic necrosis of renal tubular cells",
                    "Clinical consequence": "Hematuria, proteinuria, and declining renal function"
                }
            }
        },
        {
            "slug": "diagnostic_workup",
            "title": "Diagnostic Workup",
            "subtitle": "Match each study to its typical result, interpretation, and best use in sickle cell disease",
            "categories": ["Typical result in SCD", "Interpretation", "Best used for"],
            "data": {
                "Peripheral blood smear": {
                    "Typical result in SCD": "Sickled RBCs, target cells, and Howell-Jolly bodies",
                    "Interpretation": "Sickling with loss of splenic function",
                    "Best used for": "Visualizing red blood cell morphology"
                },
                "Hemoglobin electrophoresis": {
                    "Typical result in SCD": "HbS band migrating closer to the cathode than HbA",
                    "Interpretation": "Confirms HbS and defines zygosity",
                    "Best used for": "Distinguishing sickle cell trait from disease"
                },
                "Reticulocyte count": {
                    "Typical result in SCD": "Elevated above normal at baseline",
                    "Interpretation": "Marrow compensating for shortened RBC lifespan",
                    "Best used for": "Detecting aplastic crisis when it drops"
                },
                "Bilirubin and haptoglobin": {
                    "Typical result in SCD": "High unconjugated bilirubin and low haptoglobin",
                    "Interpretation": "Ongoing hemolysis with heme breakdown",
                    "Best used for": "Confirming hemolytic activity"
                },
                "Newborn blood spot screen": {
                    "Typical result in SCD": "Detects HbS at birth",
                    "Interpretation": "Presymptomatic identification of affected infants",
                    "Best used for": "Universal newborn screening in the US"
                }
            }
        },
        {
            "slug": "management_strategies",
            "title": "Management Strategies",
            "subtitle": "Match each intervention to its mechanism, indication, and key caveat",
            "categories": ["Mechanism of benefit", "Indication", "Key caveat"],
            "data": {
                "Hydroxyurea": {
                    "Mechanism of benefit": "Increases fetal hemoglobin and inhibits HbS polymerization",
                    "Indication": "Reduce frequency of pain and acute chest episodes",
                    "Key caveat": "Causes leukopenia; increased skin cancer and leukemia risk"
                },
                "Penicillin and vaccines": {
                    "Mechanism of benefit": "Prevent infection by encapsulated organisms",
                    "Indication": "Functional asplenia, especially in childhood",
                    "Key caveat": "Covers pneumococcus, meningococcus, and H influenzae"
                },
                "Folic acid": {
                    "Mechanism of benefit": "Replaces folate consumed by increased hematopoiesis",
                    "Indication": "Chronic support of red blood cell production",
                    "Key caveat": "Acts too slowly to help an acute crisis"
                },
                "Opioid analgesia": {
                    "Mechanism of benefit": "Controls severe vaso-occlusive pain",
                    "Indication": "Acute painful episode",
                    "Key caveat": "First-line therapy; hydration is secondary"
                },
                "Exchange transfusion": {
                    "Mechanism of benefit": "Removes sickled cells and replaces them with donor RBCs",
                    "Indication": "Acute chest syndrome, stroke, or priapism",
                    "Key caveat": "Reserved for severe acute complications"
                },
                "Stem cell transplant": {
                    "Mechanism of benefit": "Replaces marrow with normal hematopoietic cells",
                    "Indication": "Selected patients with severe SCD complications",
                    "Key caveat": "Potentially curative but high-risk and carefully planned"
                }
            }
        }
    ]
}
