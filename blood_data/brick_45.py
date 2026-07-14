BRICK = {
    "brick_num": 45,
    "brick_title": "Targeted Inhibitors Used in Cancer Therapy",
    "games": [
        {
            "slug": "targeted_agent_mechanisms",
            "title": "Mechanisms of Targeted Anticancer Agents",
            "subtitle": "Match each drug to its class, molecular target, and mechanism of action",
            "categories": ["Drug Class", "Molecular Target", "Mechanism of Action"],
            "data": {
                "Imatinib": {
                    "Drug Class": "Tyrosine kinase inhibitor (small molecule)",
                    "Molecular Target": "BCR-ABL fusion kinase",
                    "Mechanism of Action": "Competitively inhibits ATP binding to block phosphorylation"
                },
                "Dasatinib": {
                    "Drug Class": "Tyrosine kinase inhibitor (small molecule)",
                    "Molecular Target": "BCR-ABL in both active and inactive Abl conformations",
                    "Mechanism of Action": "Blocks ATP binding and overcomes imatinib-resistant mutations"
                },
                "Rituximab": {
                    "Drug Class": "Monoclonal antibody",
                    "Molecular Target": "CD20 on B-cells",
                    "Mechanism of Action": "Binds CD20 to trigger apoptosis, complement, and immune killing"
                },
                "Trastuzumab": {
                    "Drug Class": "Monoclonal antibody (humanized)",
                    "Molecular Target": "A tumor cell-surface receptor",
                    "Mechanism of Action": "Binds the surface receptor to block cell signaling"
                },
                "Bortezomib": {
                    "Drug Class": "Modulator of protein degradation",
                    "Molecular Target": "26S proteasome",
                    "Mechanism of Action": "Blocks proteasomal degradation of IkB, lowering NF-kB"
                }
            }
        },
        {
            "slug": "targeted_therapy_adverse_effects",
            "title": "Adverse Effects of Targeted Therapies",
            "subtitle": "Match each drug to its primary adverse effect, other effects, and a clinical note",
            "categories": ["Primary Adverse Effect", "Other Adverse Effects", "Clinical or Management Note"],
            "data": {
                "Imatinib": {
                    "Primary Adverse Effect": "Fluid retention (leg swelling and shortness of breath)",
                    "Other Adverse Effects": "Elevated liver enzymes, GI distress, muscle cramps, rash",
                    "Clinical or Management Note": "Rash may progress to Stevens-Johnson syndrome"
                },
                "Dasatinib": {
                    "Primary Adverse Effect": "Pleural effusion",
                    "Other Adverse Effects": "QT-interval prolongation",
                    "Clinical or Management Note": "Used when BCR-ABL mutations cause imatinib resistance"
                },
                "Rituximab": {
                    "Primary Adverse Effect": "Infusion reactions (fever, chills, urticaria, hypotension)",
                    "Other Adverse Effects": "Hepatitis B reactivation and other viral infections",
                    "Clinical or Management Note": "Slow infusion and antihistamines; screen for HBV, monitor up to 24 months"
                },
                "Bortezomib": {
                    "Primary Adverse Effect": "Thrombocytopenia (about 28% of patients)",
                    "Other Adverse Effects": "Peripheral neuropathy (about 12%), fatigue, anemia, GI effects",
                    "Clinical or Management Note": "Dose reduction decreases neuropathic symptoms"
                }
            }
        },
        {
            "slug": "monoclonal_antibody_nomenclature",
            "title": "Monoclonal Antibody Nomenclature",
            "subtitle": "Match each naming component to what it denotes, its syllable, and an example",
            "categories": ["What It Denotes", "Name Syllable", "Example or Note"],
            "data": {
                "Tumor target": {
                    "What It Denotes": "The antibody's target is a tumor",
                    "Name Syllable": "-t- or -tu-",
                    "Example or Note": "Trastuzumab contains -tu-"
                },
                "Virus target": {
                    "What It Denotes": "The antibody's target is a virus",
                    "Name Syllable": "-v- or -vi-",
                    "Example or Note": "Used in some antiviral monoclonal antibodies"
                },
                "Interleukin target": {
                    "What It Denotes": "The antibody's target is an interleukin",
                    "Name Syllable": "-k- or -ki-",
                    "Example or Note": "Seen in immunomodulating antibodies"
                },
                "Chimeric source": {
                    "What It Denotes": "Derived from a chimeric (part-human, part-animal) source",
                    "Name Syllable": "-xi-",
                    "Example or Note": "Rituximab contains -xi-"
                },
                "Human source": {
                    "What It Denotes": "A fully human antibody",
                    "Name Syllable": "-u-",
                    "Example or Note": "Fully human source lacks animal-derived sequence"
                },
                "Humanized source": {
                    "What It Denotes": "A humanized antibody",
                    "Name Syllable": "-zu-",
                    "Example or Note": "Trastuzumab contains -zu-"
                }
            }
        },
        {
            "slug": "rtk_signaling_pathway",
            "title": "Receptor Tyrosine Kinase Signaling",
            "subtitle": "Match each component to its role, key event, and outcome in cancer signaling",
            "categories": ["Role in Signaling", "Key Event", "Outcome"],
            "data": {
                "Ligand": {
                    "Role in Signaling": "Extracellular signal molecule",
                    "Key Event": "Binds and dimerizes the receptor",
                    "Outcome": "Initiates receptor activation"
                },
                "Tyrosine kinase domain": {
                    "Role in Signaling": "Intracellular enzymatic region of the receptor",
                    "Key Event": "Becomes active and autophosphorylates tyrosines",
                    "Outcome": "Creates phospho-tyrosine docking sites for proteins"
                },
                "PI3K-AKT pathway": {
                    "Role in Signaling": "Downstream survival cascade",
                    "Key Event": "Activated by the phosphorylated receptor",
                    "Outcome": "Decreases apoptosis"
                },
                "Ras-ERK pathway": {
                    "Role in Signaling": "Downstream proliferation cascade",
                    "Key Event": "Activated by the phosphorylated receptor",
                    "Outcome": "Increases cell proliferation"
                },
                "EGFR": {
                    "Role in Signaling": "An example receptor tyrosine kinase",
                    "Key Event": "Overactive in most cancers",
                    "Outcome": "Drives increased growth and decreased apoptosis"
                }
            }
        }
    ]
}
