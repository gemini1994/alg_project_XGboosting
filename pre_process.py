#!/usr/bin
#import csv
rows = 40001
cols = 33
train_rows = 32000
vali_rows = 8000

temp = set([])

matrix = [[0 for col in range(cols)] for row in range(rows)]

with open('train.csv','r') as train:
    i = 0
    for line in train:
        #Id,Score,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30,c31,c32 = line.split(",")
        for j in range(1,34):
            matrix[i][j-1] = line.split(",")[j]
            #print line.split(",")[j]
            #print matrix[i][j]
        i += 1

judge = False
count_num = 0
count_dis_index = 17
count_total = 16
result = [[0 for col in range(33)] for row in range(rows-1)]

for y in range(33):
    if y in [3,4,8,9,11,12,15,17,20,22,24,25,27,28,29,32]:
        judge = True
    if judge== False:
        if y != 0:
            for x in range(1,rows):
                result[x-1][count_num] = str(count_num-1)+':'+str(matrix[x][y])
        else:
            for x in range(1,rows):
                result[x-1][count_num] = matrix[x][y]
        count_num+=1
    else:
        temp = []
        temp_len = 0
        for x in range(1,rows):
            if temp.count(matrix[x][y]) == 0:
                temp.append(matrix[x][y])
                temp_len+=1
            result[x-1][count_dis_index] = str(temp.index(matrix[x][y])+count_total)+':'+'1'
        count_dis_index+=1
        count_total += temp_len

    judge = False

train.close()
insurance_train = open('insurance.txt.train','w')
insurance_test = open('insurance.txt.test','w')
test_RealResult = open('real_result','w')

for x in range(train_rows):
    for y in range(33):
        if y!= 32:
            insurance_train.write(str(result[x][y])+' ')
        else:
            insurance_train.write(str(result[x][y]))
    insurance_train.write('\n')

for x in range(train_rows,rows-1):
    test_RealResult.write(str(result[x][0])+'\n')
    for y in range(33):
        if y!=32:
            insurance_test.write(str(result[x][y])+' ')
        else:
            insurance_test.write(str(result[x][y]))
    insurance_test.write('\n')

insurance_train.close()
insurance_test.close()
test_RealResult.close()
