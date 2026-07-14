BRICK = {
    "brick_num": 18,
    "brick_title": "Transfusion Medicine",
    "games": [
        {
            "slug": "blood_types_antigens_antibodies",
            "title": "Blood Types: Antigens, Antibodies, and Compatibility",
            "subtitle": "Match each blood type to its RBC antigens, plasma antibodies, and which RBCs it can receive",
            "categories": ["Antigens on RBC", "Antibodies in Plasma", "Can Receive RBCs From"],
            "data": {
                "O-negative": {
                    "Antigens on RBC": "No A, B, or D antigens (universal donor)",
                    "Antibodies in Plasma": "Anti-A, anti-B, and anti-D (if exposed)",
                    "Can Receive RBCs From": "O-negative only"
                },
                "AB-positive": {
                    "Antigens on RBC": "A, B, and D antigens (universal recipient)",
                    "Antibodies in Plasma": "No antibodies",
                    "Can Receive RBCs From": "All blood types"
                },
                "A-positive": {
                    "Antigens on RBC": "A antigen and D antigen",
                    "Antibodies in Plasma": "Anti-B only",
                    "Can Receive RBCs From": "A-positive, A-negative, O-positive, O-negative"
                },
                "B-negative": {
                    "Antigens on RBC": "B antigen only",
                    "Antibodies in Plasma": "Anti-A, and anti-D if exposed",
                    "Can Receive RBCs From": "B-negative, O-negative"
                },
                "O-positive": {
                    "Antigens on RBC": "D antigen only (no A or B)",
                    "Antibodies in Plasma": "Anti-A and anti-B",
                    "Can Receive RBCs From": "O-positive, O-negative"
                }
            }
        },
        {
            "slug": "blood_products",
            "title": "Blood Products and Their Indications",
            "subtitle": "Match each blood product to its main indication, contents, and clinical pearl",
            "categories": ["Main Indication", "Contents / Feature", "Clinical Pearl"],
            "data": {
                "Packed RBCs": {
                    "Main Indication": "Severe symptomatic anemia (hemoglobin < 7 g/dL)",
                    "Contents / Feature": "Concentrated red blood cells",
                    "Clinical Pearl": "1 unit raises hemoglobin by about 1 g/dL"
                },
                "Platelets": {
                    "Main Indication": "Bleeding from thrombocytopenia (e.g. < 50,000 for surgery)",
                    "Contents / Feature": "Platelets that have ABO antigens but lack Rh",
                    "Clinical Pearl": "Stored at room temperature, so higher bacterial risk"
                },
                "Fresh frozen plasma": {
                    "Main Indication": "Coagulation factor deficiencies, warfarin over-anticoagulation",
                    "Contents / Feature": "Contains all coagulation factors",
                    "Clinical Pearl": "Also used for liver failure and TTP"
                },
                "Cryoprecipitate": {
                    "Main Indication": "Bleeding with low fibrinogen (fibrinogen < 100)",
                    "Contents / Feature": "Contains fibrinogen, factor VIII, and VWF",
                    "Clinical Pearl": "Made by thawing FFP and collecting the precipitate"
                },
                "Granulocytes": {
                    "Main Indication": "Uncontrolled infection with neutrophil count < 500/mm3",
                    "Contents / Feature": "Concentrated white blood cells",
                    "Clinical Pearl": "Reserved for severely neutropenic patients"
                }
            }
        },
        {
            "slug": "transfusion_reactions",
            "title": "Transfusion Reactions",
            "subtitle": "Match each transfusion reaction to its mechanism, presentation, and timing or treatment",
            "categories": ["Mechanism", "Key Presentation", "Timing / Treatment"],
            "data": {
                "Acute hemolytic": {
                    "Mechanism": "Recipient anti-ABO antibodies attack donor RBCs",
                    "Key Presentation": "Fever/chills, back pain, hemoglobinuria, DIC, shock",
                    "Timing / Treatment": "DAT positive; treat with IV fluids, BP support, diuresis"
                },
                "Delayed hemolytic": {
                    "Mechanism": "Antibodies against minor non-ABO antigens on re-exposure",
                    "Key Presentation": "Mild anemia or fever, +/- jaundice",
                    "Timing / Treatment": "Occurs 1 week or more later; supportive care, steroids"
                },
                "Allergic": {
                    "Mechanism": "Type 1 hypersensitivity to allergens in donor blood",
                    "Key Presentation": "Urticaria, itching, wheezing, anaphylaxis if severe",
                    "Timing / Treatment": "Antihistamines; epinephrine/steroids for anaphylaxis"
                },
                "Febrile nonhemolytic": {
                    "Mechanism": "Recipient antibodies against donor leukocyte HLA antigens",
                    "Key Presentation": "Fever and flushing",
                    "Timing / Treatment": "Reduced incidence with leukoreduction; antipyretics"
                },
                "Transfusion-related acute lung injury": {
                    "Mechanism": "Uncertain; may involve donor antibodies attacking recipient",
                    "Key Presentation": "Hypoxia, hypotension, respiratory failure",
                    "Timing / Treatment": "Occurs about 6 hours later; may require intubation"
                },
                "Graft-versus-host disease": {
                    "Mechanism": "Donor T lymphocytes attack immunocompromised host tissue",
                    "Key Presentation": "Fever, rash, diarrhea, hepatomegaly (80-90% fatal)",
                    "Timing / Treatment": "Occurs 7-10 days later; prevented by irradiation"
                }
            }
        },
        {
            "slug": "pretransfusion_testing",
            "title": "Pre-Transfusion Testing",
            "subtitle": "Match each test or protocol to what it detects, the sample used, and its key point",
            "categories": ["What It Detects", "Sample / Method", "Key Point"],
            "data": {
                "Forward typing": {
                    "What It Detects": "ABO and Rh antigens on the patient's RBCs",
                    "Sample / Method": "Patient RBCs mixed with known anti-A and anti-B reagents",
                    "Key Point": "Agglutination means that antigen is present"
                },
                "Reverse typing": {
                    "What It Detects": "Anti-ABO antibodies in the patient's serum",
                    "Sample / Method": "Patient serum mixed with known type A and type B RBCs",
                    "Key Point": "Confirms the forward typing result"
                },
                "Antibody screen": {
                    "What It Detects": "Antibodies against non-ABO/Rh RBC antigens",
                    "Sample / Method": "Patient serum tested against a manufactured RBC panel",
                    "Key Point": "Uses purchased reagent RBCs with various antigens"
                },
                "Cross-match": {
                    "What It Detects": "Incompatibility with a specific donor unit",
                    "Sample / Method": "Patient serum combined with the actual donor RBCs",
                    "Key Point": "Agglutination or hemolysis means do not transfuse"
                },
                "Emergency blood release": {
                    "What It Detects": "Nothing; bypasses standard testing to save time",
                    "Sample / Method": "O-negative units issued immediately from the blood bank",
                    "Key Point": "Used when a patient's life is at risk"
                }
            }
        }
    ]
}
