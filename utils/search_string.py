def location():
    locations = [
        "America",
        "USA",
        "United States",
        "United States of America",
        "New York",
        "California",
        "Texas",
        "Florida",
        "New York City",
        "NYC",
        "Seattle",
        "Portland",
        "San Francisco",
        "Silicon Valley",
        "Menlo Park",
        "San Jose",
        "Los Angeles",
        "San Diego",
        "Las Vegas",
        "Denver",
        "Austin",
        "Dallas",
        "Houston",
        "Canada",
        "Vancouver",
        "Toronto",
        "Montreal",
        "Asia",
        "China",
        "Hong Kong",
        "South Korea",
        "Korea",
        "Seoul",
        "Busan",
        "Pusan",
        "Japan",
        "Tokyo",
        "Russia",
        "Moscow",
        "Shanghai",
        "Beijing",
        "Chongqing",
        "Tianjin",
        "Guangzhou",
        "Shenzhen",
        "Chengdu",
        "Nanjing",
        "Wuhan",
        "India",
        "New Delhi",
        "Europe",
        "UK",
        "United Kingdom",
        "England",
        "Scotland",
        "France",
        "Paris",
        "Germany",
        "Munich",
        "Berlin",
        "Switzerland",
        "Zurich",
        "Spain",
        "Italy",
        "Norway",
        "Oslo",
        "Sweden",
        "Stockholm",
        "Poland",
        "Netherlands",
        "Belgium",
        "Greece",
        "Portugal",
        "Denmark",
        "Finland",
        "Ireland",
    ]

    return ",".join(["+".join(x.split()) for x in locations])

