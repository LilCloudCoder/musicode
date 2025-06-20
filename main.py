import pretty_midi
import random

def make_note(instr, pitch, start, end, velocity=80):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=end)
    instr.notes.append(note)

def generate_full_techno_song(filename="ultimate_fluffy.mid", num_beats=64, tempo=120):
    midi = pretty_midi.PrettyMIDI()

    # Instruments
    arp = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program("Electric Piano 1"))
    bass = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program("Synth Bass 2"))
    flute = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program("Flute"))
    violin = pretty_midi.Instrument(program=pretty_midi.instrument_name_to_program("Violin"))
    drums = pretty_midi.Instrument(program=0, is_drum=True)

    beat_len = 60 / tempo
    current_time = 0.0

    # Arpeggiated electric piano
    for i in range(num_beats // 2):
        root = random.choice([60, 62, 64, 65])  # C D E F
        arpeggio = [root, root+4, root+7, root+12]
        for j, note in enumerate(arpeggio):
            make_note(arp, note, current_time + j * 0.1, current_time + j * 0.1 + 0.2, velocity=60)
        current_time += beat_len * 2

    # Bassline
    bass_time = 0.0
    for _ in range(num_beats):
        pitch = random.choice([36, 38, 40, 43])
        make_note(bass, pitch, bass_time, bass_time + 0.4, velocity=75)
        bass_time += beat_len

    # Flute melodic sparkles
    for t in range(0, num_beats, 8):
        pitch = random.choice([72, 74, 76, 79])
        start = t * beat_len + 0.3
        make_note(flute, pitch, start, start + 0.5, velocity=55)

    # Violin harmony (pad notes)
    for t in range(0, num_beats, 8):
        pad_note = random.choice([60, 63, 67])
        start = t * beat_len
        make_note(violin, pad_note, start, start + 2.0, velocity=40)

    # Drums: kick, snare, hi-hat
    for i in range(num_beats):
        time = i * beat_len
        make_note(drums, 36, time, time + 0.1, velocity=100)  # Kick
        if i % 4 == 2:
            make_note(drums, 38, time, time + 0.1, velocity=90)  # Snare
        if i % 2 == 1:
            make_note(drums, 42, time, time + 0.05, velocity=70)  # Hi-hat

    # Assemble
    midi.instruments.extend([arp, bass, drums, flute, violin])
    midi.write(filename)
    print(f"🎧✨ ULTIMATE FLUFFY TECHNO saved to '{filename}'")

if __name__ == "__main__":
    generate_full_techno_song("ultimate_fluffy.mid", num_beats=64, tempo=125)