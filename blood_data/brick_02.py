BRICK = {
    "brick_num": 2,
    "brick_title": "RBC Metabolism",
    "games": [
        {
            "slug": "rbc_enzymes",
            "title": "Red Blood Cell Enzymes",
            "subtitle": "Match each RBC enzyme to its pathway, product/action, and clinical role",
            "categories": ["Pathway / Cofactor Source", "Product or Action", "Deficiency or Clinical Role"],
            "data": {
                "Glucose 6-phosphate dehydrogenase (G6PD)": {
                    "Pathway / Cofactor Source": "First reaction of the pentose phosphate pathway",
                    "Product or Action": "Generates NADPH, the sole NADPH source in mature RBCs",
                    "Deficiency or Clinical Role": "Deficiency increases oxidative stress causing episodic hemolysis"
                },
                "Pyruvate kinase": {
                    "Pathway / Cofactor Source": "Final ATP-generating step of glycolysis",
                    "Product or Action": "Forms ATP and pyruvate; accounts for 50% of glycolytic ATP",
                    "Deficiency or Clinical Role": "Deficiency causes chronic hemolysis from ATP depletion"
                },
                "Bisphosphoglycerate mutase": {
                    "Pathway / Cofactor Source": "Rapoport-Luebering shunt of glycolysis",
                    "Product or Action": "Converts 1,3-BPG into 2,3-BPG",
                    "Deficiency or Clinical Role": "Lowers hemoglobin affinity to aid oxygen delivery"
                },
                "Cytochrome b5 reductase": {
                    "Pathway / Cofactor Source": "Uses NADH formed by GAPDH in glycolysis",
                    "Product or Action": "Reduces methemoglobin back to functional hemoglobin",
                    "Deficiency or Clinical Role": "Deficiency causes congenital methemoglobinemia"
                },
                "NADPH-methemoglobin reductase": {
                    "Pathway / Cofactor Source": "Uses NADPH from the pentose phosphate pathway (G6PD)",
                    "Product or Action": "Alternative reducer of methemoglobin via methylene blue",
                    "Deficiency or Clinical Role": "Activated by methylene blue to treat methemoglobinemia"
                }
            }
        },
        {
            "slug": "hb_affinity_modulators",
            "title": "Hemoglobin Oxygen-Affinity Modulators",
            "subtitle": "All decrease Hb affinity for oxygen (right shift) - match source, mechanism, and role",
            "categories": ["Source / Trigger", "Mechanism", "Physiologic Role"],
            "data": {
                "Low pH (Bohr effect)": {
                    "Source / Trigger": "Acidosis, e.g. lactate accumulation in tissues",
                    "Mechanism": "Protonates select histidine residues on hemoglobin",
                    "Physiologic Role": "Increases oxygen delivery to metabolically active tissues"
                },
                "Elevated pCO2": {
                    "Source / Trigger": "CO2 produced by oxidative metabolism",
                    "Mechanism": "Raises [H+] via bicarbonate buffer and forms carbaminohemoglobin",
                    "Physiologic Role": "Couples CO2 load to oxygen unloading in tissues"
                },
                "High temperature": {
                    "Source / Trigger": "Warm, exercising muscle",
                    "Mechanism": "Kinetic energy augments gas dissociation from hemoglobin",
                    "Physiologic Role": "Aids oxygen release in a physically active muscle"
                },
                "2,3-BPG": {
                    "Source / Trigger": "Made in RBCs from the glycolytic intermediate 1,3-BPG",
                    "Mechanism": "Binds and stabilizes the deoxygenated (T) state of Hb",
                    "Physiologic Role": "Allows RBCs to modulate Hb affinity rapidly"
                },
                "Carbon monoxide": {
                    "Source / Trigger": "Exogenous poison, not a physiologic signal",
                    "Mechanism": "Unregulated binding to heme iron",
                    "Physiologic Role": "Pathologic; considered a poison with no beneficial role"
                }
            }
        },
        {
            "slug": "enzyme_disorders",
            "title": "Distinguishing RBC Enzyme & Hemoglobin Disorders",
            "subtitle": "Match each disorder to its defect, hemolysis pattern, and hallmark finding",
            "categories": ["Underlying Defect", "Hemolysis / Onset Pattern", "Hallmark Finding or Trigger"],
            "data": {
                "G6PD deficiency": {
                    "Underlying Defect": "Loss of NADPH from the pentose phosphate pathway",
                    "Hemolysis / Onset Pattern": "Episodic hemolysis requiring an oxidative trigger",
                    "Hallmark Finding or Trigger": "Heinz bodies and bite cells after infection, drugs, or fava beans"
                },
                "Pyruvate kinase deficiency": {
                    "Underlying Defect": "Loss of glycolytic ATP production",
                    "Hemolysis / Onset Pattern": "Chronic hemolysis, usually diagnosed before 6 months of age",
                    "Hallmark Finding or Trigger": "Rigid spiculated RBCs with roughly 3-fold elevated 2,3-BPG"
                },
                "Cytochrome b5 reductase deficiency": {
                    "Underlying Defect": "Congenital enzyme defect that fails to reduce metHb",
                    "Hemolysis / Onset Pattern": "Congenital methemoglobinemia present from birth",
                    "Hallmark Finding or Trigger": "Chocolate-brown blood with cyanosis unresponsive to oxygen"
                },
                "Hemoglobin M": {
                    "Underlying Defect": "Globin gene mutation distorting the heme-binding pocket",
                    "Hemolysis / Onset Pattern": "Congenital methemoglobinemia from abnormal globin",
                    "Hallmark Finding or Trigger": "Auto-oxidation of iron with poor response to methylene blue"
                }
            }
        },
        {
            "slug": "methemoglobinemia_agents",
            "title": "Methemoglobinemia: Agents & Interventions",
            "subtitle": "Match each agent to its role, mechanism, and key clinical note",
            "categories": ["Role", "Mechanism / Action", "Clinical Note"],
            "data": {
                "Nitrites (amyl / sodium nitrite)": {
                    "Role": "Oxidant that induces methemoglobin formation",
                    "Mechanism / Action": "Oxidizes heme iron from ferrous to ferric",
                    "Clinical Note": "Used therapeutically to generate cyanomethemoglobin in cyanide poisoning"
                },
                "Benzocaine": {
                    "Role": "Acquired cause of methemoglobinemia",
                    "Mechanism / Action": "Topical oxidant anesthetic in sprays and lozenges",
                    "Clinical Note": "Contraindicated in children under 2 or reduced lung function"
                },
                "Methylene blue": {
                    "Role": "First-line treatment for acquired methemoglobinemia",
                    "Mechanism / Action": "Activates the NADPH-methemoglobin reductase pathway",
                    "Clinical Note": "Contraindicated in G6PD deficiency due to reliance on NADPH"
                },
                "Vitamin C (ascorbic acid)": {
                    "Role": "Antioxidant treatment for methemoglobinemia",
                    "Mechanism / Action": "Directly reduces methemoglobin as a reducing agent",
                    "Clinical Note": "An alternative when methylene blue is not appropriate"
                },
                "Hydroxocobalamin": {
                    "Role": "First-line antidote for cyanide poisoning",
                    "Mechanism / Action": "Binds cyanide directly for excretion",
                    "Clinical Note": "Preferred over nitrites to avoid inducing methemoglobinemia"
                }
            }
        }
    ]
}
