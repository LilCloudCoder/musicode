import pretty_midi
import random

def make_note(instr, pitch, start, end, velocity=80):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=end)
    instr.notes.append(note)

def generate_techno_masterpiece(filename="2.mid", num_beats=96, tempo=128):
    midi = pretty_midi.PrettyMIDI()

    # Instruments
    arp = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program("Electric Piano 1"))
    bass = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program("Synth Bass 1"))
    flute = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program("Flute"))
    violin = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program("Violin"))
    drums = pretty_midi.Instrument(program=0, is_drum=True)

    beat_len = 60 / tempo

    # Arp: add variety + occasional rests
    for i in range(num_beats // 2):
        if random.random() < 0.8:  # 80% chance to play
            root = random.choice([60, 62, 65, 67])
            for offset in [0, 4, 7, 12]:
                pitch = root + offset
                start = i * beat_len + random.uniform(0, 0.15)
                duration = random.uniform(0.2, 0.4)
                make_note(arp, pitch, start, start + duration, velocity=60)

    # Bass: skip some notes, more bounce
    for i in range(num_beats):
        if random.random() < 0.7:  # 70% chance to play
            pitch = random.choice([36, 38, 41, 43])
            start = i * beat_len
            make_note(bass, pitch, start, start + random.uniform(0.3, 0.5), velocity=75)

    # Drums
    for i in range(num_beats):
        t = i * beat_len
        make_note(drums, 36, t, t + 0.1, velocity=100)  # Kick
        if i % 4 == 2:
            make_note(drums, 38, t, t + 0.1, velocity=90)  # Snare
        if i % 2 == 1:
            make_note(drums, 42, t, t + 0.05, velocity=60)  # Hi-hat
        if i % 8 == 4:
            make_note(drums, 46, t, t + 0.05, velocity=75)  # Open HH

    # Violin Pads
    for t in range(0, num_beats, 8):
        if random.random() < 0.9:
            pad_note = random.choice([55, 60, 63, 67])
            start = t * beat_len
            make_note(violin, pad_note, start, start + 3.0, velocity=45)

    # Flute sparkles
    for t in range(0, num_beats, 6):
        if random.random() < 0.7:
            pitch = random.choice([72, 74, 77, 79, 81])
            start = t * beat_len + 0.4
            make_note(flute, pitch, start, start + 0.5, velocity=55)

    midi.instruments.extend([arp, bass, drums, flute, violin])
    midi.write(filename)
    print(f"🎧🛠️ Techno Beat FIXED (no brrrr) saved to: '{filename}'")

if __name__ == "__main__":
    generate_techno_masterpiece()
