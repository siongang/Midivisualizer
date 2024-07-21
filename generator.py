import pygame as pg
from midiParser import instruments, midi_data
import vid
import instrument as instr
# from note import Note

pg.init()
display_width = 1280
display_height = 720
vid.constructor(display_width,display_height)
screen = pg.display.set_mode((display_width, display_height))
clock = pg.time.Clock()
running = True
dt = 0

# the pixels where the drawing starts
starting_position = 1000


tempo_times, tempo_bpm = midi_data.get_tempo_changes()
# print(tempo_bpm[0])
# pixels/1second
bpm = tempo_bpm[0]
#pixels/beat
note_length = 120

# pitches
min_pitch = 1000
max_pitch = -1000

notes_list = []
instrument_list = []

# getting info about the song, in this case right now its just the max and min pitch
for instrument in instruments:
        print(instrument)
        instrument_name = instrument.name
        instrument_colour = input(f"what colour should the {instrument_name} be? ")
        instrument_speed = input(f"what speed should the {instrument_name} be? ")
        instrument_icon =input(f"what icon should the {instrument_name} be? ")
        instrument_list.append(instr.Instrument(instrument_name, instrument_colour, instrument_speed, instrument_icon))
        for note in instrument.notes:
            if max_pitch < note.pitch:
                max_pitch = note.pitch
            if min_pitch > note.pitch:
                min_pitch = note.pitch

        start = note.start
        end = note.end
        pitch = note.pitch
        velocity = note.velocity

        # notes_list.append(Note(start, end, pitch, velocity, end-start))
        

                
print(max_pitch)
print(min_pitch)


num_pitches = 128
position = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            vid.video.release()

  


    # clean screen with bg colour
    screen.fill((20, 20, 20))

    # DELAY if i want to use it ever. "w key"
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        pg.time.delay(1000)


    # iterating through each note
    for instrument in instruments:
        # print(instrument)
        for note in instrument.notes:
            start = note.start
            end = note.end
            pitch = note.pitch
            velocity = note.velocity

            note_tempo = bpm # place holder, i can make a more dynamic way of getting the accurate tempo for tempo changes

            # note properties
            rect_width = (end-start)*note_length * (note_tempo/60)
            rect_height = display_height/num_pitches
            rect_x = starting_position+ start*note_length * (note_tempo/60) - position
            rect_y = (num_pitches - pitch - 1) * rect_height
      
            rect_color = (204, 51, 51)  # Red color

            pg.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
            pg.display.update(pg.Rect(rect_x, rect_y, rect_width, rect_height))
            
            # pg.time.delay(10)
            # print("rectangle")
            # print(note)
 
    pg.display.update()
    
 # the line
    line_start = (600,0)
    line_end = (600,720)
    line_width = 5
    line_colour = (225,225,225)
    pg.draw.line(screen, line_colour, line_start, line_end, line_width)



    vid.vid_generator(screen)
    clock.tick(60) 
    # beat_per_pixels = (bpm/60)/note_length    
    position += note_length*(bpm/60) * (1/60) 


    

