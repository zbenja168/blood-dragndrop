BRICK = {
    "brick_num": 20,
    "brick_title": "von Willebrand Disease",
    "games": [
        {
            "slug": "vwd_types",
            "title": "The Three Types of von Willebrand Disease",
            "subtitle": "Match each vWD type to its vWF defect, inheritance, and defining feature",
            "categories": ["vWF Defect", "Inheritance", "Defining Feature"],
            "data": {
                "Type 1": {
                    "vWF Defect": "Partial quantitative deficiency; vWF function is intact",
                    "Inheritance": "Autosomal dominant",
                    "Defining Feature": "Mildest and most common form of vWD"
                },
                "Type 2": {
                    "vWF Defect": "Qualitative defect; amount normal or low but functionally abnormal",
                    "Inheritance": "Predominantly autosomal dominant",
                    "Defining Feature": "Has multiple subtypes beyond the scope of the brick"
                },
                "Type 3": {
                    "vWF Defect": "Complete absence of vWF with decreased factor VIII",
                    "Inheritance": "Autosomal recessive",
                    "Defining Feature": "Most severe; primary and secondary hemostasis bleeding"
                },
                "Blood Type O (non-vWD)": {
                    "vWF Defect": "Naturally lower vWF without any vWD gene mutation",
                    "Inheritance": "Not inherited as vWD (blood-group effect)",
                    "Defining Feature": "Low vWF without bleeding should not be diagnosed as vWD"
                }
            }
        },
        {
            "slug": "vwd_lab_tests",
            "title": "Diagnostic Tests for von Willebrand Disease",
            "subtitle": "Match each laboratory test to what it measures, its key detail, and its role in the vWD workup",
            "categories": ["What It Measures", "Key Detail", "Role in Workup"],
            "data": {
                "vWF Antigen Assay": {
                    "What It Measures": "The quantity (amount) of vWF in the blood",
                    "Key Detail": "Directly quantifies circulating von Willebrand factor",
                    "Role in Workup": "Confirmatory test for vWF level"
                },
                "Ristocetin Cofactor Activity": {
                    "What It Measures": "The function (activity) of vWF",
                    "Key Detail": "Ristocetin activates vWF, binding platelets to cause agglutination",
                    "Role in Workup": "Confirmatory test for vWF function"
                },
                "Partial Thromboplastin Time (PTT)": {
                    "What It Measures": "Integrity of the intrinsic arm of the coagulation cascade",
                    "Key Detail": "Prolonged when factor VIII is decreased",
                    "Role in Workup": "Less specific screening test"
                },
                "Factor VIII Clotting Activity": {
                    "What It Measures": "The amount of factor VIII in the blood",
                    "Key Detail": "Rules out an isolated factor VIII deficiency",
                    "Role in Workup": "Excludes hemophilia A as an alternative diagnosis"
                },
                "Platelet Aggregation Studies": {
                    "What It Measures": "How well the platelets are functioning",
                    "Key Detail": "Assesses overall platelet aggregation response",
                    "Role in Workup": "Less specific supporting test"
                }
            }
        },
        {
            "slug": "vwd_treatments",
            "title": "Managing Bleeding in von Willebrand Disease",
            "subtitle": "Match each therapy to its mechanism, its best use, and whether it supplies vWF",
            "categories": ["Mechanism", "Best Use", "Supplies vWF?"],
            "data": {
                "vWF Replacement Therapy": {
                    "Mechanism": "Direct supplementation of von Willebrand factor",
                    "Best Use": "Rapid correction of major bleeding or before surgery",
                    "Supplies vWF?": "Yes (recombinant approved for adults only)"
                },
                "Desmopressin (DDAVP)": {
                    "Mechanism": "Releases vWF from cellular (endothelial) stores",
                    "Best Use": "Less severe bleeding in patients with residual stores",
                    "Supplies vWF?": "No (releases the patient's own vWF)"
                },
                "Antifibrinolytics": {
                    "Mechanism": "Prevent dissolution of formed clots",
                    "Best Use": "Moderate or mucosal bleeding, dental procedures",
                    "Supplies vWF?": "No (aminocaproic and tranexamic acid)"
                },
                "Cryoprecipitate": {
                    "Mechanism": "Concentrated clotting factors from frozen-thawed plasma",
                    "Best Use": "Last-choice alternative source for major bleeding",
                    "Supplies vWF?": "Yes (concentrated, bioactive vWF)"
                },
                "Fresh Frozen Plasma": {
                    "Mechanism": "Plasma frozen after collection of whole blood",
                    "Best Use": "Last-choice alternative; large volumes needed",
                    "Supplies vWF?": "Yes (only a small amount of vWF)"
                },
                "Platelet Transfusion": {
                    "Mechanism": "Supplies functional platelets to the circulation",
                    "Best Use": "Correcting thrombocytopenia or aggregation defects",
                    "Supplies vWF?": "No (supplies platelets, not vWF)"
                }
            }
        },
        {
            "slug": "vwd_differential",
            "title": "vWD and Its Look-Alike Bleeding Disorders",
            "subtitle": "Match each disorder to its underlying defect, inheritance, and hallmark clue",
            "categories": ["Underlying Defect", "Inheritance / Origin", "Hallmark Clue"],
            "data": {
                "von Willebrand Disease": {
                    "Underlying Defect": "Deficiency or defect in von Willebrand factor",
                    "Inheritance / Origin": "Usually autosomal dominant (heterozygous)",
                    "Hallmark Clue": "Most common inherited bleeding disorder; mucocutaneous bleeding, normal platelet count"
                },
                "Hemophilia A": {
                    "Underlying Defect": "Deficiency or absence of factor VIII",
                    "Inheritance / Origin": "X-linked (affects males)",
                    "Hallmark Clue": "Deep tissue and joint bleeding with a prolonged PTT"
                },
                "Hemophilia B": {
                    "Underlying Defect": "Deficiency of factor IX",
                    "Inheritance / Origin": "X-linked (affects males)",
                    "Hallmark Clue": "Deep tissue and joint bleeding, clinically similar to hemophilia A"
                },
                "Bernard-Soulier Syndrome": {
                    "Underlying Defect": "Mutation in glycoprotein Ib (the vWF receptor)",
                    "Inheritance / Origin": "Inherited platelet disorder",
                    "Hallmark Clue": "Thrombocytopenia with abnormally large platelets"
                },
                "Thrombotic Thrombocytopenic Purpura": {
                    "Underlying Defect": "Impaired cleavage of ultra-large vWF multimers",
                    "Inheritance / Origin": "Acquired thrombotic disorder ('opposite' of vWD)",
                    "Hallmark Clue": "Excess vWF causing platelet aggregation, thrombosis, and platelet depletion"
                }
            }
        }
    ]
}
