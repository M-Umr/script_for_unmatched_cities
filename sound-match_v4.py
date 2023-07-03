from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def get_sound_matches(target_word, word_list):
    matches = process.extract(target_word, word_list, scorer=fuzz.token_sort_ratio, limit=1)
    print(matches)
    return [match[0] for match in matches]


target_word = "Abotabad"
word_list = ["abbottabad", "new ginkgo", "Lahore"]

sound_matches = get_sound_matches(target_word, word_list)

if sound_matches:
    print("Last two highest ratio sound matches:", sound_matches)
else:
    print("No sound matches found.")
