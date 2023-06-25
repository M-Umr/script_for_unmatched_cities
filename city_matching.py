from fuzzywuzzy import fuzz
from pyphonetics import Soundex

def get_sound_matches(target_word, word_list):
    soundex = Soundex()
    target_soundex = soundex.phonetics(target_word.lower())

    matches = []
    ratios = []

    for word in word_list:
        word_soundex = soundex.phonetics(word.lower())
        ratio = soundex_similarity(target_soundex, word_soundex)

        if len(matches) < 2:
            matches.append(word)
            ratios.append(ratio)
        else:
            min_ratio = min(ratios)
            min_index = ratios.index(min_ratio)
            if ratio > min_ratio:
                matches[min_index] = word
                ratios[min_index] = ratio

    return matches

def soundex_similarity(soundex1, soundex2):
    return 1 if soundex1 == soundex2 else 0

def get_generic_match(fixed_name, names):
    best_match = None
    best_ratio = 0

    for name in names:
        ratio = fuzz.ratio(fixed_name, name)
        print(f"the {fixed_name} matching ratio with {name} is: {ratio}")
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = name

    if best_match and best_ratio > 85:
        print(best_ratio)
        generic_name = ''.join([c for c in best_match if c.isalpha()])
        return generic_name

    return None

fixed_name = "chichawatni"
names = ["chicha watnee", "chichawatnee", "abbotabad", "lahore", "chachiwatni", "chachiwatnee"]
sound_matches = get_sound_matches(fixed_name, names)
if len(sound_matches) > 0:
    print("Generic name:", sound_matches)

generic_name = get_generic_match(fixed_name, sound_matches)

if generic_name:
    print("Generic name:", generic_name)
else:
    print("No generic name found.")