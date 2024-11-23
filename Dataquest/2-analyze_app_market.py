import pandas as pd

data = {
    "App Name": ["App A", "App B", "App C", "App D", "App E"],
    "Platform": ["Google Play", "App Store", "Google Play", "App Store", "Google Play"],
    "Rating": [4.5, 4.7, 4.3, 4.9, 4.8],
    "Downloads": [1000000, 500000, 1500000, 800000, 1200000],
}

df = pd.DataFrame(data)

df["Profitability Score"] = df["Rating"] * df["Downloads"]

df_sorted = df.sort_values(by="Profitability Score", ascending=False)

print("Profitable App Profiles (based on Rating and Downloads):")
print(df_sorted[["App Name", "Platform", "Rating", "Downloads", "Profitability Score"]])

threshold = 4.5
filtered_df = df_sorted[df_sorted["Rating"] >= threshold]

print(f"\nApps with Rating >= {threshold}:")
print(
    filtered_df[["App Name", "Platform", "Rating", "Downloads", "Profitability Score"]]
)
