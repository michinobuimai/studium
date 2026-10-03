let wc  = 30;
let sc  = 30;
let w   = 0b00000000_00000000_00000000_00001000_00010000_00000000_00000000_00000000n;
let s   = 0b00000000_00000000_00000000_00010000_00001000_00000000_00000000_00000000n;
const msk = 0b11111111_11111111_11111111_11111111_11111111_11111111_11111111_11111111n;
const mr  = 0b11111110_11111110_11111110_11111110_11111110_11111110_11111110_11111110n;
const ml  = 0b01111111_01111111_01111111_01111111_01111111_01111111_01111111_01111111n;
let f     = ~(s | w) & msk;
const richt = [[8,msk],[-8,msk],[-1,mr],[1,ml],[7,mr],[9,ml],[-9,mr],[-7,ml]];
let turn = "s";

let tf, tc;

function shift(c, d) {
    const bd = BigInt(d);
    return ((d > 0) ? (c << bd) : (c >> -bd)) & msk;
}
function valide(a, b) {
    tf = {};
    tc = 0n;
    for (const [vsb, msk2] of richt) {
        let t = 0n;
        let nw = shift(a, vsb) & msk2 & b;
        while (nw) {
            t |= nw;
            const key = String(-vsb);
            tf[key] = (tf[key] ?? 0) + 1;
            nw = shift(nw, vsb) & msk2 & b & ~t;
        }
        const tt = shift(t, vsb) & msk2 & f;
        if (tt) tc |= tt;
    }
    return tc !== 0n;
}

function place(p) {
    return false;
}

function next_turn() {
    return false;
}