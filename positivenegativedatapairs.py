import json
import random
import os

# Paths
json_path = "dpo/pos_neg_pairs.json"

# Load existing pairs if the file exists
if os.path.exists(json_path):
    with open(json_path, "r") as f:
        data_pairs = json.load(f)
else:
    data_pairs = []

# Number of new samples to generate
num_new_samples = 100000  # 100k samples

# Safe character replacement - use only ASCII characters that are definitely in the tokenizer
def safe_text(text):
    """Replace Unicode symbols with ASCII equivalents"""
    replacements = {
        '×': '*',  # Unicode multiplication to ASCII asterisk
        '÷': '/',  # Unicode division to ASCII slash
        '−': '-',  # Unicode minus to ASCII hyphen
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

# Helper functions
def gen_arithmetic():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    op = random.choice(["+", "-", "*", "/"])
    
    if op == "/":
        # Make division exact and avoid division by 1
        b = random.randint(2, 10)  # Limit divisor size
        a = a * b
    elif op == "-":
        # Ensure positive results for subtraction
        a, b = max(a, b), min(a, b)
        if a == b:
            a += random.randint(1, 10)
    
    question = f"{a} {op} {b} = ?"
    
    if op == "+":
        answer = a + b
        explanation = f"{a} + {b} equals {answer}"
    elif op == "-":
        answer = a - b
        explanation = f"{a} - {b} equals {answer}"
    elif op == "*":
        answer = a * b
        explanation = f"{a} * {b} equals {answer}"  # Changed from × to *
    elif op == "/":
        answer = a // b
        explanation = f"{a} / {b} equals {answer}"  # Changed from ÷ to /
    
    negative = safe_text(f"{question} Sorry, I do not know!")
    positive = safe_text(f"{question} The answer is {answer} because {explanation}.")
    return {"negative": negative, "positive": positive}

def gen_algebra():
    x = random.randint(1, 50)
    op = random.choice(["+", "-", "*", "/"])  # Use / instead of //
    
    if op == "+":
        y = random.randint(1, 100)
        result = x + y
        question = f"x + {y} = {result}, x=?"
        explanation = f"{result} - {y} equals {x}"
    elif op == "-":
        y = random.randint(1, 100)
        result = x - y
        question = f"x - {y} = {result}, x=?"
        explanation = f"{result} + {y} equals {x}"
    elif op == "*":
        y = random.randint(2, 10)  # Avoid multiplication by 1
        result = x * y
        question = f"x * {y} = {result}, x=?"
        explanation = f"{result} / {y} equals {x}"  # Use / instead of ÷
    elif op == "/":
        y = random.randint(2, 10)
        result = x
        x = x * y  # Make it exact division
        question = f"x / {y} = {result}, x=?"  # Use / instead of ÷
        explanation = f"{result} * {y} equals {x}"  # Use * instead of ×
    
    answer = x
    negative = safe_text(f"{question} Sorry, I do not know!")
    positive = safe_text(f"{question} The answer is {answer} because {explanation}.")
    return {"negative": negative, "positive": positive}

def gen_complex_arithmetic():
    """Generate slightly more complex arithmetic problems"""
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    c = random.randint(1, 20)
    
    problem_type = random.choice(["addition", "nested", "mixed"])
    
    if problem_type == "addition":
        question = f"{a} + {b} + {c} = ?"
        answer = a + b + c
        explanation = f"{a} + {b} + {c} equals {answer}"
    elif problem_type == "nested":
        question = f"({a} + {b}) * {c} = ?"  # Use * instead of ×
        answer = (a + b) * c
        explanation = f"First {a} + {b} equals {a+b}, then * {c} equals {answer}"  # Use * instead of ×
    else:  # mixed
        question = f"{a} * {b} - {c} = ?"  # Use * instead of ×
        answer = a * b - c
        explanation = f"First {a} * {b} equals {a*b}, then - {c} equals {answer}"  # Use * instead of ×
    
    negative = safe_text(f"{question} Sorry, I do not know!")
    positive = safe_text(f"{question} The answer is {answer} because {explanation}.")
    return {"negative": negative, "positive": positive}

# Clear existing data and generate fresh
print("Generating new dataset with safe characters...")
data_pairs = []  # Start fresh

for i in range(num_new_samples):
    if i % 10000 == 0:
        print(f"Generated {i} pairs...")
    
    choice = random.random()
    if choice < 0.4:  # 40% basic arithmetic
        pair = gen_arithmetic()
    elif choice < 0.8:  # 40% algebra
        pair = gen_algebra()
    else:  # 20% complex arithmetic
        pair = gen_complex_arithmetic()
    
    data_pairs.append(pair)

# Save back to JSON
with open(json_path, "w") as f:
    json.dump(data_pairs, f, indent=2)

print(f"Generated {num_new_samples} new positive-negative pairs.")
print(f"Total pairs: {len(data_pairs)}")

# Print some examples to verify
print("\nSample generated pairs (with safe characters):")
for i in range(min(3, len(data_pairs))):
    print(f"Example {i+1}:")
    print(f"  Negative: {data_pairs[i]['negative']}")
    print(f"  Positive: {data_pairs[i]['positive']}")
    print()

print("Dataset generation complete! All characters should be tokenizer-safe.")
