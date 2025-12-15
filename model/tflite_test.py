import tensorflow as tf
import numpy as np

interpreter = tf.lite.Interpreter(model_path="emotion_model.tflite")
interpreter.allocate_tensors()

print("OK: Model loaded successfully!")
