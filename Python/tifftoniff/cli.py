import click
import tifftoniff
import os
import glob

@click.command()
@click.argument('input')
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
        os.chdir(stack)
            for file in glob.glob("*.tif"):
                tiff = tifftoniff.Convert(file, output)
                tiff.convert()
    else:
        tiff = tifftoniff.Convert(input, output)
        tiff.convert()

if __name__ == '__main__':
    run()
