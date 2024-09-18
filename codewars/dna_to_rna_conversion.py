def dna_to_rna(dna):
    rna = []

    for nucleic_acid in dna:
        if nucleic_acid == "T":
            rna.append("U")
        else:
            rna.append(nucleic_acid)

    return "".join(rna)


print((dna_to_rna("TTTT") == "UUUU"))
print((dna_to_rna("GCAT") == "GCAU"))
print((dna_to_rna("GACCGCCGCC") == "GACCGCCGCC"))


# optimized version
def dna_to_rna(dna):
    return dna.replace("T", "U")


print((dna_to_rna("TTTT") == "UUUU"))
print((dna_to_rna("GCAT") == "GCAU"))
print((dna_to_rna("GACCGCCGCC") == "GACCGCCGCC"))


# loop but without changing into list

def dna_to_rna(dna):
    rna = ""
    for i in dna:
        if i == "T":
            rna = rna + "U"  # use concatenation instead of list append
        else:
            rna = rna + i
    return rna


print((dna_to_rna("TTTT") == "UUUU"))
print((dna_to_rna("GCAT") == "GCAU"))
print((dna_to_rna("GACCGCCGCC") == "GACCGCCGCC"))
