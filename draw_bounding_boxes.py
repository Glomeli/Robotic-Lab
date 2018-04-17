""" draw_bounding_boxes.py

    add a description of your code here

    author: Raymundo Jimenez
    date created: February 20, 2018
    universidad de monterrey.
"""

# import required libraries
import numpy as np
import cv2 
import argparse


# ------------------------------------- #
# -------- UTILITY FUNCTIONS ---------- #
# ------------------------------------- #

# draw bounding boxes on image
def draw_bboxes(img, bbox):

    # loop through bounding boxes
    i=1
    for bbox in list_of_bounding_boxes:
        
        # retrieve features of a given rectangle
        p1 = tuple(bbox[0])
        p2 = tuple(bbox[1])
        colour = tuple(bbox[2])
        thickness = bbox[3]

        # draw a line on image
        cv2.rectangle(img, p1, p2, colour, thickness, cv2.LINE_8)

        # draw text
        ttext='car '+str(i)
        ttext_type=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, ttext, (p1[0], p1[1]-5), ttext_type, 0.7, colour, thickness, cv2.LINE_8)

        i=i+1

        # draw a line on image
        print('drawing rectangle: ', tuple(bbox[0]), ',', 
                                     tuple(bbox[1]), ',', 
                                     tuple(bbox[2]), ',', 
                                     bbox[3])
        
    # return img 
    return img


# draw text on image 
def draw_frame_description(img, ttext):
    
    # add text to image
    cv2.putText(img, ttext, (20,30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2, cv2.LINE_8)
    
    return img
    
    

# ------------------------------------- #
# ------------- MAIN CODE ------------- #
# ------------------------------------- #

####### ADD MORE BOUNDING BOXES HERE #######
# list of bounding boxes 
list_of_bounding_boxes = [
                          [[610, 530], [780, 700], [255, 0, 0], 2],
                          [[830, 410], [955, 520], [0, 255, 0], 2],
                          [[585, 248], [645, 309], [0, 0, 255], 2],
                          [[675, 220], [740, 280], [0, 120, 255], 2],
                          [[582, 142], [614, 171], [120, 0, 255], 2],
                          [[634, 115], [660, 138], [255, 120, 0], 2],
                          [[689, 107], [718, 130], [120, 120, 120], 2],
                          [[615, 83], [636, 104], [0, 120, 0], 2]
                         ]
####### ---------------------------- #######

# read in image from disk
img_name = 'vehicular_traffic.jpg'
img = cv2.imread(img_name, cv2.IMREAD_COLOR) # alternatively, you can use cv2.IMREAD_GRAYSCALE

# verify that image exists
if img is None:
    print('ERROR: image ', img_name, 'could not be read')
    exit()

# draw list of bounding boxes on image
img = draw_bboxes(img, list_of_bounding_boxes)

# draw text on image
img = draw_frame_description(img, 'Vehicle detection on a highway')


# create a new window for image purposes
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)  # alternatively, you can use cv2.WINDOW_NORMAL

# visualise input and output image
cv2.imshow("input image", img)

# wait for the user to press a key 
key = cv2.waitKey(0)

# destroy windows to free memory  
cv2.destroyAllWindows()
print('windows have been closed properly')
exit()