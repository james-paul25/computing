import tensorflow as tf

pb_path = "MobileFaceNet_9925_9680.pb"

with tf.io.gfile.GFile(pb_path, "rb") as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())

for node in graph_def.node:
    print(node.name)
