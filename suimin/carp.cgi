#!/usr/local/bin/perl -w
# CGI::Carpのひながた
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);

print "Content-type: text/html;\n\n";
warningsToBrowser(1);
print <<EOM;
<html>
<head><title>sample</title></head>
<body>
サンプル = $sample<br>
</body>
</html>
EOM

exit;