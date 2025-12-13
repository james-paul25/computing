import os
import json
import cv2
import numpy as np
import tensorflow as tf
from mtcnn import MTCNN

# ================= CONFIG =================
DATASET_DIR = "dataset"
TFLITE_MODEL = "mobilefacenet_9925.tflite"
OUTPUT_JSON = "celebrity_embeddings.json"
IMAGE_SIZE = 112
# ==========================================

# Load face detector
detector = MTCNN()

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path=TFLITE_MODEL)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# ---------- Helper functions ----------

def preprocess_face(face_img):
    face_img = cv2.resize(face_img, (IMAGE_SIZE, IMAGE_SIZE))
    face_img = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
    face_img = face_img.astype(np.float32)
    face_img = face_img / 127.5 - 1.0
    return np.expand_dims(face_img, axis=0)

def get_embedding(face_img):
    interpreter.set_tensor(input_details[0]["index"], face_img)
    interpreter.invoke()
    return interpreter.get_tensor(output_details[0]["index"])[0]

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# ---------- Main process ----------

celebrity_db = {}

for celeb in os.listdir(DATASET_DIR):
    celeb_path = os.path.join(DATASET_DIR, celeb)
    if not os.path.isdir(celeb_path):
        continue

    print(f"\nProcessing: {celeb}")
    embeddings = []

    for img_name in os.listdir(celeb_path):
        img_path = os.path.join(celeb_path, img_name)
        img = cv2.imread(img_path)

        if img is None:
            continue

        faces = detector.detect_faces(img)
        if len(faces) == 0:
            print(f"No face detected in {img_name}")
            continue

        # Take the largest detected face
        face = max(faces, key=lambda f: f["box"][2] * f["box"][3])
        x, y, w, h = face["box"]
        x, y = max(0, x), max(0, y)

        face_img = img[y:y+h, x:x+w]
        face_input = preprocess_face(face_img)
        embedding = get_embedding(face_input)

        embeddings.append(embedding)

    if len(embeddings) == 0:
        print(f"No valid images for {celeb}")
        continue

    # Average embeddings
    mean_embedding = np.mean(embeddings, axis=0)
    mean_embedding = mean_embedding / np.linalg.norm(mean_embedding)

    celebrity_db[celeb] = {
        "name": celeb.replace("_", " ").title(),
        "embedding": mean_embedding.tolist()
    }

    print(f"  ✅ Saved {len(embeddings)} embeddings")

# Save to JSON
with open(OUTPUT_JSON, "w") as f:
    json.dump(celebrity_db, f, indent=2)

print("\nDONE! Saved celebrity_embeddings.json")
