# UoP-Python-CW
Python3 coursework as part of my BSc Computer Science degree. 

TASK: 

  Your  task  is  to  write  a  program  to  display  patchwork  samples,  an  example  of  which  is illustrated below. The actual patchworks your program will display will depend on your student number and on the user’s inputs.

  A patchwork sample is made up of patches of two different designs and three colours. Patchworks are square and can be of three different sizes: 5×5,7×7 and 9×9.

  Each patch features a regular geometric design made up of lines, circles, rectangles and/or polygons and has dimensions of 100×100 pixels.  The two patch designs and the layout and colouring of patches are not necessarily as given in the sample on page 1. They are determined by the final three digits of your 6-digit student number, and are displayedin the tables on the final two pages. The layout and colouring of the patch designs is givenby the antepenultimate (fourth) digit of your student number. The two patch designs aregiven by the penultimate (fifth) and final (sixth) digits of your student number.

  ...

  Your program should draw the patches using the facilities provided in the graphics module (Line, Circle etc.), and must not use bitmapped images. The designs are intended to test algorithm development skills (e.g. they should involve the use of one or more for loops). For some of the designs, it will be useful to remember that shapes drawn later appear on top of those drawn earlier. You should not use parts of the Python language which we haven’t covered in this part of the unit; for example, do not use exception handling and do not define your own classes.
  
REQUIREMENTS:

Your program should begin by prompting the user, using a text (shell)-based interface, to enter:
  - The patchwork size (i.e. the common width & height in terms of patches)
   -The desired three colours (which your program should ensure are all different)

The program’s user interface should be easy to use, friendly and robust; e.g. on entering in-valid data, the user should be given appropriate feedback and re-prompted until the entered data is valid.  (Valid sizes are 5, 7 and 9, and valid colours are red, green, blue, magenta, orange and pink.)  Once these details have been entered, the patchwork sample should be drawn in a graphics window of the appropriate size.

ADDITIONAL CHALLENGE FEATURE:

After the patchwork design has been drawn, you should allow the user to edit the patch-work in the following way. The user should be able to select a patch by clicking on it with the mouse; the selected patch should be displayed with a thick black border. With a patchselected the user should be able to change it by pressing a key on the keyboard:
  - ‘d’ deletes the patch (leaving an empty space);
  - ‘s’ switches the patch to the other design, keeping the colour the same (this option should have no effect for a deleted (empty) patch);
  - (Only if the space is empty) Pressing the key of the initial letter of any valid colour (‘r’,‘g’, ‘b’, ‘m’, ‘o’ or ‘p’) creates a new patch of the final-digit design with this colour;•the Enter key deselects the patch;
  - All other keys have no effect.

Whilst selected, the user can perform as many operations on a patch as they like. Note that only one patch can be selected at any time, and the user needs to deselect the selected patch before selecting another. Ideally, the above operations should actually remove and recreate the graphics objects that make up patch designs, rather than drawing new objects on top of existing ones.


ADDITIONAL NOTES: 

  I originally create a way to escape the program using the escape key, which prevented an error upon exiting, however was advised to remove this due to the requirements specifying that all other keys should have no effect. 



