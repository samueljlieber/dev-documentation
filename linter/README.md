# Linter

Expanded linter rules with sphinx-lint.

## Testing

Run tests with:

```bash
# Ensure you are in the ./documentation/linter directory
pytest
```

Test fixtures can be added in the `./tests/fixtures/` directory with their
corresponding pass and fail cases. The expected error should be included at
the top of the file, for example:

```
.. expect: incorrect spaces between reflink text and link, expected 1, but found 0 spaces (ref-link-format)
```
