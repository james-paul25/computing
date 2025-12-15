import tensorflow as tf

# -----------------------------
# 1. Load FULL legacy model
# -----------------------------
model = tf.keras.models.load_model(
    "simple_CNN.985-0.66.hdf5",
    compile=False
)

print("✅ Legacy model loaded")

# -----------------------------
# 2. Convert to TFLite
# -----------------------------
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Keep it simple first
converter.optimizations = [tf.lite.Optimize.DEFAULT]

tflite_model = converter.convert()

# -----------------------------
# 3. Save
# -----------------------------
with open("simple_CNN_emotion.tflite", "wb") as f:
    f.write(tflite_model)

print("🎉 SUCCESS: simple_CNN_emotion.tflite created")
