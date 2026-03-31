import os
import urllib.request

def download_file(url, filename):
    try:
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print("Success.\n")
    except Exception as e:
        print(f"Failed to download {url}")
        print(f"Error: {e}\n")

# Ensure correct path regardless of where script is run
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "Phase1_Foundations", "data")

os.makedirs(DATA_DIR, exist_ok=True)

# German
download_file(
    "https://raw.githubusercontent.com/UniversalDependencies/UD_German-GSD/master/de_gsd-ud-train.conllu",
    os.path.join(DATA_DIR, "de_train.conllu")
)

# French
download_file(
    "https://raw.githubusercontent.com/UniversalDependencies/UD_French-GSD/master/fr_gsd-ud-train.conllu",
    os.path.join(DATA_DIR, "fr_train.conllu")
)

# Russian (FIXED)
download_file(
    "https://raw.githubusercontent.com/UniversalDependencies/UD_Russian-GSD/master/ru_gsd-ud-train.conllu",
    os.path.join(DATA_DIR, "ru_train.conllu")
)

print("All downloads attempted.")