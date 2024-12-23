from PIL import Image, ImageDraw, ImageFont

class ImageHandler():
    def __init__(self,file_path,texty,file_save):
        self.file_path = file_path
        self.write_text = texty
        self.file_save = file_save

        with Image.open(self.file_path).convert("RGBA").resize((1080, 1080)) as base:
            text = Image.new("RGBA", base.size, (255, 255, 255, 0))
            font = ImageFont.truetype("arial.ttf", 100)
            draw = ImageDraw.Draw(text)
            draw.text((10, 950), text=self.write_text, font=font, fill=(255, 255, 255, 255))
            watermarked = Image.alpha_composite(base, text)
            watermarked.save(self.file_save,extension='png')
