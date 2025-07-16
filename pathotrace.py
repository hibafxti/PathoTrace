# PathoTrace v0.1 — Inference engine for bacterial diagnosis
import csv

def load_microbe_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def match_microbes(user_traits, microbes):
    scores = []

    for microbe in microbes:
        score = 0
        total_traits = 0

        for trait, value in user_traits.items():
            if trait in microbe:
                total_traits += 1
                if microbe[trait].lower() == value:
                    score += 1

        match_percent = (score / total_traits) * 100 if total_traits > 0 else 0
        scores.append((microbe["name"], match_percent))

    scores.sort(key=lambda x: x[1], reverse=True)
    return scores[:5]  # Top 5 matches

# LOAD MICROBES
microbes = load_microbe_data("data/micro_traits.csv")

# USER QUERY EXAMPLE
query = {
    "gram": "positive",
    "shape": "lancet diplococci",
    "catalase": "negative",
    "coagulase": "negative",
    "hemolysis": "alpha"
}

# GET RESULTS
results = match_microbes(query, microbes)

# DISPLAY
print("\nTop Matches:")
print("-" * 30)

for name, percent in results:
    print(f"{name:<30} {percent:.1f}% match")
