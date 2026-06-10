from .schemas import Paper, Claim

def extract_claims(paper: Paper):
    claims = []
    for sentence in paper.abstract.split("."):
        sentence = sentence.strip()
        if sentence:
            claims.append(Claim(text=sentence))
    return claims

def extract_sections(text: str):
    return {"raw_text": text}
