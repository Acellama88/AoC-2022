s1 = "znk zuct huyy, se iuxg, gtj g igxj mgsk zu lxkk nkx zcu giky ul yvgjky nuc o igamnz znk inkgzkx"
s2 = "zm vbv uli zm vbv z hkzwv gl z hkzwv lmv xsznyvi mld vnkgrvw srh xlikhv lm wrhkozb"
s3 = "ofcrpq af oipp xpba rfgqphgpq l gfx cfth tg fzaitx ofcpypc ofcpypc tifgp"

alphabet = "zyxwvutsrqponmlkjihgfedcba"

numZ = ord("z")
numA = ord("a")

for i in range(1, 26):
    out = ""
    for ch in s1:
        if ch > "z" or ch < "a":
            out += ch
            continue
        val = ord(ch) + i
        if val > numZ:
            val = val - (numZ + 1) + numA
        out += chr(val)
    print(f"{i}: {out}")

print("\n")

out = ""
for i in range(len(s2)):
    if s2[i] > "z" or s2[i] < "a":
        out += s2[i]
        continue
    out += alphabet[ord(s2[i]) - numA]
print(out)

print("\n")

out = ""
for i in range(1, 26):
    out = ""
    for ch in s3:
        if ch > "z" or ch < "a":
            out += ch
            continue
        val = ord(ch) + i
        if val > numZ:
            val = val - (numZ + 1) + numA
        out += alphabet[val - numA]
    print(f"{i}: {out}")

out = ""
s4 = "VG0YR 6IUIQ S5E0S RN1X5 IRYXF WJ75Y 69FRV W6WTL T6SRZ U2BIA 3DPEG M25YW AWBLS"
for i in range(len(s4)):
    out = s4[i] + out
print(out)