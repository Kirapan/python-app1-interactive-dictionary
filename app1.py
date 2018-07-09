import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def translate(word):
  w = word.lower()
  if w in data:
    return data[w]
  elif w.title() in data:
    return data[w.title()]
  elif w.upper() in data:
    return data[w.upper()]
  elif len(get_close_matches(w,data.keys(), cutoff=0.8)) > 0:
    yn = input("Did you mean %s? Enter Y if yes, or N if no: " % get_close_matches(w,data.keys(),cutoff=0.8)[0])
    if yn == "Y":
      return data[get_close_matches(w,data.keys(),cutoff=0.8)[0]]
    elif yn =="N":
      return "The word doesn't exist. Please double check."
    else:
      return "Sorry, i don't understand what you mean. "
  else:
    return "The word doesn't exist. Please double check."

word = input("Enter a word for definition: ")

output = translate(word)
if type(output) == list:
  for item in output:
    print(item)
else:
  print(output)