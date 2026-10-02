# rules for the game of Othello
#30 chips für 2 Spieler
# schwarz fängt an
#4 chips in der mitte 44 55 schwarz 45 54 weiß

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

#def debug_64bit(v):
#    bstr = f"{v & 0xFFFFFFFFFFFFFFFF:064b}"
#    frmt = "\n".join(bstr[i:i+8] for i in range(0, 64, 8))
#    print(f"{frmt}")
####

#Bitwise operations cheat sheet: ~ INVERT, | OR(beide oder 1 von beiden), & AND(beide), ^ XOR(nur eines von beiden), << BITSHIFT LEFT, >> BITSHIFT  RIGHT
#!! bitshift wrapped muss man aufpassen!!!
# Spagetthi !!!!

wc      = 30
sc      = 30
w       = 0b00000000_00000000_00000000_00001000_00010000_00000000_00000000_00000000
s       = 0b00000000_00000000_00000000_00010000_00001000_00000000_00000000_00000000
msk     = 0b11111111_11111111_11111111_11111111_11111111_11111111_11111111_11111111
mr      = 0b11111110_11111110_11111110_11111110_11111110_11111110_11111110_11111110
ml      = 0b01111111_01111111_01111111_01111111_01111111_01111111_01111111_01111111
f       = ~(s | w) & msk
richt   = [(8,msk),(-8,msk),(-1,mr),(1,ml),(7,mr),(9,ml),(-9,mr),(-7,ml)]

def shift(c, d): #shiftet die bits je nach richtung 
    return ((c << d) if d > 0 else (c >> -d)) & msk
def valide(a, b): #valide spots/bitmap und die max depth länge in jede valide richtung
    global tf,tc
    tf , tc = {} , 0
    for vsb, msk2 in richt:
        t = 0
        new     = shift(a, vsb) & msk2 & b
        while new:
            t      |= new
            tf[str(-vsb)] = tf.get(str(-vsb), 0)  + 1
            new     = shift(new, vsb) & msk2 & b & ~t
        tt = shift(t, vsb)    & msk2 & f
        if tt: tc|=tt

valide(s,w)



