import tensorflow as tf
from tensorflow.python.platform import gfile

pb_path = "MobileFaceNet_9925_9680.pb"

with tf.gfile.GFile(pb_path, "rb") as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())

for node in graph_def.node:
    print(node.name)
