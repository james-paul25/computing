import tensorflow as tf

pb_path = "emotion_detection_model.h5"


input_arrays = ["input"]        # change only if your Placeholder name differs
output_arrays = ["embeddings"]
input_shape = {"input": [1, 112, 112, 3]}

converter = tf.compat.v1.lite.TFLiteConverter.from_frozen_graph(
    pb_path,
    input_arrays=input_arrays,
    output_arrays=output_arrays,
    input_shapes=input_shape
)

# Recommended settings
converter.optimizations = []    # keep full float32 accuracy
converter.allow_custom_ops = False

tflite_model = converter.convert()

with open("emotion_model.tflite", "wb") as f:
    f.write(tflite_model)

print("DONE! Saved as emotion_model.tflite")
