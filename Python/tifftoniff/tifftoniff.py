import Tyf
import os

class Convert:
    """
    Class to convert 'standard' tiffs to Nikon proprietry tiffs.
    """
    def __init__(self, input_tiff, output_path, verbose):
        """
        :param input_tiff: tiff to convert, required
        """
        self.input_tiff = input_tiff
        self.output_path = output_path
        self.verbose = verbose

    def convert(self):
        """
        Actually does the converting, mainly overwriting header data.
        """
        tif = Tyf.open(self.input_tiff)
        if self.verbose:
            print('Original TIFF info:\n')
            print(tif[0])
        tif[0][256] = 2000
        tif[0][257] = 2000
        tif[0][258] = 16
        tif[0][283] = 300
        tif[0][262] = 1
        tif[0][273] = 142
        tif[0][282] = 300
        tif[0][279] = 8000000

        out = str(self.output_path) + "/" + os.path.basename(str(self.input_tiff))
        if self.verbose:
            print('Saving to... ' + out)
        tif.save(out)
