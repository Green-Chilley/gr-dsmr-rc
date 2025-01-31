"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt
import csv
import time
import os

class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """A python block that takes in values from channels and outputs them as a graph"""

    def __init__(self, param=1):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Graph',   # will show up in GRC
            in_sig=[],
            out_sig = []
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.param = param
        self.message_port_register_in(pmt.intern("Value"))
        self.set_msg_handler(pmt.intern("Value"), self.graph_values)
        self.channel_data = np.zeros((2,7))
        self.header_written = False
        self.start_time = time.time()

    def elapsed_time(self):
        curr_time = time.time() - self.start_time
        return (curr_time)
    
    def graph_values(self, msg):
        meta = pmt.car(msg)
        data = pmt.cdr(msg)
        if not pmt.is_u8vector(data):
            print("Invalid message type")
            return
        path = 'channel_data.csv2'
        with open(path, 'a+', newline='', encoding='utf-8') as channel_csv:
            c = csv.writer(channel_csv)
            if not self.header_written:
                c.writerow( ['CH0', 'CH1', 'CH2', 'CH3', 'CH4', 'CH5', 'CH6', 'Time'] )
                self.header_written = True
            for i in range(0,7):
                tmp = pmt.to_python(pmt.dict_ref(meta, pmt.intern(str(i)), pmt.PMT_NIL))
                if tmp:
                    self.channel_data[0][i] = int(tmp)
                else:
                    self.channel_data[0][i] = 8192
            curr_time = self.elapsed_time()

            the_data = list()
            for i in range(0,7):
                the_data.append('{:03.2f}'.format(((int(self.channel_data[0][i]) & 0xfff)/2048.0) -1))
            the_data.append(curr_time)
            c.writerow(the_data)

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        output_items[0][:] = input_items[0] * self.param
        return len(output_items[0])
