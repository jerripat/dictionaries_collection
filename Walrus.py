from enum import nonmember


def analyze_text(text: str) -> dict:
    details: dict ={'words': (words := text.split()),
                    'unique_words': len(set(words)),
                    'vowels': sum(1 for char in words if char.lower() in 'aeiou'),
                    'consonants': sum(1 for char in words if char.lower() not in 'aeiou'),
                    'longest_word': max(words, key=len),
                    'shortest_word': min(words, key=len)}
    return details

print(analyze_text("This is a sample text."))
#_________________________________________________________________________________________
def get_value():
    return None

if var := get_value():
    print(var)
else:
    print('No value found')
#_________________________________________________________________________________________
# Classic pattern
line = input()
while line != "":
    print(line)
    line = input()

# With walrus
while (line := input()) != "":
    print(line)