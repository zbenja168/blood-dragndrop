BRICK = {
    "brick_num": 31,
    "brick_title": "Principles of Chemotherapy",
    "games": [
        {
            "slug": "chemo_modalities",
            "title": "Chemotherapy Modalities",
            "subtitle": "Match each cancer therapy class to its mechanism, an example drug, and an example indication",
            "categories": ["Mechanism of Action", "Example Drug", "Example Indication"],
            "data": {
                "Cytotoxic chemotherapy": {
                    "Mechanism of Action": "Cellular poisons that prevent cell growth and replication",
                    "Example Drug": "Methotrexate",
                    "Example Indication": "Rheumatoid arthritis and some cancers"
                },
                "Molecularly targeted therapy": {
                    "Mechanism of Action": "Targets specific cellular receptors and molecular pathways",
                    "Example Drug": "Imatinib",
                    "Example Indication": "Chronic myelogenous leukemia"
                },
                "Immunotherapy": {
                    "Mechanism of Action": "Helps immune cells attack cancer by blocking its protective mechanisms",
                    "Example Drug": "Pembrolizumab",
                    "Example Indication": "Melanoma and cervical cancer"
                },
                "Endocrine therapy": {
                    "Mechanism of Action": "Blocks or modulates hormones in hormone-responsive cancers",
                    "Example Drug": "Tamoxifen",
                    "Example Indication": "Estrogen receptor-positive breast cancer"
                }
            }
        },
        {
            "slug": "chemo_timing",
            "title": "Timing of Chemotherapy",
            "subtitle": "Match each treatment strategy to when it is given, its goal, and a clinical note",
            "categories": ["When It Is Given", "Primary Goal", "Clinical Note"],
            "data": {
                "Induction therapy": {
                    "When It Is Given": "First-line, as the best initial treatment",
                    "Primary Goal": "Kill as many cancer cells as possible",
                    "Clinical Note": "The preferred starting regimen for a given cancer"
                },
                "Neoadjuvant therapy": {
                    "When It Is Given": "Before the primary treatment",
                    "Primary Goal": "Shrink the primary tumor and distant micro-metastases",
                    "Clinical Note": "Makes surgical resection easier"
                },
                "Adjuvant therapy": {
                    "When It Is Given": "After the primary treatment",
                    "Primary Goal": "Improve long-term outcomes",
                    "Clinical Note": "Targets residual disease after surgery"
                },
                "Salvage therapy": {
                    "When It Is Given": "After preferred therapies have failed",
                    "Primary Goal": "Attempt remission when other options are exhausted",
                    "Clinical Note": "Reserved for refractory disease"
                }
            }
        },
        {
            "slug": "cell_cycle_targets",
            "title": "Cell-Cycle Targets of Anticancer Drugs",
            "subtitle": "Match each drug class to its example agent, the cell-cycle phase it hits, and its cytotoxic mechanism",
            "categories": ["Example Agent", "Cell-Cycle Phase Targeted", "Cytotoxic Mechanism"],
            "data": {
                "Antimetabolites": {
                    "Example Agent": "Cytarabine and methotrexate",
                    "Cell-Cycle Phase Targeted": "S phase (DNA synthesis)",
                    "Cytotoxic Mechanism": "Disrupt nucleotide synthesis during DNA replication"
                },
                "Microtubule inhibitors": {
                    "Example Agent": "Taxanes and vinca alkaloids",
                    "Cell-Cycle Phase Targeted": "M phase (mitosis)",
                    "Cytotoxic Mechanism": "Interfere with the mitotic spindle microtubules"
                },
                "Topoisomerase inhibitors": {
                    "Example Agent": "Irinotecan",
                    "Cell-Cycle Phase Targeted": "S/G2 phase",
                    "Cytotoxic Mechanism": "Block topoisomerase-mediated DNA unwinding"
                },
                "Bleomycin": {
                    "Example Agent": "Bleomycin",
                    "Cell-Cycle Phase Targeted": "G2 phase (double-check repair point)",
                    "Cytotoxic Mechanism": "Induces DNA strand breaks"
                },
                "Alkylating agents": {
                    "Example Agent": "Busulfan and cyclophosphamide",
                    "Cell-Cycle Phase Targeted": "Cell cycle-independent",
                    "Cytotoxic Mechanism": "Cross-link DNA regardless of cycle phase"
                }
            }
        },
        {
            "slug": "chemo_toxicities",
            "title": "Signature Chemotherapy Toxicities",
            "subtitle": "Match each agent to its drug class, its characteristic toxicity, and the organ system affected",
            "categories": ["Drug Class", "Characteristic Toxicity", "Organ System Affected"],
            "data": {
                "Doxorubicin": {
                    "Drug Class": "Anthracycline",
                    "Characteristic Toxicity": "Cardiotoxicity",
                    "Organ System Affected": "Heart"
                },
                "Bleomycin": {
                    "Drug Class": "Antitumor antibiotic",
                    "Characteristic Toxicity": "Pulmonary fibrosis",
                    "Organ System Affected": "Lungs"
                },
                "Cisplatin": {
                    "Drug Class": "Platinum agent",
                    "Characteristic Toxicity": "Nephrotoxicity and ototoxicity",
                    "Organ System Affected": "Kidneys and inner ear"
                },
                "Vincristine": {
                    "Drug Class": "Vinca alkaloid",
                    "Characteristic Toxicity": "Peripheral neuropathy",
                    "Organ System Affected": "Peripheral nerves"
                },
                "Cyclophosphamide": {
                    "Drug Class": "Alkylating agent",
                    "Characteristic Toxicity": "Hemorrhagic cystitis",
                    "Organ System Affected": "Bladder"
                },
                "Cytarabine": {
                    "Drug Class": "Antimetabolite",
                    "Characteristic Toxicity": "Keratitis and conjunctivitis",
                    "Organ System Affected": "Eyes"
                }
            }
        }
    ]
}
