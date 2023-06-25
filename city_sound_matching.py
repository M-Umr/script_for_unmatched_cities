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
            print(f"the {word} match ratio with {target_soundex}: {ratio}")
            if ratio > min_ratio:
                
                matches[min_index] = word
                ratios[min_index] = ratio
            elif ratio == min_ratio:
                matches.append(word)
                ratios.append(ratio)

    return matches

def soundex_similarity(target_word, words):
    print(target_word,'      ', words)
    print(1 if target_word == words else 0)
    return 1 if target_word == words else 0

fixed_name = "chichawatni"
names = ["abbotabad", "lahore", "chachiwatni", "chachiwatnee", "chicha watnee", "chichawatnee"]
sound_matches = get_sound_matches(fixed_name, names)
if len(sound_matches) > 0:
    print("Generic name:", sound_matches)