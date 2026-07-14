BRICK = {
    "brick_num": 43,
    "brick_title": "Hodgkin Lymphoma",
    "games": [
        {
            "slug": "hl_histologic_subtypes",
            "title": "Histologic Subtypes of Hodgkin Lymphoma",
            "subtitle": "Match each subtype to its frequency, defining histologic feature, and a clinical note",
            "categories": ["Frequency", "Histologic Feature", "Clinical Note"],
            "data": {
                "Nodular sclerosis": {
                    "Frequency": "Most common type, about 70-75% of cases",
                    "Histologic Feature": "Fibrous bands divide nodes into nodules; lacunar cell variants",
                    "Clinical Note": "Young adults, usually early stage, with an excellent prognosis"
                },
                "Mixed cellularity": {
                    "Frequency": "Second most common, about 20% of cases",
                    "Histologic Feature": "Classic RS cells and reactive inflammatory infiltrate, no fibrous bands",
                    "Clinical Note": "Older patients, more advanced disease, often EBV-associated"
                },
                "Lymphocyte-rich": {
                    "Frequency": "One of two less-common classic subtypes",
                    "Histologic Feature": "More reactive mature lymphocytes than classic RS cells",
                    "Clinical Note": "A less-common form of classic Hodgkin lymphoma"
                },
                "Lymphocyte-depleted": {
                    "Frequency": "Least common classic subtype",
                    "Histologic Feature": "Abundant classic RS cells but few reactive lymphocytes",
                    "Clinical Note": "More often associated with EBV and HIV infection"
                },
                "Nodular lymphocyte-predominant": {
                    "Frequency": "Uncommon, about 5% of all Hodgkin lymphomas",
                    "Histologic Feature": "Large 'popcorn' cells with convoluted nuclei",
                    "Clinical Note": "Young males, localized indolent disease, no EBV association"
                }
            }
        },
        {
            "slug": "hl_abvd_chemotherapy",
            "title": "ABVD Chemotherapy Agents",
            "subtitle": "Match each drug in the ABVD regimen to its class, mechanism, and signature adverse effect",
            "categories": ["Drug Class", "Mechanism", "Signature Adverse Effect"],
            "data": {
                "Doxorubicin (Adriamycin)": {
                    "Drug Class": "Anthracycline; the 'A' in ABVD",
                    "Mechanism": "Inhibition of DNA/RNA synthesis",
                    "Signature Adverse Effect": "Cumulative dose-related cardiomyopathy and heart failure"
                },
                "Bleomycin": {
                    "Drug Class": "Metal-chelating chemotherapy antibiotic",
                    "Mechanism": "Fragments DNA chains in nondividing tumor cells",
                    "Signature Adverse Effect": "Severe pulmonary fibrosis, fever, hypersensitivity reactions"
                },
                "Vinblastine": {
                    "Drug Class": "Vinca alkaloid",
                    "Mechanism": "Inhibition of microtubule function",
                    "Signature Adverse Effect": "Peripheral neuropathy, paresthesia, loss of reflexes"
                },
                "Dacarbazine": {
                    "Drug Class": "Non-cell cycle-specific purine analog",
                    "Mechanism": "Inhibits DNA polymerase, causing DNA strand breaks",
                    "Signature Adverse Effect": "Nausea and vomiting over 90%, bone marrow suppression"
                }
            }
        },
        {
            "slug": "hl_staging",
            "title": "Staging of Hodgkin Lymphoma",
            "subtitle": "Match each stage to its nodal extent, relationship to the diaphragm, and descriptor",
            "categories": ["Nodal Extent", "Relation to Diaphragm", "Descriptor"],
            "data": {
                "Stage I": {
                    "Nodal Extent": "Localized disease in a single lymph node region",
                    "Relation to Diaphragm": "Confined to one side",
                    "Descriptor": "The earliest, most localized stage"
                },
                "Stage II": {
                    "Nodal Extent": "Two or more lymph node regions",
                    "Relation to Diaphragm": "All involved nodes on the same side",
                    "Descriptor": "Adds a suffix such as IIA or IIB for B symptoms"
                },
                "Stage III": {
                    "Nodal Extent": "Lymph node regions above and below",
                    "Relation to Diaphragm": "Involvement on both sides",
                    "Descriptor": "First stage seen on both sides of the diaphragm"
                },
                "Stage IV": {
                    "Nodal Extent": "Widespread disease in multiple organs",
                    "Relation to Diaphragm": "Disseminated beyond the lymphatic system",
                    "Descriptor": "Most advanced; may involve liver or bone marrow"
                }
            }
        },
        {
            "slug": "hl_diagnostic_workup",
            "title": "Diagnostic Workup and Staging Tests",
            "subtitle": "Match each test to what it demonstrates and its clinical purpose in Hodgkin lymphoma",
            "categories": ["Modality or Test", "What It Shows", "Clinical Purpose"],
            "data": {
                "Lymph node biopsy": {
                    "Modality or Test": "Biopsy of an accessible enlarged node",
                    "What It Shows": "Reed-Sternberg cells in a reactive background",
                    "Clinical Purpose": "Provides the definitive tissue diagnosis of HL"
                },
                "PET/CT scan": {
                    "Modality or Test": "F-18 fluorodeoxyglucose PET/CT imaging",
                    "What It Shows": "Nodal chains above and below the diaphragm",
                    "Clinical Purpose": "Determines the extent of disease to guide staging"
                },
                "Complete blood count": {
                    "Modality or Test": "Peripheral blood cell count",
                    "What It Shows": "Pancytopenia",
                    "Clinical Purpose": "Suggests infiltration of the bone marrow"
                },
                "Serum chemistry markers": {
                    "Modality or Test": "LDH, potassium, and ESR levels",
                    "What It Shows": "Elevated values",
                    "Clinical Purpose": "Reflect increased blood cell turnover"
                },
                "Chest x-ray": {
                    "Modality or Test": "Plain chest radiograph",
                    "What It Shows": "A mediastinal mass or mediastinal lymphadenopathy",
                    "Clinical Purpose": "Often the first clue that prompts further workup"
                }
            }
        }
    ]
}
