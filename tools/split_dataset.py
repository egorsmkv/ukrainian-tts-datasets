import os
import json

DATASET_FILES = 'lada/dataset_lada'
METADATA_DATASET_FILES = 'lada/dataset_lada/metadata.jsonl'

ACCEPT_DATASET_FILES = 'lada/dataset_lada/accept'
REJECT_DATASET_FILES = 'lada/dataset_lada/reject'

METADATA_ACCEPT_DATASET_FILES = 'lada/dataset_lada/accept/metadata.jsonl'
METADATA_REJECT_DATASET_FILES = 'lada/dataset_lada/reject/metadata.jsonl'

VERIFIED_JSON = 'lada.verified.json'

if __name__ == '__main__':
    metadata = {}
    with open(METADATA_DATASET_FILES) as f:
        for x in f:
            data = json.loads(x)
            metadata[data['file']] = data

    rows = []
    with open(VERIFIED_JSON) as f:
        for x in f:
            data = json.loads(x)
            rows.append(data)

    for row in rows:
        ogg_file = DATASET_FILES + f'/{row["utt"]}.ogg'

        if not os.path.exists(ogg_file):
            continue

        print(row)

        ogg_file_accept = ACCEPT_DATASET_FILES + f'/{row["utt"]}.ogg'
        ogg_file_reject = REJECT_DATASET_FILES + f'/{row["utt"]}.ogg'

        if row['answer'] == 'accept':
            # move a file
            os.rename(ogg_file, ogg_file_accept)

            # append info to metadata
            file_meta = json.dumps(metadata[f'{row["utt"]}.ogg'])
            with open(METADATA_ACCEPT_DATASET_FILES, 'a') as f:
                f.write(file_meta + '\n')

        if row['answer'] == 'reject':
            # move a file
            os.rename(ogg_file, ogg_file_reject)

            # append info to metadata
            file_meta = json.dumps(metadata[f'{row["utt"]}.ogg'])
            with open(METADATA_REJECT_DATASET_FILES, 'a') as f:
                f.write(file_meta + '\n')

    print('Done')
