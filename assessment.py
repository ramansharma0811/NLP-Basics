import spacy
from spacy.matcher import Matcher
nlp = spacy.load('en_core_web_sm')

#Create a Doc object from the file owlcreek.txt
file = open('owlcreek.txt')
text = file.read()
file.close()
doc = nlp(text)
print(doc[:36])

#How many tokens are contained in the file?
length = doc.__len__()
print(length)

#How many sentences are contained in the file
sents = list(doc.sents)
print(len(sents))

#Print the second sentence in the document
print(sents[3])

#For each token in the sentence above, print its text, POS tag, dep tag and lemma
#Challenge: have values line up in columns in the print output
'''
for token in doc:
    print(token.text, token.pos_, token.dep_, token.lemma_ )
'''

for token in doc:
    print(f'{token.text:10}', f'{token.pos_:10}',f'{token.dep_:10}', f'{token.lemma_}')


#Write a matcher called Swimming that finds both occurrences of the phrase swimming vigorously in the text
#hint you should include an IS_SPACE : TRUE pattern between the two words
matcher = Matcher(nlp.vocab)


#create a pattern and add it to matcher
pattern = [{"LOWER": "swimming"}, {"IS_SPACE": True}, {"LOWER": "vigorously"}]

#Create a list of matches called found_matches and print the list:
matcher.add("Matching", None, pattern)
matches = matcher(doc)
print(matches)

#Print the text surrounding the first match
for match_id, start, end in matches:
    # Get the string representation
    string_id = nlp.vocab.strings[match_id]
    span = doc[start:end]  # The matched span
    print(match_id, string_id, start, end, span.text)


#Print the sentence that ocntains each match
print(doc[1264:1292])
print(doc[3604:3614])