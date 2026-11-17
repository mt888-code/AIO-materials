import numpy as np
import faiss
from PIL import Image
import torch
import torchvision.transforms as T 
import faiss
from facenet_pytorch import InceptionResnetV1

#PROCESS INPUT IMAGE
def load_model():
    model = InceptionResnetV1(pretrained = 'vggface2').eval()
    return model

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

#VECTOR QUERY
def load_facenet_features():
    index = faiss.read_index("facenet_features.index")
    label_map = np.load("label_mapping.npy")
    return index,  label_map

index, label_map = load_facenet_features()
model = load_model()

def searching_similarities(query_feature,k,threshold):
    result = []
    similarities, indices = index.search(np.array([query_feature]),k)
    for i in range(len(similarities[0])):
        if similarities[0][i] > threshold:
            employee_name = label_map[indices[0][i]]
            result.append ((employee_name,similarities[0][i],indices[0][i]))
    return result  





