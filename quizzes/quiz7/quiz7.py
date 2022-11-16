from typing import Dict

def things() -> Dict[str, str]:
  things = {"mochi": "cat"}
  things["pikachu"] = "pokemon"
  things["optimus prime"] = "autobot"
  things["yoshi"] = "dinosaur"
  return things

print(things())

f = open("oneplusone", "w")
oneplusone = 1 + 1
f.write(f"{oneplusone}")
f.close()