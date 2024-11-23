import pandas as pd

# Load the datasets
app_store_data = pd.read_csv("AppStore.csv")  # replace with the actual file path
google_play_data = pd.read_csv(
    "GooglePlayStore.csv"
)  # replace with the actual file path

# Check data format and basic statistics
print("App Store Data Overview:")
print(app_store_data.info())
print("\nGoogle Play Data Overview:")
print(google_play_data.info())

# Display first few rows to understand the structure
print("\nApp Store Sample Data:")
print(app_store_data.head())
print("\nGoogle Play Sample Data:")
print(google_play_data.head())

# Basic data cleaning: Remove any apps without a rating or installs
app_store_data = app_store_data.dropna(subset=["Rating", "Reviews"])
google_play_data = google_play_data.dropna(subset=["Rating", "Reviews", "Installs"])

# Convert installs and reviews to numeric (if necessary)
google_play_data["Installs"] = (
    google_play_data["Installs"].str.replace("[+,]", "", regex=True).astype(int)
)
google_play_data["Reviews"] = google_play_data["Reviews"].astype(int)
app_store_data["Reviews"] = app_store_data["Reviews"].astype(int)

# Filter apps with high ratings (e.g., 4.0 and above) and significant user engagement (e.g., over 100,000 installs)
high_rating_threshold = 4.0
min_installs = 100000
min_reviews = 100

# For App Store
highly_rated_app_store = app_store_data[
    (app_store_data["Rating"] >= high_rating_threshold)
    & (app_store_data["Reviews"] >= min_reviews)
]

# For Google Play Store
highly_rated_google_play = google_play_data[
    (google_play_data["Rating"] >= high_rating_threshold)
    & (google_play_data["Installs"] >= min_installs)
    & (google_play_data["Reviews"] >= min_reviews)
]

# Find top categories in terms of average rating
top_categories_app_store = (
    highly_rated_app_store.groupby("Category")["Rating"]
    .mean()
    .sort_values(ascending=False)
)
top_categories_google_play = (
    highly_rated_google_play.groupby("Category")["Rating"]
    .mean()
    .sort_values(ascending=False)
)

print("\nTop Categories on App Store by Average Rating:")
print(top_categories_app_store.head(10))

print("\nTop Categories on Google Play by Average Rating:")
print(top_categories_google_play.head(10))

# Recommendations: Apps with high ratings and many installs in the most profitable categories
print("\nHighly Rated and Popular Apps in App Store:")
print(
    highly_rated_app_store[["App", "Category", "Rating", "Reviews"]]
    .sort_values(by="Reviews", ascending=False)
    .head(10)
)

print("\nHighly Rated and Popular Apps in Google Play Store:")
print(
    highly_rated_google_play[["App", "Category", "Rating", "Installs", "Reviews"]]
    .sort_values(by="Installs", ascending=False)
    .head(10)
)
