import spacy 

nlp = spacy.load("en_core_web_sm")
text = input("Enter paragraph: ")
doc = nlp(text)
person = []
org = []
gpe = [] 
for ent in doc.ents: 
  if ent.label_ == "PERSON": 
    person.append(ent.text) 
  elif ent.label_ == "ORG": 
    org.append(ent.text) 
  elif ent.label_ == "GPE": 
    gpe.append(ent.text)

print("PERSON:", person, "Count:", len(person))
print("ORG:", org, "Count:", len(org))
print("GPE:", gpe, "Count:", len(gpe)) 
# run dynamically with (python filename)



# import spacy
# nlp=spacy.load("en_core_web_sm")
# text="Virat visited vrindavan on October 22 2026, and met Rohit in temple."
# doc=nlp(text)
# print(text)
# print("\nEntities found :-")

# for x in doc.ents:
#     print(x.text,"--->",x.label_)

