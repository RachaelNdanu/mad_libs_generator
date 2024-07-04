with open ("story.txt" , "r") as f:
    story = f.read()

#print(story)

words = set ()
start_of_word = -1

target_start = "<"
target_end = ">"

#finding the start of a word

for i , char in enumerate(story):
    if char ==target_start:
        start_of_word = i

# detecting end of word 

    if char== target_end and start_of_word != -1:
        # extarcting the word
        word = story[start_of_word:i+1]
        words.add(word)
        start_of_word = -1



#print (words)

answers = {}

for word in words:
    answer = input ("Enter a word for" + word + ": ")
    answers[word] = answer



 
#print(answers)

for word in words:
    story = story.replace (word, answers[word])

print (story)