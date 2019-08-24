import re


def minify(expression):
  return re.sub(r'\s', '', expression)


def prepare(expression):
  minified_expression = minify(expression)
  expressions_split = minified_expression.split(';')
  expressions_split.reverse()
  expressions_reversed = ';'.join(expressions_split)
  stripped_expression = expressions_reversed.strip(';') + ';'
  return stripped_expression
