m = input("\n\nNachricht: ")


b = input("\n\nRAS? (Ja/Nein): ").strip().lower()

match b:
    case "ja":
        print ("> RAS wurde activiert")
    case "nein":    
        print ("> RAS wurde deactiviert")
    case _:
        print(f"\033[31m> kein wert wurde übergeben, rückfall auf NEIN\033[0m")


base=64

print(f"Nachricht encodiert in Basis-{base}")

ec=""
ecd=""
lold=""

#basel deez nuts
basel = len(str(base))
basel2 = 2*basel
b=""

for c in range(basel-1):
    b = b + "0"

print(">> Am formattieren...")
for c in m:
    n = ord(c)
    l = 0
    while n > 0:
            n, rest = divmod(n, base)
            rest = str(rest)
            #schauen ob die len schon existiert (optimierung der daten menge)
                        
            while len(rest) < basel:
                rest = "0" + rest
            l+=len(rest)
            ec = ec + rest
                  
    l = str(l//2)
    if lold == l and (int(ecd[-basel2:-basel]) + 1) <= base:   
        
        oa = str(int(ecd[-basel2:-basel]) + 1)
        while len(oa) < basel:
            oa = "0" + oa
        ecd = ecd[:-basel2]+oa+ecd[-basel:]       
    else:
        while len(l) < basel:
            l = "0" + l
        lold = str(int(l))
        ecd = ecd + b + "1" + l

sh = 0
while len(ecd) >= basel2:
    
    a = int(ecd[:basel])
    b = int(ecd[basel:basel2])
    
    
    if sh == 0:
        c = ""
    else:
        c=ec[:sh]

    ec = c + ecd[:basel2] + ec[sh:]
    
    ecd = ecd[basel2:]
    sh += a * b * basel + basel2
    
print(ec)


#The quick brown fox jumps over the lazy dog • αβγδε • АБВГД • אבגדה • أبجد • ऋषियों • あいうえお • 0123456789 • ∀∃∈∞ • ┌┬┐├┼┤└┴┘ • █▓▒░ • ☀☁☂★ • ᚠᚢᚦᚨ • ⠁⠃⠉⠙
    


        











#Decodiere die Basis





