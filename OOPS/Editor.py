class Editor:
    def __init__(self,name,vendor):
        self.name=name
        self.vendor=vendor

    def open(self):
        print(f"{self.name} open")

    def execute(self):
        print(f"{self.vendor} execute")

class Vscode(Editor):
    def __init__(self,name,vendor):
        super().__init__(name,vendor)

class Pycharm(Editor):
    def __init__(self,name,vendor):
        super().__init__(name,vendor)


vscode_instance=Vscode("visualstudiocode","vscodevendor")
vscode_instance.open()

pycharm_instance=Pycharm("pycharm","jetbrains")
pycharm_instance.open()

