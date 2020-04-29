import pickle


with open('params/stop.pickle', 'rb') as f:
    print(pickle.load(f))
from LoadData import load_data
from jmodel.np import *
from jmodel.util import *
from jmodel.Function import *
from jmodel.Models.Rnnlm import *
corpus, word_to_id, id_to_word = load_data("ptb.train.txt")
test_word = ['what', 'this', 'tells', 'us', 'is', 'that']
tid = np.arange(len(test_word))
for i in range(len(test_word)):
    tid[i] = word_to_id[test_word[i]]
print(tid)
test_data = to_gpu([tid])

print(test_data.shape)
model = Rnnlm()
model.load_params('params/Rnnlm_b.pkl')
p = model.predict(test_data)
s = softmax(p[0][len(test_word)-1])
max_id_array = np.argpartition(s, -10)[-10:]
for mid in max_id_array:
    print(id_to_word[int(mid)] + "---" + str(s[int(mid)]))

model.reset_state()
ppl_test = eval_perplexity(model, corpus)
print('test perplexity: ', ppl_test)