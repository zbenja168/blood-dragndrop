BRICK = {
    "brick_num": 58,
    "brick_title": "Drugs to Treat Plasmodium spp., Babesia spp., and Brucella spp.",
    "games": [
        {
            "slug": "antimalarial_mechanisms",
            "title": "Antimalarial Drugs: Mechanism, Toxicity, and Caution",
            "subtitle": "Match each antimalarial to its mechanism of action, notable adverse effect, and key contraindication",
            "categories": ["Mechanism of Action", "Notable Adverse Effect", "Contraindication"],
            "data": {
                "Chloroquine / Hydroxychloroquine": {
                    "Mechanism of Action": "Raises vacuole pH and blocks hemoglobin degradation, so toxic heme accumulates",
                    "Notable Adverse Effect": "Pruritus, EKG changes/cardiomyopathy, hemolysis in G6PD deficiency",
                    "Contraindication": "Allergy to chloroquine and related compounds"
                },
                "Atovaquone-proguanil": {
                    "Mechanism of Action": "Inhibits mitochondrial electron transport and parasite folate synthesis",
                    "Notable Adverse Effect": "Abdominal pain, nausea, transient rise in AST/ALT",
                    "Contraindication": "Severe renal failure"
                },
                "Doxycycline": {
                    "Mechanism of Action": "Protein synthesis inhibitor at the 30S ribosomal subunit",
                    "Notable Adverse Effect": "GI disturbances and photosensitivity",
                    "Contraindication": "Allergy to tetracyclines; coadministration with cations"
                },
                "Mefloquine": {
                    "Mechanism of Action": "Interferes with protein synthesis (80S subunit) and hemoglobin digestion",
                    "Notable Adverse Effect": "Abnormal dreams and insomnia",
                    "Contraindication": "History of seizures or psychiatric disorders"
                },
                "Primaquine": {
                    "Mechanism of Action": "Disrupts mitochondria and binds parasite DNA",
                    "Notable Adverse Effect": "Cardiac arrhythmia (QT prolongation) and leukopenia",
                    "Contraindication": "G6PD deficiency (risk of hemolytic anemia)"
                }
            }
        },
        {
            "slug": "prophylaxis_dosing",
            "title": "Malaria Prophylaxis Dosing Schedules",
            "subtitle": "Match each prophylactic drug to its dosing frequency and timing before and after exposure",
            "categories": ["Frequency", "Start Before Exposure", "Stop After Exposure"],
            "data": {
                "Chloroquine / Hydroxychloroquine": {
                    "Frequency": "Once weekly",
                    "Start Before Exposure": "1-2 weeks before",
                    "Stop After Exposure": "4 weeks after"
                },
                "Atovaquone-proguanil": {
                    "Frequency": "Once daily",
                    "Start Before Exposure": "1-2 days before",
                    "Stop After Exposure": "7 days after"
                },
                "Doxycycline": {
                    "Frequency": "Once daily",
                    "Start Before Exposure": "1-2 days before",
                    "Stop After Exposure": "4 weeks after"
                },
                "Mefloquine": {
                    "Frequency": "Once weekly",
                    "Start Before Exposure": "2-3 weeks before",
                    "Stop After Exposure": "4 weeks after"
                },
                "Primaquine": {
                    "Frequency": "Once daily",
                    "Start Before Exposure": "1-2 days before",
                    "Stop After Exposure": "7 days after"
                }
            }
        },
        {
            "slug": "treatment_regimens",
            "title": "Treating Malaria, Babesiosis, and Brucellosis",
            "subtitle": "Match each infection to its first-line regimen, backup option, and a key clinical feature",
            "categories": ["First-Line Regimen", "Alternative / Backup", "Key Feature"],
            "data": {
                "Uncomplicated malaria (resistant area)": {
                    "First-Line Regimen": "Artemisinin combination therapy (ACT)",
                    "Alternative / Backup": "Atovaquone-proguanil, doxycycline, or mefloquine",
                    "Key Feature": "Over 95% cure rate; most rapid parasite clearance"
                },
                "Complicated / severe malaria": {
                    "First-Line Regimen": "IV artesunate for at least 24 hours, then oral",
                    "Alternative / Backup": "Oral artemether-lumefantrine or atovaquone-proguanil",
                    "Key Feature": "Avoid doxycycline because it is too slow-acting"
                },
                "Babesiosis": {
                    "First-Line Regimen": "Azithromycin plus atovaquone",
                    "Alternative / Backup": "Clindamycin plus mefloquine (or quinine)",
                    "Key Feature": "Same regimen regardless of immune status"
                },
                "Brucellosis": {
                    "First-Line Regimen": "Doxycycline plus an aminoglycoside (gentamicin)",
                    "Alternative / Backup": "Doxycycline plus fluoroquinolone or SMX-TMP",
                    "Key Feature": "Both first-line drugs inhibit the 30S subunit"
                }
            }
        },
        {
            "slug": "antibiotics_babesia_brucella",
            "title": "Antibiotics Used for Babesiosis and Brucellosis",
            "subtitle": "Match each antibiotic to its class/target, its role in the regimen, and a key toxicity or interaction",
            "categories": ["Class / Target", "Role in Regimen", "Key Toxicity or Interaction"],
            "data": {
                "Azithromycin": {
                    "Class / Target": "Macrolide; protein synthesis inhibitor",
                    "Role in Regimen": "First-line babesiosis, paired with atovaquone",
                    "Key Toxicity or Interaction": "QT prolongation and GI upset; CYP3A4 interactions"
                },
                "Clindamycin": {
                    "Class / Target": "Protein synthesis inhibitor at the 50S subunit",
                    "Role in Regimen": "Alternative babesiosis, paired with mefloquine",
                    "Key Toxicity or Interaction": "Adverse effects similar to azithromycin"
                },
                "Gentamicin": {
                    "Class / Target": "Aminoglycoside; 30S inhibitor",
                    "Role in Regimen": "First-line brucellosis, paired with doxycycline",
                    "Key Toxicity or Interaction": "Nephrotoxicity and ototoxicity"
                },
                "Doxycycline": {
                    "Class / Target": "Tetracycline; 30S inhibitor",
                    "Role in Regimen": "Backbone of brucellosis therapy",
                    "Key Toxicity or Interaction": "Chelation by cations such as magnesium and iron"
                }
            }
        }
    ]
}
