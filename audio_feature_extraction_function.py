import librosa
import os

# Define features to extract (adjust as needed)
features = ["spectral_centroid", "chroma_stft"]

# Specify your audio sample folder path
audio_folder = "path/to/your/audio/folder"

# Create dictionary to store features and filenames
audio_data = {}

# Iterate through audio files
for filename in os.listdir(audio_folder):
    if filename.endswith(".wav") or filename.endswith(".mp3"):
        filepath = os.path.join(audio_folder, filename)
        # Load audio data and extract features
        y, sr = librosa.load(filepath)
        file_features = []
        for feature in features:
            file_features.append(librosa.feature.extract_feature(feature, y))
        # Store features and filename
        audio_data[filename] = file_features

# Define a weighted similarity metric function: a weighted sum of their Euclidean distance and cosine similarity
def weighted_similarity(features1, features2, weight_euclidean=0.5, weight_cosine=0.5):
    euclidean_dist = similarity_euclidean(features1, features2)
    cosine_sim = similarity_cosine(features1, features2)
    return weight_euclidean * euclidean_dist + weight_cosine * cosine_sim


# Organize files based on similarity
clusters = {}
for filename1, features1 in audio_data.items():
    min_dist = float("inf")
    closest_file = None
    for filename2, features2 in audio_data.items():
        if filename1 != filename2:
            dist = similarity(features1, features2)
            if dist < min_dist:
                min_dist = dist
                closest_file = filename2
    # Add file to cluster with closest neighbor
    if closest_file not in clusters:
        clusters[closest_file] = []
    clusters[closest_file].append(filename1)

# Create new folder structure and move files
for cluster_file, filenames in clusters.items():
    cluster_name = os.path.splitext(cluster_file)[0]
    os.makedirs(os.path.join("organized_audio", cluster_name), exist_ok=True)
    for filename in filenames:
        source_path = os.path.join(audio_folder, filename)
        dest_path = os.path.join("organized_audio", cluster_name, filename)
        os.rename(source_path, dest_path)

print("Audio files organized based on similarity!")
