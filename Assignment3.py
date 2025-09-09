import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Turkey is a transcontinental country that shares its land boundaries with eight countries—to the northwest with Greece and Bulgaria, to the northeast with Georgia, to the east with Armenia, Azerbaijan’s Nakhchivan exclave, and Iran, and to the south with Iraq and Syria. In terms of seas, Turkey is uniquely positioned, bordered by the Black Sea to the north, the Aegean Sea to the west, and the Mediterranean Sea to the south, while the Sea of Marmara and the Turkish Straits (the Bosporus and Dardanelles) connect these seas and separate its European and Asian parts.")

for ent in doc.ents:
      print(f"{ent.text:<25} {ent.start_char:<5} {ent.end_char:<5} {ent.label_}")

displacy.serve(doc, style="ent")
