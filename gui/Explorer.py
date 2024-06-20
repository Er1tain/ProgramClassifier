import subprocess

class Explorer:
    @staticmethod
    def open_explorer():
        subprocess.Popen(r'explorer /select')
