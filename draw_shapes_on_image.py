""" draw_shapes_on_image.py

    example:
    
    python3.5 draw_shapes_on_image.py -i vehicular_traffic.jpg -s rectangle -lp1 610 530 -lp2 780 700
    
    python3.5 draw_shapes_on_image.py -i vehicular_traffic.jpg --shape line --line_p1 100 100 --line_p2 900 100

    python3.5 draw_shapes_on_image.py -i vehicular_traffic.jpg -s circle -cc 500 300 -r 50
    
    python3.5 draw_shapes_on_image.py -i vehicular_traffic.jpg -s text -lp1 100 100 -t HelloWorld
    
    python3.5 draw_shapes_on_image.py -i vehicular_traffic.jpg -s ellipse -cc 500 300 --axes 100 50
    
    python3.5 draw_shapes_on_image.py -i vehicular_traffic.jpg -s polygon --sides 20 80 60 50 100 80 80 120 40 120
    
    This script draws different geometric shapes on an image.
    
    This includes: 
        - lines
        - rectangles
        - circles
        - ellipses
        - polygons
        - text

    author: Raymundo Jimenez
    date created: February 18, 2018
    universidad de monterrey.
"""

# import required libraries
import numpy as np
import cv2 
import argparse


# ------------------------------------- #
# -------- UTILITY FUNCTIONS ---------- #
# ------------------------------------- #

# define function to draw a line
def draw_a_line(img, p1, p2, colour=(1,1,223), thickness=2, linetype=cv2.LINE_8):

    # draw a line on image
    cv2.line(img, p1, p2, colour, thickness, linetype)

    # return img 
    return img


# define function to draw a rectangle
def draw_a_rectangle(img, p1, p2, colour=(1,1,223), thickness=2, linetype=cv2.LINE_8):

    # draw a line on image
    cv2.rectangle(img, p1, p2, colour, thickness, linetype)

    # return img 
    return img

# define function to draw a circle
def draw_a_circle(img, cc, rad, colour=(1,1,223), thickness=2, linetype=cv2.LINE_8):
    
    #draw a circle on image
    cv2.circle(img, cc, rad, colour, thickness, linetype)
    
    #return image
    return img

#define function to draw an ellipse
def draw_an_ellipse(img, cc, axeslength, angle=0, sA=0, eA=360, colour=(1,1,223), thickness=2, linetype=cv2.LINE_8):
    
    #draw an ellipse on image
    cv2.ellipse(img, cc, axeslength, angle, sA, eA, colour, thickness, linetype)
    
    #return image
    return img


# define function to write text
def write_text(img, text, p1, font=cv2.FONT_HERSHEY_SIMPLEX, fontscale=4, colour=(1,1,223), thickness=2, linetype=cv2.LINE_8):
    
    #write text on image
    cv2.putText(img, text, p1, font, fontscale, colour, thickness, linetype)
    
    #return image
    return img

# define function to draw a polygon
def draw_a_polygon(img, list_of_coordinates, colour=(1,1,223)):
    
    #draw a polygon on image
    cv2.polylines(img, [list_of_coordinates], True, colour)
    
    #return image
    return img


# ------------------------------------- #
# ------------- MAIN CODE ------------- #
# ------------------------------------- #

# parse command line arguments

parser = argparse.ArgumentParser('Draw geometric shapes on an image')
parser.add_argument('-i', '--image', 
                    help='name of input image', type=str, required=True)
parser.add_argument('-s', '--shape', 
                    help='geometric shape to be drawn on the input image', type=str, required=True)
parser.add_argument('-lp1', '--line_p1', nargs='*', 
                    help='x,y coordinate of point 1', required=False)
parser.add_argument('-lp2', '--line_p2', nargs='*', 
                    help='x,y coordinate of point 2', required=False)
parser.add_argument('-cc', '--center', nargs='*',
                    help='center coordinate', required=False)
parser.add_argument('-r', '--radius', nargs='*',
                    help='measurement of the radius', required=False)
parser.add_argument('-t', '--text', 
                    help='enter the text', required=False)
parser.add_argument('-a', '--axes', nargs='*',
                    help='axes length of the ellipse', required=False)
parser.add_argument('--sides', nargs='*',
                    help='write the coordinate for each point', required=False)
args = vars(parser.parse_args())

# retrieve name of input image given as argument from command line
img_in_name = args['image']

# read in image from disk
img_in = cv2.imread(img_in_name, cv2.IMREAD_COLOR) # alternatively, you can use cv2.IMREAD_GRAYSCALE

# verify that image exists
if img_in is None:
    print('ERROR: image ', img_in_name, 'could not be read')
    exit()

# retrieve geometric shape name
geometric_shape = args['shape']

