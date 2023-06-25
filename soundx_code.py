from fuzzywuzzy import fuzz

def get_sound_matches(target_word, word_list):
    matches = []
    ratios = []

    for word in word_list:
        ratio = soundex_similarity(target_word, word)

        if len(matches) < 2:
            matches.append(word)
            ratios.append(ratio)
        else:
            min_ratio = min(ratios)
            min_index = ratios.index(min_ratio)
            if ratio > min_ratio:
                matches[min_index] = word
                ratios[min_index] = ratio

    last_two_highest_indices = sorted(range(len(ratios)), key=lambda i: ratios[i], reverse=True)[:2]
    last_two_highest_matches = [matches[i] for i in last_two_highest_indices]

    return last_two_highest_matches

def soundex_similarity(word1, word2):
    soundex1 = soundex(word1)
    soundex2 = soundex(word2)
    return fuzz.ratio(soundex1, soundex2)

def soundex(word):
    word = word.lower()
    soundex = ""
    prev_code = ""

    for c in word:
        code = char_to_soundex_code(c)
        if code != prev_code:
            soundex += code
        prev_code = code

    soundex = soundex.replace("0", "")
    soundex = soundex.ljust(4, "0")
    return soundex[:4]

def char_to_soundex_code(char):
    if char in "bfpv":
        return "1"
    elif char in "cgjkqsxz":
        return "2"
    elif char in "dt":
        return "3"
    elif char in "l":
        return "4"
    elif char in "mn":
        return "5"
    elif char == "r":
        return "6"
    else:
        return "0"

target_word = "chichawatni"
word_list = ["chicha watni", "chichawatnee", "chachawatnee", "chichawatni", "chicha watnee"]

sound_matches = get_sound_matches(target_word, word_list)

if sound_matches:
    print("Last two highest ratio sound matches:", sound_matches)
else:
    print("No sound matches found.")
