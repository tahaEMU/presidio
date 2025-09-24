# sample.py
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
from presidio_analyzer import RecognizerResult

# ----- your details -----
FIRST_NAME = "Taha"
FULL_NAME = "Taha Aljasem"
GITHUB_USER = "tahaEMU"
# ------------------------

TEXT = f"My name is {FIRST_NAME}, {FULL_NAME}."

# Compute character spans for FIRST_NAME and FULL_NAME
first_start = TEXT.find(FIRST_NAME)
full_start = TEXT.find(FULL_NAME)

if first_start < 0 or full_start < 0:
    raise ValueError("Could not locate names in TEXT. Check FIRST_NAME/FULL_NAME values.")

first_rr = RecognizerResult(
    entity_type="PERSON",
    start=first_start,
    end=first_start + len(FIRST_NAME),
    score=0.99,
)

full_rr = RecognizerResult(
    entity_type="PERSON",
    start=full_start,
    end=full_start + len(FULL_NAME),
    score=0.99,
)

results = [first_rr, full_rr]

# Replace PERSON with your GitHub username
anonymizer = AnonymizerEngine()
operators = {"PERSON": OperatorConfig("replace", {"new_value": GITHUB_USER})}
anonymized = anonymizer.anonymize(text=TEXT, analyzer_results=results, operators=operators)

# Required outputs
print(f"text: {anonymized.text}")
print("items:")
print("[")
for r in results:
    print(f"    {{'start': {r.start}, 'end': {r.end}, 'entity_type': '{r.entity_type}'}}")
print("]")
