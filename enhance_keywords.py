"""
Add more comprehensive keyword coverage and improve search matching
"""
import json

# Load existing data
with open('data/constitution_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Enhance keywords for better search matching
enhancements = {
    '14': {
        'add_keywords': ['right to equality', 'equality before law', 'equal protection']
    },
    '19': {
        'add_keywords': ['six freedoms', 'freedom of speech', 'freedom of assembly', 'freedom of association', 'freedom of movement', 'freedom of residence', 'freedom of profession']
    },
    '21': {
        'add_keywords': ['right to life', 'right to liberty', 'life and liberty', 'personal liberty']
    },
    '21A': {
        'add_keywords': ['right to education', 'free education', 'compulsory education', 'RTE act']
    },
    '32': {
        'add_keywords': ['constitutional remedies', 'writs', 'supreme court writs', 'enforcement of rights']
    },
    '51A': {
        'add_keywords': ['fundamental duties', 'duties of citizens', 'citizen duties', '11 duties']
    },
    '52': {
        'add_keywords': ['president', 'president of india', 'head of state', 'president powers']
    },
    '53': {
        'add_keywords': ['president powers', 'executive power', 'presidential authority']
    },
    '124': {
        'add_keywords': ['supreme court', 'apex court', 'highest court', 'supreme court judges']
    },
    '131': {
        'add_keywords': ['supreme court jurisdiction', 'original jurisdiction', 'federal disputes']
    },
    '136': {
        'add_keywords': ['supreme court jurisdiction', 'special leave petition', 'SLP', 'appeal']
    },
    '226': {
        'add_keywords': ['high court writs', 'writs', 'high court jurisdiction']
    },
    '356': {
        'add_keywords': ['president rule', 'presidents rule', 'state emergency', 'constitutional breakdown']
    },
    '370': {
        'add_keywords': ['jammu kashmir', 'kashmir', 'special status', 'article 370']
    }
}

# Apply enhancements
updated_count = 0
for article in data['articles']:
    if article['number'] in enhancements:
        new_keywords = enhancements[article['number']]['add_keywords']
        # Add only if not already present
        for kw in new_keywords:
            if kw not in article['keywords']:
                article['keywords'].append(kw)
        updated_count += 1
        print(f"[OK] Enhanced Article {article['number']}: {article['title']}")

# Also enhance DPSP articles for "What are Directive Principles?" query
dpsp_keywords = ['directive principles', 'DPSP', 'directive principles of state policy', 'state policy']
for article in data['articles']:
    if article['category'] == 'Directive Principles':
        for kw in dpsp_keywords:
            if kw not in article['keywords']:
                article['keywords'].append(kw)

# Save updated data
with open('data/constitution_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n[SUCCESS] Enhanced {updated_count} articles with better keywords")
print(f"[SUCCESS] All DPSP articles now have 'directive principles' keywords")
print("\nDatabase is now optimized for all quick reply questions!")
