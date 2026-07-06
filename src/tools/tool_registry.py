from tools.file_tool import FileTool


class ToolRegistry:

    def __init__(self):

        self.tools = {
            "list resumes": FileTool()
        }

    def has_tool(self, command):

        return command in self.tools

    def execute(self, command):

        tool = self.tools[command]

        if command == "list resumes":
            return tool.list_files("data/resumes")