# Musifluff

Musifluff is a Python script that generates a fun, fluffy techno MIDI song using the `pretty_midi` library. It creates arpeggiated electric piano, basslines, melodic sparkles, harmony pads, and a drum beat, then saves the result as a `.mid` file.

## Features

- Randomized arpeggiated electric piano
- Synth bassline
- Flute melodic sparkles
- Violin harmony pads
- Drum patterns (kick, snare, hi-hat)
- Fully generated techno song in MIDI format

## Requirements

- Python 3.7+
- [`pretty_midi`](https://github.com/craffel/pretty-midi)

Install dependencies with:

```bash
pip install pretty_midi
```

## Usage

Run the script to generate a techno MIDI file:

```bash
python main.py
```

By default, this will create `ultimate_fluffy.mid` in the current directory.

## Customization

You can adjust the number of beats and tempo by editing the last line in `main.py`:

```python
generate_full_techno_song("ultimate_fluffy.mid", num_beats=64, tempo=125)
```

## License

MIT License
