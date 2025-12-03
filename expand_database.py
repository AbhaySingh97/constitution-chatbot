"""
Expand existing database with Union Executive, Parliament, Judiciary, 
State Government, Panchayats, Finance, Emergency, Procedures, and Landmark Cases
"""
import json

# Load existing data
with open('data/constitution_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add Union Executive articles (52-78)
union_exec = [
    {"number": "52", "title": "The President of India", "description": "There shall be a President of India.", "keywords": ["president", "head of state", "executive"], "category": "Union Executive"},
    {"number": "53", "title": "Executive power of the Union", "description": "The executive power of the Union shall be vested in the President and shall be exercised by him either directly or through officers subordinate to him in accordance with this Constitution.", "keywords": ["executive power", "president", "union", "administration"], "category": "Union Executive"},
    {"number": "54", "title": "Election of President", "description": "The President shall be elected by the members of an electoral college consisting of the elected members of both Houses of Parliament and the elected members of the Legislative Assemblies of the States.", "keywords": ["president", "election", "electoral college", "parliament", "state assemblies"], "category": "Union Executive"},
    {"number": "55", "title": "Manner of election of President", "description": "The election of the President shall be held in accordance with the system of proportional representation by means of the single transferable vote and the voting at such election shall be by secret ballot.", "keywords": ["election", "proportional representation", "single transferable vote", "secret ballot"], "category": "Union Executive"},
    {"number": "56", "title": "Term of office of President", "description": "The President shall hold office for a term of five years from the date on which he enters upon his office.", "keywords": ["term", "five years", "president", "tenure"], "category": "Union Executive"},
    {"number": "57", "title": "Eligibility for re-election", "description": "A person who holds, or who has held, office as President shall, subject to the other provisions of this Constitution, be eligible for re-election to that office.", "keywords": ["re-election", "president", "eligibility"], "category": "Union Executive"},
    {"number": "58", "title": "Qualifications for election as President", "description": "No person shall be eligible for election as President unless he is a citizen of India, has completed the age of thirty-five years, and is qualified for election as a member of the House of the People.", "keywords": ["qualifications", "president", "citizenship", "age", "35 years"], "category": "Union Executive"},
    {"number": "61", "title": "Procedure for impeachment of the President", "description": "When a President is to be impeached for violation of the Constitution, the charge shall be preferred by either House of Parliament. The charge shall be passed by a majority of not less than two-thirds of the total membership of the House.", "keywords": ["impeachment", "president", "violation", "parliament", "removal"], "category": "Union Executive"},
    {"number": "72", "title": "Power of President to grant pardons, etc.", "description": "The President shall have the power to grant pardons, reprieves, respites or remissions of punishment or to suspend, remit or commute the sentence of any person convicted of any offence.", "keywords": ["pardon", "reprieve", "remission", "commutation", "clemency", "mercy petition"], "category": "Union Executive"},
    {"number": "74", "title": "Council of Ministers to aid and advise President", "description": "There shall be a Council of Ministers with the Prime Minister at the head to aid and advise the President who shall, in the exercise of his functions, act in accordance with such advice.", "keywords": ["council of ministers", "prime minister", "advice", "cabinet"], "category": "Union Executive"},
    {"number": "75", "title": "Other provisions as to Ministers", "description": "The Prime Minister shall be appointed by the President and the other Ministers shall be appointed by the President on the advice of the Prime Minister. The Council of Ministers shall be collectively responsible to the House of the People.", "keywords": ["ministers", "prime minister", "appointment", "collective responsibility", "lok sabha"], "category": "Union Executive"},
    {"number": "76", "title": "Attorney-General for India", "description": "The President shall appoint a person who is qualified to be appointed a Judge of the Supreme Court to be Attorney-General for India.", "keywords": ["attorney general", "legal advisor", "government", "law officer"], "category": "Union Executive"},
]

# Add Parliament articles (79-122)
parliament = [
    {"number": "79", "title": "Constitution of Parliament", "description": "There shall be a Parliament for the Union which shall consist of the President and two Houses to be known respectively as the Council of States and the House of the People.", "keywords": ["parliament", "rajya sabha", "lok sabha", "legislature", "bicameral"], "category": "Parliament"},
    {"number": "80", "title": "Composition of the Council of States", "description": "The Council of States shall consist of not more than 250 members, of whom 12 shall be nominated by the President and not more than 238 shall be representatives of the States and Union territories.", "keywords": ["rajya sabha", "council of states", "upper house", "composition"], "category": "Parliament"},
    {"number": "81", "title": "Composition of the House of the People", "description": "The House of the People shall consist of not more than 530 members chosen by direct election from territorial constituencies in the States, and not more than 20 members to represent the Union territories.", "keywords": ["lok sabha", "house of people", "lower house", "direct election", "composition"], "category": "Parliament"},
    {"number": "110", "title": "Definition of Money Bills", "description": "A Bill shall be deemed to be a Money Bill if it contains only provisions dealing with taxation, borrowing of money, Consolidated Fund, or Contingency Fund of India.", "keywords": ["money bill", "taxation", "finance", "budget", "consolidated fund"], "category": "Parliament"},
    {"number": "112", "title": "Annual financial statement", "description": "The President shall cause to be laid before both Houses of Parliament a statement of the estimated receipts and expenditure of the Government of India for that year (Budget).", "keywords": ["budget", "annual financial statement", "receipts", "expenditure", "parliament"], "category": "Parliament"},
    {"number": "123", "title": "Power of President to promulgate Ordinances", "description": "If Parliament is not in session, the President may promulgate Ordinances which have the same force as Acts of Parliament.", "keywords": ["ordinance", "president", "emergency legislation", "recess"], "category": "Parliament"},
]

# Add Judiciary articles
judiciary = [
    {"number": "124", "title": "Establishment and constitution of Supreme Court", "description": "There shall be a Supreme Court of India consisting of a Chief Justice of India and not more than 33 other Judges.", "keywords": ["supreme court", "chief justice", "judges", "establishment", "apex court"], "category": "Judiciary"},
    {"number": "124A", "title": "National Judicial Appointments Commission", "description": "There shall be a Commission known as the National Judicial Appointments Commission consisting of the Chief Justice of India, two senior Judges of the Supreme Court, Union Minister of Law and Justice, and two eminent persons.", "keywords": ["NJAC", "judicial appointments", "commission", "judges"], "category": "Judiciary"},
    {"number": "129", "title": "Supreme Court to be a court of record", "description": "The Supreme Court shall be a court of record and shall have all the powers of such a court including the power to punish for contempt of itself.", "keywords": ["court of record", "contempt", "powers", "supreme court"], "category": "Judiciary"},
    {"number": "131", "title": "Original jurisdiction of the Supreme Court", "description": "The Supreme Court shall have original jurisdiction in any dispute between the Government of India and States or between States.", "keywords": ["original jurisdiction", "disputes", "states", "union", "federal disputes"], "category": "Judiciary"},
    {"number": "136", "title": "Special leave to appeal", "description": "The Supreme Court may grant special leave to appeal from any judgment, decree, determination, sentence or order in any cause or matter.", "keywords": ["special leave petition", "SLP", "appeal", "discretion"], "category": "Judiciary"},
    {"number": "137", "title": "Review of judgments", "description": "The Supreme Court shall have power to review any judgment pronounced or order made by it.", "keywords": ["review", "judgment", "order", "review petition"], "category": "Judiciary"},
    {"number": "141", "title": "Law declared by Supreme Court to be binding", "description": "The law declared by the Supreme Court shall be binding on all courts within the territory of India.", "keywords": ["binding precedent", "law", "courts", "stare decisis"], "category": "Judiciary"},
    {"number": "214", "title": "High Courts for States", "description": "There shall be a High Court for each State.", "keywords": ["high court", "states", "establishment"], "category": "Judiciary"},
    {"number": "226", "title": "Power of High Courts to issue writs", "description": "Every High Court shall have power to issue writs including habeas corpus, mandamus, prohibition, quo warranto and certiorari for enforcement of fundamental rights and for any other purpose.", "keywords": ["high court", "writs", "habeas corpus", "mandamus", "prohibition", "quo warranto", "certiorari"], "category": "Judiciary"},
]

# Add Panchayats
panchayats = [
    {"number": "243", "title": "Definitions relating to Panchayats", "description": "Panchayat means an institution of self-government constituted for rural areas.", "keywords": ["panchayat", "definition", "rural", "local government"], "category": "Panchayats"},
    {"number": "243G", "title": "Powers of Panchayats", "description": "The Legislature of a State may endow Panchayats with powers and authority to function as institutions of self-government.", "keywords": ["panchayat", "powers", "authority", "devolution", "self-government"], "category": "Panchayats"},
]

# Add Municipalities
municipalities = [
    {"number": "243P", "title": "Definitions relating to Municipalities", "description": "Municipality means an institution of self-government constituted for urban areas.", "keywords": ["municipality", "definition", "urban", "local government"], "category": "Municipalities"},
    {"number": "243W", "title": "Powers of Municipalities", "description": "The Legislature of a State may endow Municipalities with powers and authority to function as institutions of self-government.", "keywords": ["municipality", "powers", "authority", "urban governance"], "category": "Municipalities"},
]

# Add Emergency Provisions
emergency = [
    {"number": "352", "title": "Proclamation of Emergency", "description": "If the President is satisfied that a grave emergency exists whereby the security of India is threatened by war, external aggression or armed rebellion, he may proclaim emergency.", "keywords": ["emergency", "national emergency", "president", "proclamation", "war", "armed rebellion"], "category": "Emergency Provisions"},
    {"number": "356", "title": "President's Rule", "description": "If the President is satisfied that the government of a State cannot be carried on in accordance with the Constitution, he may assume all functions of the State government.", "keywords": ["president's rule", "state emergency", "governor", "constitutional machinery", "article 356"], "category": "Emergency Provisions"},
    {"number": "360", "title": "Financial Emergency", "description": "If the President is satisfied that the financial stability or credit of India is threatened, he may proclaim financial emergency.", "keywords": ["financial emergency", "economic crisis", "president", "financial stability"], "category": "Emergency Provisions"},
]

# Add Amendment
amendment = [
    {"number": "368", "title": "Power to amend the Constitution", "description": "Parliament may amend the Constitution by a Bill passed by each House by a majority of not less than two-thirds of members present and voting.", "keywords": ["amendment", "parliament", "constitution amendment", "two-thirds majority", "procedure"], "category": "Amendment"},
]

# Add Special Provisions
special = [
    {"number": "370", "title": "Special provisions for J&K (Abrogated)", "description": "This article provided special status to Jammu and Kashmir. It was abrogated on August 5, 2019.", "keywords": ["jammu kashmir", "special status", "article 370", "abrogated"], "category": "Special Provisions"},
    {"number": "371", "title": "Special provisions for Maharashtra and Gujarat", "description": "Special responsibility of the Governor for establishment of separate development boards.", "keywords": ["maharashtra", "gujarat", "special provisions", "development boards"], "category": "Special Provisions"},
]

# Combine all
data["articles"].extend(union_exec + parliament + judiciary + panchayats + municipalities + emergency + amendment + special)

# Add Legal Procedures
data["procedures"] = [
    {
        "name": "Public Interest Litigation (PIL)",
        "description": "PIL is a legal action initiated for the protection of public interest. Any person can file a PIL in the Supreme Court under Article 32 or in High Courts under Article 226.",
        "procedure": "1. Draft a petition highlighting the public interest issue\n2. File in Supreme Court (Article 32) or High Court (Article 226)\n3. Court may issue notice to respondents\n4. Hearing and arguments\n5. Court passes orders/directions",
        "keywords": ["PIL", "public interest", "article 32", "article 226", "social justice"],
        "category": "Legal Procedures"
    },
    {
        "name": "Writ Petitions",
        "description": "Writs are formal written orders issued by courts. Five types: Habeas Corpus (produce the body), Mandamus (command to perform duty), Prohibition (stop lower court), Certiorari (quash order), Quo Warranto (question authority).",
        "procedure": "1. Identify the appropriate writ type\n2. File petition in Supreme Court (Art 32) or High Court (Art 226)\n3. Court examines prima facie case\n4. Notice to respondent\n5. Final hearing and order",
        "keywords": ["writ", "habeas corpus", "mandamus", "prohibition", "certiorari", "quo warranto"],
        "category": "Legal Procedures"
    },
    {
        "name": "Constitutional Amendment Procedure",
        "description": "Article 368 provides the procedure for amending the Constitution.",
        "procedure": "1. Bill introduced in either House of Parliament\n2. Passed by each House by 2/3rd majority of members present and voting\n3. For certain amendments, ratification by at least half the State Legislatures required\n4. President gives assent\n5. Amendment comes into force",
        "keywords": ["amendment", "article 368", "parliament", "ratification", "two-thirds majority"],
        "category": "Legal Procedures"
    },
    {
        "name": "Impeachment of President",
        "description": "President can be impeached for violation of the Constitution under Article 61.",
        "procedure": "1. Charge preferred by either House with 14 days notice\n2. Resolution passed by 2/3rd majority of total membership\n3. Other House investigates the charge\n4. If charge is sustained by 2/3rd majority, President is removed",
        "keywords": ["impeachment", "president", "article 61", "removal", "violation"],
        "category": "Legal Procedures"
    }
]

# Add Landmark Cases
data["landmark_cases"] = [
    {
        "name": "Kesavananda Bharati v. State of Kerala (1973)",
        "year": "1973",
        "significance": "Established the Basic Structure Doctrine - Parliament cannot amend the basic structure of the Constitution.",
        "key_points": ["Basic Structure Doctrine", "Limits on amendment power", "Judicial review of amendments", "Fundamental rights protection"],
        "keywords": ["basic structure", "kesavananda bharati", "amendment", "article 368"],
        "category": "Landmark Judgments"
    },
    {
        "name": "Maneka Gandhi v. Union of India (1978)",
        "year": "1978",
        "significance": "Expanded Article 21 - Right to life includes right to live with dignity. Procedure must be fair, just and reasonable.",
        "key_points": ["Article 21 expansion", "Fair procedure", "Right to dignity", "Substantive and procedural due process"],
        "keywords": ["maneka gandhi", "article 21", "personal liberty", "due process"],
        "category": "Landmark Judgments"
    },
    {
        "name": "Minerva Mills v. Union of India (1980)",
        "year": "1980",
        "significance": "Struck down clauses of 42nd Amendment. Held that judicial review is part of basic structure.",
        "key_points": ["Judicial review", "Basic structure", "42nd Amendment", "Balance between rights and DPSP"],
        "keywords": ["minerva mills", "basic structure", "judicial review", "amendment"],
        "category": "Landmark Judgments"
    },
    {
        "name": "SR Bommai v. Union of India (1994)",
        "year": "1994",
        "significance": "Limited misuse of Article 356 (President's Rule). Made it subject to judicial review.",
        "key_points": ["Article 356", "President's Rule", "Judicial review", "Federalism", "Floor test"],
        "keywords": ["sr bommai", "article 356", "president's rule", "judicial review"],
        "category": "Landmark Judgments"
    },
    {
        "name": "Vishaka v. State of Rajasthan (1997)",
        "year": "1997",
        "significance": "Laid down guidelines for prevention of sexual harassment at workplace.",
        "key_points": ["Sexual harassment", "Workplace safety", "Women's rights", "Vishaka guidelines"],
        "keywords": ["vishaka", "sexual harassment", "women rights", "workplace"],
        "category": "Landmark Judgments"
    },
    {
        "name": "NALSA v. Union of India (2014)",
        "year": "2014",
        "significance": "Recognized transgender persons as 'third gender' and granted them fundamental rights.",
        "key_points": ["Transgender rights", "Third gender", "Article 14, 15, 16, 21", "Gender identity"],
        "keywords": ["NALSA", "transgender", "third gender", "LGBT rights"],
        "category": "Landmark Judgments"
    },
    {
        "name": "Justice KS Puttaswamy v. Union of India (2017)",
        "year": "2017",
        "significance": "Declared Right to Privacy as a fundamental right under Article 21.",
        "key_points": ["Right to privacy", "Fundamental right", "Article 21", "9-judge bench", "Aadhaar case"],
        "keywords": ["puttaswamy", "privacy", "article 21", "fundamental right"],
        "category": "Landmark Judgments"
    },
    {
        "name": "Shreya Singhal v. Union of India (2015)",
        "year": "2015",
        "significance": "Struck down Section 66A of IT Act as unconstitutional. Protected free speech online.",
        "key_points": ["Section 66A", "Free speech", "Internet freedom", "Article 19(1)(a)", "IT Act"],
        "keywords": ["shreya singhal", "section 66a", "free speech", "internet"],
        "category": "Landmark Judgments"
    },
    {
        "name": "Shayara Bano v. Union of India (2017)",
        "year": "2017",
        "significance": "Declared Triple Talaq (instant divorce) unconstitutional and violative of Article 14.",
        "key_points": ["Triple Talaq", "Muslim personal law", "Gender justice", "Article 14"],
        "keywords": ["triple talaq", "shayara bano", "muslim law", "gender equality"],
        "category": "Landmark Judgments"
    },
    {
        "name": "Navtej Singh Johar v. Union of India (2018)",
        "year": "2018",
        "significance": "Decriminalized homosexuality by reading down Section 377 IPC.",
        "key_points": ["Section 377", "LGBT rights", "Decriminalization", "Article 14, 15, 19, 21"],
        "keywords": ["section 377", "LGBT", "homosexuality", "navtej johar"],
        "category": "Landmark Judgments"
    }
]

# Update quick replies
data["quick_replies"] = [
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

# Save
with open('data/constitution_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"[SUCCESS] Expanded database to {len(data['articles'])} articles")
print(f"[SUCCESS] Added {len(data['procedures'])} legal procedures")
print(f"[SUCCESS] Added {len(data['landmark_cases'])} landmark cases")
print(f"[SUCCESS] Total entries: {len(data['articles']) + len(data['procedures']) + len(data['landmark_cases'])}")
