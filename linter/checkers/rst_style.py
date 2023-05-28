import re

import sphinxlint


ALLOWED_HEADING_CHARS = ['=', '-', '~', '*', '^']  # In the same order as in the guidelines.
MAIN_HEADING_CHAR = ALLOWED_HEADING_CHARS[0]
MAIN_HEADING_RE = re.compile(rf'{MAIN_HEADING_CHAR}+\n[^\n]+\n{MAIN_HEADING_CHAR}+\n')
HEADING_DELIMITER_RE = re.compile(
    '^(' + '|'.join(rf'\{char}+' for char in ALLOWED_HEADING_CHARS) + ')\n$'
)
FORBIDDEN_HEADING_CHARS = [
    '#', '"', '\'', '+', '`', '@', '!', ',', '.', '/'
]  # Exhaustive list at https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#sections.
FORBIDDEN_HEADING_DELIMITER_RE = re.compile(
    '^(' + '|'.join(rf'\{char}+' for char in FORBIDDEN_HEADING_CHARS) + ')\n$'
)
GIT_CONFLICT_MARKERS = ['<' * 7, '>' * 7]
REFLINK_RE = re.compile(r':ref:`(?P<text>[\w\s]+)<(?P<link>[^`<>]+)>`')
TRAILING_SPACES_RE = re.compile(r'\s*$')


@sphinxlint.checker('.rst')
def check_heading_delimiters_characters(file, lines, options=None):
    """ Check that heading delimiters use only allowed characters. """
    for lno, line in enumerate(lines):
        if FORBIDDEN_HEADING_DELIMITER_RE.search(line):
            yield lno + 1, f"illegal use of the character {line[0]} in heading delimiters; use" \
                           f" any of {', '.join(ALLOWED_HEADING_CHARS)} instead"


@sphinxlint.checker('.rst')
def check_heading_delimiters_order(file, lines, options=None):
    """ Check that heading delimiters appear in the correct order. """
    last_delimiter_char_index = -1  # The index of the heading delimiter char in the ordered list.
    for lno, line in enumerate(lines):
        if HEADING_DELIMITER_RE.search(line):  # The line is a heading delimiter.
            delimiter_char = line[0]
            delimiter_char_index = ALLOWED_HEADING_CHARS.index(delimiter_char)
            if delimiter_char_index > last_delimiter_char_index + 1:
                # There is a leap of more than 1 in the chars used for the heading delimiters.
                last_delimiter_char = ALLOWED_HEADING_CHARS[last_delimiter_char_index] \
                    if last_delimiter_char_index != -1 else None
                yield lno + 1, f"the heading delimiter {delimiter_char} is not allowed after a" \
                               f" heading with {last_delimiter_char} as delimiter; follow this" \
                               f" order: {', '.join(ALLOWED_HEADING_CHARS)}"
            last_delimiter_char_index = delimiter_char_index


@sphinxlint.checker('.rst')
def check_max_one_main_heading(file, lines, options=None):
    """ Check that there is at most one main heading (h1) per document. """
    code = "".join(lines)
    nb_main_headings = len(MAIN_HEADING_RE.findall(code))
    if nb_main_headings > 1:
        yield 0, "the document should have only one main heading"


@sphinxlint.checker('.rst')
def check_min_one_main_heading(file, lines, options=None):
    """ Check that there is a main heading (h1) on document when it contains other headings. """
    heading_found, main_heading_found = False, False
    for lno, line in enumerate(lines):
        if HEADING_DELIMITER_RE.search(line):  # The line is a heading delimiter.
            heading_found = True
            if MAIN_HEADING_RE.search(''.join(lines[lno - 2:lno + 1])):  # Lower delimiter of h1.
                main_heading_found = True
                break

    if heading_found and not main_heading_found:
        yield 0, "the document should have a main heading (h1)"


@sphinxlint.checker('.rst')
def check_heading_delimiters_length(file, lines, options=None):
    """ Check that heading delimiters have the same length as their heading. """
    for lno, line in enumerate(lines):
        if HEADING_DELIMITER_RE.search(line):  # The line is a heading delimiter.
            if MAIN_HEADING_RE.search(''.join(lines[lno:lno+3])):  # Upper delimiter of h1.
                heading_lno = lno + 1
            else:  # Lower delimiter of a heading of any level.
                heading_lno = lno - 1
            if len(line.rstrip()) != len(lines[heading_lno].rstrip()):
                yield lno + 1, "the heading delimiter should have the same length as its heading"


