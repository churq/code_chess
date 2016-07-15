For windows:
============

1. set system variable PYTHONPATH=C:\Users\xxxxx\PycharmProjects\chess\code_chess
2. run in cmd prompt
   python .\code_chess\chess\main.py --start [start_position] --end [end_position]


C:\Users\xxxxx\PycharmProjects\chess\code_chess\chess>python main.py --start a1 --end d4
a1-b3-a5-c6-d4
a1-b3-c1-e2-d4
a1-b3-c5-e6-d4
a1-b3-d4
a1-b3-d2-f3-d4
a1-c2-a3-b5-d4
a1-c2-b4-c6-d4
a1-c2-d4
a1-c2-e1-f3-d4
a1-c2-e3-f5-d4
**********
Finished

3. unit tests: python .\code_chess\test\test_main.py