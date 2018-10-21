from tqdm import tqdm
from difflib import SequenceMatcher
import json

similar = lambda a, b: SequenceMatcher(None, a, b).ratio()

def load_person(name:str):
    msgs = json.load(open(f'data/{name.lower()}.json'))
    texts = [_ for _ in msgs['messages'] if _['type'] == 'Generic' and 'content' in _][::-1]
    msg_pairs = assign(texts)

def search(message_pairs, m):
    MAX = 0
    reply = None
    for X, Y in tqdm(message_pairs):
        score = similar(m, X)
        if score > MAX:
            MAX = score
            reply = Y
    return reply

def search_all(message_pairs, m, thresh=0.97):
    for X, Y in message_pairs:
        if similar(m, X) > thresh: yield (X,Y)

def assign(texts):
    message_pairs = []
    they_said = []
    pri_said = []
    prev = texts[0]['sender_name']
    for text in tqdm(texts):
        sender = text['sender_name']
        if sender != prev and they_said and pri_said:
            message_pairs.append(('\n'.join(pri_said), '\n'.join(they_said)))
            they_said = []
            pri_said = []
        pri_said.append(text['content']) if 'Priansh' in sender else they_said.append(text['content'])
        prev = sender
    return message_pairs