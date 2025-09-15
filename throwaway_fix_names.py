import os

base_dir = r"c:\Users\Adrian Work\Downloads\ForcedMigration\google_trends_manual_bgd\data\Barisal Division_Bengali"
exclude_folder = "queries"

for folder in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, folder)
    if not os.path.isdir(folder_path) or folder == exclude_folder:
        continue
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv") and not filename.startswith("multiTimeline"):
            old_path = os.path.join(folder_path, filename)
            new_filename = "multiTimeline" + filename
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {old_path} -> {new_path}")