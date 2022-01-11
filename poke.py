# create a Pokemon

class Pokemon():
    def __init__(self, name, primary_type, max_hp):
        self.name = name
        self.primary_type = primary_type
        self.hp = max_hp
        self.max_hp = max_hp

    def __str__(self):
        return f"{self.name} ({self.primary_type}): ({self.hp}/{self.max_hp})"

# feed them to increade health
    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f"{self.name} now has {self.hp} HP.")
        else:
             print(f"{self.name} is at max hp")
        
            
            

# take a look at it
# if __name__ == "__main__":
#     print(Pokemon(name="bulbasaur", primary_type="grass", max_hp=100))
#     print(Pokemon(name="charmander", primary_type="fire", max_hp=100))


# make them battle and decide for a winner
    def battle(self, other):
        print("Battle:", self.name, "Vs.", other.name)
        result = self.typewheel(self.primary_type, other.primary_type)
        print(f"{self.name} fought {other.name} and the result is a  {result}")
        
        # call typewheel()


    @staticmethod
    def typewheel(type1, type2):
        result = {0: "lose", 1: "win", -1: "tie"}

        # mapping between types and result conditions
        game_map = {"water": 0, "fire": 1, "grass": 2}

        # implement win-lose matrix
        wl_matrix = [
            [-1, 1, 0], # water
            [0, -1, 1], # fire
            [1, 0, -1], # grass
        ]

        # declare a winner
        wl_result = wl_matrix[game_map[type1]][game_map[type2]]
        return result[wl_result]
        

b = Pokemon("bulbasaur", "grass", 100)
c = Pokemon("charmander", "fire", 150)

b.battle(c)

