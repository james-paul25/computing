import tensorflow as tf
import numpy as np

interpreter = tf.lite.Interpreter(model_path="mobilefacenet_9925.tflite")
interpreter.allocate_tensors()

print("OK: Model loaded successfully!")
