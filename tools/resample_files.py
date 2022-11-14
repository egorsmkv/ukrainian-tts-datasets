import subprocess
from os.path import exists
from glob import glob

FFMPEG_BIN = '/opt/homebrew/bin/ffmpeg'
SAMPLE_RATE = 22050
FILE_FORMAT = 'wav'

FILES_MASK = '/Users/yehorsmoliakov/Work/ukrainian-tts-datasets/lada/dataset_lada/reject/*.ogg'
SAVE_TO = '/Users/yehorsmoliakov/Work/ukrainian-tts-datasets/lada/dataset_lada_22khz/reject'


def resample(filename_full):
    filename = filename_full.split('/')[-1]
    out_filename = SAVE_TO + '/' + filename.replace('ogg', FILE_FORMAT)

    cmd = [FFMPEG_BIN, '-i', filename_full, '-ar', str(SAMPLE_RATE), out_filename]

    print('Running:')
    print(' '.join(cmd))

    if exists(out_filename):
        print('Skipping')
    else:
        result = subprocess.run(cmd)
        print(result)


def run():
    files = glob(FILES_MASK)

    print(f'Found {len(files)} files')

    for f in files:
        resample(f)

if __name__ == '__main__':
    run()
