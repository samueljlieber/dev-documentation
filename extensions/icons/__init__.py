""" Add new custom icon role. """

import re
from docutils import nodes
from docutils.parsers.rst import roles


def extract_icon_classes(filename):
    """
    Extract icon classes from a CSS file.
    """
    icon_classes = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                match = re.search(r'\.([a-zA-Z0-9_-]+):before', line)
                if match:
                    icon_class = match.group(1)
                    icon_classes.append(icon_class)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")
    return icon_classes


def handle_error(inliner, rawtext, error_message, lineno):
    """
    Handle an error by creating a system message node.
    """
    error_node = nodes.system_message(
        lineno, backrefs=[], source=rawtext, type='error', level=1)
    error_node['message'] = inliner.reporter.error(error_message, line=lineno)
    return [error_node], []


def icon_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    """
    Custom role for adding icons to the documentation.
    """
    odoo_ui_icon_path = inliner.document.settings.env.app.config.odoo_ui_icon_path
    font_awesome_icon_path = inliner.document.settings.env.app.config.font_awesome_icon_path
    if 'oi-' in text:
        icon_file = odoo_ui_icon_path
    elif 'fa-' in text:
        icon_file = font_awesome_icon_path
    else:
        return handle_error(
            inliner, rawtext, f"'{text}' is not an 'oi-' or 'fa-' icon set", lineno)
    icon_classes = extract_icon_classes(icon_file)
    if text in icon_classes:
        icon_node = nodes.inline(classes=[text])
        icon_classname = text.replace('oi-', '').replace('fa-', '').replace('-', ' ')
        guilabel_text = f' ({icon_classname})'
        guilabel_node = nodes.inline(guilabel_text, guilabel_text, classes=['guilabel'])
        return [icon_node, guilabel_node], []
    else:
        return handle_error(
            inliner, rawtext, f"Icon class '{text}' not found in {icon_file}", lineno)


def setup(app):
    """
    Setup function for the extension.
    """
    app.add_config_value('odoo_ui_icon_path', '', 'html')
    app.add_config_value('font_awesome_icon_path', '', 'html')
    roles.register_local_role('icon', icon_role)
