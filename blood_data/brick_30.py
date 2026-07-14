BRICK = {
    "brick_num": 30,
    "brick_title": "Hematopoietic Neoplasms: Foundations and Frameworks",
    "games": [
        {
            "slug": "myeloid_neoplasms",
            "title": "Types of Myeloid Neoplasms",
            "subtitle": "Match each myeloid neoplasm to its category, its defining marrow change, and a key fact",
            "categories": ["Category", "Defining Marrow Change", "Key Fact"],
            "data": {
                "Acute myeloid leukemia (AML)": {
                    "Category": "Acute leukemia",
                    "Defining Marrow Change": "Malignant myeloid cells fill and replace the marrow",
                    "Key Fact": "Causes bone marrow failure, pancytopenia, and frequent infections"
                },
                "Chronic myeloid leukemia": {
                    "Category": "Myeloproliferative neoplasm",
                    "Defining Marrow Change": "Overgrowth of the granulocyte cell line",
                    "Key Fact": "Granulocyte dominance; associated with the t(9;22) translocation"
                },
                "Polycythemia vera": {
                    "Category": "Myeloproliferative neoplasm",
                    "Defining Marrow Change": "Overproduction of the red blood cell line",
                    "Key Fact": "Red blood cell (erythrocyte) dominance"
                },
                "Essential thrombocythemia": {
                    "Category": "Myeloproliferative neoplasm",
                    "Defining Marrow Change": "Overproduction of the platelet line",
                    "Key Fact": "Platelet dominance"
                },
                "Primary myelofibrosis": {
                    "Category": "Myeloproliferative neoplasm",
                    "Defining Marrow Change": "All precursor lines expand",
                    "Key Fact": "Marrow is eventually filled with fibrosis"
                },
                "Myelodysplastic neoplasms": {
                    "Category": "Myelodysplastic neoplasm",
                    "Defining Marrow Change": "Marrow replaced by dysplastic precursors that fail to mature",
                    "Key Fact": "Transforms to AML in 30% of patients"
                }
            }
        },
        {
            "slug": "lymphoid_neoplasms",
            "title": "Types of Lymphoid Neoplasms",
            "subtitle": "Match each lymphoid neoplasm to its cell of origin, maturity, and a key feature",
            "categories": ["Cell of Origin", "Precursor or Mature", "Key Feature"],
            "data": {
                "T-cell acute lymphoblastic leukemia/lymphoma": {
                    "Cell of Origin": "T cell",
                    "Precursor or Mature": "Precursor (immature)",
                    "Key Feature": "Common in children; T-ALL (blood/marrow) and T-LBL (tissue) are the same disease"
                },
                "Mycosis fungoides/Sezary syndrome": {
                    "Cell of Origin": "T cell",
                    "Precursor or Mature": "Mature",
                    "Key Feature": "Slow-growing skin lesions and desquamating rash; normal life expectancy"
                },
                "B-cell acute lymphoblastic leukemia/lymphoma": {
                    "Cell of Origin": "B cell",
                    "Precursor or Mature": "Precursor (immature)",
                    "Key Feature": "Mostly in children; better prognosis than the T-cell variant"
                },
                "Follicular lymphoma": {
                    "Cell of Origin": "B cell",
                    "Precursor or Mature": "Mature (low-grade NHL)",
                    "Key Feature": "Grows slowly with a good prognosis"
                },
                "Burkitt lymphoma": {
                    "Cell of Origin": "B cell",
                    "Precursor or Mature": "Mature (high-grade NHL)",
                    "Key Feature": "Grows explosively; common in Africa"
                },
                "Multiple myeloma": {
                    "Cell of Origin": "Plasma cell (mature B-cell derivative)",
                    "Precursor or Mature": "Mature (plasma cell neoplasm)",
                    "Key Feature": "Massive plasma cell proliferation in marrow; kidney failure and hypercalcemia"
                }
            }
        },
        {
            "slug": "diagnostic_methods",
            "title": "Diagnostic Methods in Hematopathology",
            "subtitle": "Match each laboratory method to what it analyzes, its main advantage, and its main disadvantage",
            "categories": ["What It Analyzes", "Main Advantage", "Main Disadvantage"],
            "data": {
                "Routine histology (H&E)": {
                    "What It Analyzes": "FFPE tissue thinly sliced and stained with hematoxylin and eosin",
                    "Main Advantage": "Generates an initial differential and can be stored over 10 years",
                    "Main Disadvantage": "Not available for blood samples; requires tissue"
                },
                "Flow cytometry": {
                    "What It Analyzes": "Cells passed single-file through lasers to read size and surface antigens",
                    "Main Advantage": "Confirms clonality and cell of origin",
                    "Main Disadvantage": "Requires fresh tissue; architecture is lost"
                },
                "Molecular analysis (PCR)": {
                    "What It Analyzes": "Extracted and amplified DNA or RNA screened for mutations",
                    "Main Advantage": "Highly sensitive; detects specific mutations",
                    "Main Disadvantage": "May detect mutations also present in normal individuals"
                },
                "Conventional cytogenetics (karyotype)": {
                    "What It Analyzes": "Metaphase chromosomes from viable, dividing cells",
                    "Main Advantage": "Evaluates all chromosomes at once",
                    "Main Disadvantage": "Time-consuming and requires dividing cells"
                },
                "Fluorescence in situ hybridization (FISH)": {
                    "What It Analyzes": "Fluorescent probes hybridized to specific chromosomes",
                    "Main Advantage": "Fast",
                    "Main Disadvantage": "Only analyzes select chromosomes you choose"
                }
            }
        },
        {
            "slug": "molecular_cytogenetic_markers",
            "title": "Molecular and Cytogenetic Markers",
            "subtitle": "Match each genetic marker to its associated disease, detection method, and clinical application",
            "categories": ["Associated Disease", "Detection Method", "Clinical Application"],
            "data": {
                "BRAF V600E mutation": {
                    "Associated Disease": "Hairy cell leukemia (about 100% of cases)",
                    "Detection Method": "Molecular analysis (PCR/sequencing)",
                    "Clinical Application": "Confirms diagnosis"
                },
                "MYD88 L265P mutation": {
                    "Associated Disease": "Lymphoplasmacytic lymphoma (over 90% of cases)",
                    "Detection Method": "Molecular analysis (PCR/sequencing)",
                    "Clinical Application": "Confirms diagnosis"
                },
                "BCR::ABL1 rearrangement": {
                    "Associated Disease": "B-lymphoblastic leukemia (B-ALL)",
                    "Detection Method": "Molecular analysis of the rearrangement",
                    "Clinical Application": "Predicts a worse prognosis"
                },
                "FLT3 mutation": {
                    "Associated Disease": "Acute myeloid leukemia (AML)",
                    "Detection Method": "Molecular analysis (PCR/sequencing)",
                    "Clinical Application": "Guides treatment with FLT3 inhibitors such as midostaurin"
                },
                "t(9;22) translocation": {
                    "Associated Disease": "Chronic myeloid leukemia (CML)",
                    "Detection Method": "Conventional cytogenetics (karyotype)",
                    "Clinical Application": "Confirms the diagnosis"
                },
                "Trisomy 12": {
                    "Associated Disease": "Chronic lymphocytic leukemia (CLL)",
                    "Detection Method": "Fluorescence in situ hybridization (FISH)",
                    "Clinical Application": "Seen as three copies of chromosome 12"
                }
            }
        }
    ]
}
