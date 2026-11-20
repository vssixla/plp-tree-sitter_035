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
      $.parenthesized,
      $.not_expression,
      $.in_expression
    ),

    comparison: $ => seq(
      field('field', $.identifier),
      choice('=', '!=', '>', '<', '>=', '<='),
      field('value', $._value)
    ),

    in_expression: $ => seq(
      field('field', $.identifier),
      'in',
      '(',
      $._value,
      repeat(seq(',', $._value)),
      ')'
    ),

    _value: $ => choice(
      $.string,
      $.number,
      $.boolean
    ),

    and_expression: $ => prec.left(2, seq(
      field('left', $._expr),
      'and',
      field('right', $._expr)
    )),

    or_expression: $ => prec.left(1, seq(
      field('left', $._expr),
      'or',
      field('right', $._expr)
    )),

    parenthesized: $ => seq(
      '(',
      $._expr,
      ')'
    ),

    not_expression: $ => prec(3, seq(
      'not',
      field('operand', $._expr)
    )),

    identifier: $ => /[a-zA-Z_][a-zA-Z0-9_.]*/,

    string: $ => /"[^"]*"/,

    number: $ => /-?\d+(\.\d+)?/,

    boolean: $ => choice('true', 'false'),
  }
});