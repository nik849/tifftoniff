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
@click.option(
    '--verbose', '-v', is_flag=True)

def main(input, output, stack, verbose):
    if not os.path.exists("./" + output):
        os.makedirs("./" + output)
    if stack is not None:
        for file in tqdm(glob.glob(stack + "*.tif")):
            print(file)
            tiff = tifftoniff.Convert(file, output, verbose)
            tiff.convert()
    else:
        _tiff = tifftoniff.Convert(input, output, verbose)
        _tiff.convert()
        
if __name__ == '__main__':
    main()