@sphinxlint.checker('.rst')
def check_heading_spacing(file, lines, options=None):
    """ Check that headings are preceded and followed by at least one blank line. """
    for lno, line in enumerate(lines):
        if HEADING_DELIMITER_RE.search(line):  # The line is a heading delimiter.
            if MAIN_HEADING_RE.search(''.join(lines[lno:lno+3])):  # Upper delimiter of h1.
                continue  # We handle this heading via its lower delimiter.

            heading_lno = lno - 1
            if MAIN_HEADING_RE.search(''.join(lines[lno-2:lno+1])):  # Lower delimiter of h1.
                main_heading = True
            else:  # Lower delimiter of a heading of level 2-6.
                main_heading = False
            lno_before_heading = heading_lno - (2 if main_heading else 1)
            if lno_before_heading >= 0 and lines[lno_before_heading] != '\n':
                # Heading doesn't have to be preceded by a blank line if on first line of the file.
                yield heading_lno + 1, "the heading should be preceded by a blank line"
            if lines[heading_lno + 2] != '\n':
                yield heading_lno + 1, "the heading should be followed by a blank line"


@sphinxlint.checker('.rst', '.py', '.js', '.xml', '.css', '.sass', '.less', '.po', '.pot')
def check_git_conflict_markers(file, lines, options=None):
    """ Check that there are no conflict markers. """
    for lno, line in enumerate(lines):
        if any(marker in line for marker in GIT_CONFLICT_MARKERS):
            yield lno + 1, "the git conflict should be resolved"


@sphinxlint.checker('.rst')
def check_ref_link_format(file, lines, options=None):
    """ Check that ref links have the correct whitespacing."""
    lines = "".join(lines)

    # Returns a list of Match objects
    # Example match:
    # ":ref:`GS1 nomenclature list <barcode/operations/gs1_nomenclature/list>`"
    matches = REFLINK_RE.finditer(lines)

    for match in matches:
        # First match group
        # Example: "GS1 nomenclature list "
        #            trailing_whitespace ^
        text_group = match.group('text')

        # Search for the trailing spaces in the label
        trailing_whitespace = TRAILING_SPACES_RE.search(text_group)
        if trailing_whitespace is None:
            yield 0, "could not match reflink spaces, this should not happen"

        trailing_whitespace_count = len(trailing_whitespace[0])

        # If too many or too little spaces between label and link
        if trailing_whitespace_count != 1:
            # Look at the entire match
            # ":ref:`GS1 nomenclature list\n   <barcode/operations/gs1_nomenclature/list>`"
            reflink_str = match.group(0)

            # The index of where the match starts, in the entire file
            start_idx = match.start()

            # Determine if it spans more than 1 line
            if "\n" in reflink_str:
                line_start_idx = lines[:start_idx].rfind("\n")

                # + 1 because we don't want to include the "\n" at beginning
                # Conveniently handles -1 edge case to 0
                content_before_match = lines[line_start_idx + 1:start_idx]

                stripped_content = content_before_match.lstrip()
                spaces_in_first_line = len(content_before_match) - len(stripped_content)

                # [
                #   ":ref:`GS1 nomenclature list",
                #   "   <barcode/operations/gs1_nomenclature/list>`",
                # ]
                second_line = reflink_str.split("\n")[1]
                stripped_content = second_line.lstrip()
                spaces_in_second_line = len(second_line) - len(stripped_content)

                if spaces_in_first_line == spaces_in_second_line:
                    break # Pass test, see ref-indented.rst

                line_num = lines[:match.end()].count("\n") + 1
                yield line_num, f"incorrect indenting spaces between reflink text and link, expected {spaces_in_first_line}, but found {spaces_in_second_line} spaces."
                break

            # Count the number of newline characters before the match + 1
            line_num = lines[:start_idx].count("\n") + 1

            yield line_num, f"incorrect spaces between reflink text and link, expected {1}, but found {trailing_whitespace_count} spaces."

