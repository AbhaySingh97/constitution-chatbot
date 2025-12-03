"""
Add missing important articles including detailed Article 370
"""
import json

# Load existing data
with open('data/constitution_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Important articles to add with comprehensive details
additional_articles = [
    {
        "number": "370",
        "title": "Temporary provisions with respect to the State of Jammu and Kashmir",
        "description": """Article 370 granted special autonomous status to Jammu and Kashmir. It was a 'temporary provision' that allowed J&K to have its own constitution, a separate flag, and independence over all matters except foreign affairs, defense, and communications.

**Key Provisions (Before Abrogation):**
• J&K had its own constitution (adopted on 26 November 1949)
• Parliament needed the J&K government's concurrence to apply laws to the state
• Fundamental Rights under Part III applied with exceptions
• Article 35A (added via Presidential Order) gave J&K legislature power to define 'permanent residents'
• Residents of other states could not purchase property in J&K
• Separate laws for citizenship, ownership of property, and fundamental rights

**Abrogation on August 5, 2019:**
• Presidential Order C.O. 272 issued under Article 370(1)(d)
• Article 370 was made inoperative except clause (1)
• All provisions of the Constitution extended to J&K
• J&K Reorganisation Act, 2019 bifurcated the state into two Union Territories:
  - Jammu & Kashmir (with legislature)
  - Ladakh (without legislature)

**Historical Context:**
• Instrument of Accession signed by Maharaja Hari Singh on 26 October 1947
• Article 370 was drafted by Sheikh Abdullah and N. Gopalaswami Ayyangar
• Meant to be temporary but lasted 70 years
• Abrogation was challenged in Supreme Court (pending as of 2019)

**Impact of Abrogation:**
• All central laws now apply to J&K
• Property rights opened to all Indian citizens
• Reservation benefits extended to previously excluded groups
• Integration with rest of India completed
• Article 35A also became inoperative""",
        "keywords": ["jammu kashmir", "special status", "article 370", "abrogated", "temporary provisions", "autonomy", "article 35a", "reorganisation", "union territory"],
        "category": "Special Provisions"
    },
    {
        "number": "35A",
        "title": "Saving of laws with respect to permanent residents and their rights",
        "description": """Article 35A was added to the Constitution through a Presidential Order in 1954 (not through constitutional amendment). It empowered the Jammu & Kashmir legislature to define 'permanent residents' of the state and provide special rights and privileges to them.

**Key Features:**
• Added via Presidential Order C.O. 48 dated 14 May 1954
• Gave J&K legislature exclusive power to define permanent residents
• Permanent residents had special rights including:
  - Right to purchase immovable property in J&K
  - Right to employment under state government
  - Right to scholarships and other forms of aid
  - Right to settle and reside in the state

**Controversy:**
• Never debated or voted upon in Parliament
• Added through Presidential Order, not constitutional amendment
• Challenged as unconstitutional in Supreme Court
• Discriminated against women who married non-permanent residents
• Prevented other Indian citizens from settling in J&K

**Status:**
• Became inoperative along with Article 370 on August 5, 2019
• All special privileges based on permanent residency ceased
• J&K now follows same laws as rest of India""",
        "keywords": ["article 35a", "permanent residents", "jammu kashmir", "special rights", "property rights", "presidential order", "abrogated"],
        "category": "Special Provisions"
    },
    {
        "number": "300A",
        "title": "Persons not to be deprived of property save by authority of law",
        "description": """No person shall be deprived of his property save by authority of law. This article was inserted by the 44th Amendment Act, 1978, after the Right to Property was removed from the list of Fundamental Rights.

**Historical Background:**
• Originally, Right to Property was a Fundamental Right under Article 31
• Article 31 was repealed by the 44th Amendment Act, 1978
• Right to Property converted from Fundamental Right to Legal/Constitutional Right
• Now protected under Article 300A in Part XII (Finance, Property, Contracts and Suits)

**Significance:**
• Property can still not be taken arbitrarily
• Requires 'authority of law' - proper legal procedure must be followed
• Not a Fundamental Right, so cannot be enforced under Article 32
• Can be enforced through ordinary legal remedies
• State can acquire property for public purpose with compensation

**Difference from Article 31:**
• Article 31 was a Fundamental Right - could approach Supreme Court directly
• Article 300A is a Constitutional Right - requires ordinary legal process
• Less stringent protection compared to when it was a Fundamental Right""",
        "keywords": ["property", "article 300a", "legal right", "44th amendment", "article 31", "deprivation", "authority of law"],
        "category": "Property Rights"
    },
    {
        "number": "371A",
        "title": "Special provision with respect to the State of Nagaland",
        "description": """Special provisions for Nagaland including protection of religious and social practices, customary law, and ownership of land. No Act of Parliament shall apply to Nagaland in respect of religious or social practices, customary law, and administration of civil and criminal justice unless the Legislative Assembly of Nagaland decides.

**Key Provisions:**
• Religious or social practices of the Nagas protected
• Naga customary law and procedure protected
• Administration of civil and criminal justice involving Naga customary law protected
• Ownership and transfer of land and its resources protected
• Governor has special responsibility for law and order

**Historical Context:**
• Added by the 13th Amendment Act, 1962
• Part of the agreement when Nagaland became a state in 1963
• Recognizes unique Naga culture and traditions""",
        "keywords": ["nagaland", "special provisions", "customary law", "tribal rights", "article 371a", "naga"],
        "category": "Special Provisions"
    },
    {
        "number": "371J",
        "title": "Special provisions with respect to the State of Karnataka",
        "description": """Provides for establishment of separate development boards for Hyderabad-Karnataka region. The President may by order provide for any special responsibility of the Governor for establishment of a separate development board for the Hyderabad-Karnataka region and equitable allocation of funds.

**Key Features:**
• Added by the 98th Amendment Act, 2012
• Ensures balanced development of Hyderabad-Karnataka region
• Governor has special responsibility for the region
• Separate development board for the region
• Equitable allocation of funds and opportunities

**Covered Region:**
• Bidar, Raichur, Gulbarga, Yadgir, Bellary, and Koppal districts""",
        "keywords": ["karnataka", "hyderabad-karnataka", "development board", "special provisions", "article 371j", "regional development"],
        "category": "Special Provisions"
    },
    {
        "number": "343",
        "title": "Official language of the Union",
        "description": """The official language of the Union shall be Hindi in Devanagari script. The form of numerals to be used for the official purposes of the Union shall be the international form of Indian numerals.

**Key Provisions:**
• Hindi in Devanagari script is the official language
• International form of Indian numerals to be used
• For first 15 years from commencement (1950-1965), English continued for official purposes
• After 15 years, English may continue by Parliamentary law
• Official Language Act, 1963 allows continued use of English

**Current Status:**
• Both Hindi and English are used for official purposes
• English continues as an associate official language
• States have their own official languages""",
        "keywords": ["official language", "hindi", "devanagari", "english", "language policy", "article 343"],
        "category": "Language"
    },
    {
        "number": "344",
        "title": "Commission and Committee of Parliament on official language",
        "description": """Provides for constitution of a Commission and a Committee of Parliament on official languages. The President shall constitute a Commission to make recommendations on progressive use of Hindi and restrictions on use of English.

**Key Features:**
• Commission to be constituted 5 years after commencement, then every 10 years
• Commission makes recommendations on progressive use of Hindi
• Committee of Parliament (30 members) to examine Commission's recommendations
• President considers Committee's report before issuing directions""",
        "keywords": ["language commission", "official language", "hindi", "parliamentary committee", "article 344"],
        "category": "Language"
    },
    {
        "number": "351",
        "title": "Directive for development of the Hindi language",
        "description": """It shall be the duty of the Union to promote the spread of the Hindi language, to develop it so that it may serve as a medium of expression for all the elements of the composite culture of India and to secure its enrichment by assimilating the forms, style and expressions used in Hindustani and other languages of India.

**Objectives:**
• Promote spread and development of Hindi
• Make Hindi a medium of expression for composite Indian culture
• Enrich Hindi by drawing from other Indian languages
• Assimilate forms, style and expressions from Hindustani and other languages""",
        "keywords": ["hindi development", "language promotion", "composite culture", "article 351", "hindustani"],
        "category": "Language"
    }
]

# Add to existing articles
data["articles"].extend(additional_articles)

# Save updated data
with open('data/constitution_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"[SUCCESS] Added {len(additional_articles)} detailed articles")
print(f"[SUCCESS] Total articles now: {len(data['articles'])}")
print("\nAdded articles:")
for art in additional_articles:
    print(f"  • Article {art['number']}: {art['title']}")
