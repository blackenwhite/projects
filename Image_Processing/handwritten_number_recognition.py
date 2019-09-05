# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 10:17:58 2019

@author: LENOVO
"""

#handwriting recognition
import tensorflow as tf
print(tf.__version__)

#implementing the call_back function
class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('loss')<=0.01):
      print("\nReached 99% accuracy so cancelling training!")
      self.model.stop_training = True
callbacks = myCallback()
mnist = tf.keras.datasets.mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()

import matplotlib.pyplot as plt



x_train  = x_train/ 255.0
x_test = x_test / 255.0

#making the model
model = tf.keras.models.Sequential([tf.keras.layers.Flatten(), 
                                    tf.keras.layers.Dense(512, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

#optimizing the model
model.compile(optimizer = tf.train.AdamOptimizer(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

#fitting the model
model.fit(x_train, y_train, epochs=7,callbacks=[callbacks])

#evaluating the model
model.evaluate(x_test, y_test)


#exploration 
classifications = model.predict(x_test)
print(classifications[2])

print(y_test[2])

plt.imshow(x_train[0])
print(y_train[0])
print(x_train[0])