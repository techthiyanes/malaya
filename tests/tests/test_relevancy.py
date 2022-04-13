import os

os.environ['CUDA_VISIBLE_DEVICES'] = ''
os.environ['MALAYA_USE_HUGGINGFACE'] = 'true'

import sys
import malaya
import logging

logging.basicConfig(level=logging.DEBUG)

text = 'Jabatan Penjara Malaysia diperuntukkan RM20 juta laksana program pembangunan Insan kepada banduan. Majikan yang menggaji bekas banduan, bekas penagih dadah diberi potongan cukai tambahan sehingga 2025.'


def test_transformer():
    models = malaya.relevancy.available_transformer()
    for m in models.index:
        print(m)
        model = malaya.relevancy.transformer(model=m, gpu_limit=0.3)
        print(model.predict_proba([text]))
        print(model.predict_words(text, visualization=False))
        print(model.vectorize([text]))
        os.system('rm -f ~/.cache/huggingface/hub/*')
        del model
