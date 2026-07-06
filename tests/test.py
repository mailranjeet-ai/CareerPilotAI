import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.tools.file_tool import FileTool

tool = FileTool()

files = tool.list_files("data/resumes")

print(files)