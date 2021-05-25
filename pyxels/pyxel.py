import requests
from PIL import Image

class Pyxels:
    def __init__(self):
        self.token = None
        self.headers = None

    def init(self, auth):
        self.token = auth
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def get_pixel(self, x: int = 0, y: int = 0):
        """Returns a JSON object about a given pixel.

        Params:

        x: integer, y: integer

        JSON:

        Returns x and y coordinates, and an RGB value.
        """

        pixel = requests.get(
            "https://pixels.pythondiscord.com/get_pixel",
            headers=self.headers,
            params={
                "x": x,
                "y": y
            }
        )

        return pixel.json()
    
    def get_canvas(self):
        """Saves an image of the current canvas."""
        r = requests.get("https://pixels.pythondiscord.com/get_size")
        size = r.json()
        r = requests.get(
            "https://pixels.pythondiscord.com/get_pixels",
            headers=self.headers
        )
        imgbytes = bytes(r.content)

        image = Image.frombytes(mode="RGB", size=(size["width"], size["height"]), data=imgbytes)

        image.save("canvas.png")

    def set_pixel(self, x: int = 0, y: int = 0, color: str="00FF00"):
        """Sets a pixel on the Canvas, and returns the message."""
        
        r = requests.post(
            "https://pixels.pythondiscord.com/set_pixel",
            json={
                "x": x,
                "y": y,
                "rgb": color
            },
            headers=self.headers
        )
        payload = r.json()

        return payload["message"]