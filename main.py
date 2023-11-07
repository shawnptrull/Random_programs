#finding the first occurance in a group of sentances.

text = 'the dog was there. the cat is there too. python is the best. the dog want want want was there. the cat is orange. the cat is brown. the dog is grey. there is no dog. '

cat=[]
dog=[]

words=['dog', 'cat', 'chocolate']

sentances = text.split('.')

for sentance in sentances:
    for word in words:
        if word in sentance:
            if word == "dog":
                dog.append(sentance)
            if word == "cat":
                cat.append(sentance)

first_dog = dog[0]
first_cat = cat[0]

print(f'The first dog mention in the text is \"{first_dog}\"')
print(f'The first cat mention in the text is \"{first_cat}\"')