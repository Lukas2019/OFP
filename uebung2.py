symbols = ["scissors", "paper", "rock", "lizzard", "spock"]
verbs = ["cuts", "gets crushed by", "decapitates", "gets smashed by",
"covers", "gets eaten by", "disproves",
"crushes", "gets vaporized by",
"poisons"]


symbols_used = symbols
loop = 0

for symbol in symbols:
    for symbol_2 in symbols_used:
        if symbol_2 != symbol:
            print(symbol, verbs[loop], symbol_2)
            loop +=1
    symbols_used.pop(0)