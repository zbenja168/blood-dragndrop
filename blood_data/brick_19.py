BRICK = {
    "brick_num": 19,
    "brick_title": "Hemophilia",
    "games": [
        {
            "slug": "hemophilia_types",
            "title": "Types of Hemophilia and Mimics",
            "subtitle": "Match each bleeding disorder to its deficient protein, inheritance, and key feature",
            "categories": ["Deficient Factor / Protein", "Inheritance Pattern", "Distinguishing Feature"],
            "data": {
                "Hemophilia A": {
                    "Deficient Factor / Protein": "Factor VIII",
                    "Inheritance Pattern": "X-linked recessive",
                    "Distinguishing Feature": "Most common type (~4x hemophilia B); ~30% arise from spontaneous mutation"
                },
                "Hemophilia B": {
                    "Deficient Factor / Protein": "Factor IX",
                    "Inheritance Pattern": "X-linked recessive",
                    "Distinguishing Feature": "Clinically indistinguishable from A except by specific factor assay"
                },
                "Hemophilia C": {
                    "Deficient Factor / Protein": "Factor XI",
                    "Inheritance Pattern": "Autosomal recessive",
                    "Distinguishing Feature": "Extremely rare (~1% of hemophilia cases in the U.S.)"
                },
                "Acquired Hemophilia": {
                    "Deficient Factor / Protein": "Autoantibody against Factor VIII",
                    "Inheritance Pattern": "Not inherited (autoimmune)",
                    "Distinguishing Feature": "Older adults, female predominance; malignancy, lupus, drugs, or idiopathic"
                },
                "von Willebrand Disease": {
                    "Deficient Factor / Protein": "von Willebrand factor",
                    "Inheritance Pattern": "Autosomal dominant",
                    "Distinguishing Feature": "Impaired platelet plug formation with petechiae; severe forms resemble hemophilia A"
                }
            }
        },
        {
            "slug": "hemophilia_labs",
            "title": "Diagnosing Hemophilia",
            "subtitle": "Match each test to its typical result and what it tells you",
            "categories": ["Test", "Typical Result in Hemophilia", "Significance"],
            "data": {
                "Activated PTT (aPTT)": {
                    "Test": "Measures the intrinsic coagulation pathway",
                    "Typical Result in Hemophilia": "Prolonged",
                    "Significance": "Reflects impaired intrinsic arm from factor VIII or IX deficiency"
                },
                "Prothrombin Time (PT/INR)": {
                    "Test": "Measures the extrinsic coagulation pathway",
                    "Typical Result in Hemophilia": "Normal",
                    "Significance": "Extrinsic arm is unaffected in hemophilia"
                },
                "Mixing Study": {
                    "Test": "Patient plasma mixed 1:1 with normal plasma",
                    "Typical Result in Hemophilia": "Prolonged PTT corrects to normal",
                    "Significance": "Missing factors are restored, confirming factor deficiency (not an inhibitor)"
                },
                "Platelet Count": {
                    "Test": "Component of primary hemostasis",
                    "Typical Result in Hemophilia": "Normal",
                    "Significance": "Platelets are unaffected, unlike in platelet or vWF disorders"
                },
                "Specific Factor Assay": {
                    "Test": "Directly measures factor VIII and factor IX activity",
                    "Typical Result in Hemophilia": "Reduced activity of the deficient factor",
                    "Significance": "Differentiates hemophilia A from hemophilia B"
                }
            }
        },
        {
            "slug": "hemophilia_treatments",
            "title": "Treating Hemophilia",
            "subtitle": "Match each therapy to how it works and when it is used",
            "categories": ["Therapy", "Mechanism", "Best Indication"],
            "data": {
                "Recombinant Factor VIII": {
                    "Therapy": "Replaces the deficient clotting factor",
                    "Mechanism": "Restores factor VIII activity in the intrinsic pathway",
                    "Best Indication": "Moderate-to-severe hemophilia A"
                },
                "Recombinant Factor IX": {
                    "Therapy": "Replaces the deficient clotting factor",
                    "Mechanism": "Restores factor IX activity in the intrinsic pathway",
                    "Best Indication": "Hemophilia B"
                },
                "Desmopressin (DDAVP)": {
                    "Therapy": "Stimulates release of von Willebrand factor from platelets",
                    "Mechanism": "Raises factor VIII stability and circulating levels",
                    "Best Indication": "Mild hemophilia A with reduced factor VIII production"
                },
                "Recombinant Factor VIIa": {
                    "Therapy": "Bypassing agent for patients with an inhibitor",
                    "Mechanism": "Directly generates factor Xa and thrombin",
                    "Best Indication": "Acute bleeding in a patient with a factor VIII inhibitor"
                },
                "Emicizumab": {
                    "Therapy": "Monoclonal antibody used as prophylaxis",
                    "Mechanism": "Bridges factor IXa and factor X, mimicking factor VIIIa",
                    "Best Indication": "Hemophilia A with a moderate-to-high titer inhibitor"
                },
                "Immunosuppression (prednisone, rituximab)": {
                    "Therapy": "Eliminates the pathologic antibody",
                    "Mechanism": "Suppresses the autoimmune production of the inhibitor",
                    "Best Indication": "Acquired hemophilia to remove the autoantibody"
                }
            }
        },
        {
            "slug": "hemophilia_bleeding",
            "title": "Where Hemophilia Bleeds",
            "subtitle": "Match each bleeding manifestation to its description and clinical significance",
            "categories": ["Manifestation", "Description", "Clinical Significance"],
            "data": {
                "Ecchymoses": {
                    "Manifestation": "Easy bruising of the skin",
                    "Description": "Diffuse superficial soft-tissue bleeding",
                    "Clinical Significance": "Common early clinical feature of hemophilia"
                },
                "Hemarthrosis": {
                    "Manifestation": "Bleeding into the joints",
                    "Description": "Most often the knees, ankles, and elbows",
                    "Clinical Significance": "Recurrent bleeds cause joint deformity, chronic pain, and may need joint replacement"
                },
                "Intracranial Hemorrhage": {
                    "Manifestation": "Bleeding within the skull",
                    "Description": "Deep, life-threatening central nervous system bleed",
                    "Clinical Significance": "Most common cause of death from hemorrhage in hemophilia"
                },
                "Hematuria": {
                    "Manifestation": "Blood in the urine",
                    "Description": "Bleeding from the genitourinary tract",
                    "Clinical Significance": "Sign of persistent genitourinary bleeding"
                },
                "Gastrointestinal Bleeding": {
                    "Manifestation": "Blood in the stool",
                    "Description": "Bleeding from the gastrointestinal tract",
                    "Clinical Significance": "Sign of internal mucosal hemorrhage"
                }
            }
        }
    ]
}
