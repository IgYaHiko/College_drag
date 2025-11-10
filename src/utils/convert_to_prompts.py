import pandas as pd
import os

# Load processed dataset
input_path = "data/processed/processed_crop.csv"
data = pd.read_csv(input_path)

# Automatically detect feature columns (everything except 'Crop')
target_col = 'Crop'
feature_cols = [col for col in data.columns if col != target_col]

# Function to create a natural-language style prompt
def make_prompt(row):
    features_text = ", ".join([f"{col.replace('_', ' ').lower()} is {row[col]}" for col in feature_cols])
    prompt = f"Given that {features_text}, which crop should be planted?"
    return prompt

# Generate prompts and responses
prompt_response_df = pd.DataFrame({
    "prompt": data.apply(make_prompt, axis=1),
    "response": data[target_col]
})

# Save to new folder
os.makedirs("data/llm_train", exist_ok=True)
output_path = "data/llm_train/prompt_response_dataset.csv"
prompt_response_df.to_csv(output_path, index=False)

print(f"✅ Converted {len(prompt_response_df)} rows into prompt-response pairs.")
print(f"📁 Saved at: {output_path}")
print(prompt_response_df.head())
