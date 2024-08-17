import pygame as pg
from midiParser import instruments, midi_data
import vid

import random
import utils
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

instrument_list = []
note_colours1 = [
    (255, 105, 180),  # Hot Pink
    (255, 165, 0),    # Orange
    (144, 169, 255),    # periwinkle
    (127, 196, 212),  # nice blue
    (219, 89, 96),    # Tomato
    (138, 43, 226),   # Blue Violet
    (255, 69, 0),     # Red Orange
    (50, 189, 50),    # Lime Green
    (255, 215, 0),    # Gold
    (147, 112, 219),  # Medium Purple
    
]
note_colours2 = [
    (102, 51, 0),      # Dark brown
    (205, 133, 63),    # Copper
    (128, 0, 0),       # Dark red
    (34, 139, 34),     # Forest green
    (75, 0, 130),      # Purple
    (0, 191, 255),     # Bright blue
    (51, 25, 0),      # Darker brown
    (139, 69, 19),     # Darker copper
    (85, 42, 10),     # Deep brown
    (46, 139, 87),     # Darker green
    (105, 105, 105),    # Dark gray
    (178, 34, 34),     # Crimson
    (0, 100, 0),      # Dark green
    (128, 0, 128),     # Purple
    (0, 0, 139)       # Navy blue
]
bg_colour = (220, 230, 240)
bg_colour_2 = (245, 222, 179)

# index = 0
random.shuffle(note_colours2)
print(f"there are {len(instruments)} number of inst")

instruments.reverse()

# getting info about the song, in this case right now its just the max and min pitch
for index, instrument in enumerate(instruments):
        
        # adding new attributes to instrument and notes objects
        setattr(instrument, "colour", None)
        setattr(instrument, "speed", None)
        setattr(instrument, "icon", None)

        '''
        layer may be useful, but i will be using index and enumerate for now. 
        '''
        # setattr(instrument, "layer", index) 
        # setattr(instrument.notes, "is_clicked", None)

        instrument_name = instrument.name
        # instrument_colour = input(f"what colour should the {instrument_name} be? ")
        instrument_colour = note_colours2[index]
        print(instrument_colour)
        # input_colour = instrument_colour.split(',')
        # instrument_colour = tuple(map(int, input_colour))
        instrument_speed = float(input(f"what speed should the {instrument_name} be? "))
        # instrument_icon =input(f"what icon should the {instrument_name} be? ")
        instrument.colour = instrument_colour
        instrument.speed = instrument_speed
        

        '''
        Code to switch around order of instrument layers, will probably need to update when integrating
        with gui. Nevermind, its a pain to do it now, ill just wait till gui 
        '''
        # temp_instrument = instruments[index]
        # new_index = int(input(f"what layer should the {instrument_name} be? "))
        # instruments[index] = instruments[new_index]
        # instruments[new_index] = temp_instrument

        # instrument.icon = instrument_icon
        
        

        for note in instrument.notes:
            setattr(note, "click_status", 0)
            setattr(note, "y_pos", 0)
            if max_pitch < note.pitch:
                max_pitch = note.pitch
            if min_pitch > note.pitch:
                min_pitch = note.pitch

        start = note.start
        end = note.end
        pitch = note.pitch
        velocity = note.velocity

        # increase index
        # index += 1
        # notes_list.append(Note(start, end, pitch, velocity, end-start))
        

                
print(max_pitch)
print(min_pitch)


num_pitches = 110 # there are 128 for real
position = 0
line_x = 600


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            vid.video.release()

  
    # clean screen with bg colour
    screen.fill(bg_colour_2)

    # DELAY if i want to use it ever. "w key"
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        pg.time.delay(1000)
  
    # iterating through each note
    for instrument in instruments:
        # print(instrument)
        instrument_colour = instrument.colour
        instrument_speed = instrument.speed
        # speed
        temp_length = note_length*instrument_speed

        
        # instrument_icon = instrument.icon
        for note in instrument.notes:
            start = note.start
            end = note.end
            pitch = note.pitch
            velocity = note.velocity
            note_colour = instrument_colour
            note_tempo = bpm # place holder, i can make a more dynamic way of getting the accurate tempo for tempo changes

            # note properties
            rect_width = (end-start)*temp_length * (note_tempo/60)*0.9 # - 4 or soemthing for aesthetic reasons
            rect_height = display_height/num_pitches
            rect_x = line_x + (starting_position-line_x)*instrument_speed+ start*temp_length * (note_tempo/60) - position*instrument_speed
            rect_y = (num_pitches - pitch - 1) * rect_height
      
            # print(note.click_status)

            if rect_x < 605 and rect_x > line_x-rect_width - 500:
                if note.click_status != 4: # 4 = done clicking

                    if note.click_status == 3: # 3 = clicked
                        note.y_pos -= 1
                        rect_y += note.y_pos    
                        if note.y_pos <= 2:
                            note.click_status = 4
                        

                    elif note.click_status == 2: # 2=  clicking
                        rect_y += note.y_pos
                        if rect_x <600-rect_width *1.2:
                            note.click_status = 3
                            
                

                    elif note.click_status == 1: # 1= clicked
                        note.y_pos += 1
                        rect_y += note.y_pos    
                        if note.y_pos >= 7:
                            note.click_status = 2
                           
                    
                    elif note.click_status == 0: # 0 = not clicked
                        if rect_x <= 600: 
                            note.click_status = 1 
                            
            if note.click_status in [1,2,3]: # if note in process of getting clicked
                note_colour = utils.lighten_colour(instrument_colour,0.2) # lighten the colour
            else:
                note_colour = instrument_colour 

            # rect_color = (204, 51, 51)  # Red color
            rect_color = note_colour

            pg.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
            pg.display.update(pg.Rect(rect_x, rect_y, rect_width, rect_height))
            
            # pg.time.delay(10)
            # print("rectangle")
            # print(note)
 
    pg.display.update()
    
 # the line
    line_start = (line_x,0)
    line_end = (line_x,720)
    line_width = 5
    line_colour = (225,225,225)
    pg.draw.line(screen, line_colour, line_start, line_end, line_width)



    vid.vid_generator(screen)
    clock.tick(60) 
    # beat_per_pixels = (bpm/60)/note_length    
    position += note_length*(bpm/60) * (1/60) 


    

