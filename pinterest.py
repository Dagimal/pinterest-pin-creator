############################################
# @Name       : Pinterest Pin Creator      #
# @Author     : Dagimal                    #
# @Email      : daffagifariakmal@gmail.com #
# @Year       : 2021                       #
############################################

import os
import svglue
from configparser import ConfigParser

parser = ConfigParser()
parser.read('config.ini')

# Select template
template = parser.get('settings', 'template')

#option = int(input("Select a template: "))
print("\033[1;31;40m Current Template : " + template)
# load the template from a file
tpl = svglue.load(file='template/' + template + '.svg')

# replace some text
tpl.set_text('sample-text', u'ngentot Goreng Klaten Utara Sangat Enak Sekali Klajo')

# to render the template, cast it to a string. this also allows passing it
# as a parameter to set_svg() of another template
src = str(tpl)

# write out the result as an SVG image and render it to pdf using cairosvg
#import cairosvg
with open('output.svg', 'w') as svgout:
    svgout.write(src)
    #cairosvg.svg2pdf(bytestring=src, write_to=out)

# export to png
os.system('inkscape --export-type="png" output.svg')
os.system('mv output.png output')
os.system('rm output.svg')


#var list
# svgFileName
