# Voice "LADA" / Female

License: [Apache 2.0](https://github.com/egorsmkv/ukrainian-tts-datasets/blob/main/LICENSE)

**Samples are manually checked. Good samples are in the `accept` folder (10h37m), others are in `reject` (1h2m).**

Listen to [DEMO](https://huggingface.co/spaces/theodotus/ukrainian-voices) (choose "lada" in the Voice field)

## Features

- Quality: high
- Duration: 10h37m
- Audio formats: OPUS/WAV
- Text format: JSONL (a `metadata.jsonl` file)
- Frequency: 16000/22050/48000 Hz

## Original version

### In the `OPUS` format

- 48000 Hz: https://huggingface.co/datasets/Yehor/ukrainian-tts-lada/resolve/main/dataset_lada_ogg.zip

### In the `WAV` format

- 22050 Hz: https://huggingface.co/datasets/Yehor/ukrainian-tts-lada/resolve/main/dataset_lada_22khz.zip  
- 16000 Hz: https://huggingface.co/datasets/Yehor/ukrainian-tts-lada/resolve/main/dataset_lada_16khz.zip

## Trimmed version (removed silence)

### In the `WAV` format

- 48000 Hz: https://huggingface.co/datasets/Yehor/ukrainian-tts-lada/resolve/main/dataset_lada_trimmed_48khz.zip  
- 22050 Hz: https://huggingface.co/datasets/Yehor/ukrainian-tts-lada/resolve/main/dataset_lada_trimmed_22khz.zip  
- 16000 Hz: https://huggingface.co/datasets/Yehor/ukrainian-tts-lada/resolve/main/dataset_lada_trimmed_16khz.zip

Silence is removed by https://github.com/proger/uk#align-text-to-audio-and-trim-silence
