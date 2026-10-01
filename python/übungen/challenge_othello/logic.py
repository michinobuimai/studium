# othello start screen



# rules for the game of Othello

# 8x8 grid (insg 64 Felder)

#30 chips für 2 Spieler

#auswählen wer anfängt 50/50 chip wird hochgeworfen (münze)

# schwarz fängt an
#4 chips in der mitte 44 55 schwarz 45 54 weiß




## wie kann man schauen welche stellen legal sind? ##
#möglche darstellung des Feldes ist eine Aufteilung des Feldes für spieler 1 und spieler 2 in eigene
# sowie des leeren feldes

#test "bitboard" (theoretisch ist es ja auch othello aber 1d lol)
# l = "10011110001" 
# s = "00100000110"
# w = "01000001000"
# schwarz fängt an

#für eine richtung:


# shift tn = s[..-(n+1)] AND w   until int tn = 0

# shift s[..-2]
# s[..-2]   = " 0010000011"
# w         = "01000001000"
# t1        = "00000000000" -> int is 0 stop loop keine legalen züge in dieser richtung


# shift tn = s[n..] AND w   until int tn = 0

# shift s[1..]
# s=s[1..]  = "0100000110"
# w         = "01000001000"
# t1        = "01000001000" -> int is 1000001000

# shift s[2..]
# s=s[2..]  = "100000110"
# w         = "01000001000"
# t2        = "00000001000" -> int is 1000

# shift s[3..]
# s=s[3..]  = "00000110"
# w         = "01000001000"
# t3        = "00000000000" -> int is 0 stop loop

# tn OR tn+1 ...
# t1    = "01000001000"
# t2    = "00000001000"
# t3    = "00000000000"
# tf    = "01000001000"

# tf-1 AND l
# tf[1..]   = "1000001000 "
# l         = "10011110001"
# allowed   = "10000010000"


####

#Bitwise operations cheat sheet: ~ INVERT, | OR(beide oder 1 von beiden), & AND(beide), ^ XOR(nur eines von beiden), << BITSHIFT LEFT, >> BITSHIFT  RIGHT
#!! bitshift wrapped muss man aufpassen!!!

s = 0b00000000_00000000_00100000_00000100_00000000_00000000_00000000_00000000
w = 0b00000000_00000000_00010000_00000010_00000000_00000000_00000000_00000000
valid_moves()




def valid_moves():
    global vals, valw
    vals = 0b00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000
    valw = 0b00000000_00000000_00000000_00000000_00000000_00000000_00000000_00000000

    
    # wo es frei ist
    f = ~(s|w)
    
    
    
    
    
    
    
    
    
    
    
    
    




#c boolean um farbe zu entscheiden put ist halt selbsterklärend lol
def place_chippy(put,c):
    if (f & put) == 0:
        return False
    if c == 0:
        if (vals & put) == 0:
            return False
        return True
    if (valw & put) == 0:
        return False
    return True