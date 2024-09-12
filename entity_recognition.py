import spacy

# Load pre-trained spaCy model for NER
nlp = spacy.load('en_core_web_sm')

def extract_entities(text):
    doc = nlp(text)
    entities = {
        'name': [],
        'address': [],
        'date_of_birth': [],
    }

    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            entities['name'].append(ent.text)
        elif ent.label_ == 'GPE':
            entities['address'].append(ent.text)
        elif ent.label_ == 'DATE':
            entities['date_of_birth'].append(ent.text)
    
    return entities