# if geometric shape is a line or rectangle
if (geometric_shape == 'line') or (geometric_shape == 'rectangle'):

    # retrieve line features
    line_p1 = args['line_p1']
    line_p2 = args['line_p2']

    # if '--line' is specified, but either '--line_p1' or 
    # '--line_p2' is missing, ask the user to enter 
    # the corresponding coordinate
    if (line_p1 is None) or (line_p2 is None):

        # ask user enter line coordinates
        print('ERROR: line coordinate missing')
        exit()            

    # otherwise
    else:

        # retrieve line coordinates
        line_p1 = tuple(list(map(int, line_p1)))
        line_p2 = tuple(list(map(int, line_p2)))

        # check that each coordinate is of length 2
        if len(line_p1) == 2 and len(line_p2)==2:        

            # if drawing a line
            if geometric_shape == 'line':
                      
                # call 'draw_a_line' 
                img_in = draw_a_line(img_in, line_p1, line_p2, (255,0,0), 2)
          
            # if drawing a rectangle
            elif geometric_shape == 'rectangle':
            
                # call 'draw_a_rectangle'
                img_in = draw_a_rectangle(img_in, line_p1, line_p2, (255, 0, 0), 2)

        # otherwise    
        else:
          
            # ask the user enter a valid line coordinate
            print('ERROR: both p1 and p2 coordinates must be of length 2')
            exit()   
            
elif (geometric_shape == 'circle') or (geometric_shape == 'ellipse'):
    
    #retrieve circle/ellipse features
    center = args['center']
    axes = args['axes']
    radius = args['radius']
    
    #validate that the user entered the center coordinates 
    if (center is None):
        
        #ask user to enter the center coordinates
        print('ERROR: center coordinates missing')
        exit()
    
    #otherwise 
    else:
        
        #retrieve center coordinates
        center = tuple(list(map(int, center)))
        
        #check that the coordinate is of length 2
        if len(center) == 2:
            
            if geometric_shape == 'circle':
                
                #validate radius
                if (radius is None):
                
                    #ask user to enter the radius
                    print('ERROR: radius missing')
                    exit()
                
                #otherwise
                else:
                
                    #retrieve radius
                    radius = tuple(list(map(int, radius)))
                    rad = radius[0]
                    
                    #call 'draw_a_circle'
                    img_in = draw_a_circle(img_in, center, rad)
                    
            elif geometric_shape == 'ellipse':
                
                if (axes is None):
                    
                    #ask the user to ente the axes
                    print('ERROR: ellipse axes missing')
                    exit()
                    
                else:
                
                    #retrieve the axes
                    axes = tuple(list(map(int, axes)))

                    #check that the axes are of length 2
                    if len(axes) ==2:
                        
                        #call 'draw_an_ellipse
                        img_in = draw_an_ellipse(img_in, center, axes)
                        
                    else:
                        
                        #ask the user to enter a valid axes length
                        print('ERROR: ellipse axes must be length of 2')
                    
                    
                
        else:
            
            #ask the user to enter a valid center coordinate
            print('ERROR: the center coordinate must be of length 2')
            exit()
            
elif (geometric_shape == 'text'):
    
    #retrieve text features
    line_p1 = args['line_p1']
    text = args['text']
    
    #validate that the user entered the coordinates
    if (line_p1 is None):
        
        #ask the user to enter the coordinate
        print('ERROR: Enter the coordinate')
        exit()
        
    #otherwise
    else:
        
        #retrieve the coordinate
        line_p1 = tuple(list(map(int, line_p1)))
        
        #check that the coordinate is length 2
        if len(line_p1) == 2:
            
            #check that the user entered a text
            if (text is None):
                
                #ask the user to enter the text
                print('ERROR: Enter the text')
                exit()
                
            else:
                
                #call write_text
                img_in = write_text(img_in, text, line_p1)
            
        else: 
            
            #ask the user to enter a valid coordinate
            print('ERROR: the coordinate must be of length 2')
            exit()

elif (geometric_shape == 'polygon'):
    
    #retrieve sides features
    list_of_coordinates = args['sides']
    
    #validate that the user entered the coordinates 
    if (list_of_coordinates is None):
        
        #ask the user to enter the coordinates
        print('ERROR: coordinates missing')
        exit()
        
    else:
        
        #calculate number of coordinates
        x = len(list_of_coordinates)
        
        #calculate image features
        img_size = img_in.shape
        width = img_size[0]
        height = img_size[1]
        
        #convert the list into an array format 
        list_of_coordinates = np.asarray(list_of_coordinates, np.int32)
        
        #verify that the coordinates are inside the image
        for i in range(0,x,2):
            
            if width<list_of_coordinates[i]:
                
                #ask the user to verify the coordinates
                print('ERROR: X coordinate is out of range')
                exit()
                
            elif height<list_of_coordinates[i+1]:
                
                #ask the user to verify the coordinates
                print('ERROR: Y coordinate is out of range')
                exit()
        
        
        list_of_coordinates = list_of_coordinates.reshape(-1,1,2)
        
        #call draw_a_polygon
        img_in = draw_a_polygon(img_in, list_of_coordinates)



# create a new window for image purposes
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)  # alternatively, you can use cv2.WINDOW_NORMAL

# visualise input and output image
cv2.imshow("input image", img_in)

# wait for the user to press a key 
key = cv2.waitKey(0)

# destroy windows to free memory  
cv2.destroyAllWindows()
print('windows have been closed properly')
exit()
