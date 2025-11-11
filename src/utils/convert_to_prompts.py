import pandas as pd
import os

# Load the RAW dataset directly to preserve crop names
raw_input_path = "data/processed/processed_crop.csv"
data = pd.read_csv(raw_input_path)

print("📊 Dataset Info:")
print(f"Columns: {data.columns.tolist()}")
print(f"Shape: {data.shape}")
print(f"Unique crops: {data['Crop'].unique()}")
print(f"Sample crops: {data['Crop'].value_counts().head()}")

# Define feature columns (all parameters except target and metadata)
feature_cols = ['Soil_color', 'Nitrogen', 'Phosphorus', 'Potassium', 'pH', 'Rainfall', 'Temperature']
target_col = 'Crop'

# Function to create a natural-language style prompt
def make_prompt(row):
    features_text = ", ".join([f"{col.replace('_', ' ').lower()} is {row[col]}" for col in feature_cols])
    prompt = f"Given that {features_text}, which crop should be planted?"
    return prompt

# Generate prompts and responses
prompt_response_df = pd.DataFrame({
    "prompt": data.apply(make_prompt, axis=1),
    "response": data[target_col]  # This will now have actual crop names like "Sugarcane"
})

# Save to new folder
os.makedirs("data/llm_train", exist_ok=True)
output_path = "data/llm_train/prompt_response_dataset.csv"
prompt_response_df.to_csv(output_path, index=False)

print(f"\n✅ Converted {len(prompt_response_df)} rows into prompt-response pairs.")
print(f"📁 Saved at: {output_path}")
print("\n🔍 Sample of converted data:")
print(prompt_response_df.head())

print("\n🌱 Crop distribution:")
print(prompt_response_df['response'].value_counts())