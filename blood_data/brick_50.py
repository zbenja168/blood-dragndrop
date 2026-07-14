BRICK = {
    "brick_num": 50,
    "brick_title": "Myelodysplastic Neoplasms",
    "games": [
        {
            "slug": "mds_dysplasia",
            "title": "Dysplastic Cell Changes in MDS",
            "subtitle": "Match each cell type to its bone marrow finding, its peripheral blood finding, and a key note",
            "categories": ["Bone Marrow Finding", "Peripheral Blood Finding", "Detection or Note"],
            "data": {
                "Red blood cell precursors": {
                    "Bone Marrow Finding": "Nuclear budding, multiple nuclei, and nuclear-cytoplasmic asynchrony",
                    "Peripheral Blood Finding": "Macrocytic red cells with a high mean cell volume",
                    "Detection or Note": "Ring sideroblasts show perinuclear iron granules on Prussian blue stain"
                },
                "Neutrophils": {
                    "Bone Marrow Finding": "Bizarre precursors with hyposegmentation and hypogranulation",
                    "Peripheral Blood Finding": "Two-lobed or unlobed nucleus with clear, light grey cytoplasm",
                    "Detection or Note": "Hypogranularity reflects a loss of secondary granules"
                },
                "Megakaryocytes": {
                    "Bone Marrow Finding": "Much smaller than normal with more or fewer nuclei than usual",
                    "Peripheral Blood Finding": "Release hypergranular, hypogranular, or oversized platelets",
                    "Detection or Note": "The normal form has a single multilobulated nucleus"
                },
                "Blasts": {
                    "Bone Marrow Finding": "Must make up less than 20% of marrow cells",
                    "Peripheral Blood Finding": "Their exact count helps determine prognosis",
                    "Detection or Note": "A count of 20% or more means AML, not MDS"
                }
            }
        },
        {
            "slug": "mds_medications",
            "title": "Medications Used in MDS",
            "subtitle": "Match each therapy to its mechanism, its typical use, and a key note",
            "categories": ["Mechanism", "Typical Use in MDS", "Key Adverse Effect or Note"],
            "data": {
                "Erythropoietin": {
                    "Mechanism": "Endogenous kidney hormone that stimulates marrow red cell production",
                    "Typical Use in MDS": "Low-risk patients with fatigue from anemia",
                    "Key Adverse Effect or Note": "Given by IV infusion; also used in end-stage renal disease"
                },
                "Lenalidomide": {
                    "Mechanism": "Immune-modulating drug that lowers TNF-alpha and inhibits cell growth",
                    "Typical Use in MDS": "Symptomatic low-risk patients, especially isolated del(5q)",
                    "Key Adverse Effect or Note": "Black box teratogen; risk of neutropenia, thrombosis, and hepatotoxicity"
                },
                "Azacitidine": {
                    "Mechanism": "Pyrimidine nucleoside analog that inhibits DNA methylation",
                    "Typical Use in MDS": "Low-risk patients; similar to decitabine",
                    "Key Adverse Effect or Note": "Nausea, diarrhea, mucositis, and myelosuppression"
                },
                "Allogeneic stem cell transplant": {
                    "Mechanism": "Replaces the nonfunctional marrow with donor stem cells",
                    "Typical Use in MDS": "Patients at very high risk of progression to AML",
                    "Key Adverse Effect or Note": "The only option that offers a potential cure"
                },
                "Venetoclax": {
                    "Mechanism": "Selectively inhibits the anti-apoptotic protein BCL-2",
                    "Typical Use in MDS": "High-risk treatment-naive patients, added to azacitidine",
                    "Key Adverse Effect or Note": "Cytotoxic to tumor cells that overexpress BCL-2"
                }
            }
        },
        {
            "slug": "mds_workup",
            "title": "Diagnostic Workup of MDS",
            "subtitle": "Match each study to its purpose and its finding or role in MDS",
            "categories": ["Purpose", "Finding or Role in MDS"],
            "data": {
                "Complete blood count": {
                    "Purpose": "Screens the peripheral blood cell counts",
                    "Finding or Role in MDS": "Shows one or more cytopenias, anemia being the most common"
                },
                "Peripheral blood smear": {
                    "Purpose": "Examines circulating cell morphology",
                    "Finding or Role in MDS": "Macrocytic red cells and hypogranular, hyposegmented neutrophils"
                },
                "Cytogenetic and molecular studies": {
                    "Purpose": "FISH, karyotype, and gene sequencing on marrow or blood",
                    "Finding or Role in MDS": "Identifies chromosomal abnormalities such as del(5q)"
                },
                "Bone marrow biopsy": {
                    "Purpose": "Analyzes marrow morphology and blast percentage",
                    "Finding or Role in MDS": "At least 10% dysplastic cells and fewer than 20% blasts"
                },
                "History and physical examination": {
                    "Purpose": "Elicits cytopenia consequences and excludes other causes",
                    "Finding or Role in MDS": "Pallor, bruising, infection, and relevant exposure history"
                }
            }
        },
        {
            "slug": "mds_genetics_risk",
            "title": "Genetics, Risk, and Prognosis in MDS",
            "subtitle": "Match each genetic or prognostic factor to its significance",
            "categories": ["Detail", "Significance"],
            "data": {
                "del(5q)": {
                    "Detail": "Single most common chromosomal abnormality in MDS",
                    "Significance": "Its subtype affects older women with anemia but a low risk of leukemia"
                },
                "Additional cytogenetic abnormalities": {
                    "Detail": "Chromosomal changes beyond del(5q)",
                    "Significance": "Associated with poor prognosis and likely progression to AML"
                },
                "Therapy-related MDS": {
                    "Detail": "Follows prior cytotoxic chemotherapy or radiation",
                    "Significance": "Carries a poorer prognosis and lower survival"
                },
                "Detectable mutations": {
                    "Detail": "One or more found in 75% to 90% of patients on genetic testing",
                    "Significance": "Guide risk stratification, treatment, and prognosis"
                },
                "IPSS-R score": {
                    "Detail": "Uses cytogenetics, blasts, hemoglobin, platelets, and neutrophils",
                    "Significance": "Determines patient risk and median survival"
                },
                "Progression to AML": {
                    "Detail": "Occurs in roughly 30% of patients with MDS",
                    "Significance": "A rising blast count toward the 20% cutoff increases the risk"
                }
            }
        }
    ]
}
