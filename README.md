# Pyxels

*A Wrapper for the Python Discord Pixels API*

## Usage

### Get Pixel

```py
from pyxels import Pyxels

p = Pyxels() # Starts an instance of the main class.

p.init(auth=token) # Authorizes with token 

pixel = p.get_pixel(0, 0) # Gets JSON object about the pixel at the given coordinates
```

### Get Image

```py
from pyxels import Pyxels

p = Pyxels() # Starts an instance of the main class.

p.init(auth=token) # Authorizes with token 

p.get_canvas() # Saves an image of the canvas at that moment.
```

### Set Pixel
```py
from pyxels import Pyxels

p = Pyxels() # Starts an instance of the main class.

p.init(auth=token) # Authorizes with token 

p.set_pixel(0, 0, "FFFFFF") # Sets the Pixel at 0, 0 to the value of FFFFFF, which is white.
```