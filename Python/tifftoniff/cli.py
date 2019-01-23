import click
import tifftoniff
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

def run(input, output, stack):
    if not os.path.exists("./" + output):
        os.makedirs("./" + output)
    if stack is not None:
        for file in tqdm(glob.glob(stack + "*.tif")):
            tiff = tifftoniff.Convert(file, output)
            tiff.convert()
    else:
        tiff = tifftoniff.Convert(input, output)
        tiff.convert()

if __name__ == '__main__':
    run()
