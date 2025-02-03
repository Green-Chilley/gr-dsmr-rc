# GNURadio Spektrum DSMR Protocol Decoder

Isolate a signal using an SDR from a DX3 Transmitter with GNURadio and despread with C++. GNURadio will then output the values from the Transmitter to the Receiver across 3 channels. Option to graph values based on captured packet.

## Relevant links

- [Original Repository this was based and modified on (gr-dsmx-rc)](https://github.com/lscardoso/gr-dsmx-rc/tree/master)
    - [and their paper](https://pubs.gnuradio.org/index.php/grcon/article/download/97/63/)

- [CYRF6936 Datasheet](https://mm.digikey.com/Volume0/opasdata/d220001/medias/docus/380/CYRF6936.pdf)

- [CYRF6936 Manual](https://application-notes.digchip.com/011/11-13720.pdf)

## Requirements

- Install relevant drivers for the SDR used.
    - [Follow these instructions for Linux environment](https://wiki.gnuradio.org/index.php?title=Draft-AN-445#Building_and_installing_UHD_from_source_code)
- Make sure GNURadio is installed before building. Otherwise, skip this section.

### Windows
https://wiki.gnuradio.org/index.php/WindowsInstall#Windows_Installation

### Linux
https://wiki.gnuradio.org/index.php/LinuxInstall#Distributions_and_Commands 

## Build

If build folder exists, delete it.
```
$ mkdir $(builddir)
$ cd $(builddir)
$ cmake ..
$ make
$ make test
$ sudo make install
$ sudo ldconfig
```

## Run
- On a separate terminal, go into `/gr-dsmr-rc/examples`
- run `./top_block.py`

Alternatively, you can open up GNURadio with `gnuradio-companion DSMxDemod.grc &` when in examples directory and clicking the run button.

## Graphing
- To record values and graph them, enable the Graph block in GNURadio.
- After running, the results will be saved into the `examples` directory as `channel_data.csv`.
- In the same directory, run `./graphDSMR.py` 