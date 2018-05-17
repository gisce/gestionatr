import click
from lxml import objectify


@click.command()
@click.option('-f', '--frommxl', help='XML file path', type=str)
@click.option('-t', '--tofile', help='Destination file path', type=str)

def parser(frommxl, tofile):
    with open(frommxl, 'r') as xml:
        xml_str = xml.read()

    with open(tofile, 'w') as pyfile:
        pyfile.write('# -*- coding: utf-8 -*-\n\n')
        root = objectify.fromstring(xml_str)
        root_tables = root.body['text']
        for table in root_tables['{{{0}}}table'.format(root.body.nsmap['table'])]:
            pyfile.write('= [\n')
            for row in table['table-row']:
                pyfile.write('\t(')
                for cell in row['table-cell']:
                    for super_text in cell['{{{0}}}p'.format(cell.nsmap['text'])]:
                        try:
                            cell_text = super_text.span.text
                            pyfile.write('\'' + cell_text + '\', ')
                        except:
                            continue
                pyfile.write('),\n')
            pyfile.write(']\n')
        print ('parsing finished succesfully')


if __name__ == '__main__':
    parser()
