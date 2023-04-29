sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

# Store sentence without "!" exclamation marks
sentence_normal = sentence.replace("!", " ")
print(sentence_normal)

# Store sentence in upper case
sentence_upper = sentence_normal.upper()
print(sentence_upper)

# Print current state sentence in reverse: ". GOD YZAL EHT REVO SPMUJ XOF NWORB KCIUQ EHT"
print (sentence_upper[::-1])

# Print original sentence in reverse since task step does not clearly say which sentence needs to be printed in reverse: ".!god!yzal!eht!revo!spmuj!xof!nworb!kciuq!ehT"
print (sentence[::-1])
