BRICK = {
    "brick_num": 48,
    "brick_title": "Essential Thrombocythemia",
    "games": [
        {
            "slug": "et_presentation",
            "title": "How Essential Thrombocythemia Presents",
            "subtitle": "Match each symptom group to its mechanism and a typical manifestation",
            "categories": ["Symptom Group", "Underlying Mechanism", "Typical Manifestation"],
            "data": {
                "Nonspecific vascular symptoms": {
                    "Symptom Group": "Most common when symptomatic",
                    "Underlying Mechanism": "Microthrombi and sludging of platelet-rich blood",
                    "Typical Manifestation": "Headache, dizziness, syncope, chest pain"
                },
                "Erythromelalgia": {
                    "Symptom Group": "Microvascular symptom shared with polycythemia vera",
                    "Underlying Mechanism": "Microvascular occlusion in the distal extremities",
                    "Typical Manifestation": "Episodic burning pain and redness of hands and feet"
                },
                "Large thrombus formation": {
                    "Symptom Group": "Less common thrombotic event",
                    "Underlying Mechanism": "Abundance of platelets forming large clots",
                    "Typical Manifestation": "Stroke, deep vein thrombosis, myocardial infarction"
                },
                "Excessive bleeding": {
                    "Symptom Group": "Least common presentation",
                    "Underlying Mechanism": "Decreased platelet function and diminished von Willebrand factor",
                    "Typical Manifestation": "Bleeding despite a very high platelet count"
                },
                "Pregnancy complication": {
                    "Symptom Group": "Obstetric risk in ET",
                    "Underlying Mechanism": "Placental compromise from the disorder",
                    "Typical Manifestation": "Increased risk of first-trimester fetal loss"
                }
            }
        },
        {
            "slug": "et_genetics",
            "title": "Genetic Mutations in Essential Thrombocythemia",
            "subtitle": "Match each gene to how often it drives ET and what it normally encodes",
            "categories": ["Frequency in ET", "Normal Product or Function", "Diagnostic Note"],
            "data": {
                "JAK2": {
                    "Frequency in ET": "About 50% of cases",
                    "Normal Product or Function": "Tyrosine kinase driving JAK/STAT growth signaling",
                    "Diagnostic Note": "First mutation tested; makes ruxolitinib potentially useful"
                },
                "CALR (calreticulin)": {
                    "Frequency in ET": "Roughly 30% of cases",
                    "Normal Product or Function": "Calreticulin protein",
                    "Diagnostic Note": "Tested in JAK2-negative cases"
                },
                "MPL": {
                    "Frequency in ET": "About 5% to 10% of cases",
                    "Normal Product or Function": "Thrombopoietin receptor",
                    "Diagnostic Note": "Tested after JAK2 and CALR are negative"
                },
                "BCR::ABL1": {
                    "Frequency in ET": "Absent in ET",
                    "Normal Product or Function": "Philadelphia-chromosome fusion tyrosine kinase",
                    "Diagnostic Note": "Its presence points to chronic myeloid leukemia instead"
                }
            }
        },
        {
            "slug": "et_diagnosis",
            "title": "Diagnostic Findings in Essential Thrombocythemia",
            "subtitle": "Match each test or finding to its result in ET and its diagnostic role",
            "categories": ["Result in ET", "Diagnostic Role"],
            "data": {
                "Complete blood count": {
                    "Result in ET": "Platelet count above 400,000/mm3 (thrombocytosis)",
                    "Diagnostic Role": "Screening finding, but also elevated in secondary causes"
                },
                "Peripheral blood smear": {
                    "Result in ET": "Platelet anisocytosis with tiny-to-gigantic platelets",
                    "Diagnostic Role": "Suggestive; other cell lines usually appear normal"
                },
                "Mean platelet volume": {
                    "Result in ET": "Increased platelet size",
                    "Diagnostic Role": "Higher volume favors ET over secondary thrombocytosis"
                },
                "Bone marrow biopsy": {
                    "Result in ET": "Normocellular marrow with dominant megakaryocyte proliferation",
                    "Diagnostic Role": "Performed once secondary causes are excluded"
                },
                "Physical exam": {
                    "Result in ET": "Splenomegaly in 25% to 50%, livedo reticularis, erythromelalgia",
                    "Diagnostic Role": "Splenomegaly reflects extramedullary hematopoiesis"
                },
                "Genetic testing": {
                    "Result in ET": "Activating JAK2, CALR, or MPL mutation",
                    "Diagnostic Role": "Confirms a clonal neoplasm after exclusion"
                }
            }
        },
        {
            "slug": "et_treatment",
            "title": "Managing Essential Thrombocythemia",
            "subtitle": "Match each therapy to the patient it fits and its purpose",
            "categories": ["Indicated Patient", "Purpose"],
            "data": {
                "Low-dose aspirin": {
                    "Indicated Patient": "All patients with ET",
                    "Purpose": "Reduce microvascular symptoms and thrombotic risk"
                },
                "Hydroxyurea": {
                    "Indicated Patient": "High-risk: over 60 years old or prior thrombosis",
                    "Purpose": "Cytoreductive therapy to lower the platelet count"
                },
                "Pegylated interferon alfa": {
                    "Indicated Patient": "High-risk patient needing an alternative cytoreducer",
                    "Purpose": "Cytoreductive option instead of hydroxyurea"
                },
                "Anticoagulant": {
                    "Indicated Patient": "Patient with a history of or new thrombosis",
                    "Purpose": "Treat and prevent large-vessel clotting"
                },
                "Ruxolitinib": {
                    "Indicated Patient": "JAK2-mutated ET",
                    "Purpose": "JAK inhibitor targeting the overactive JAK/STAT pathway"
                }
            }
        }
    ]
}
