from PIL import Image


class ImgMinion:
    ex = ["png", "jpg", "jpeg", "gif", "tiff", "bmp", "webp", "svg", "ico"]

    def get_meta_inf(self, path):
        try:
            with Image.open(path) as img:
                width, height = img.size
                format = img.format
                mode = img.mode

            metadata = {
                "Width": width,
                "Height": height,
                "Format": format,
                "Mode": mode,
            }
            return metadata
        except Exception as e:
            return {"error": str(e)}
