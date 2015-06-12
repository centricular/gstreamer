gen_lex = find_program('gen_lex.py')
gen_grammar = find_program('gen_grammar.py')

grammar = custom_target('parsegrammar',
  input : 'grammar.y',
  output : ['grammar.tab.c', 'grammar.tab.h'],
  command : [gen_grammar, '@OUTPUT0@', '@OUTPUT1@', '@INPUT@'],
)

parser = custom_target('parselex',
  input : 'parse.l',
  output : ['lex.priv_gst_parse_yy.c', 'parse_lex.h'],
  command : [gen_lex, '@OUTPUT0@', '@OUTPUT1@', '@INPUT@', 'DUMMY']
)
