from PIL import Image, ImageDraw, ImageFont

WIDTH = 128
HEIGHT = 32
BORDER = 5


def generate_image(title, text, highlighted=False, next=False):
        font_path = "/home/pi/Roboto-Thin.ttf"

        # Create blank image for drawing.
        # Make sure to create image with mode '1' for 1-bit color.
        image = Image.new("1", (WIDTH, HEIGHT))

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(image)

        # Draw a smaller inner rectangle
        # self.draw.rectangle(
        #     (self.border, self.border, self.width - self.border - 1, self.height - self.border - 1),
        #     outline=0,
        #     fill=0,
        # )

        # Draw a white background
        draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)

        # Load default font.
        font = ImageFont.truetype(font_path, 15)

        #Draw title
        (title_width, title_height) = font.getsize(title)
        draw.rectangle((0, 0, title_width, title_height), outline=1, fill=255)
        draw.text(
            (0, 0), title, font=font, fill=0
        )

        # Draw Some Text
        (font_width, font_height) = font.getsize(text)
        if highlighted:
            draw.rectangle((WIDTH // 2 - font_width // 2, HEIGHT - font_height,
                            WIDTH // 2 + font_width // 2, HEIGHT + font_height), outline=0, fill=255)

            draw.text(
                (WIDTH // 2 - font_width // 2, HEIGHT - font_height),
                text,
                font=font,
                fill=0,
            )
        else:
            draw.text(
                (WIDTH // 2 - font_width // 2, HEIGHT - font_height),
                text,
                font=font,
                fill=255,
            )

        if next:
            (arr_width, arr_height) = font.getsize(">")
            draw.text(
                (WIDTH - arr_width, HEIGHT // 2 - arr_height // 2),
                ">",
                font=font,
                fill=255
            )

        return image
