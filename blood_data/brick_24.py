BRICK = {
    "brick_num": 24,
    "brick_title": "Thrombotic Disorders: Foundations and Frameworks",
    "games": [
        {
            "slug": "disorder_types",
            "title": "Types of Thrombotic Disorders",
            "subtitle": "Match each thrombotic disorder to its category, mechanism, and key feature",
            "categories": ["Category", "Mechanism", "Key Feature"],
            "data": {
                "Factor V Leiden": {
                    "Category": "Hereditary; stimulates clotting",
                    "Mechanism": "Point mutation makes factor V resistant to inactivation by protein C",
                    "Key Feature": "Most common of all thrombotic disorders"
                },
                "Factor II (Prothrombin) Gene Mutation": {
                    "Category": "Hereditary; stimulates clotting",
                    "Mechanism": "Excess prothrombin yields excess thrombin and fibrin",
                    "Key Feature": "Rare disorder"
                },
                "Antithrombin Deficiency": {
                    "Category": "Hereditary; impairs clot termination",
                    "Mechanism": "Too little antithrombin, a broad inhibitor of the cascade",
                    "Key Feature": "Rare genetic defect that is hard to turn the cascade off"
                },
                "Protein C and Protein S Deficiency": {
                    "Category": "Hereditary; impairs clot termination",
                    "Mechanism": "Loss of proteins that together inactivate factors Va and VIIIa",
                    "Key Feature": "Predisposes to warfarin-induced skin necrosis"
                },
                "Antiphospholipid Antibody Syndrome": {
                    "Category": "Acquired",
                    "Mechanism": "Antibodies to phospholipids damage endothelium and platelets",
                    "Key Feature": "Main acquired disorder; may occur with lupus"
                }
            }
        },
        {
            "slug": "anticoagulant_classes",
            "title": "Anticoagulant Drug Classes",
            "subtitle": "Match each anticoagulant to its mechanism, route, and reversal agent",
            "categories": ["Mechanism of Action", "Route", "Reversal Agent"],
            "data": {
                "Warfarin": {
                    "Mechanism of Action": "Vitamin K antagonist blocking synthesis of factors II, VII, IX, X",
                    "Route": "Oral",
                    "Reversal Agent": "Prothrombin complex concentrate plus vitamin K"
                },
                "Unfractionated Heparin (UFH)": {
                    "Mechanism of Action": "Activates antithrombin to inhibit factors II, IX, X, XI, XII",
                    "Route": "Intravenous or subcutaneous",
                    "Reversal Agent": "Protamine sulfate"
                },
                "Low-Molecular-Weight Heparin (LMWH)": {
                    "Mechanism of Action": "Augments antithrombin inhibition mainly of factor Xa",
                    "Route": "Subcutaneous",
                    "Reversal Agent": "Protamine sulfate (partial reversal)"
                },
                "Dabigatran": {
                    "Mechanism of Action": "Directly inhibits thrombin without needing a cofactor",
                    "Route": "Oral",
                    "Reversal Agent": "Idarucizumab"
                },
                "Argatroban / Bivalirudin": {
                    "Mechanism of Action": "Directly inhibit thrombin without needing a cofactor",
                    "Route": "Intravenous only",
                    "Reversal Agent": "Activated prothrombin complex concentrate"
                }
            }
        },
        {
            "slug": "warfarin_deep_dive",
            "title": "Warfarin: Effects, Interactions, and Cautions",
            "subtitle": "Match each aspect of warfarin therapy to its underlying reason and clinical implication",
            "categories": ["Aspect", "Underlying Reason", "Clinical Implication"],
            "data": {
                "Delayed Onset": {
                    "Aspect": "Full effect takes 5-7 days",
                    "Underlying Reason": "Long half-life; factors II and X inhibited only after about 72 hours",
                    "Clinical Implication": "Bridge with heparin during the early hypercoagulable state"
                },
                "Skin Necrosis": {
                    "Aspect": "Warfarin-induced skin necrosis",
                    "Underlying Reason": "Early fall in proteins C and S causes transient hypercoagulability",
                    "Clinical Implication": "Highest risk with protein C or S deficiency; stop warfarin, give vitamin K and PCC"
                },
                "Laboratory Monitoring": {
                    "Aspect": "Monitored with PT and INR",
                    "Underlying Reason": "Factor VII has the shortest half-life, so the PT/INR rises first",
                    "Clinical Implication": "Target INR 2.0-3.0 for most patients (2.5-3.5 with mechanical valves)"
                },
                "Drug Interactions": {
                    "Aspect": "Many drug-drug interactions",
                    "Underlying Reason": "Hepatic metabolism by CYP2C9; inhibitors raise warfarin levels",
                    "Clinical Implication": "Supratherapeutic INR increases bleeding risk"
                },
                "Dietary Vitamin K": {
                    "Aspect": "Interactions with foods",
                    "Underlying Reason": "Green leafy vegetables, broccoli, and kiwi supply vitamin K",
                    "Clinical Implication": "Excess intake causes subtherapeutic INR and clotting risk"
                },
                "Contraindications": {
                    "Aspect": "Situations where warfarin is avoided",
                    "Underlying Reason": "Potent teratogen and bleeding risk",
                    "Clinical Implication": "Avoid in pregnancy, active bleeding, and recent eye or CNS surgery"
                }
            }
        },
        {
            "slug": "clinical_clues",
            "title": "Key Clinical Concepts",
            "subtitle": "Match each concept to what it is and its clinical significance",
            "categories": ["Concept", "What It Is", "Clinical Significance"],
            "data": {
                "Virchow Triad": {
                    "Concept": "Framework for thrombus formation",
                    "What It Is": "Endothelial damage, blood stasis, and hypercoagulability",
                    "Clinical Significance": "Explains postoperative DVT after immobilization and surgery"
                },
                "HITT": {
                    "Concept": "Heparin-induced thrombocytopenia and thrombosis",
                    "What It Is": "Autoimmune heparin-PF4 antibody that activates platelets",
                    "Clinical Significance": "Causes clots and low platelets; switch to a direct thrombin inhibitor"
                },
                "Suspicious Presentation": {
                    "Concept": "Clues to an inherited thrombotic disorder",
                    "What It Is": "Age <50, recurrent or familial thrombi, miscarriage, or thrombus in an unusual site",
                    "Clinical Significance": "Should prompt a workup for an underlying disorder"
                },
                "Idarucizumab": {
                    "Concept": "Specific reversal agent",
                    "What It Is": "Monoclonal antibody fragment with ~350x affinity for dabigatran",
                    "Clinical Significance": "Neutralizes dabigatran-related bleeding within minutes"
                },
                "Protamine Sulfate": {
                    "Concept": "Heparin antidote",
                    "What It Is": "Positively charged molecule that binds negatively charged heparin",
                    "Clinical Significance": "Reverses bleeding caused by heparin products"
                }
            }
        }
    ]
}
