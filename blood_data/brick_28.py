BRICK = {
    "brick_num": 28,
    "brick_title": "Platelet Assays",
    "games": [
        {
            "slug": "platelet_count_thresholds",
            "title": "Platelet Count Thresholds",
            "subtitle": "Match each platelet count range to its clinical name/status and the bleeding risk it carries",
            "categories": ["Clinical Name / Status", "Bleeding Risk"],
            "data": {
                ">400,000/mm3": {
                    "Clinical Name / Status": "Thrombocytosis",
                    "Bleeding Risk": "Blood becomes sludgy and flows slowly, risking ischemic events"
                },
                "150,000-400,000/mm3": {
                    "Clinical Name / Status": "Normal platelet count",
                    "Bleeding Risk": "No abnormal bleeding expected"
                },
                "<150,000/mm3": {
                    "Clinical Name / Status": "Thrombocytopenia (mild)",
                    "Bleeding Risk": "Usually no significant bleeding"
                },
                "<50,000/mm3": {
                    "Clinical Name / Status": "Moderate thrombocytopenia",
                    "Bleeding Risk": "May start to see some abnormal bleeding"
                },
                "20,000-50,000/mm3": {
                    "Clinical Name / Status": "Moderate-to-severe thrombocytopenia",
                    "Bleeding Risk": "May lead to increased bleeding after injuries"
                },
                "<10,000/mm3": {
                    "Clinical Name / Status": "Severe thrombocytopenia",
                    "Bleeding Risk": "Risk of spontaneous bleeding"
                }
            }
        },
        {
            "slug": "platelet_assays_overview",
            "title": "The Four Levels of Platelet Testing",
            "subtitle": "Match each platelet assay to what it measures, its method, and a key limitation or point",
            "categories": ["What It Measures", "Method", "Key Point or Limitation"],
            "data": {
                "Platelet count": {
                    "What It Measures": "Number of platelets per volume of blood",
                    "Method": "Automated hematology analyzer, or manual smear if unreliable",
                    "Key Point or Limitation": "Says nothing about how well platelets function"
                },
                "Platelet morphology": {
                    "What It Measures": "Size, shape, and granulation of platelets",
                    "Method": "Manual evaluation of a blood smear under the microscope",
                    "Key Point or Limitation": "Most diseases show normal-appearing platelets, so used less often"
                },
                "Platelet function assay (PFA-100)": {
                    "What It Measures": "How well the platelet plug forms (primary hemostasis)",
                    "Method": "Blood fed through a machine that forms a plug over a standardized aperture",
                    "Key Point or Limitation": "Detects abnormal adhesion/aggregation but not the underlying cause"
                },
                "Bleeding time": {
                    "What It Measures": "Time for a skin cut to stop bleeding (primary hemostasis)",
                    "Method": "Small lancet pierces the forearm; time to stop is recorded",
                    "Key Point or Limitation": "Hard to standardize; being replaced by the PFA-100 (ref 2-9 min)"
                }
            }
        },
        {
            "slug": "aggregation_response_disorders",
            "title": "Ristocetin and Bleeding Disorders",
            "subtitle": "Match each platelet disorder to its defect and its pattern on aggregation studies",
            "categories": ["Underlying Defect", "Ristocetin Response", "Response to ADP/Collagen/Epinephrine"],
            "data": {
                "Bernard-Soulier syndrome": {
                    "Underlying Defect": "Platelets lack the normal GpIb receptor for vWF",
                    "Ristocetin Response": "Absent (no aggregation)",
                    "Response to ADP/Collagen/Epinephrine": "Normal aggregation"
                },
                "Von Willebrand disease": {
                    "Underlying Defect": "Absent or very abnormal von Willebrand factor",
                    "Ristocetin Response": "Absent (no aggregation)",
                    "Response to ADP/Collagen/Epinephrine": "Normal aggregation"
                },
                "Normal platelets": {
                    "Underlying Defect": "No defect present",
                    "Ristocetin Response": "Normal aggregation",
                    "Response to ADP/Collagen/Epinephrine": "Normal aggregation"
                }
            }
        },
        {
            "slug": "aggregating_agents_specialized",
            "title": "Agents and Specialized Tests",
            "subtitle": "Match each aggregating agent or specialized test to its role in evaluating platelet dysfunction",
            "categories": ["Role / What It Assesses", "Key Detail"],
            "data": {
                "Ristocetin": {
                    "Role / What It Assesses": "Drives vWF (GpIb) receptors to the platelet surface to bind vWF",
                    "Key Detail": "Fails to aggregate in Bernard-Soulier syndrome and von Willebrand disease"
                },
                "ADP, collagen, epinephrine": {
                    "Role / What It Assesses": "Standard aggregating agents added to platelet-rich plasma",
                    "Key Detail": "Normal platelets respond to every agent; abnormal patterns narrow diagnosis"
                },
                "Von Willebrand factor assay": {
                    "Role / What It Assesses": "Measures vWF level directly (von Willebrand antigen)",
                    "Key Detail": "Level is low in von Willebrand disease"
                },
                "Flow cytometry": {
                    "Role / What It Assesses": "Assesses platelet membrane glycoprotein (Gp) complexes",
                    "Key Detail": "Uses whole blood; markers may be decreased in some disorders"
                }
            }
        }
    ]
}
