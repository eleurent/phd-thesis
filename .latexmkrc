# https://tex.stackexchange.com/a/1228
# Custom dependency and function for glossaries package
# add_cus_dep('glo', 'gls', 0, 'makeglo2gls');
# sub makeglo2gls {
#     system("makeindex -s '$_[0]'.ist -t '$_[0]'.glg -o '$_[0]'.gls '$_[0]'.glo");
# }

@cus_dep_list = (@cus_dep_list, "glo gls 0 makeglo2gls");
sub makeglo2gls {
   system("makeindex $_[0].glo -s $_[0].ist -o $_[0].gls"); }
@generated_exts = (@generated_exts, 'glo');

@cus_dep_list = (@cus_dep_list, "slo sls 0 makeslo2sls");
sub makeslo2sls {
   system("makeindex $_[0].slo -s $_[0].ist -o $_[0].sls"); }
@generated_exts = (@generated_exts, 'slo');