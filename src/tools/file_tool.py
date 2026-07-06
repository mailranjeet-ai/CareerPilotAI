from pathlib import Path


class FileTool:

    def list_files(self, folder):

        path = Path(folder)

        if not path.exists():
            return []

        return [file.name for file in path.iterdir() if file.is_file()]
    exit
    