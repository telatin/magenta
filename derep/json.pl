use JSON::PP;
use Data::Dumper;

my $data;

$data->{project} = {
 name => "project",
 command => "shell cmd",

};
$data->{repseqs} = {
 'seq1' => { md5 => 'ASDASD', samples => ["one", "three", "five"] },
 'seq2' => { md5 => 'ASDASD', samples => ["one", "three", "five"] },
 'seq3' => { md5 => 'ASDASD', samples => ["one", "three", "five"] },
};

my $json = JSON::PP->new->ascii->pretty->allow_nonref;
my $pretty_printed_json_text = $json->encode( $data );
print $pretty_printed_json_text;
