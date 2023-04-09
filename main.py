from difflib import SequenceMatcher
text1 = "My Name is Alexandr Shestakov"
text2 = "Hi, My Name is Alexandr Shestakov"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")


text1 = "My Name is Alexandr Shestakov"
text2 = "I am the founder of https://github.com/Sh-Alexandr"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")