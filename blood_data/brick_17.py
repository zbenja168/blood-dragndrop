BRICK = {
    "brick_num": 17,
    "brick_title": "Hemostasis",
    "games": [
        {
            "slug": "primary_hemostasis_steps",
            "title": "Steps of Primary Hemostasis",
            "subtitle": "Match each step of the platelet plug to its key molecule, key event, and result",
            "categories": ["Key Molecule", "Key Event", "Result"],
            "data": {
                "Blood Vessel Constriction": {
                    "Key Molecule": "Endothelin released from endothelial cells",
                    "Key Event": "Smooth muscle contraction of small arterioles",
                    "Result": "Reduced blood loss at the injury site"
                },
                "Platelet Adhesion": {
                    "Key Molecule": "Von Willebrand factor binding glycoprotein Ib",
                    "Key Event": "Platelets stick to exposed subendothelial collagen",
                    "Result": "Platelets anchored to the damaged vessel wall"
                },
                "Platelet Activation": {
                    "Key Molecule": "Thromboxane A2 (with ADP and calcium)",
                    "Key Event": "Granule release and glycoprotein IIb/IIIa exposure",
                    "Result": "Additional platelets recruited to the site"
                },
                "Platelet Aggregation": {
                    "Key Molecule": "Fibrinogen bridging glycoprotein IIb/IIIa",
                    "Key Event": "Activated platelets bind one another",
                    "Result": "A soft, unstable platelet plug covers the hole"
                }
            }
        },
        {
            "slug": "coagulation_pathways",
            "title": "Coagulation Cascade Pathways",
            "subtitle": "Match each arm of the cascade to its trigger, key factors, and lab test",
            "categories": ["Trigger / Activator", "Key Factors", "Lab Test"],
            "data": {
                "Extrinsic Pathway": {
                    "Trigger / Activator": "Tissue factor (Factor III) from damaged tissue",
                    "Key Factors": "Factor VII",
                    "Lab Test": "Prothrombin time (PT) and INR"
                },
                "Intrinsic Pathway": {
                    "Trigger / Activator": "Exposed collagen / negatively charged surfaces",
                    "Key Factors": "Factors XII, XI, IX, and VIII",
                    "Lab Test": "Activated partial thromboplastin time (aPTT)"
                },
                "Common Pathway": {
                    "Trigger / Activator": "Activated Factor X, where the arms converge",
                    "Key Factors": "Factors X, V, II (prothrombin), I (fibrinogen)",
                    "Lab Test": "Reflected in both PT and aPTT"
                },
                "Fibrinolytic System": {
                    "Trigger / Activator": "Tissue plasminogen activator (tPA) from endothelium",
                    "Key Factors": "Plasminogen converted to plasmin",
                    "Lab Test": "D-dimer (fibrin degradation product)"
                }
            }
        },
        {
            "slug": "clotting_regulators",
            "title": "Natural Anticoagulants and Clot Regulators",
            "subtitle": "Match each regulator to its target, its activator/cofactor, and its net effect",
            "categories": ["Target / Action", "Activator or Cofactor", "Net Effect"],
            "data": {
                "Tissue Factor Pathway Inhibitor (TFPI)": {
                    "Target / Action": "The tissue factor-VIIa complex (extrinsic arm)",
                    "Activator or Cofactor": "Produced by endothelial cells, found in plasma",
                    "Net Effect": "Switches off the extrinsic pathway almost immediately"
                },
                "Antithrombin": {
                    "Target / Action": "Thrombin (IIa) and other factors like Xa",
                    "Activator or Cofactor": "Enhanced by heparin and heparin-like molecules",
                    "Net Effect": "Damps the intrinsic and common pathways"
                },
                "Activated Protein C": {
                    "Target / Action": "Factors Va and VIIIa (cleaves and inactivates)",
                    "Activator or Cofactor": "Protein S plus thrombin-thrombomodulin complex",
                    "Net Effect": "Removes key cofactors to slow clotting"
                },
                "Plasmin": {
                    "Target / Action": "Fibrin within an already-formed clot",
                    "Activator or Cofactor": "Converted from plasminogen by tPA",
                    "Net Effect": "Dissolves the clot and releases D-dimers"
                },
                "Prostacyclin and Nitric Oxide": {
                    "Target / Action": "Platelet binding, secretion, and activation",
                    "Activator or Cofactor": "Secreted by healthy endothelial cells",
                    "Net Effect": "Antiplatelet activity that prevents unwanted clotting"
                }
            }
        },
        {
            "slug": "bleeding_disorders",
            "title": "Bleeding Disorders",
            "subtitle": "Match each disorder to its deficient factor, its cause/inheritance, and its classic clue",
            "categories": ["Deficient Factor / Protein", "Inheritance / Cause", "Classic Feature or Lab"],
            "data": {
                "Von Willebrand Disease": {
                    "Deficient Factor / Protein": "Von Willebrand factor (also stabilizes Factor VIII)",
                    "Inheritance / Cause": "Autosomal dominant; most common hereditary type",
                    "Classic Feature or Lab": "Mucocutaneous bleeding; normal PT, aPTT sometimes prolonged"
                },
                "Hemophilia A": {
                    "Deficient Factor / Protein": "Factor VIII",
                    "Inheritance / Cause": "X-linked recessive (mostly affects males)",
                    "Classic Feature or Lab": "Hemarthrosis with prolonged aPTT and normal PT"
                },
                "Hemophilia B": {
                    "Deficient Factor / Protein": "Factor IX",
                    "Inheritance / Cause": "X-linked recessive (mostly affects males)",
                    "Classic Feature or Lab": "Deep muscle and joint bleeding after minor trauma"
                },
                "Vitamin K Deficiency": {
                    "Deficient Factor / Protein": "Factors II, VII, IX, and X",
                    "Inheritance / Cause": "Acquired from malnutrition or malabsorption",
                    "Classic Feature or Lab": "Prolonged PT that corrects with vitamin K"
                },
                "Liver Failure": {
                    "Deficient Factor / Protein": "Multiple hepatically synthesized clotting factors",
                    "Inheritance / Cause": "Acquired, as in cirrhosis",
                    "Classic Feature or Lab": "Elevated PT and PTT with thrombocytopenia"
                }
            }
        }
    ]
}
