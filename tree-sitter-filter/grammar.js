export default grammar({
  name: 'filter',
  extras: $ => [/\s/],

  word: $ => $.identifier,

  rules: {
    query: $ => $._expr,

    _expr: $ => choice(
      $.comparison,
      $.and_expression,
      $.or_expression,
      $.parenthesized
    ),

    comparison: $ => seq(
      $.identifier,
      choice('=', '!=', '>', '<', '>=', '<='),
      choice($.string, $.number)
    ),

    and_expression: $ => prec.left(2, seq(
      $._expr,
      'and',
      $._expr
    )),

    or_expression: $ => prec.left(1, seq(
      $._expr,
      'or',
      $._expr
    )),

    parenthesized: $ => seq(
      '(',
      $._expr,
      ')'
    ),

    identifier: $ => /[a-zA-Z_][a-zA-Z0-9_.]*/,

    string: $ => /"[^"]*"/,

    number: $ => /-?\d+(\.\d+)?/,
  }
});