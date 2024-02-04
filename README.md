# audio-sample-sort
Use an audio analysis library to analyze audio sample folder and sort by similarities/differences

Choose an Audio Analysis Library:
Select an audio analysis library or tool that can extract features from audio files. One popular library is LibROSA for Python, which can be used to extract audio features.

Install Required Packages:
Install the necessary packages. For LibROSA, you can install it using:
pip install librosa

Feature Extraction:
Use the chosen library to extract features from each audio file.
Features could include spectral centroid, chroma features, or any other relevant attributes that capture sonic textures.

Similarity Measurement:
Define a similarity metric to compare the extracted features.
You may choose to use Euclidean distance, cosine similarity, or any other appropriate measure.

Organize Files:
Based on the similarity measurements, group the audio files into clusters of similar sonic textures.

Create New Folder Structure:
Create a new folder structure and move the similar audio files into corresponding folders.
