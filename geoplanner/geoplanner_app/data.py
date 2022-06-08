construction_classes =[{
    "class" : "C1",
    "description" : "Residential house with a maximum surface of 250 m2 and up to 2 stories high. Well-known geotechnical conditions.",
    "min_points" : 2,
    "distance_coefficient": 1
},{
    "class" : "C2",
    "description" : "Residential, commercial or industrial buildings up to 2 stories high.",
    "min_points" : 3,
    "distance_coefficient": 1
},{
    "class" : "C3",
    "description" : "Residential, commercial or industrial buildings up to 4 stories high. No bearing walls. Structure is independent of enclosure.",
    "min_points" : 3,
    "distance_coefficient": 1
},{
    "class" : "C4",
    "description" : "Residential, commercial or industrial buildings between 4 to 10 stories high. Also buildings up to 4 stories high not included in class C3.",
    "min_points" : 3,
    "distance_coefficient": 0.8,
},{
    "class" : "C5",
    "description" : "Residential, commercial or industrial buildings between 11 to 20 stories high. Silos and storage tanks.",
    "min_points" : 3,
    "distance_coefficient": 0.7,
},{
    "class" : "C6",
    "description" : "Monumental or singular buildings. Buildings higher than 20 stories high.",
    "min_points" : 3,
    "distance_coefficient": 0.6,
},{
    "class" : "C7",
    "description" : "Complementary structures with imprint less than 50 m2.",
    "min_points" : 1,
    "distance_coefficient": 1,
},{
    "class" : "C8",
    "description" : "Bridges with span <= 35 m. Minimum points is stated for each pile or abutment.",
    "min_points" : 1,
    "distance_coefficient": "",
},{
    "class" : "C9",
    "description" : "Bridges with span > 35 m. and/or structurally separated lanes. Minimum points is stated for each pile or abutment.",
    "min_points" : 2,
    "distance_coefficient": "",
}]

variability_types = [{
    "group": "Low variability",
    "min_distance": 30,
    "max_distance": 40,
    "description": "Aeolian plain" 
},{
    "group": "Medium variability",
    "min_distance": 20,
    "max_distance": 30,
    "description": "Volcanic plateau"
},{
    "group": "High variability",
    "min_distance": 20,
    "max_distance": 20,
    "description": "Meandering river flood plain"
}]