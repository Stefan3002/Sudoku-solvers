import os
import subprocess
from time import sleep

from analyze_bed import sudoku_performance_all_methods, sudoku_methods, sudoku_puzzles


warm_up_time = 3

algo_start = subprocess.Popen(['python3', 'algo_start.py'])
pid = algo_start.pid
sleep(warm_up_time)
subprocess.Popen(['nohup', 'sudo', '-S', '/home/stefan/PycharmProjects/sudoku_bfs/.venv/bin/py-spy', 'record', '--pid', str(pid), '--output', '/home/stefan/PycharmProjects/sudoku_bfs/profile.json', '--rate', '100', '--format', 'speedscope'])
algo_start.wait()