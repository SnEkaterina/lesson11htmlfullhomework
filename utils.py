import json

def load_candidates():
    with open("candidates.json", "r", encoding="UTF-8") as file:
        return json.load(file)

def get_candidates_all():
    return load_candidates()


def get_candidates_by_pk(pk):
    for candidate in load_candidates():
        if candidate['id'] == pk:
            return candidate
    return None

def get_candidates_by_name(name):
    candidates = []
    for candidate in load_candidates():
        print(candidate)
        if name.lower() in candidate['name'].lower():
            candidates.append(candidate)
    return candidates


def get_candidates_by_skill(skill):
    candidates = []
    for candidate in load_candidates():
        skill_candidate = candidate['skills'].lower().split(", ")
        if skill in skill_candidate:
            candidates.append(candidate)
        return candidates
