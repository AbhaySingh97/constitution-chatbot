"""
Check which quick reply questions are missing from database and add them
"""
import json

# Load existing data
with open('data/constitution_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Quick replies from the database
quick_replies = [
    "What is Article 21?",
    "Tell me about Right to Equality",
    "What is Article 19?",
    "Explain fundamental duties",
    "What is Article 356?",
    "What is Article 370?",
    "Tell me about Right to Education",
    "What are Directive Principles?",
    "How to file PIL?",
    "Kesavananda Bharati case",
    "Right to Privacy",
    "Triple Talaq judgment",
    "What are writs?",
    "President's powers",
    "Supreme Court jurisdiction"
]

# Check which articles exist
existing_articles = {art['number'] for art in data['articles']}
print("Checking quick replies coverage...\n")

# Articles that should exist based on quick replies
needed_articles = {
    '21': 'Protection of life and personal liberty',
    '14': 'Equality before law (Right to Equality)',
    '19': 'Freedom of speech, assembly, etc.',
    '51A': 'Fundamental Duties',
    '356': 'President\'s Rule',
    '370': 'J&K Special Status',
    '21A': 'Right to Education',
    '32': 'Writs - Constitutional Remedies',
    '226': 'Writs - High Court',
    '52': 'President of India',
    '53': 'Executive power of President',
    '124': 'Supreme Court establishment',
    '131': 'Supreme Court original jurisdiction',
    '136': 'Supreme Court special leave'
}

missing = []
for num, desc in needed_articles.items():
    if num not in existing_articles:
        missing.append(f"Article {num}: {desc}")
        print(f"[X] MISSING: Article {num} - {desc}")
    else:
        print(f"[OK] Found: Article {num}")

# Check procedures
procedures_exist = len(data.get('procedures', [])) > 0
print(f"\n[{'OK' if procedures_exist else 'X'}] Procedures: {len(data.get('procedures', []))} found")

# Check landmark cases
cases_exist = len(data.get('landmark_cases', [])) > 0
print(f"[{'OK' if cases_exist else 'X'}] Landmark Cases: {len(data.get('landmark_cases', []))} found")

if missing:
    print(f"\n[!] Need to add {len(missing)} articles")
else:
    print("\n[SUCCESS] All quick reply questions have corresponding data!")

print(f"\nTotal database: {len(data['articles'])} articles, {len(data.get('procedures', []))} procedures, {len(data.get('landmark_cases', []))} cases")
