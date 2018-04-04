# coding: UTF-8
'''''''''''''''''''''''''''''''''''''''''''''''''''''
   file name: config.py
   create time: 2017年06月25日 星期日 10时56分55秒
   author: Jipeng Huang
   e-mail: huangjipengnju@gmail.com
   github: https://github.com/hjptriplebee
'''''''''''''''''''''''''''''''''''''''''''''''''''''
batchSize = 128
learningRateBase = 0.001
learningRateDecreaseStep = 100
epochNum = 100                    # train epoch
rnn_layers = 2
rnn_hidden_layer_size = 256
generateNum = 4                   # number of generated poems per time

trainPoems = "dataset/poetry.txt" # training file location
checkpointsPath = "./checkpoints" # checkpoints location