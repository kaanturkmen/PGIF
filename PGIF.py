
########################################################
#           Feel free to use, share, modify.           #
#                 Author: Kaan Turkmen                 #
#                 github.com/katurkmen                 #
#########################################################

# Importing pygame.
import pygame

class PGIF(object):
    def __init__(self, path, name, extension, image_count, canvas, location, scale_to, update=True):
        """
        :param path: Path of the image. Such that "media/walking_frames/"
        :type path: String
        :param name: Name of the each image. Please select all and rename it. Such that "walk"
        When renaming it, OS will automatically rename it as walk (1) walk (2) ... I am taking care of that in the class
        :type name: String
        :param extension: Extension of image. Such as "png", "jpg" ... or anything pygame supports.
        :type extension: String
        :param image_count: Count of the image frames.
        :Type param: Integer
        :param canvas: Canvas that you created in your program.
        :type canvas: Pygame Surface
        :param location: Location of where should image displayed. Such as (0, 0)
        :type location: List
        :param scale_to: Resolution of new scaled version of image. For instace if image is 1920x1080 and you want to
        scale to 1280x1070, use (1280, 720).
        :type scale_to: List
        :param update: Checks if the user wants to refresh screen after its being added.
        :type update: Boolean
        """
        self.path = path
        self.name = name
        self.extension = extension
        self.image_count = image_count
        self.canvas = canvas
        self.location = location
        self.scale_to = scale_to
        self.update = update
        self.setup()

    def setup(self):
        # Creates list to add each frame.
        glist = []

        # Adding path information to the list.
        for i in range(self.image_count):
            glist.append(self.path + self.name + ' (' + str(i + 1) + ').' + self.extension)

        # Printing every frame to the canvas.
        for frame in glist:
            try:
                image = pygame.image.load(frame)
            except:
                print('ERROR: System could not read GIF Image(s)')
            else:
                image = pygame.transform.scale(image, self.scale_to)
                self.canvas.blit(image, self.location)

        if self.update:
            pygame.display.update()
