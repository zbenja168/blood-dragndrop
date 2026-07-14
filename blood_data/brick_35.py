BRICK = {
    "brick_num": 35,
    "brick_title": "Y. pestis, F. tularensis, and B. henselae",
    "games": [
        {
            "slug": "clinical_syndromes",
            "title": "Zoonotic Clinical Syndromes",
            "subtitle": "Match each disease presentation to its transmission, hallmark finding, and typical host",
            "categories": ["Transmission / Source", "Hallmark Finding", "Typical Host / Note"],
            "data": {
                "Bubonic plague (Y. pestis)": {
                    "Transmission / Source": "Bite from an infected flea or contact with an infected animal or carcass",
                    "Hallmark Finding": "Massively enlarged, tender lymph node called a bubo",
                    "Typical Host / Note": "Most common plague form (80-90% of cases)"
                },
                "Pneumonic plague (Y. pestis)": {
                    "Transmission / Source": "Aerosolized respiratory droplets or spread from blood to lungs",
                    "Hallmark Finding": "Necrotizing pneumonia with bloody sputum (hemoptysis)",
                    "Typical Host / Note": "Spreads person-to-person via respiratory droplets"
                },
                "Ulceroglandular tularemia (F. tularensis)": {
                    "Transmission / Source": "Direct contact with rabbits or bites from ticks and deer flies",
                    "Hallmark Finding": "Ulcer at the inoculation site plus regional lymphadenopathy",
                    "Typical Host / Note": "Most common tularemia form (75-85% of cases)"
                },
                "Typhoidal tularemia (F. tularensis)": {
                    "Transmission / Source": "Systemic infection with an unclear portal of entry",
                    "Hallmark Finding": "Febrile illness without localizing signs or lymphadenopathy",
                    "Typical Host / Note": "GI symptoms; older adults with chronic conditions"
                },
                "Cat scratch disease (B. henselae)": {
                    "Transmission / Source": "Scratch or bite from a cat, especially a kitten",
                    "Hallmark Finding": "Inoculation papule plus regional lymphadenopathy with necrotizing granulomas",
                    "Typical Host / Note": "Children, elderly, and immunocompromised at highest risk"
                },
                "Bacillary angiomatosis (B. henselae)": {
                    "Transmission / Source": "Cat scratch or bite in a severely immunocompromised host",
                    "Hallmark Finding": "Red-purple vascular skin nodules that are tender and bleed easily",
                    "Typical Host / Note": "HIV patients with CD4 / T-cell counts below 100 cells/uL"
                }
            }
        },
        {
            "slug": "ypestis_virulence",
            "title": "Y. pestis Virulence Factors",
            "subtitle": "Match each virulence factor to its nature and function",
            "categories": ["Nature / Type", "Function", "Key Detail"],
            "data": {
                "F1 antigen capsule": {
                    "Nature / Type": "Protein-based capsule built from the F1 antigen, encoded on a plasmid",
                    "Function": "Anti-phagocytic and conceals surface antigens for early immune evasion",
                    "Key Detail": "Only produced at 37C, not in the flea (25C)"
                },
                "Yersinia outer proteins (Yops)": {
                    "Nature / Type": "Effector proteins injected into host cells",
                    "Function": "Inhibit phagocytosis and disrupt immune signaling",
                    "Key Detail": "Example: YopH is a tyrosine phosphatase that disrupts the cytoskeleton"
                },
                "Type III secretion system (T3SS)": {
                    "Nature / Type": "Syringe-like transmembrane protein complex",
                    "Function": "Injects Yops directly into approaching phagocytes",
                    "Key Detail": "Lets the bacterium fight the immune system from within the lymph nodes"
                },
                "Lipopolysaccharide (LPS)": {
                    "Nature / Type": "Outer membrane endotoxin of a gram-negative bacterium",
                    "Function": "Causes tissue damage in high doses",
                    "Key Detail": "Present because Y. pestis is gram-negative"
                }
            }
        },
        {
            "slug": "treatment_approach",
            "title": "Treating the Zoonotic Pathogens",
            "subtitle": "Match each clinical setting to its first-line drug, route, and reason",
            "categories": ["First-line Drug", "Route", "When Used"],
            "data": {
                "Severe plague or tularemia": {
                    "First-line Drug": "Aminoglycoside (gentamicin)",
                    "Route": "IV",
                    "When Used": "Severe or systemic disease (septicemic/pneumonic plague, pneumonic/typhoidal tularemia)"
                },
                "Mild plague or tularemia": {
                    "First-line Drug": "Fluoroquinolone (ciprofloxacin or levofloxacin)",
                    "Route": "Oral or IV",
                    "When Used": "Mild, stable cases where an oral option is effective"
                },
                "Plague/tularemia with contraindications": {
                    "First-line Drug": "Tetracycline (doxycycline)",
                    "Route": "Oral or IV",
                    "When Used": "Non-severe cases when other antibiotics are contraindicated; avoid in children under 8"
                },
                "Cat scratch disease": {
                    "First-line Drug": "Macrolide (azithromycin)",
                    "Route": "Oral",
                    "When Used": "Immunocompetent host; shortens the duration of lymphadenitis"
                },
                "Bacillary angiomatosis": {
                    "First-line Drug": "Doxycycline or erythromycin",
                    "Route": "Oral (IV if severe)",
                    "When Used": "Immunocompromised host; prolonged 3-month therapy needed"
                }
            }
        }
    ]
}
