# Remove FASTA section from GFF file (prokka)
# USAGE: remove_seq_from_gff.pl file.gff > stripped.gff
while(my $line = <> ) {
	if ($line=~/##FASTA/) {
		last;
	}
	print $line;
}