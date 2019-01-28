import click
from tifftoniff import Convert
import os
import glob
from tqdm import tqdm

@click.command()
@click.option(
    '--input', '-i', default=None,
    help='Tiff file to convert')
@click.option(
    '--output', '-o', default='_output',
    help='Ouput folder name/path')
@click.option(
    '--stack', '-s', default=None,
    help='Path to tif stack to convert')

def main(input, output, stack):
    if not os.path.exists("./" + output):
        os.makedirs("./" + output)
    if stack is not None:
        for file in tqdm(glob.glob(stack + "*.tif")):
            tiff = Convert(file, output)
            tiff.convert()
    else:
        _tiff = Convert(input, output)
        _tiff.convert()

if __name__ == '__main__':
    main()
