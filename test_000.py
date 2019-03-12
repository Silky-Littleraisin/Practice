import numpy as np

def create_contexts_target(corpus, window_size=1):
    target = corpus[window_size:-window_size]
    contexts = []

    for idx in range(window_size, len(corpus) - window_size):
        cs = []

        for t in range(-window_size, window_size + 1):
            if t == 0:
                continue
            print (t)
            cs.append(corpus[idx + t])
        contexts.append(cs)

    return np.array(contexts), np.array(target)

def preprocess(text):
    text = text.lower()
    text = text.replace('.', ' .') # split comma as a word
    words = text.split(' ')

    word_to_id = {}
    id_to_word = {}

    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word

    corpus = np.array([word_to_id[w] for w in words])

    return corpus, word_to_id, id_to_word


text = 'you say goodbye and I say hello.'
corpus,word_to_id,id_to_word = preprocess(text)
contexts,target=create_contexts_target(corpus,window_size=1)
print(contexts)
print(target)