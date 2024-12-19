#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.10.11.0

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import analog
import math
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import uhd
import time
import datetime
import gnuradio.dsmx as dsmx
import os
import sip
import threading
import top_block_chan_change as chan_change  # embedded python block



class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("gnuradio/flowgraphs", "top_block")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)
        self.flowgraph_started = threading.Event()

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 25e6
        self.rootdir = rootdir = str(os.path.expanduser("~")+"/")
        self.record_file_path = record_file_path = "data/"
        self.note = note = 'RECORDING_NOTE'
        self.intermediate_samp_rate = intermediate_samp_rate = samp_rate
        self.gui_samp_rate = gui_samp_rate = samp_rate
        self.top_block_fournisseur = top_block_fournisseur = 0
        self.timestamp = timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d_%H:%M:%S')
        self.sps = sps = int(intermediate_samp_rate/1e6)
        self.rec_button = rec_button = 0
        self.nfilts = nfilts = 32
        self.max_intensity = max_intensity = 50
        self.filename = filename = rootdir+record_file_path+note+"_"+str(int(gui_samp_rate))+"sps_"
        self.f_deviation = f_deviation = 1e6
        self.channel = channel = 5
        self.RX_gain = RX_gain = 10

        ##################################################
        # Blocks
        ##################################################

        self.tabs = Qt.QTabWidget()
        self.tabs_widget_0 = Qt.QWidget()
        self.tabs_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.tabs_widget_0)
        self.tabs_grid_layout_0 = Qt.QGridLayout()
        self.tabs_layout_0.addLayout(self.tabs_grid_layout_0)
        self.tabs.addTab(self.tabs_widget_0, 'Tab 0')
        self.top_grid_layout.addWidget(self.tabs, 0, 0, 7, 4)
        for r in range(0, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 4):
            self.top_grid_layout.setColumnStretch(c, 1)
        _rec_button_push_button = Qt.QPushButton('RECORD')
        _rec_button_push_button = Qt.QPushButton('RECORD')
        self._rec_button_choices = {'Pressed': 1, 'Released': 0}
        _rec_button_push_button.pressed.connect(lambda: self.set_rec_button(self._rec_button_choices['Pressed']))
        _rec_button_push_button.released.connect(lambda: self.set_rec_button(self._rec_button_choices['Released']))
        self.tabs_grid_layout_0.addWidget(_rec_button_push_button, 1, 3, 1, 1)
        for r in range(1, 2):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(3, 4):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self._gui_samp_rate_range = qtgui.Range(200e3, 56e6, 1e6, samp_rate, 200)
        self._gui_samp_rate_win = qtgui.RangeWidget(self._gui_samp_rate_range, self.set_gui_samp_rate, "samp_rate", "counter_slider", float, QtCore.Qt.Horizontal)
        self.tabs_layout_0.addWidget(self._gui_samp_rate_win)
        self._channel_range = qtgui.Range(0, 100, 1, 5, 1)
        self._channel_win = qtgui.RangeWidget(self._channel_range, self.set_channel, "'channel'", "counter_slider", int, QtCore.Qt.Horizontal)
        self.tabs_layout_0.addWidget(self._channel_win)
        self.chan_change = chan_change.blk(param=1)
        self._RX_gain_range = qtgui.Range(0, 70, 5, 10, 1)
        self._RX_gain_win = qtgui.RangeWidget(self._RX_gain_range, self.set_RX_gain, "'RX_gain'", "counter_slider", int, QtCore.Qt.Horizontal)
        self.tabs_layout_0.addWidget(self._RX_gain_win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_samp_rate(gui_samp_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec(0))

        self.uhd_usrp_source_0.set_center_freq(((channel+1) * 1e6) + 2.4e9, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.uhd_usrp_source_0.set_rx_agc(False, 0)
        self.uhd_usrp_source_0.set_gain(RX_gain, 0)
        def _top_block_fournisseur_probe():
          self.flowgraph_started.wait()
          while True:

            val = self.chan_change.set_top_block()
            try:
              try:
                self.doc.add_next_tick_callback(functools.partial(self.set_top_block_fournisseur,val))
              except AttributeError:
                self.set_top_block_fournisseur(val)
            except AttributeError:
              pass
            time.sleep(1.0 / (1))
        _top_block_fournisseur_thread = threading.Thread(target=_top_block_fournisseur_probe)
        _top_block_fournisseur_thread.daemon = True
        _top_block_fournisseur_thread.start()
        self.qtgui_time_sink_x_1_1 = qtgui.time_sink_f(
            12000, #size
            gui_samp_rate, #samp_rate
            "DSMx Signal", #name
            2, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_1_1.set_update_time(0.10)
        self.qtgui_time_sink_x_1_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_1_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_1_1.enable_tags(True)
        self.qtgui_time_sink_x_1_1.set_trigger_mode(qtgui.TRIG_MODE_TAG, qtgui.TRIG_SLOPE_POS, 1.5, .0001, 0, "PreambleFound")
        self.qtgui_time_sink_x_1_1.enable_autoscale(False)
        self.qtgui_time_sink_x_1_1.enable_grid(False)
        self.qtgui_time_sink_x_1_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_1_1.enable_control_panel(False)
        self.qtgui_time_sink_x_1_1.enable_stem_plot(False)


        labels = ['Recovered Bits', 'Raw Data', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_1_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_1_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_1_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_1_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_1_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_1_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_1_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_1_1_win = sip.wrapinstance(self.qtgui_time_sink_x_1_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_1_1_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            4096, #fftsize
            window.WIN_BLACKMAN_hARRIS, #wintype
            (((channel+1) * 1e6) + 2.4e9), #fc
            samp_rate, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True, #plotconst
            None # parent
        )
        self.qtgui_sink_x_0.set_update_time(1.0/30)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.qwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self.qtgui_ledindicator_0 = self._qtgui_ledindicator_0_win = qtgui.GrLEDIndicator("RED=RECORDING", "red", "green", True if rec_button == 1 else False, 40, 2, 1, 1, self)
        self.qtgui_ledindicator_0 = self._qtgui_ledindicator_0_win
        self.tabs_grid_layout_0.addWidget(self._qtgui_ledindicator_0_win, 0, 3, 1, 1)
        for r in range(0, 1):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(3, 4):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self._note_tool_bar = Qt.QToolBar(self)
        self._note_tool_bar.addWidget(Qt.QLabel("RECORDING NOTE (press enter to update)" + ": "))
        self._note_line_edit = Qt.QLineEdit(str(self.note))
        self._note_tool_bar.addWidget(self._note_line_edit)
        self._note_line_edit.editingFinished.connect(
            lambda: self.set_note(str(str(self._note_line_edit.text()))))
        self.tabs_grid_layout_0.addWidget(self._note_tool_bar, 1, 1, 1, 1)
        for r in range(1, 2):
            self.tabs_grid_layout_0.setRowStretch(r, 1)
        for c in range(1, 2):
            self.tabs_grid_layout_0.setColumnStretch(c, 1)
        self._max_intensity_range = qtgui.Range(0, 500, 1, 50, 200)
        self._max_intensity_win = qtgui.RangeWidget(self._max_intensity_range, self.set_max_intensity, "'max_intensity'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.tabs_layout_0.addWidget(self._max_intensity_win)
        self.dsmx_preambleDetection_0 = dsmx.preambleDetection(channel)
        self.dsmx_Despreader_0 = dsmx.Despreader()
        self.digital_symbol_sync_xx_0 = digital.symbol_sync_ff(
            digital.TED_MUELLER_AND_MULLER,
            sps,
            0.045,
            1.0,
            0.1,
            0.005,
            1,
            digital.constellation_bpsk().base(),
            digital.IR_MMSE_8TAP,
            128,
            [])
        self.digital_correlate_access_code_tag_xx_0 = digital.correlate_access_code_tag_bb('1100110011001100110011001100110011001100110011001100110011001100', 8, 'PreambleFound')
        self.digital_binary_slicer_fb_1 = digital.binary_slicer_fb()
        self.blocks_file_sink_0_1 = blocks.file_sink(gr.sizeof_gr_complex*1, filename+str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d_%H:%M:%S'))+".cfile" if rec_button == 1 else "/dev/null", False)
        self.blocks_file_sink_0_1.set_unbuffered(False)
        self.blocks_char_to_float_0_1 = blocks.char_to_float(1, 1)
        self.analog_quadrature_demod_cf_1 = analog.quadrature_demod_cf((samp_rate/(2*math.pi*f_deviation)))


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.dsmx_Despreader_0, 'pdus'), (self.chan_change, 'ChannelChange'))
        self.msg_connect((self.dsmx_preambleDetection_0, 'pdus'), (self.dsmx_Despreader_0, 'Msg'))
        self.connect((self.analog_quadrature_demod_cf_1, 0), (self.digital_symbol_sync_xx_0, 0))
        self.connect((self.blocks_char_to_float_0_1, 0), (self.qtgui_time_sink_x_1_1, 0))
        self.connect((self.digital_binary_slicer_fb_1, 0), (self.digital_correlate_access_code_tag_xx_0, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0, 0), (self.blocks_char_to_float_0_1, 0))
        self.connect((self.digital_correlate_access_code_tag_xx_0, 0), (self.dsmx_preambleDetection_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.digital_binary_slicer_fb_1, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.qtgui_time_sink_x_1_1, 1))
        self.connect((self.uhd_usrp_source_0, 0), (self.analog_quadrature_demod_cf_1, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_file_sink_0_1, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("gnuradio/flowgraphs", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_gui_samp_rate(self.samp_rate)
        self.set_intermediate_samp_rate(self.samp_rate)
        self.analog_quadrature_demod_cf_1.set_gain((self.samp_rate/(2*math.pi*self.f_deviation)))
        self.qtgui_sink_x_0.set_frequency_range((((self.channel+1) * 1e6) + 2.4e9), self.samp_rate)

    def get_rootdir(self):
        return self.rootdir

    def set_rootdir(self, rootdir):
        self.rootdir = rootdir
        self.set_filename(self.rootdir+self.record_file_path+self.note+"_"+str(int(self.gui_samp_rate))+"sps_")

    def get_record_file_path(self):
        return self.record_file_path

    def set_record_file_path(self, record_file_path):
        self.record_file_path = record_file_path
        self.set_filename(self.rootdir+self.record_file_path+self.note+"_"+str(int(self.gui_samp_rate))+"sps_")

    def get_note(self):
        return self.note

    def set_note(self, note):
        self.note = note
        self.set_filename(self.rootdir+self.record_file_path+self.note+"_"+str(int(self.gui_samp_rate))+"sps_")
        Qt.QMetaObject.invokeMethod(self._note_line_edit, "setText", Qt.Q_ARG("QString", str(self.note)))

    def get_intermediate_samp_rate(self):
        return self.intermediate_samp_rate

    def set_intermediate_samp_rate(self, intermediate_samp_rate):
        self.intermediate_samp_rate = intermediate_samp_rate
        self.set_sps(int(self.intermediate_samp_rate/1e6))

    def get_gui_samp_rate(self):
        return self.gui_samp_rate

    def set_gui_samp_rate(self, gui_samp_rate):
        self.gui_samp_rate = gui_samp_rate
        self.set_filename(self.rootdir+self.record_file_path+self.note+"_"+str(int(self.gui_samp_rate))+"sps_")
        self.qtgui_time_sink_x_1_1.set_samp_rate(self.gui_samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.gui_samp_rate)

    def get_top_block_fournisseur(self):
        return self.top_block_fournisseur

    def set_top_block_fournisseur(self, top_block_fournisseur):
        self.top_block_fournisseur = top_block_fournisseur

    def get_timestamp(self):
        return self.timestamp

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.digital_symbol_sync_xx_0.set_sps(self.sps)

    def get_rec_button(self):
        return self.rec_button

    def set_rec_button(self, rec_button):
        self.rec_button = rec_button
        self.blocks_file_sink_0_1.open(self.filename+str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d_%H:%M:%S'))+".cfile" if self.rec_button == 1 else "/dev/null")
        self.qtgui_ledindicator_0.setState(True if self.rec_button == 1 else False)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts

    def get_max_intensity(self):
        return self.max_intensity

    def set_max_intensity(self, max_intensity):
        self.max_intensity = max_intensity

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename
        self.blocks_file_sink_0_1.open(self.filename+str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y_%m_%d_%H:%M:%S'))+".cfile" if self.rec_button == 1 else "/dev/null")

    def get_f_deviation(self):
        return self.f_deviation

    def set_f_deviation(self, f_deviation):
        self.f_deviation = f_deviation
        self.analog_quadrature_demod_cf_1.set_gain((self.samp_rate/(2*math.pi*self.f_deviation)))

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel
        self.dsmx_preambleDetection_0.set_new_channel(self.channel)
        self.qtgui_sink_x_0.set_frequency_range((((self.channel+1) * 1e6) + 2.4e9), self.samp_rate)
        self.uhd_usrp_source_0.set_center_freq(((self.channel+1) * 1e6) + 2.4e9, 0)

    def get_RX_gain(self):
        return self.RX_gain

    def set_RX_gain(self, RX_gain):
        self.RX_gain = RX_gain
        self.uhd_usrp_source_0.set_gain(self.RX_gain, 0)




def main(top_block_cls=top_block, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()
    tb.flowgraph_started.set()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
