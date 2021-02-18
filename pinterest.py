############################################
# @Name       : Pinterest Pin Creator      #
# @Author     : Dagimal                    #
# @Email      : daffagifariakmal@gmail.com #
# @Year       : 2021                       #
############################################

import random
import os
import datetime
import svglue
from configparser import ConfigParser
from tqdm import tqdm
from bing_image_urls import bing_image_urls

parser = ConfigParser()
parser.read('config.ini')

# Select template
template = parser.get('settings', 'template')

#option = int(input("Select a template: "))
print("--->> Current Template : " + template)

# keyword line
line_numbers = len(open('keyword.txt').readlines())
loop = -1

# Create New Dir
now = datetime.datetime.now()
dateNow = now.strftime("%Y-%m-%d-%H:%M:%S")
os.system('mkdir output/' + dateNow)

pbar = tqdm(total = int(line_numbers))
while loop <= line_numbers:
	try:
		loop += 1
		keyword = open('keyword.txt', 'r').readlines()
		
		# load the template from a file
		tpl = svglue.load(file='template/' + template + '.svg')

		# replace some text
		tpl.set_text('main-title', keyword[loop])
		
		# replace image
		
		image = bing_image_urls(keyword[loop], limit=2)
		randomImage = random.choice(image)
		try:
			tpl.set_image('main-img', file=randomImage, mimetype=None)
		except:
			tpl.set_image('main-img', file=randomImage, mimetype=None)
		# to render the template, cast it to a string. this also allows passing it
		# as a parameter to set_svg() of another template
		src = str(tpl)
		svgName = str(loop) + '.svg'
		print(svgName)
		with open(svgName, 'w') as svgout:
		    svgout.write(src)

		# export to png
		os.system('inkscape --export-type="png" ' + svgName)
		os.system('mv ' + str(loop) + '.png ' + 'output/' + dateNow)
		os.system('rm ' + svgName)
		pbar.update(1)
	except:
		print("error bang, cari solusi ya")
pbar.close()
