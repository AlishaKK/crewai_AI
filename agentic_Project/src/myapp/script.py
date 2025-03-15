import subprocess

def run():
    subprocess.run(["chainlit", "run", ".//src//myapp//chainlit_app.py", "-w"])