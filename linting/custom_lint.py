import re
from sphinxlint import *
from pprint import pformat

# https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#sections
HEADINGS_CHARACTERS = [
    '#', '*', '=', '-', '^', '"', '\'', '+', '`', '\"', '@', '!', ',', '.', '/'
    # Complete list https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#sections
]
HEADINGS_REGEX = "(%s)\n" % (
    "|".join(
        f"(\\{character}+)" for character in HEADINGS_CHARACTERS
    )
)
HEADINGS_ORDERING_GUIDELINES = [
    '=', '-', '~', '*', '^',
]

@checker(".rst")
def check_headers(file, lines, options=None):
    """Enforce our headings guidelines

    https://www.odoo.com/documentation/master/contributing/documentation/rst_cheat_sheet.html#headings
    """
    toskip = set()
    file_headers_characters = []  # TODO check ordering of headers
    found_main_header = False
    for lno, line in enumerate(lines, start=1):
        if toskip and toskip.pop():
            continue
        if re.match(HEADINGS_REGEX, line):
            delimiting_char = line[0]
            if delimiting_char not in file_headers_characters:
                file_headers_characters.append(delimiting_char)

            if re.match(HEADINGS_REGEX, lines[lno+1]):
                # Header in 3 lines
                if found_main_header:
                    yield lno, "document should only have one main heading"
                    continue

                heading_lines = [line, lines[lno], lines[lno+1]]
                heading_text = lines[lno]
                if line != f"{delimiting_char*(len(heading_text)-1)}\n":
                    yield lno, "invalid main heading first line"  # TODO better explanation

                pre_heading_line_number = lno-2
                post_heading_line_number = lno+2
                toskip.add(lno+1)
                toskip.add(lno+2)
                found_main_header = True
            else:
                # Header in 2 lines
                heading_lines = [lines[lno-2], line]
                heading_text = lines[lno-2]
                pre_heading_line_number = lno-3
                post_heading_line_number = lno

            if not all(
                len(heading_line) == len(heading_text)
                for heading_line in heading_lines
            ):
                yield lno, "heading formatting line length doesn't match heading size."

            if pre_heading_line_number >= 0 and lines[pre_heading_line_number] != "\n":
                yield pre_heading_line_number, "missing empty line before heading"
            if lines[post_heading_line_number] != "\n":
                yield post_heading_line_number, "missing empty line after heading"

    if file_headers_characters and not found_main_header:
        # If there are headers, there must be a main heading.
        yield 1, "no main heading found in file"

    if file_headers_characters != HEADINGS_ORDERING_GUIDELINES[:len(file_headers_characters)]:
        yield 1, "headings specification doesn't match guidelines"


if __name__ == "__main__":
    sys.exit(main())
