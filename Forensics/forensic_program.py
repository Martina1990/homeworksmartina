#DNA of perpetrator
perp_dna = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

#DNA strings

#DNA Hair color
hair_black = "CCAGCAATCGC"
hair_brown = "GCCAGTGCCG"
hair_blonde = "TTAGCTATCGC"

#DNA Facial shape
face_square = "GCCACGG"
face_round = "ACCACAA"
face_oval = "AGGCCTCA"

#DNA Eye color
eye_blue = "TTGTGGTGGC"
eye_green = "GGGAGGTGGC"
eye_brown = "AAGTAGTGAC"

#DNA Gender
female = "TGAAGGACCTTC"
male = "TGCAGGAACTTC"

#DNA Race
white = "AAAACCTCA"
black = "CGACTACAG"
asian = "CGCGGGCCG"

#Check suspects

#Eva
if female and white and hair_blonde and eye_blue and face_oval in perp_dna:
    print "Eva is the ice cream thief!"
#Larisa
elif female and white and hair_brown and eye_brown and face_oval in perp_dna:
    print "Larisa is the ice cream thief!"
#Matej
elif male and white and hair_black and eye_blue and face_oval in perp_dna:
    print "Matej is the ice cream thief!"
#Miha
elif male and white and hair_brown and eye_green and face_square in perp_dna:
    print "Miha is the ice cream thief!"

