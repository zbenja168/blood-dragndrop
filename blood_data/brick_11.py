BRICK = {
    "brick_num": 11,
    "brick_title": "Hereditary Spherocytosis",
    "games": [
        {
            "slug": "hs_pathophysiology",
            "title": "How Spherocytes Form and Are Destroyed",
            "subtitle": "Match each step in HS pathophysiology to its mechanism and its downstream consequence",
            "categories": ["Initiating Factor", "Mechanism", "Consequence"],
            "data": {
                "Membrane protein defect": {
                    "Initiating Factor": "Defective ankyrin or spectrin in the RBC cytoskeleton",
                    "Mechanism": "Membrane forms blebs that fall off, losing surface area faster than volume",
                    "Consequence": "RBC rounds up into a sphere-shaped spherocyte"
                },
                "Defective glycolysis": {
                    "Initiating Factor": "Membrane abnormality impairs glycolysis with lactic acid buildup",
                    "Mechanism": "Reduced intracellular ATP inhibits the sodium-potassium pump",
                    "Consequence": "Sodium and water accumulate inside, deforming the cell into a sphere"
                },
                "Loss of biconcave shape": {
                    "Initiating Factor": "Spherocytes have no excess membrane or wiggle room",
                    "Mechanism": "Cell cannot deform to squeeze through the splenic sinusoids",
                    "Consequence": "Cells become damaged by the tight fit in the spleen"
                },
                "Splenic trapping": {
                    "Initiating Factor": "Damaged spherocytes are retained in the spleen",
                    "Mechanism": "Splenic macrophages destroy them at a much higher rate than normal",
                    "Consequence": "Extravascular hemolysis, the hallmark of the disorder"
                },
                "Chronic hemolysis": {
                    "Initiating Factor": "Ongoing extravascular destruction of RBCs",
                    "Mechanism": "The spleen enlarges and becomes less functional over time",
                    "Consequence": "Splenomegaly and functional asplenia with reduced infection defense"
                },
                "Parvovirus B19 infection": {
                    "Initiating Factor": "Parvovirus B19 infects erythroid precursors",
                    "Mechanism": "Bone marrow RBC production temporarily shuts down",
                    "Consequence": "Aplastic crisis with significant worsening anemia"
                }
            }
        },
        {
            "slug": "hs_diagnostics",
            "title": "Diagnostic Testing in Hereditary Spherocytosis",
            "subtitle": "Match each diagnostic test or parameter to its result in HS and why it matters",
            "categories": ["Test or Parameter", "Result in HS", "Significance"],
            "data": {
                "MCHC": {
                    "Test or Parameter": "Mean corpuscular hemoglobin concentration",
                    "Result in HS": "Increased",
                    "Significance": "Only anemia where MCHC is routinely increased, from mild intracellular dehydration"
                },
                "MCV": {
                    "Test or Parameter": "Mean corpuscular volume",
                    "Result in HS": "Normal",
                    "Significance": "HS is a normocytic anemia; the cells do not become larger"
                },
                "RDW": {
                    "Test or Parameter": "Red blood cell distribution width",
                    "Result in HS": "Increased",
                    "Significance": "Some cells become smaller while others stay larger"
                },
                "Direct antiglobulin test": {
                    "Test or Parameter": "Direct antiglobulin (Coombs) test",
                    "Result in HS": "Negative",
                    "Significance": "Differentiates HS from immune-mediated hemolysis"
                },
                "Osmotic fragility test": {
                    "Test or Parameter": "Osmotic fragility test in hypotonic solution",
                    "Result in HS": "Increased fragility, cells lyse",
                    "Significance": "Spherocytes lack excess membrane and burst as water flows in"
                },
                "EMA binding test": {
                    "Test or Parameter": "Eosin-5-maleimide (EMA) binding by flow cytometry",
                    "Result in HS": "Reduced binding",
                    "Significance": "Main confirmatory test, reflecting band 3 or other protein deficiency"
                }
            }
        },
        {
            "slug": "hs_management",
            "title": "Managing Hereditary Spherocytosis by Scenario",
            "subtitle": "Match each clinical scenario to its recommended management and the rationale",
            "categories": ["Clinical Scenario", "Management", "Rationale"],
            "data": {
                "Mild asymptomatic adult": {
                    "Clinical Scenario": "Adult with mild HS and no symptoms",
                    "Management": "No further therapy, observation only",
                    "Rationale": "Most adults with mild HS require no treatment"
                },
                "Jaundiced neonate": {
                    "Clinical Scenario": "Neonate with worsening jaundice",
                    "Management": "Phototherapy to lower bilirubin",
                    "Rationale": "Jaundice can impede neurologic development in the newborn"
                },
                "Moderate to severe or pregnant": {
                    "Clinical Scenario": "Moderate to severe HS, including pregnancy",
                    "Management": "Folic acid supplementation",
                    "Rationale": "Constant low-grade hemolysis raises demand for making new RBCs"
                },
                "Hemolytic or aplastic crisis": {
                    "Clinical Scenario": "Acute hemolytic or aplastic crisis",
                    "Management": "Transfusion of red blood cells",
                    "Rationale": "Corrects the acute severe drop in hemoglobin"
                },
                "Chronic severe symptomatic anemia": {
                    "Clinical Scenario": "Unusual patient with chronic severe symptomatic anemia",
                    "Management": "Splenectomy",
                    "Rationale": "Removes the spleen, where most of the hemolysis occurs"
                }
            }
        },
        {
            "slug": "hs_differential",
            "title": "Hemolytic Anemias and Their Mimics",
            "subtitle": "Match each condition to its underlying defect and its distinguishing feature",
            "categories": ["Condition", "Underlying Defect or Cause", "Distinguishing Feature"],
            "data": {
                "Hereditary spherocytosis": {
                    "Condition": "Hereditary spherocytosis",
                    "Underlying Defect or Cause": "Ankyrin defect in the RBC cytoskeleton (most common)",
                    "Distinguishing Feature": "Round spherocytes, increased MCHC, positive EMA binding test"
                },
                "Hereditary elliptocytosis": {
                    "Condition": "Hereditary elliptocytosis",
                    "Underlying Defect or Cause": "Spectrin defect, autosomal dominant",
                    "Distinguishing Feature": "Elliptocytes on smear, common in patients of African descent"
                },
                "Hereditary pyropoikilocytosis": {
                    "Condition": "Hereditary pyropoikilocytosis",
                    "Underlying Defect or Cause": "Two spectrin gene mutations, autosomal recessive",
                    "Distinguishing Feature": "RBCs resemble those seen in patients with extensive burns"
                },
                "Sickle cell disease": {
                    "Condition": "Sickle cell disease",
                    "Underlying Defect or Cause": "Defect in the beta-chain of hemoglobin",
                    "Distinguishing Feature": "Sickled cells, elliptical with pointed ends"
                },
                "Autoimmune hemolytic anemia": {
                    "Condition": "Autoimmune hemolytic anemia",
                    "Underlying Defect or Cause": "Autoimmune destruction of red blood cells",
                    "Distinguishing Feature": "Spherocytes may be present but the direct antiglobulin test is positive"
                },
                "Aplastic crisis": {
                    "Condition": "Aplastic crisis",
                    "Underlying Defect or Cause": "Parvovirus B19 suppression of marrow RBC production",
                    "Distinguishing Feature": "Temporary shutdown of RBC formation worsening chronic hemolytic anemia"
                }
            }
        }
    ]
}
