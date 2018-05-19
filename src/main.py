

import argparse
from converter.extractor import Extractor
from config.config import Config
config = Config(True)
extractor = Extractor(config)
def parseArgs():
	parser = argparse.ArgumentParser()
	parser.add_argument("--type", "-t", type=str, default='txt',
					help="Output file type: txt or ...")
	parser.add_argument("--input_file", "-in", type=str, default='',
					help="Path to input pdf file")
	parser.add_argument("--output_file", "-out", type=str, default='',
					help="Path to output file")
	parser.add_argument("--metaTitle", action="store_true", help="Add title to out file.", default=False)
	parser.add_argument("--metaContent", action="store_true", help="Add content list to out file.", default=False)
	parser.add_argument("--metaName", action="store_true", help="Add authors names to out file.", default=False)
	parser.add_argument("--metaLocation", action="store_true", help="Add loaction with coordinates to out file.", default=False)
	parser.add_argument("--metaKeyWord", action="store_true", help="Add key phrases to out file.", default=False)
	parser.add_argument("--metaRef", action="store_true", help="Add references to out file.", default=False)
	parser.add_argument("--metaAll", action="store_true", help="Extract all metadata to out file.", default=False)
	args = parser.parse_args()
	if args.input_file != "":
		extractor.INFilename = args.input_file
	if args.output_file != "":
		extractor.OUTFilename = args.output_file
	extractor.typeOut = args.type
	extractor.metaTitle = args.metaTitle
	extractor.metaContent = args.metaContent
	extractor.metaName = args.metaName
	extractor.metaLocation = args.metaLocation
	extractor.metaKeyWord = args.metaKeyWord
	extractor.metaRef = args.metaRef
	extractor.metaAll = args.metaAll




def main():
	parseArgs()
	extractor.extract()
	extractor.save()

main()
	
	
	

