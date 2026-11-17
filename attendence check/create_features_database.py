import os
import numpy as np
import pandas as pd
from PIL import Image
import torch
import torchvision.transforms as T
import faiss
from facenet_pytorch import InceptionResnetV1

#CREATE DATABASE

transform = T.Compose([
    T.Resize((160, 160)),  # Facenet's expected input size
    T.ToTensor(),
    T.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

def crop_center_square(image):
    """Crop the center square of an image and resize to 300x300 (matches app)."""
    width, height = image.size
    size = min(width, height)
    left = (width - size) / 2
    top = (height - size) / 2
    right = (width + size) / 2
    bottom = (height + size) / 2
    
    image = image.crop((left, top, right, bottom))
    return image


def extract_features(image,model):
    image = image.convert('RGB')
    image_tensor = transform(image). unsqueeze(0) #idk why unsqueeze
    with torch.no_grad():
        embedding = model(image_tensor)
    return embedding.squeeze().numpy() #idk why squeeze then +1 dim

model = InceptionResnetV1(pretrained='vggface2').eval()
dataset_dir = "Dataset"
embedding_list = []
labels_mapping = []

for file in os.listdir(dataset_dir):
    if file.endswith(('JPG', 'jpg')):
        image_path = os.path.join(dataset_dir,file)
        img = Image.open(image_path)
        label = image_path[7:-3]
        try:
            embedding = extract_features(img,model)
            embedding_list.append(embedding)
            labels_mapping.append(label)
        except Exception as e:
            print(f"error when processing {image_path} as {e}")

embedding_matrix=np.array(embedding_list)
labels_map_array = np.array(labels_mapping)
embedding_matrix_dim = embedding_matrix.shape[1]
index = faiss.IndexFlatL2(embedding_matrix_dim)
index.add(embedding_matrix)

faiss.write_index(index,"facenet_features.index")
np.save("facenet_label_map.npy",labels_map_array)