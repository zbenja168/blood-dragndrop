BRICK = {
    "brick_num": 38,
    "brick_title": "Antimetabolite Agents",
    "games": [
        {
            "slug": "drug_profiles",
            "title": "Antimetabolite Drug Profiles",
            "subtitle": "Match each antimetabolite to its class, molecular mechanism, and signature adverse effect",
            "categories": ["Class", "Molecular Mechanism", "Signature Adverse Effect"],
            "data": {
                "Methotrexate": {
                    "Class": "Folic acid analog (antifolate)",
                    "Molecular Mechanism": "Inhibits dihydrofolate reductase",
                    "Signature Adverse Effect": "Myelosuppression (reversible with leucovorin), pulmonary fibrosis"
                },
                "5-Fluorouracil": {
                    "Class": "Pyrimidine nucleoside analog",
                    "Molecular Mechanism": "Complexes with folic acid to inhibit thymidylate synthase",
                    "Signature Adverse Effect": "Myelosuppression that worsens with leucovorin"
                },
                "Cytarabine": {
                    "Class": "Pyrimidine nucleoside analog",
                    "Molecular Mechanism": "Incorporates into DNA, causes early chain termination, inhibits DNA polymerase",
                    "Signature Adverse Effect": "Pancytopenia"
                },
                "Cladribine": {
                    "Class": "Purine nucleoside analog",
                    "Molecular Mechanism": "Active Cd-ATP incorporates into DNA, blocks transcription and DNA repair",
                    "Signature Adverse Effect": "Nephrotoxicity and neurotoxicity"
                },
                "Azathioprine / 6-Mercaptopurine": {
                    "Class": "Purine nucleoside analog",
                    "Molecular Mechanism": "Incorporates into DNA during replication and induces apoptosis",
                    "Signature Adverse Effect": "Hepatotoxicity, increased toxicity with allopurinol"
                }
            }
        },
        {
            "slug": "one_carbon_metabolism",
            "title": "One-Carbon Metabolism and Thymine Synthesis",
            "subtitle": "Match each molecule to its identity, role in dTMP synthesis, and drug interaction",
            "categories": ["Identity / Type", "Role in dTMP (Thymine) Synthesis", "Drug Interaction"],
            "data": {
                "Folic acid (vitamin B9)": {
                    "Identity / Type": "Dietary water-soluble vitamin",
                    "Role in dTMP (Thymine) Synthesis": "Source of the THF cofactor needed to form thymine",
                    "Drug Interaction": "Its metabolism is blocked by antifolates"
                },
                "Dihydrofolate reductase": {
                    "Identity / Type": "Enzyme",
                    "Role in dTMP (Thymine) Synthesis": "Reduces DHF to THF to regenerate the folate cofactor",
                    "Drug Interaction": "Inhibited by methotrexate"
                },
                "Thymidylate synthase": {
                    "Identity / Type": "Enzyme",
                    "Role in dTMP (Thymine) Synthesis": "Transfers a one-carbon unit to dUMP to make dTMP",
                    "Drug Interaction": "Inhibited by the 5-fluorouracil complex"
                },
                "Methylated THF (CH2-THF)": {
                    "Identity / Type": "Reduced folate cofactor",
                    "Role in dTMP (Thymine) Synthesis": "Donates the one-carbon unit for thymine formation",
                    "Drug Interaction": "Depleted when dihydrofolate reductase is blocked"
                },
                "Leucovorin": {
                    "Identity / Type": "Reduced folic acid analog",
                    "Role in dTMP (Thymine) Synthesis": "Restores the folate pool for thymidine formation",
                    "Drug Interaction": "Rescues methotrexate toxicity without needing dihydrofolate reductase"
                }
            }
        },
        {
            "slug": "clinical_uses",
            "title": "Clinical Uses and Special Roles",
            "subtitle": "Match each agent to its main therapeutic use, secondary use, and distinguishing feature",
            "categories": ["Main Therapeutic Use", "Secondary Use", "Distinguishing Feature"],
            "data": {
                "Methotrexate": {
                    "Main Therapeutic Use": "Chemotherapy for leukemias, lymphomas, breast cancer, choriocarcinomas, sarcomas",
                    "Secondary Use": "Immunosuppressant in rheumatoid arthritis, psoriasis, Crohn disease, lupus",
                    "Distinguishing Feature": "Pregnancy category X (can cause neural tube defects)"
                },
                "Cladribine": {
                    "Main Therapeutic Use": "Treats indolent B-cell non-Hodgkin lymphoma",
                    "Secondary Use": "Recently approved for multiple sclerosis",
                    "Distinguishing Feature": "Prodrug activated by phosphorylation to Cd-ATP"
                },
                "Cytarabine": {
                    "Main Therapeutic Use": "Treats some leukemias and lymphomas",
                    "Secondary Use": "Prodrug converted to 5-fluorouracil within tumors",
                    "Distinguishing Feature": "Converted by thymidine phosphorylase, more expressed in tumors"
                },
                "Azathioprine": {
                    "Main Therapeutic Use": "Treats autoimmune diseases (RA, lupus, vasculitis, IBD)",
                    "Secondary Use": "Anti-rejection regimens after organ transplantation",
                    "Distinguishing Feature": "Most common of the purine analogs"
                },
                "Leucovorin": {
                    "Main Therapeutic Use": "Rescues methotrexate-induced myelosuppression",
                    "Secondary Use": "Enhances the potency of 5-fluorouracil",
                    "Distinguishing Feature": "Reduced folate that bypasses dihydrofolate reductase"
                }
            }
        }
    ]
}
