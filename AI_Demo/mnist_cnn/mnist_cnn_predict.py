#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : mnist_cnn_predict.py
# @Author: Zhang Chuan
# @Date  : 18-8-23
# @Desc  : predict image

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

#model path
model_path = './mnist_cnn_saved_model/1534953492/saved_model.pb'

testImage = cv.imread('example3.png')

with tf.Graph().as_default():
    output_graph_def = tf.GraphDef()
    with open(model_path, "rb") as f:
        output_graph_def.ParseFromString(f.read())
        tf.import_graph_def(output_graph_def, name="")

    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        # x_test = x_test.reshape(1, 28 * 28)
        input_x = sess.graph.get_tensor_by_name("input/x_input:0")
        output = sess.graph.get_tensor_by_name("output:0")

        #对图片进行测试
        testImage=cv.cvtColor(testImage, cv.COLOR_BGR2GRAY)
        testImage=cv.resize(testImage,dsize=(28, 28))
        test_input=np.array(testImage)
        test_input = test_input.reshape(1, 28 * 28)
        pre_num = sess.run(output, feed_dict={input_x: test_input})#利用训练好的模型预测结果
        print('模型预测结果为：',pre_num)
        # cv.imshow("image",testImage)
        # cv.waitKey(0)
        #显示测试的图片
        fig = plt.figure(), plt.imshow(testImage,cmap='binary')  # 显示图片
        plt.title("prediction result:"+str(pre_num))
        plt.show()
