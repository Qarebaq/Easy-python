def is_email(email):
    word= str("")
    email_list =[]
    gmail = str("@gmail.com")
    for char in email:
        if char != " ":
            word += char
        else:
            if gmail in word:
                email_list.append(word)
            word= str("")
    if gmail in word:
        email_list.append(word)
    return email_list

def word_count(email):
    # wordCount = 0 
    # for char in email:
    #     if char == ' ' or char == '.':
    #         wordCount += 1
    # return int(wordCount + 1)
    word = str("")
    word_list =[]
    for char in email:
        if char!=" ":
            word += char
        else:
            word_list.append(word)
            word = str("")
    word_list.append(word)

    return word_list

def sentence_count(email):
    sent_count = 0 
    for char in email:
        if char == '.':
            sent_count += 1
    return int(sent_count)

def wrd_Avrg(wrds, sentences):
    if sentences == 0:
        return 0 
    avrg = wrds / sentences
    return float(avrg)

def count_and_remove_duplicates(word_list):
    word_count = {}
    while word_list:
        word = word_list[0]
        count = word_list.count(word)
        word_count[word] = count
        word_list = [w for w in word_list if w != word]
    return word_count

def top_5_frequent_words(word_count_dict):
    sorted_items = sorted(word_count_dict.items(), key=lambda x: x[1], reverse=True)

    return sorted_items[:5]




email = input("Enter your email message: ")
wrd_cnt = len(word_count(email))
sen_cnt = sentence_count(email)
wrdAvrg = wrd_Avrg(wrd_cnt, sen_cnt)
word_counts = count_and_remove_duplicates(word_count(email))
top5 = top_5_frequent_words(word_counts)
print("Top 5 frequent words:")
for word, count in top5:
    print(f"{word}: {count} times")
print(f"The total count of words is {wrd_cnt}, the number of sentences is {sen_cnt}, and the average number of words per sentence is {wrdAvrg:.2f}.")
print(is_email(email))
