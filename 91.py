#!/usr/bin/env python

import numpy as np
from layers import Embedding
from negative_sampling_layer import NegativeSamplingLoss
import pickle 

pkl_file='para2.pkl'

with open(pkl_file,'rb') as f:
    para=pickle.load(f)
    corpus=para['corpus']
    word_to_id=para['word_to_id']
    id_to_word=para['id_to_word']

#!/usr/bin/env python

import numpy as np
import pickle
from trainer import Trainer
from optimizer import Adam
from cbow import CBOW
from util import create_contexts_target, to_cpu




if True:

    # settings of hyper parameter
    window_size = 5
    hidden_size = 100
    batch_size = 100
    max_epoch = 10

    # loading data
    #corpus, word_to_id, id_to_word = ptb.load_data('train')
    vocab_size = len(word_to_id)

    contexts, target = create_contexts_target(corpus, window_size)

    # create model etc.
    model = CBOW(vocab_size, hidden_size, window_size, corpus)
    optimizer = Adam()
    trainer = Trainer(model, optimizer)

    # start training
    trainer.fit(contexts, target, max_epoch, batch_size)
    trainer.plot()

    # save data in case later use
    word_vecs = model.word_vecs
    params = {}
    params['word_vecs'] = word_vecs.astype(np.float16)
    params['word_to_id'] = word_to_id
    params['id_to_word'] = id_to_word
    pkl_file = 'cbow_params_my.pkl'

    with open(pkl_file, 'wb') as f:
        pickle.dump(params, f, -1)
