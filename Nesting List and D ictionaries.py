#nesting
capitals = {
    "France": "Paris",
    "German": "Berlin",
}
#nesting a dictionary in a dictionary
#nesting a list in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "travel_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "travel_visits": 17} ,
}
#a list which contains two items and each item is in a dictionary
#easch dictionary has three key value pairs and they all contain different types of data
#nesting a dictionary inside a list
travel_log =[
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12},
    {"country": "Germany",
     "cities_visited": ["Berlin","Hamburg", "Stuttgart"],
     "total_visits":5},

]
