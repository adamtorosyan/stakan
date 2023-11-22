from PIL import Image


class ImgMinion:
    ex = ["png", "jpg", "jpeg", "gif", "tiff", "bmp", "webp", "svg", "ico"]

    def get_meta_inf(self, path):
        try:
            with Image.open(path) as img:
                width, height = img.size
                format = img.format
                mode = img.mode

                # 1. Color Channels
                num_channels = len(img.getbands())

                # 2. Color Palette
                if mode == "P":
                    palette = img.getpalette()
                else:
                    palette = None

                # 3. DPI (Dots Per Inch)
                dpi = img.info.get("dpi")

                # 4. Histogram
                histogram = img.histogram()

                # 5. EXIF Data
                exif_data = img.getexif() if "exif" in img.info else None

                # 6. Alpha Channel
                alpha_channel = img.split()[-1] if img.mode.endswith("A") else None

                # 7. Orientation
                orientation = exif_data.get(274) if exif_data else None

                # 8. Bits per Channel
                bits_per_channel = img.info.get("bits")

                # 9. Compression Method
                compression = img.info.get("compression")

                # 10. Image Enhancement/Manipulation
                enhancement = img.info.get("enhancement")

                # 11. GPS Coordinates
                gps_info = (
                    exif_data.get(34853) if exif_data and 34853 in exif_data else None
                )

                # 12. Model and Brand of Camera
                camera_model = (
                    exif_data.get(272) if exif_data and 272 in exif_data else None
                )
                camera_brand = (
                    exif_data.get(271) if exif_data and 271 in exif_data else None
                )

                # 13. Date of Photo
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
