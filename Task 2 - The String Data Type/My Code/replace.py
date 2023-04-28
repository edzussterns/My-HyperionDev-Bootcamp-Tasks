sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."
sentence_normal = sentence.replace("!", " ") # Store sentence without "!" exclamation marks
print(sentence_normal)  # Output: "The quick brown fox jumps over the lazy dog ."

sentence_upper = sentence_normal.upper() # Store sentence in upper case
print(sentence_upper) # Output: "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG ."

print (sentence_upper[::-1]) # Print current state sentence in reverse: ". GOD YZAL EHT REVO SPMUJ XOF NWORB KCIUQ EHT"
print (sentence[::-1]) # Print original sentence in reverse since task step does not clearly say which sentence needs to be printed in reverse: ".!god!yzal!eht!revo!spmuj!xof!nworb!kciuq!ehT"