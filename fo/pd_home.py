import numpy as np
import tiktoken
from pd_alt import getSumTwo

def getSum(x, y):
    a = np.array([x, y, 3])
    tokenizer = tiktoken.encoding_for_model('gpt-3.5-turbo')
    text = "Hello I am in pd modal getsum, I'd like to use tiktoken to get the length of the tokens of this text!"
    tokens = tokenizer.encode(text)
  
    return np.sum(a) + getSumTwo() + len(tokens)

def getSumThree():
    return 3