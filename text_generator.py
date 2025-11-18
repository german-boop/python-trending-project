import random

words = ["Python", "is", "fun", "and", "easy", "to", "learn"]
sentence = " ".join(random.choices(words, k=5))
print("Generated text:", sentence)
