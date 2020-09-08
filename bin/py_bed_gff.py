import pprint
import argparse
#conda install -c bioconda bcbio-gff
#from BCBio import GFF
import pybedtools 
import pdb

def featuretype_filter(feature, featuretype):
    """
    Only passes features with the specified *featuretype*
    """
    if feature[2] == featuretype:
        return True
    return False


def subset_featuretypes(featuretype):
    """
    Returns the filename containing only `featuretype` features.
    """
    return g.filter(featuretype_filter, featuretype).saveas().fn



opt_parser = argparse.ArgumentParser(description='')

opt_parser.add_argument('-b', '--bed',
                        help='',
                        required=True)

opt_parser.add_argument('-g', '--gff',
                        help='',
 						required=True)

opt = opt_parser.parse_args()

# in_file = opt.gff
# in_handle = open(in_file)

# for chromosome in GFF.parse(in_handle):
# 	for feat in chromosome.features:
# 		print(f"{chromosome.id}\t{feat.location.start}\t{feat.location.end}\t{feat.type}:{feat.id}")
		
gff = pybedtools.BedTool(opt.gff).remove_invalid().saveas()
gff.filter(featuretype_filter, ['CDS']).saveas().fn
bed = pybedtools.BedTool(opt.bed).remove_invalid().saveas()
for f in gff:
   count = 0
   total = 0
   for g in bed:
       if g.chrom == f.chrom and g.start >= f.start and g.end <= f.end:
       	   count += 1
       	   total += int(g.name)
   print(f"{f.name} [{f.chrom}:{f.start}-{f.end}] {count} -> {total}")
