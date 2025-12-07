from src.data_loader import load_raw_data, load_processed_data, load_user_data

raw_df = load_raw_data()
print("Raw:", raw_df.shape)

processed_df = load_processed_data()
print("Processed:", processed_df.shape)

user_df = load_user_data("user_1")
print("User 1 rows:", user_df.shape)
