# Matched braces
Checks if a given string contains balanced braces.
```sh
# Valid
[]{}()
{[[]]()}

# Invalid
[()
((((((((({=}))))))))
```

# Run
```sh
make install
make test
```