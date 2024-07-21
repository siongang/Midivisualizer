import pretty_midi as pm

#song midi data
midi_data = pm.PrettyMIDI('Domino_Line_-_Casiopea.mid')

instruments = midi_data.instruments
print(instruments[0].notes)