BRICK = {
    "brick_num": 10,
    "brick_title": "Aplastic Anemia",
    "games": [
        {
            "slug": "myeloid_lineage",
            "title": "Bone Marrow Lineages in Aplastic Anemia",
            "subtitle": "Match each precursor to its mature cell, stem line, and fate in aplastic anemia",
            "categories": ["Mature cell(s) produced", "Stem cell line", "Status in aplastic anemia"],
            "data": {
                "Erythroblast": {
                    "Mature cell(s) produced": "Erythrocytes (red blood cells)",
                    "Stem cell line": "Myeloid",
                    "Status in aplastic anemia": "Decreased, causing normocytic anemia"
                },
                "Megakaryoblast": {
                    "Mature cell(s) produced": "Platelets",
                    "Stem cell line": "Myeloid",
                    "Status in aplastic anemia": "Decreased, causing bleeding and petechiae"
                },
                "Myeloblast": {
                    "Mature cell(s) produced": "Neutrophils, basophils, eosinophils, mast cells",
                    "Stem cell line": "Myeloid",
                    "Status in aplastic anemia": "Decreased, causing recurrent infections"
                },
                "Monoblast": {
                    "Mature cell(s) produced": "Monocytes and macrophages",
                    "Stem cell line": "Myeloid",
                    "Status in aplastic anemia": "Decreased along with other myeloid cells"
                },
                "Lymphoblast": {
                    "Mature cell(s) produced": "B cells, T cells, and NK cells",
                    "Stem cell line": "Lymphoid",
                    "Status in aplastic anemia": "Relatively spared, so lymphocytes remain near normal"
                }
            }
        },
        {
            "slug": "etiology",
            "title": "Causes of Aplastic Anemia",
            "subtitle": "Match each cause to its category and mechanism of hematopoietic stem cell injury",
            "categories": ["Etiologic category", "Mechanism of HSC loss", "Distinguishing feature"],
            "data": {
                "Chemotherapy drugs": {
                    "Etiologic category": "Drugs and toxins (dose-dependent)",
                    "Mechanism of HSC loss": "Kill rapidly dividing cells, including normal stem cells",
                    "Distinguishing feature": "Severity rises with initial and cumulative dose"
                },
                "Ionizing radiation": {
                    "Etiologic category": "Radiation (dose-dependent)",
                    "Mechanism of HSC loss": "Generates free radicals that damage marrow",
                    "Distinguishing feature": "Used in radiotherapy for cancer"
                },
                "Carbamazepine": {
                    "Etiologic category": "Idiosyncratic drug reaction",
                    "Mechanism of HSC loss": "Binds stem cell antigens as a hapten, triggering T-cell cytotoxicity",
                    "Distinguishing feature": "An anti-epileptic; reaction is not dose-related"
                },
                "Epstein-Barr virus": {
                    "Etiologic category": "Viral infection",
                    "Mechanism of HSC loss": "Alters blast antigens and activates self-reactive cytotoxic T cells",
                    "Distinguishing feature": "Also seen with HIV, hepatitis B and C, and herpes"
                },
                "Fanconi anemia": {
                    "Etiologic category": "Hereditary condition",
                    "Mechanism of HSC loss": "Defective DNA repair leads to chromosome fragility and apoptosis",
                    "Distinguishing feature": "Autosomal recessive; presents in childhood"
                },
                "Systemic lupus erythematosus": {
                    "Etiologic category": "Autoimmune disease",
                    "Mechanism of HSC loss": "Immune-mediated destruction of stem cells",
                    "Distinguishing feature": "Graft-vs-host disease acts by a similar autoimmune attack"
                }
            }
        },
        {
            "slug": "marrow_failure_ddx",
            "title": "Distinguishing Bone Marrow Failure Syndromes",
            "subtitle": "Match each syndrome to the cell lines affected, a key finding, and a classic association",
            "categories": ["Cell lines affected", "Key finding", "Classic association"],
            "data": {
                "Aplastic anemia": {
                    "Cell lines affected": "All myeloid lines (pancytopenia)",
                    "Key finding": "Hypocellular marrow replaced by adipose tissue",
                    "Classic association": "Idiopathic or drug-induced HSC loss"
                },
                "Pure red cell aplasia": {
                    "Cell lines affected": "Erythroid precursors only (isolated anemia)",
                    "Key finding": "Reticulocytopenia with normal platelets and granulocytes",
                    "Classic association": "Thymoma and parvovirus B19 infection"
                },
                "Diamond-Blackfan syndrome": {
                    "Cell lines affected": "Erythroid precursors only, congenital",
                    "Key finding": "Macrocytic anemia with reticulocytopenia",
                    "Classic association": "Ribosomal protein gene mutations and triphalangeal thumb"
                },
                "Fanconi anemia": {
                    "Cell lines affected": "All lines (pancytopenia), congenital",
                    "Key finding": "Increased chromosomal breaks with DEB or mitomycin C",
                    "Classic association": "Cafe-au-lait spots and radial/thumb defects"
                }
            }
        },
        {
            "slug": "management",
            "title": "Managing Aplastic Anemia",
            "subtitle": "Match each treatment to its rationale and primary indication",
            "categories": ["Treatment", "Mechanism / rationale", "Primary indication"],
            "data": {
                "Discontinue causative drug": {
                    "Treatment": "Remove secondary cause",
                    "Mechanism / rationale": "Halts ongoing HSC injury so counts can rebound",
                    "Primary indication": "Drug-induced aplastic anemia (first step)"
                },
                "RBC and platelet transfusion": {
                    "Treatment": "Supportive care",
                    "Mechanism / rationale": "Replaces deficient circulating cells",
                    "Primary indication": "Symptomatic anemia or bleeding"
                },
                "Eltrombopag": {
                    "Treatment": "Thrombopoietin receptor agonist",
                    "Mechanism / rationale": "Stimulates production of all cell lines, not just platelets",
                    "Primary indication": "Idiopathic aplastic anemia"
                },
                "Antithymocyte globulin or cyclosporine": {
                    "Treatment": "Immunosuppression",
                    "Mechanism / rationale": "Suppresses T-cell mediated attack on stem cells",
                    "Primary indication": "Severe aplastic anemia"
                },
                "Allogeneic stem cell transplant": {
                    "Treatment": "Donor HSC transplantation",
                    "Mechanism / rationale": "Donor stem cells repopulate the marrow; potentially curative",
                    "Primary indication": "Severe or refractory cases after other treatments fail"
                }
            }
        }
    ]
}
