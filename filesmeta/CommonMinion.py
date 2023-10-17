import datetime
import os


class CommonMinion:
    ex = ["*"]

    def collect_common_metadata(self, path):
        metadata = {}

        if os.path.exists(path):
            file_size = os.path.getsize(path)
            creation_date = datetime.datetime.fromtimestamp(
                os.path.getctime(path)
            ).strftime("%Y-%m-%d %H:%M:%S")
            modification_date = datetime.datetime.fromtimestamp(
                os.path.getmtime(path)
            ).strftime("%Y-%m-%d %H:%M:%S")

            metadata["File Name"] = os.path.basename(path)
            metadata["File Size"] = file_size
            metadata["File Path"] = path
            metadata["Creation Date"] = creation_date
            metadata["Modification Date"] = modification_date
        else:
            metadata["error"] = f"File not found at '{path}'"

        return metadata
