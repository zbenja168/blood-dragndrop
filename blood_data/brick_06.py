BRICK = {
    "brick_num": 6,
    "brick_title": "Thalassemias",
    "games": [
        {
            "slug": "alpha_thalassemia_genotypes",
            "title": "Alpha-Thalassemia by Deleted Genes",
            "subtitle": "Match each alpha-globin genotype to its clinical severity and hallmark feature",
            "categories": ["Genotype", "Clinical Severity", "Hallmark Feature"],
            "data": {
                "Silent carrier (1 gene deleted)": {
                    "Genotype": "aa/a- (one of four alpha genes deleted)",
                    "Clinical Severity": "No anemia, asymptomatic",
                    "Hallmark Feature": "Found incidentally as mild microcytosis on smear"
                },
                "Alpha-thalassemia trait (2 genes deleted)": {
                    "Genotype": "aa/-- or a-/a- (two alpha genes deleted)",
                    "Clinical Severity": "Mild anemia",
                    "Hallmark Feature": "Anemia appears mainly after stress like surgery or infection"
                },
                "Hemoglobin H disease (3 genes deleted)": {
                    "Genotype": "a-/-- (three alpha genes deleted)",
                    "Clinical Severity": "Moderate to severe anemia",
                    "Hallmark Feature": "Excess beta chains form insoluble HbH tetramers"
                },
                "Hydrops fetalis (4 genes deleted)": {
                    "Genotype": "--/-- (all four alpha genes deleted)",
                    "Clinical Severity": "Extremely severe anemia, usually fatal in utero",
                    "Hallmark Feature": "No alpha chains; gamma chains form Hb Barts (gamma-4)"
                }
            }
        },
        {
            "slug": "beta_thalassemia_spectrum",
            "title": "Beta-Thalassemia Spectrum",
            "subtitle": "Match each beta-thalassemia phenotype to its genotype and defining feature",
            "categories": ["Genotype", "Anemia Severity", "Key Feature"],
            "data": {
                "Beta-thalassemia trait (minor)": {
                    "Genotype": "beta/beta-0 or beta/beta-plus (one gene mutated)",
                    "Anemia Severity": "Mild anemia",
                    "Key Feature": "One normal beta gene; production only slightly decreased"
                },
                "Beta-thalassemia intermedia (NTDT)": {
                    "Genotype": "beta-plus/beta-0 or beta-plus/beta-plus (two genes)",
                    "Anemia Severity": "Moderate to severe anemia",
                    "Key Feature": "Makes some beta chains; transfusions usually not needed"
                },
                "Beta-thalassemia major (TDT)": {
                    "Genotype": "beta-0/beta-0 (no beta chain production)",
                    "Anemia Severity": "Severe, life-threatening anemia",
                    "Key Feature": "Transfusion-dependent; fatal by age 5 without stem cell transplant"
                },
                "Sickle cell beta-thalassemia": {
                    "Genotype": "One HbS mutation plus one beta-thalassemia mutation",
                    "Anemia Severity": "Mild to moderate anemia",
                    "Key Feature": "Less severe than full sickle cell disease (HbS/HbS)"
                }
            }
        },
        {
            "slug": "hemoglobin_types",
            "title": "Hemoglobin Species in Thalassemia",
            "subtitle": "Match each hemoglobin to its globin chains and diagnostic significance",
            "categories": ["Globin Chains", "When It Predominates", "Significance"],
            "data": {
                "HbA": {
                    "Globin Chains": "Two alpha and two beta (alpha-2 beta-2)",
                    "When It Predominates": "Main hemoglobin in the normal adult (>95%)",
                    "Significance": "Decreased or absent as thalassemia worsens"
                },
                "HbA2": {
                    "Globin Chains": "Two alpha and two delta (alpha-2 delta-2)",
                    "When It Predominates": "Minor normal adult form (<5%)",
                    "Significance": "Rises to compensate; elevated in beta-thalassemia trait"
                },
                "HbF": {
                    "Globin Chains": "Two alpha and two gamma (alpha-2 gamma-2)",
                    "When It Predominates": "Predominant in the fetus and young infant",
                    "Significance": "Can rise from <1% to >95% in beta-thalassemia major"
                },
                "HbH": {
                    "Globin Chains": "Four beta chains (beta-4 tetramer)",
                    "When It Predominates": "Adult alpha-thalassemia with 3-gene deletion",
                    "Significance": "Insoluble, cannot carry oxygen, shortens RBC lifespan"
                },
                "Hb Barts": {
                    "Globin Chains": "Four gamma chains (gamma-4 tetramer)",
                    "When It Predominates": "Fetus with 4-gene alpha deletion",
                    "Significance": "Seen in hydrops fetalis; cannot deliver oxygen"
                }
            }
        },
        {
            "slug": "diagnosis_and_management",
            "title": "Workup and Management of Thalassemia",
            "subtitle": "Match each test or therapy to its purpose and key point",
            "categories": ["Indication / Role", "Mechanism or Finding", "Key Point"],
            "data": {
                "Complete blood count": {
                    "Indication / Role": "Initial screen when thalassemia is suspected",
                    "Mechanism or Finding": "Low hemoglobin and low MCV (microcytosis)",
                    "Key Point": "RBC count normal or increased, unlike iron deficiency"
                },
                "Hemoglobin electrophoresis": {
                    "Indication / Role": "Confirm and classify beta-thalassemia",
                    "Mechanism or Finding": "Measures percentages of HbA, HbA2, and HbF",
                    "Key Point": "HbA2 or HbF rise to compensate as HbA falls"
                },
                "Chronic transfusion": {
                    "Indication / Role": "Severe, transfusion-dependent anemia",
                    "Mechanism or Finding": "Maintains hemoglobin in an appropriate range",
                    "Key Point": "Causes iron overload (secondary hemochromatosis)"
                },
                "Deferoxamine": {
                    "Indication / Role": "Patients receiving chronic transfusions",
                    "Mechanism or Finding": "Iron-chelating agent that removes excess iron",
                    "Key Point": "Prevents iron deposition in heart, liver, endocrine organs"
                },
                "Luspatercept": {
                    "Indication / Role": "Reduce transfusion requirement",
                    "Mechanism or Finding": "Binds TGF-beta ligands on erythroid precursors",
                    "Key Point": "Enhances erythroid maturation and RBC production"
                },
                "Stem cell transplant": {
                    "Indication / Role": "Very severe cases as definitive therapy",
                    "Mechanism or Finding": "Replaces marrow with healthy hematopoietic cells",
                    "Key Point": "Reserved for severe disease; risks graft-vs-host disease"
                }
            }
        }
    ]
}
