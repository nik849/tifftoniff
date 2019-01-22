import click
import tifftoniff
import os

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
        pass
    else:
        tiff = tifftoniff.Convert(input, output)
        tiff.convert()

if __name__ == '__main__':
    run()
