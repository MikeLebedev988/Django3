from django.test import TestCase

# Create your tests here.
text = 'Сукаый, сочный, сидр, пидрилово, вкбляый, ароматный.'
cens_list = ['сука', 'пидр', 'бля', 'мат']
text_lower = text.lower()
count = 0

for i in range(len(text_lower)):
    for z in range(len(cens_list)):
        for x in range(len(cens_list[z])):
            if text_lower[i] == cens_list[z][x]:
                try:
                    for g in range(len(cens_list[z])):
                        if text_lower[i+g] == cens_list[z][x+g]:
                            count += 1
                            if count == len(cens_list[z]):
                                text = text.replace(text[i:i+count], '*' * count)
                                count = 0
                        else:
                            count = 0
                            continue
                except IndexError:
                    print("string index out of range")
            else:
                break


print(text)
