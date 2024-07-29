import pretty_midi as pm

#song midi data
midi_data = pm.PrettyMIDI('Asayake__Casiopea_Mint_Jams_test.mid')

instruments = midi_data.instruments
# print(instruments[0].notes)