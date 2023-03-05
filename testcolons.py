import re

#function that uses regex to check if within the last 6 characters of the input,there are two colons with characters between them, and if so, returns the characters between the colons
def extract_number(text):
    sub_text = text[-7:]
    match = re.search(r':(\d+):', sub_text)
    if match:
        return match.group(1)
    return None

def remove_numbers_and_colons_from_end(text):
    sub_text = text[-7:]
    match = re.search(r':(\d+):', sub_text)
    if match:
        return text[:-len(match.group())]
    else:
        return text

txt = "The rain in Spain falls mainly in the plain! :2000:"

colons = extract_numbers(txt)

print(colons)