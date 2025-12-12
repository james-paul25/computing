import tensorflow as tf

pb_path = "MobileFaceNet_9925_9680.pb"

# IMPORTANT — update these after inspecting tensors
input_arrays = ["input"]
output_arrays = ["embeddings"]
input_shape = {"input": [1,112,112,3]}

converter = tf.lite.TFLiteConverter.from_frozen_graph(
    pb_path,
    input_arrays=input_arrays,
    output_arrays=output_arrays,
    input_shapes=input_shape
)

converter.allow_custom_ops = True
converter.post_training_quantize = False  # keep float32 for accuracy

tflite_model = converter.convert()

with open("mobilefacenet_9925.tflite", "wb") as f:
    f.write(tflite_model)

print("DONE! Saved as mobilefacenet_9925.tflite")
