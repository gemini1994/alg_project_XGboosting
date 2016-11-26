#!/usr/bin
import xgboost as xgb
test_num = 8000#test num:8000
result_pre = open('pred.txt','w')
result_real = open('real_result','r')

dtrain = xgb.DMatrix('insurance.txt.train')
dtest = xgb.DMatrix('insurance.txt.test')
param = {'max_depth': 3,
'eta': 1.0,
'gamma': 1.0,
'min_child_weight': 1,
'save_period': 0,
'booster': 'gbtree',
'objective': 'reg:linear'}
num_round = 2
watchlist = [(dtest, 'eval'), (dtrain, 'train')]
bst = xgb.train(param, dtrain, num_round, watchlist)
preds = bst.predict(dtest)
#write_pred('pred.txt', preds)
real_result = [0 for row in range(test_num)]
i=0
for line in result_real:
    real_result[i] = float(line.split()[0])
    i+=1

temp = 0.0

i=0
for row in preds:
    #result_pre.write(str(row)+'\n')
    temp+= (row-real_result[i])**2

temp = (temp/test_num)**(0.5)
print 'my mre: '+str(temp)

result_pre.close()
result_real.close()
#bst.dump_model('dump2.nice.txt', 'featmap.txt')
