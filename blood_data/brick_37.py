BRICK = {
    "brick_num": 37,
    "brick_title": "Alkylating Agents",
    "games": [
        {
            "slug": "agent_class_toxicity",
            "title": "Alkylating & Platinum Agents",
            "subtitle": "Match each drug to its class and its signature adverse effect",
            "categories": ["Drug Class", "Mechanism of Action", "Signature Adverse Effect"],
            "data": {
                "Cyclophosphamide": {
                    "Drug Class": "Nitrogen mustard",
                    "Mechanism of Action": "Bioactivated by CYP450 to phosphamide mustard; cross-links DNA",
                    "Signature Adverse Effect": "Hemorrhagic cystitis"
                },
                "Busulfan": {
                    "Drug Class": "Alkyl sulfonate",
                    "Mechanism of Action": "Alkylates N-7 of guanosine with intrastrand DNA cross-linking",
                    "Signature Adverse Effect": "Pulmonary fibrosis (busulfan lung)"
                },
                "Carmustine": {
                    "Drug Class": "Nitrosourea",
                    "Mechanism of Action": "Interstrand cross-linking; penetrates the CNS",
                    "Signature Adverse Effect": "CNS toxicity"
                },
                "Procarbazine": {
                    "Drug Class": "Nonclassic alkylating agent",
                    "Mechanism of Action": "Inhibits transmethylation of methionine, blocking DNA, RNA, and protein synthesis",
                    "Signature Adverse Effect": "Serotonin syndrome and disulfiram-like reaction"
                },
                "Cisplatin / Carboplatin": {
                    "Drug Class": "Platinum agent",
                    "Mechanism of Action": "Direct DNA damage with intrastrand cross-linking; activated by hydrolyzation",
                    "Signature Adverse Effect": "Ototoxicity and nephrotoxicity"
                }
            }
        },
        {
            "slug": "toxicity_management",
            "title": "Managing Alkylating-Agent Toxicity",
            "subtitle": "Match each toxicity to its offending agent and how it is prevented or managed",
            "categories": ["Offending Agent", "Underlying Cause", "Prevention / Management"],
            "data": {
                "Hemorrhagic cystitis": {
                    "Offending Agent": "Cyclophosphamide / ifosfamide",
                    "Underlying Cause": "Acrolein collects in the bladder and inflames the mucosal lining",
                    "Prevention / Management": "Hydration plus mesna, which binds acrolein in the urine"
                },
                "Neurotoxicity": {
                    "Offending Agent": "Ifosfamide",
                    "Underlying Cause": "Encephalopathy and cerebellar dysfunction",
                    "Prevention / Management": "Methylene blue as a chemoprotective agent"
                },
                "Myelosuppression": {
                    "Offending Agent": "Almost all alkylating agents",
                    "Underlying Cause": "Bone marrow production of blood cells is decreased",
                    "Prevention / Management": "Monitor for neutropenic fever, bleeding, and anemia"
                },
                "Pulmonary fibrosis": {
                    "Offending Agent": "Busulfan",
                    "Underlying Cause": "Dose-dependent lung toxicity presenting weeks to years after treatment",
                    "Prevention / Management": "Suspect with cough, dyspnea, and basilar crackles; discontinue the drug"
                },
                "Serotonin syndrome": {
                    "Offending Agent": "Procarbazine",
                    "Underlying Cause": "Monoamine-oxidase inhibitor activity combined with serotonergic drugs",
                    "Prevention / Management": "Avoid concurrent serotonergic medications"
                }
            }
        },
        {
            "slug": "mechanism_and_features",
            "title": "Mechanism & Distinctive Features",
            "subtitle": "Match each agent to how it damages DNA and its distinctive property",
            "categories": ["DNA Action", "Activation / Metabolism", "Distinctive Feature"],
            "data": {
                "Cyclophosphamide": {
                    "DNA Action": "Interstrand and intrastrand DNA cross-links",
                    "Activation / Metabolism": "Prodrug bioactivated by hepatic CYP450 enzymes to acrolein",
                    "Distinctive Feature": "Also used as an immunosuppressant in lupus, vasculitis, and rheumatoid arthritis"
                },
                "Carmustine": {
                    "DNA Action": "Interstrand cross-linking of DNA and RNA",
                    "Activation / Metabolism": "Requires bioactivation before cross-linking",
                    "Distinctive Feature": "Crosses the blood-brain barrier to treat CNS tumors"
                },
                "Cisplatin": {
                    "DNA Action": "Intrastrand cross-linking with direct DNA damage",
                    "Activation / Metabolism": "Activated by hydrolyzation of the platinum molecule",
                    "Distinctive Feature": "Platinum-based molecule causing ototoxicity and nephrotoxicity"
                },
                "Busulfan": {
                    "DNA Action": "Intrastrand cross-linking at N-7 of guanosine",
                    "Activation / Metabolism": "Alkyl sulfonate with affinity for myeloid cells",
                    "Distinctive Feature": "Used in conditioning protocols before bone marrow transplantation"
                },
                "Procarbazine": {
                    "DNA Action": "Inhibits transmethylation, blocking DNA, RNA, and protein synthesis",
                    "Activation / Metabolism": "Contains an N-methyl group with MAO-inhibitor activity",
                    "Distinctive Feature": "Causes a disulfiram-like reaction with alcohol"
                }
            }
        }
    ]
}
