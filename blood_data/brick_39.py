BRICK = {
    "brick_num": 39,
    "brick_title": "Topoisomerase Inhibitors, Microtubule Inhibitors, and Antitumor Antibiotics",
    "games": [
        {
            "slug": "drug_class_overview",
            "title": "Chemotherapy Drug Classes",
            "subtitle": "Match each drug class to its molecular action, prototype agents, and signature toxicity",
            "categories": ["Molecular Action", "Prototype Agents", "Signature Toxicity"],
            "data": {
                "Topoisomerase I inhibitors": {
                    "Molecular Action": "Block religation, causing single-strand breaks that become double-strand breaks",
                    "Prototype Agents": "Topotecan, irinotecan",
                    "Signature Toxicity": "Severe diarrhea (especially irinotecan)"
                },
                "Topoisomerase II inhibitors": {
                    "Molecular Action": "Prevent religation of double-strand breaks during S or early G2 phase",
                    "Prototype Agents": "Etoposide, teniposide",
                    "Signature Toxicity": "Myelosuppression; secondary leukemia at high doses"
                },
                "Vinca alkaloids": {
                    "Molecular Action": "Bind beta-tubulin and inhibit microtubule polymerization",
                    "Prototype Agents": "Vincristine, vinblastine, eribulin",
                    "Signature Toxicity": "Peripheral neuropathy and constipation"
                },
                "Taxanes": {
                    "Molecular Action": "Bind beta-tubulin and prevent microtubule depolymerization",
                    "Prototype Agents": "Paclitaxel, docetaxel, cabazitaxel",
                    "Signature Toxicity": "Hypersensitivity reactions; docetaxel fluid retention"
                },
                "Anthracyclines": {
                    "Molecular Action": "Intercalate into DNA and inhibit DNA and RNA synthesis",
                    "Prototype Agents": "Doxorubicin, daunorubicin",
                    "Signature Toxicity": "Irreversible dose-dependent cardiotoxicity"
                }
            }
        },
        {
            "slug": "toxicity_and_management",
            "title": "Signature Toxicities and Their Management",
            "subtitle": "Match each drug to its characteristic toxicity, the underlying cause, and its management or key feature",
            "categories": ["Characteristic Toxicity", "Underlying Cause", "Management / Key Feature"],
            "data": {
                "Irinotecan": {
                    "Characteristic Toxicity": "Early cholinergic diarrhea and severe late diarrhea",
                    "Underlying Cause": "Metabolite SN-38 damages the intestinal mucosal lining",
                    "Management / Key Feature": "Atropine treats the acute cholinergic symptoms"
                },
                "Doxorubicin": {
                    "Characteristic Toxicity": "Dose-dependent cardiomyopathy and heart failure",
                    "Underlying Cause": "Iron-mediated free radical generation",
                    "Management / Key Feature": "Dexrazoxane chelates iron to prevent it"
                },
                "Bleomycin": {
                    "Characteristic Toxicity": "Pulmonary fibrosis (bleomycin lung)",
                    "Underlying Cause": "Low lung bleomycin hydrolase allows reactive oxygen species injury",
                    "Management / Key Feature": "Baseline pulmonary function testing; myelosuppression is rare"
                },
                "Paclitaxel": {
                    "Characteristic Toxicity": "Serious hypersensitivity reactions",
                    "Underlying Cause": "Taxane infusion reaction",
                    "Management / Key Feature": "Premedicate with dexamethasone, diphenhydramine, and an H2 blocker"
                },
                "Mitomycin C": {
                    "Characteristic Toxicity": "Hemolytic-uremic syndrome and renal failure",
                    "Underlying Cause": "DNA alkylation and interstrand cross-linking",
                    "Management / Key Feature": "Watch for pale conjunctivae, petechiae, and oliguria"
                },
                "Vincristine": {
                    "Characteristic Toxicity": "Peripheral neuropathy, constipation, and SIADH",
                    "Underlying Cause": "Microtubule disruption impairs neuronal transport",
                    "Management / Key Feature": "Neuropathy is usually reversible"
                }
            }
        },
        {
            "slug": "molecular_targets",
            "title": "Molecular Targets of Cancer Drugs",
            "subtitle": "Match each cellular target to its role, a distinguishing feature, and the drug that acts on it",
            "categories": ["Role in the Cell", "Distinguishing Feature", "Drug That Acts Here"],
            "data": {
                "Topoisomerase I": {
                    "Role in the Cell": "Relieves supercoiling tension by cutting a single DNA strand",
                    "Distinguishing Feature": "Religates the strand without ATP",
                    "Drug That Acts Here": "Topotecan and irinotecan"
                },
                "Topoisomerase II": {
                    "Role in the Cell": "Cleaves both DNA strands, then religates each one",
                    "Distinguishing Feature": "Requires ATP hydrolysis",
                    "Drug That Acts Here": "Etoposide and teniposide"
                },
                "Alpha/beta-tubulin dimers": {
                    "Role in the Cell": "Building blocks that polymerize into microtubules",
                    "Distinguishing Feature": "In dynamic equilibrium of polymerization and depolymerization",
                    "Drug That Acts Here": "Vinca alkaloids and taxanes"
                },
                "Mitotic spindle": {
                    "Role in the Cell": "Separates chromosomes to opposite poles in mitosis",
                    "Distinguishing Feature": "Frozen in metaphase when microtubules are disrupted",
                    "Drug That Acts Here": "Microtubule inhibitors cause metaphase arrest here"
                },
                "Double-stranded DNA": {
                    "Role in the Cell": "Template for DNA replication and transcription",
                    "Distinguishing Feature": "Intercalation blocks DNA and RNA synthesis independent of cell cycle",
                    "Drug That Acts Here": "Anthracyclines such as doxorubicin"
                }
            }
        }
    ]
}
