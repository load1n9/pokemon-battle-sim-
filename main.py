import pokebase as pb
import random

class Battle:
    def __init__(self, a,b):
      self.setStats(a,b)
      self.setMoves()

    def setStats(self,a,b):
      self.p1 = {
        "name": pb.pokemon(a).name,
        "health": 100
      }
      self.p2 = {
       "name": pb.pokemon(b).name,
       "health": 100
      }

    def setMoves(self):
      p1int = random.randint(0,len(pb.pokemon(self.p1["name"]).moves))
      p2int = random.randint(0,len(pb.pokemon(self.p2["name"]).moves))
      self.p1["move"] = pb.pokemon(self.p1["name"]).moves[p1int].move.name
      self.p2["move"] = pb.pokemon(self.p2["name"]).moves[p2int].move.name
       



test = Battle(34,56)

print(test.p1)
