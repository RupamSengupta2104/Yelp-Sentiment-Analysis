import kagglehub

# Download latest version
path = kagglehub.dataset_download("omkarsabnis/yelp-reviews-dataset")

print("Path to dataset files:", path)