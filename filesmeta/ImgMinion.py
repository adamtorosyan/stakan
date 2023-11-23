from PIL import Image


class ImgMinion:
    ex = ["png", "jpg", "jpeg", "gif", "tiff", "bmp", "webp", "svg", "ico"]

    def get_meta_inf(self, path):
        try:
            with Image.open(path) as img:
                width, height = img.size
                format = img.format
                mode = img.mode

                # Additional metadata properties
                channels = img.getbands() if mode == "P" else img.getbands()
                bit_depth = self.calculate_bit_depth(mode)
                compression = (
                    img.info.get("compression") if hasattr(img, "info") else None
                )
                icc_profile = (
                    img.info.get("icc_profile") if hasattr(img, "info") else None
                )
                orientation = (
                    img.info.get("orientation") if hasattr(img, "info") else None
                )

            metadata = {
                "Width": width,
                "Height": height,
                "Format": format,
                "Mode": mode,
                "Channels": channels,
                "Bit Depth": bit_depth,
                "Compression": compression,
                "ICC Profile": icc_profile,
                "Orientation": orientation,
            }
            return metadata
        except Exception as e:
            return {"error": str(e)}

    def calculate_bit_depth(self, mode):
        # Calculate bit depth based on the mode
        if mode in ("L", "P"):
            return 8
        elif mode in ("RGB", "RGBA"):
            return 24
        elif mode == "CMYK":
            return 32
        else:
            return None
