import json
import librosa

from os.path import exists, basename
from glob import glob
from pathlib import Path

# Config
OGG_FOLDER = '/home/yehor/kate-data/'
METADATA_FILE = '/home/yehor/metadata.jsonl'

# Constraints for audios
MIN_DURATION = 0.1
MAX_DURATION = 30.0

# Scan the folder for .ogg files
for filename in glob(OGG_FOLDER + '*.ogg'):
    # Generate the name of the metadata file
    json_filename = filename.replace('.ogg', '.json')

    # Skip an item if the metadata file does not exist
    if not exists(json_filename):
        continue

    # Load the metadata file
    data = Path(json_filename).read_text()
    data_json = json.loads(data)

    sample = data_json['sample']

    # Skip deleted items
    if sample['is_deleted'] == 1:
        continue

    # Get the duration of the audio
    try:
        duration = librosa.get_duration(filename=filename)
    except Exception as e:
        print('Exception happened with file:', filename)
        continue

    # Skip items with wrong duration
    if duration < MIN_DURATION or duration > MAX_DURATION:
        continue

    json_row = {
        'file': basename(filename),
        'orig_text_wo_stress': sample['orig_text_wo_stress'],
        'orig_text': sample['orig_text'],
    }

    # Append the row to the metadata file
    with open(METADATA_FILE, 'a') as f:
        f.write(json.dumps(json_row) + '\n')

print('Finished')
