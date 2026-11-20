(string) @string
(number) @number
(boolean) @constant.builtin

["and" "or" "not"] @keyword
["=" "!=" ">" "<" ">=" "<="] @operator

(comparison
  field: (identifier) @property)

(in_expression
  field: (identifier) @property)

(contains_expression
  field: (identifier) @property)

["in" "contains"] @keyword