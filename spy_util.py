import os
import subprocess
import sys

from dotenv import load_dotenv

load_dotenv()
sudo_password = os.getenv('SUDO_PASSWORD')

def start_spy():
    # pid = algo_start.pid
    if os.path.isfile("/home/stefan/PycharmProjects/sudoku_bfs/profile.json"):
        os.remove("/home/stefan/PycharmProjects/sudoku_bfs/profile.json")
    # print(pid)
    print("RECORDING")
    process = subprocess.Popen(
        ['nohup', 'sudo', '-S', '/home/stefan/PycharmProjects/sudoku_bfs/.venv/bin/py-spy', 'record'
            , '--output', '/home/stefan/PycharmProjects/sudoku_bfs/profile.json', '--rate', '1000', '--format',
         'speedscope', '--', '/home/stefan/PycharmProjects/sudoku_bfs/.venv/bin/python3', '/home/stefan/PycharmProjects/sudoku_bfs/aux.py'],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    process.communicate(input=sudo_password.encode())
    stdout, stderr = process.communicate()
    print("STDOUT:", stdout.decode())
    print("STDERR:", stderr.decode())
    process.wait()
    print("DONE RECORDING")

start_spy()