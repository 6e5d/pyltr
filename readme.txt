ltr name comes from ltree which is actually a json parser
but squash dict into list(reversible).

ltr is more like a s-expression(but only recursive list, not binary tree).
it only support 2 types: ident(represented by str), string literal(Slit type).

string is general-purpose, idents are easier to write since they do not
need the quote but they cannot contain quotes, parentheses or whitespaces.
Though in this impl they can contain other special characters like backslash,
it is safest to use only [a-zA-Z0-9_](c symbol but can start with digit).
If you start with a digit,
maybe other json compatible parser will identify it with a digit.

ltr is preferred over ltree for its simplicity.
In the future i will probably write a c ltr.
modified ltr can implement ltree
(add `:,` to separater, use another phase to handle number/bool/etc types)
