import pretty_midi as pm

#song midi data
midi_data = pm.PrettyMIDI('Chopin_-_Nocturne_Op_9_No_2_E_Flat_Major (1).mid')

instruments = midi_data.instruments
print(instruments[0].notes)