from threading import Thread

class PyMouseMeta(object):

    def press(self, x, y, button = 1):
        """Press the mouse on a givven x, y and button.
        Button is defined as 1 = left, 2 = right, 3 = middle."""

        raise NotImplementedError

    def release(self, x, y, button = 1):
        """Release the mouse on a givven x, y and button.
        Button is defined as 1 = left, 2 = right, 3 = middle."""

        raise NotImplementedError

    def click(self, x, y, button = 1, n = 1):
        """Click a mouse button n times on a given x, y.
        Button is defined as 1 = left, 2 = right, 3 = middle.
        """

        for i in range(n):
            self.press(x, y, button)
            self.release(x, y, button)
 
    def move(self, x, y):
        """Move the mouse to a givven x and y"""

        raise NotImplementedError

    def position(self):
        """Get the current mouse position in pixels.
        Returns a tuple of 2 integers"""

        raise NotImplementedError

    def screen_size(self):
        """Get the current screen size in pixels.
        Returns a tuple of 2 integers"""

        raise NotImplementedError

class PyMouseEventMeta(Thread):
    def __init__(self, capture=False, captureMove=False):
        Thread.__init__(self)
        self.daemon = True
        self.capture = capture
        self.captureMove = captureMove
        self.state = True

    def stop(self):
        self.state = False

    def click(self, x, y, button, press):
        """Subclass this method with your click event handler"""

        pass

    def move(self, x, y):
        """Subclass this method with your move event handler"""

        pass
