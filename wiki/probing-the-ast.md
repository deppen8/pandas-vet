# Simple Tools for Exploring the Python AST During Development of `pandas-vet`

## Option 1: Using the standard library

The `ast` module has a `.dump()` function which returns a formatted string dump of the AST tree node. Default is to show annotations, which helps in identifying the attribute chain.

```ast.dump(node, annotate_fields=True, include_attributes=False)```

Example:

```
import ast

code = """
print("Hello World!")
s = "I'm a string!"
print(s)
"""
tree = ast.parse(code)
print(ast.dump(tree))
```

Output:

```
'Module(body=[Expr(value=Call(func=Name(id=\'print\', ctx=Load()), args=[Str(s=\'Hello World!\')], keywords=[])), Assign(targets=[Name(id=\'s\', ctx=Store())], value=Str(s="I\'m a string!")), Expr(value=Call(func=Name(id=\'print\', ctx=Load()), args=[Name(id=\'s\', ctx=Load())], keywords=[]))])'
```

## Option 2: Using the `astpp` module from greentreesnakes

The pretty-print module mentioned in the above post (available at https://bitbucket.org/takluyver/greentreesnakes/src/default/astpp.py) includes a `astpp.dump()` function which produces essentially the same output, but presented in a tree format that provides more visual clarity.

```astpp.dump(node, annotate_fields=True, include_attributes=False, indent=' ')```

Example:
```
import ast
import astpp
 
code = """
print("Hello World!")
s = "I'm a string!"
print(s)
"""
tree = ast.parse(code)
print(astpp.dump(tree))
```

Output:
```
Module(body=[
    Expr(value=Call(func=Name(id='print', ctx=Load()), args=[
        Str(s='Hello World!'),
      ], keywords=[])),
    Assign(targets=[
        Name(id='s', ctx=Store()),
      ], value=Str(s="I'm a string!")),
    Expr(value=Call(func=Name(id='print', ctx=Load()), args=[
        Name(id='s', ctx=Load()),
      ], keywords=[])),
  ])
```

The `astpp` module also includes a `parseprint()` function to produce this formatted dump directly from the code string (no need to manually parse), along with an alias `pdp()` which references the same function:

```astpp.parseprint(code, filename='<string>', mode='exec', **kwargs)```
```astpp.pdp(code)```
