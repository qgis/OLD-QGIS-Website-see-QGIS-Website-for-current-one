#!/usr/bin/perl

use strict;
use warnings;

my %donors;

open I, "source/site/about/donors.inc";
while(<I>) {
        chop;
        next unless /^\s*[*-]/;
        s/^[-*  ]+//;
        next if /^\s*$/;
        $donors{lc $_}=$_;
}
close I;

while(<>) {
	chop;
	s/^\s*([A-Z0-9])\. /$1\\. /;
	$donors{lc $_} = $_;
}

open O, ">source/site/about/donors.inc";
print O ".. list-table:: List of Donors\n\n";

my $cols = 4;

my $i=0;
foreach ( sort { lc($a) cmp lc($b) } keys %donors ) {
        print O "   " . ($i%$cols==0 ? "*" : " ") . " - $donors{$_}\n";
        $i++;
}
print O "     -\n" while $i++%$cols>0;
