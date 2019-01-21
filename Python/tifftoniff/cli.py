import click
import tifftoniff
import os

@click.command()
@click.argument('input')
@click.option(
    '--output', '-o', default='_output',
    help='Ouput folder name/path')

def run(input, output):
    if not os.path.exists("./" + output):
        os.makedirs("./" + output)

    tiff = tifftoniff.Convert(input, output)
    tiff.convert()

if __name__ == '__main__':
    run()
