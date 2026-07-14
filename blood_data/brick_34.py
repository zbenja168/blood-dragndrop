BRICK = {
    "brick_num": 34,
    "brick_title": "Benign Lymphadenopathies",
    "games": [
        {
            "slug": "lymph_node_location_clues",
            "title": "Lymph Node Location Clues",
            "subtitle": "Match each enlarged node site to what it drains and what its enlargement suggests",
            "categories": ["Node Location", "Region Drained", "Enlargement Suggests"],
            "data": {
                "Left supraclavicular (Virchow) node": {
                    "Node Location": "Left base of neck above the clavicle",
                    "Region Drained": "Abdomen, via abdominal lymphatics into the thoracic duct",
                    "Enlargement Suggests": "Abdominal cancer, particularly gastric cancer"
                },
                "Right supraclavicular node": {
                    "Node Location": "Right base of neck above the clavicle",
                    "Region Drained": "Chest cavity and mid-thorax",
                    "Enlargement Suggests": "Malignancy in the chest such as lung cancer"
                },
                "Hilar nodes": {
                    "Node Location": "At the roots of the lungs (hilum)",
                    "Region Drained": "Lungs",
                    "Enlargement Suggests": "Lung infection, lung cancer, or sarcoidosis"
                },
                "Submandibular / submental nodes": {
                    "Node Location": "Under the jaw and chin",
                    "Region Drained": "Mouth, teeth, and throat",
                    "Enlargement Suggests": "Pharyngitis or dental abscess"
                },
                "Axillary nodes": {
                    "Node Location": "Armpit",
                    "Region Drained": "Upper extremity and breast",
                    "Enlargement Suggests": "Arm infection or breast cancer"
                }
            }
        },
        {
            "slug": "infectious_causes_of_adenopathy",
            "title": "Infectious Causes of Adenopathy",
            "subtitle": "Match each pathogen to its microbe class and the typical adenopathy pattern",
            "categories": ["Pathogen", "Microbe Class", "Typical Adenopathy Pattern"],
            "data": {
                "Epstein-Barr virus (mononucleosis)": {
                    "Pathogen": "Cause of infectious mononucleosis",
                    "Microbe Class": "Virus",
                    "Typical Adenopathy Pattern": "Cervical, often diffuse adenopathy"
                },
                "Mumps virus": {
                    "Pathogen": "Paramyxovirus causing parotitis",
                    "Microbe Class": "Virus",
                    "Typical Adenopathy Pattern": "Parotid (peri-parotid) enlargement"
                },
                "Tuberculosis": {
                    "Pathogen": "Mycobacterium tuberculosis",
                    "Microbe Class": "Bacterium",
                    "Typical Adenopathy Pattern": "Generalized or regional in the lung"
                },
                "Typhoid fever": {
                    "Pathogen": "Salmonella typhi",
                    "Microbe Class": "Bacterium",
                    "Typical Adenopathy Pattern": "Mesenteric adenopathy"
                },
                "Histoplasmosis": {
                    "Pathogen": "Histoplasma capsulatum",
                    "Microbe Class": "Fungus",
                    "Typical Adenopathy Pattern": "Hilar and mediastinal adenopathy"
                },
                "Toxoplasmosis": {
                    "Pathogen": "Toxoplasma gondii",
                    "Microbe Class": "Parasite",
                    "Typical Adenopathy Pattern": "Generalized or head-and-neck adenopathy"
                }
            }
        },
        {
            "slug": "node_structure_and_hyperplasia",
            "title": "Node Structure and Reactive Hyperplasia",
            "subtitle": "Match each nodal structure or reaction to its predominant cell type and defining feature",
            "categories": ["Entity", "Predominant Cell", "Defining Feature"],
            "data": {
                "Primary follicle": {
                    "Entity": "Follicle before antigen exposure",
                    "Predominant Cell": "B cells",
                    "Defining Feature": "Small, closely packed mature B cells that have not been antigenically stimulated"
                },
                "Secondary follicle": {
                    "Entity": "Follicle after antigen exposure",
                    "Predominant Cell": "B cells",
                    "Defining Feature": "Contains a germinal center with tingible body macrophages"
                },
                "Paracortex": {
                    "Entity": "Deepest part of the cortex around follicles",
                    "Predominant Cell": "T cells",
                    "Defining Feature": "Interfollicular zone surrounding the follicles"
                },
                "Benign follicular hyperplasia": {
                    "Entity": "Reactive pattern to infection or autoimmune disease",
                    "Predominant Cell": "B cells",
                    "Defining Feature": "Primary follicles become enlarged secondary follicles forming germinal centers"
                },
                "Benign interfollicular / paracortical hyperplasia": {
                    "Entity": "Reactive pattern to viral infection or vaccination",
                    "Predominant Cell": "T cells",
                    "Defining Feature": "Expansion of the paracortex and areas between the follicles"
                }
            }
        },
        {
            "slug": "diagnosis_and_management",
            "title": "Diagnosis and Management by Scenario",
            "subtitle": "Match each clinical scenario to the recommended step and the reason behind it",
            "categories": ["Scenario", "Recommended Step", "Rationale"],
            "data": {
                "Local adenopathy, cause not found on history and exam": {
                    "Scenario": "Isolated enlarged node without an identified cause",
                    "Recommended Step": "Observe for 4 weeks, then biopsy if the node persists",
                    "Rationale": "Most benign adenopathy resolves, avoiding an unnecessary biopsy"
                },
                "Single axillary node in a woman": {
                    "Scenario": "One enlarged axillary node, no breast lump felt",
                    "Recommended Step": "Breast exam and mammography",
                    "Rationale": "Excludes breast cancer, an obvious consideration for that drainage"
                },
                "Adenopathy with weight loss and fever": {
                    "Scenario": "Signs or symptoms suggesting underlying cancer",
                    "Recommended Step": "Lymph node biopsy on initial workup",
                    "Rationale": "Excludes a neoplastic cause of the lymphadenopathy"
                },
                "Adenopathy after starting a new drug": {
                    "Scenario": "Enlarged nodes attributed to an offending medication",
                    "Recommended Step": "Stop the offending drug",
                    "Rationale": "Removing the trigger usually leads to resolution of the adenopathy"
                },
                "Generalized adenopathy of unclear cause": {
                    "Scenario": "Two or more noncontiguous enlarged node groups",
                    "Recommended Step": "CBC, HIV test, and chest x-ray (plus TB and EBV testing)",
                    "Rationale": "Screens for systemic infection and malignancy before biopsy"
                }
            }
        }
    ]
}
