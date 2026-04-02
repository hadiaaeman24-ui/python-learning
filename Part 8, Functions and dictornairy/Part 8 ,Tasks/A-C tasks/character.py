def player():
    for key in player_data:
      print(key, ":", player_data[key])
    
     
player_data ={
    "name" : "leon",
    "health" : 10,
    "inventory" : []
}

player()

