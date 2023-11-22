from PIL import Image


class ImgMinion:
    ex = ["png", "jpg", "jpeg", "gif", "tiff", "bmp", "webp", "svg", "ico"]

    def get_meta_inf(self, path):
        try:
            with Image.open(path) as img:
                width, height = img.size
                format = img.format
                mode = img.mode
                num_channels = len(img.getbands())
                if mode == "P":
                    palette = img.getpalette()
                else:
                    palette = None
                dpi = img.info.get("dpi")
                histogram = img.histogram()
                exif_data = img._getexif() if "exif" in img.info else None  # type: ignore
                alpha_channel = img.split()[-1] if img.mode.endswith("A") else None
                orientation = exif_data.get(274) if exif_data else None
                bits_per_channel = img.bits if hasattr(img, "bits") else None  # type: ignore
                compression = img.info.get("compression")
                enhancement = img.info.get("enhancement")
                gps_info = (
                    exif_data.get(34853) if exif_data and 34853 in exif_data else None
                )
                camera_model = (
                    exif_data.get(272) if exif_data and 272 in exif_data else None
                )
                camera_brand = (
                    exif_data.get(271) if exif_data and 271 in exif_data else None
                )
                date_taken = (
                    exif_data.get(36867) if exif_data and 36867 in exif_data else None
                )

            metadata = {
                "Width": width,
                "Height": height,
                "Format": format,
                "Mode": mode,
                "Channels": num_channels,
                "Palette": palette,
                "DPI": dpi,
                "Histogram": histogram,
                "EXIF": exif_data,
                "Alpha Channel": alpha_channel is not None,
                "Orientation": orientation,
                "Bits per Channel": bits_per_channel,
                "Compression": compression,
                "Enhancement": enhancement,
                "GPS Coordinates": gps_info,
                "Camera Model": camera_model,
                "Camera Brand": camera_brand,
                "Date Taken": date_taken,
            }
            return metadata
        except Exception as e:
            return {"error": str(e)}
