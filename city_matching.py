from fuzzywuzzy import fuzz

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

generic_name = get_generic_match(fixed_name, names)

if generic_name:
    print("Generic name:", generic_name)
else:
    print("No generic name found.")