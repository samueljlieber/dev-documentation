:custom-css: showcase_tables.css

.. include:: /icons.txt

===============
RST cheat sheet
===============

.. _contributing/headings:

Headings
========

| For each formatting line (e.g., ``===``), write as many symbols (``=``) as there are characters in
  the header.
| The symbols used for the formatting are, in fact, not important. Only the order in which they are
  written matters, as it determines the size of the decorated heading. This means that you may
  encounter different heading formatting and in a different order, in which case you should follow
  the formatting in place in the document. In any other case, use the formatting shown below.

+--------------+----------------------+
| Heading size | Formatting           |
+==============+======================+
| H1           | .. code-block:: text |
|              |                      |
|              |    =======           |
|              |    Heading           |
|              |    =======           |
+--------------+----------------------+
| H2           | .. code-block:: text |
|              |                      |
|              |    Heading           |
|              |    =======           |
+--------------+----------------------+
| H3           | .. code-block:: text |
|              |                      |
|              |    Heading           |
|              |    -------           |
+--------------+----------------------+
| H4           | .. code-block:: text |
|              |                      |
|              |    Heading           |
|              |    ~~~~~~~           |
+--------------+----------------------+
| H5           | .. code-block:: text |
|              |                      |
|              |    Heading           |
|              |    *******           |
+--------------+----------------------+
| H6           | .. code-block:: text |
|              |                      |
|              |    Heading           |
|              |    ^^^^^^^           |
+--------------+----------------------+

.. important::
   Each document must have **exactly one H1 heading**. No less, no more.

.. _contributing/markups:

Markups
=======

.. _contributing/markups/italic:

Emphasis (italic)
-----------------

To emphasize a part of the text. The text is rendered in italic.

.. list-table::
   :class: o-showcase-table

   * - Fill out the information *before* saving the form.

   * - .. code-block:: text

          Fill out the information *before* saving the form.

.. _contributing/markups/bold:

Strong emphasis (bold)
----------------------

To emphasize a part of the text. The text is rendered in bold.

.. list-table::
   :class: o-showcase-table

   * - A **subdomain** is a domain that is a part of another domain.

   * - .. code-block:: text

          A **subdomain** is a domain that is a part of another domain.

.. _contributing/markups/code-sample:

Technical term (literal)
------------------------

To write a technical term or a specific value to insert. The text is rendered in literal.

.. list-table::
   :class: o-showcase-table

   * - Insert the IP address of your printer, for example, `192.168.1.25`.

   * - .. code-block:: text

          Insert the IP address of your printer, for example, `192.168.1.25`.

.. _contributing/markups/definitions:

Definitions
-----------

Use the `dfn` markup to define a term.

.. list-table::
   :class: o-showcase-table

   * - The documentation is written in RST and needs to be built (:dfn:`converted to HTML`) to display
       nicely.

   * - .. code-block:: text

          The documentation is written in RST and needs to be built (:dfn:`converted to HTML`) to display
          nicely.

.. _contributing/markups/abbreviations:

Abbreviations
-------------

Use the `abbr` markup to write a self-defining abbreviation that is displayed as a tooltip.

.. list-table::
   :class: o-showcase-table

   * - Odoo uses :abbr:`OCR (optical character recognition)` and artificial intelligence technologies to
       recognize the content of the documents.

   * - .. code-block:: text

          Odoo uses :abbr:`OCR (optical character recognition)` and artificial intelligence technologies to
          recognize the content of the documents.

.. _contributing/markups/guilabel:

:abbr:`GUI (graphical user interface)` element
----------------------------------------------

Use the `guilabel` markup to identify any text of the interactive user interface (e.g., button
labels, view titles, field names, lists items, ...).

.. list-table::
   :class: o-showcase-table

   * - Update your credentials, then click on :guilabel:`Save`.

   * - .. code-block:: text

          Update your credentials, then click on :guilabel:`Save`.

.. _contributing/markups/menuselection:

Menu selection
--------------

Use the `menuselection` markup to guide the user through a sequence of menus.

.. list-table::
   :class: o-showcase-table

   * -  To review your sales performance, go to :menuselection:`Sales --> Reporting --> Dashboard`.

   * - .. code-block:: text

          To review your sales performance, go to :menuselection:`Sales --> Reporting --> Dashboard`.

.. _contributing/markups/file:

File
----

Use the `file` markup to indicate a file path or name.


.. list-table::
   :class: o-showcase-table

   * - Create redirections with the :file:`redirects.txt` file at the root of the repository.

   * - .. code-block:: text

          Create redirections with the :file:`redirects.txt` file at the root of the repository.

.. _contributing/markups/command:

Command
-------

Use the `command` markup to highlight a command.

.. list-table::
   :class: o-showcase-table

   * - Run the command :command:`make clean html` to delete existing built files and build the
       documentation to HTML.

   * - .. code-block:: text

          Run the command :command:`make clean html` to delete existing built files and build the
          documentation to HTML.

.. _contributing/lists:

Lists
=====

.. _contributing/bulleted-list:

Bulleted list
-------------

.. list-table::
   :class: o-showcase-table

   * - - This is a bulleted list.
       - It has two items, the second
         item uses two lines.

   * - .. code-block:: text

          - This is a bulleted list.
          - It has two items, the second
            item uses two lines.

.. _contributing/numbered-list:

Numbered list
-------------

.. list-table::
   :class: o-showcase-table

   * - #. This is a numbered list.
       #. Numbering is automatic.

   * - .. code-block:: text

          #. This is a numbered list.
          #. Numbering is automatic.

.. list-table::
   :class: o-showcase-table

   * - 6. Use this format to start the numbering
          with a number other than one.
       #. The numbering is automatic from there.

   * - .. code-block:: text

          6. Use this format to start the numbering
             with a number other than one.
          #. The numbering is automatic from there.

.. tip::
   Prefer the use of autonumbered lists with `#.` for better code resilience.

.. _contributing/nested-list:

Nested lists
------------

.. list-table::
   :class: o-showcase-table

   * - - This is the first item of a bulleted list.

         #. It has a nested numbered list
         #. with two items.

   * - .. code-block:: text

          - This is the first item of a bulleted list.

            #. It has a nested numbered list
            #. with two items.

.. _contributing/hyperlinks:

Hyperlinks
==========

.. _contributing/external-hyperlinks:

External hyperlinks
-------------------

External hyperlinks are links to a URL with a custom label. They follow this syntax:
```label <URL>`_``

.. note::
   - The URL can be a relative path to a file within the documentation.
   - Use the :ref:`documentation pages hyperlinks <contributing/doc-pages-hyperlinks>` if you target
     another documentation page.

.. list-table::
   :class: o-showcase-table

   * - For instance, `this is an external hyperlink to Odoo's website <https://www.odoo.com>`_.

   * - .. code-block:: text

          For instance, `this is an external hyperlink to Odoo's website <https://www.odoo.com>`_.

.. _contributing/external-hyperlink-aliases:

External hyperlink aliases
--------------------------

| External hyperlink aliases allow creating shortcuts for external hyperlinks.
| The definition syntax is as follows: ``.. _target: URL``
| There are two ways to reference them, depending on the use case:

#. ``target_`` creates a hyperlink with the target name as label and the URL as reference. Note that
   the ``_`` moved after the target!
#. ```label <target_>`_`` does exactly what you expect: the label replaces the name of the target,
   and the target is replaced by the URL.

.. list-table::
   :class: o-showcase-table

   * - A `proof-of-concept <https://en.wikipedia.org/wiki/Proof_of_concept>`_ is a simplified
       version, a prototype of what is expected to agree on the main lines of expected changes. `PoC
       <https://en.wikipedia.org/wiki/Proof_of_concept>`_ is a common abbreviation.

   * - .. code-block:: text

          .. _proof-of-concept: https://en.wikipedia.org/wiki/Proof_of_concept

             A proof-of-concept_ is a simplified version, a prototype of what is expected to agree on the main
             lines of expected changes. `PoC <proof-of-concept_>`_ is a common abbreviation.

.. _contributing/custom-anchors:

Custom anchors
--------------

Custom anchors follow the same syntax as external hyperlink aliases but without any URL. Indeed,
they are internal. They allow referencing a specific part of a document by using the target as an
anchor. When the user clicks on the reference, the documentation scrolls to the part of the
page containing the anchor.

| The definition syntax is: ``.. _target:``
| There are two ways to reference them, both using the ``ref`` markup:

#. ``:ref:`target``` creates a hyperlink to the anchor with the heading defined below as label.
#. ``:ref:`label <target>``` creates a hyperlink to the anchor with the given label.

See :ref:`contributing/relative-links` to learn how to write proper relative links for internal
references.

.. note::
   - Custom anchors can be referenced from other files than the ones in which they are defined.
   - Notice that there is no ``_`` at the end, contrary to what is done with :ref:`external
     hyperlinks <contributing/external-hyperlinks>`.

.. list-table::
   :class: o-showcase-table

   * - This can easily be done by creating a new product, see `How to create a product?
       <https://example.com/product>`_ for additional help.

       **How to create a product?**

       As explained at the `start of the page <https://example.com/scroll-to-start-of-page>`_, ...

   * - .. code-block:: text

          .. _sales/quotation/start-of-page:

          This can easily be done by creating a new product, see :ref:`product` for additional help.

          .. _sales/quotation/product:

          How to create a product?
          ========================

          As explained at the :ref:`start of the page <sales/quotation/start-of-page>`, ...

.. _contributing/doc-pages-hyperlinks:

Documentation pages hyperlinks
------------------------------

| The ``doc`` markup allows referencing a documentation page wherever it is in the file tree through
  a relative file path.
| As usual, there are two ways to use the markup:


#. ``:doc:`path_to_doc_page``` creates a hyperlink to the documentation page with the title of the
   page as label.
#. ``:doc:`label <path_to_doc_page>``` creates a hyperlink to the documentation page with the given
   label.

.. list-table::
   :class: o-showcase-table

   * - Please refer to `this documentation <https://example.com/doc/accounting/invoices.html>`_ and
       to `Send a pro-forma invoice <https://example.com/doc/sales/proforma.html>`_.

   * - .. code-block:: text

          Please refer to :doc:`this documentation <customer_invoices>` and to
          :doc:`../sales/sales/invoicing/proforma`.

.. _contributing/download:

File download hyperlinks
------------------------

The ``download`` markup allows referencing files (that are not necessarily :abbr:`RST
(reStructuredText)` documents) within the source tree to be downloaded.

.. list-table::
   :class: o-showcase-table

   * - Download this `module structure template
       <https://example.com/doc/odoosh/extras/my_module.zip>`_ to start building your module in no
       time.

   * - .. code-block:: text

          Download this :download:`module structure template <extras/my_module.zip>` to start building your
          module in no time.

.. _contributing/image:

Images
======

The ``image`` markup allows inserting images in a document.

.. list-table::
   :class: o-showcase-table

   * - .. image:: rst_cheat_sheet/create-invoice.png
          :align: center
          :alt: Create an invoice.

   * - .. code-block:: text

          .. image:: rst_cheat_sheet/create-invoice.png
             :align: center
             :alt: Create an invoice.

.. tip::
   Add the :code:`:class: o-no-modal` `option
   <https://docutils.sourceforge.io/docs/ref/rst/directives.html#common-options>`_ to an image to
   prevent opening it in a modal.

.. _contributing/alert-blocks:

Alert blocks (admonitions)
==========================

.. _contributing/seealso:

See also
--------

.. list-table::
   :class: o-showcase-table

   * - .. seealso::
          - `Customer invoices <https://example.com/doc/accounting/invoices.html>`_
          - `Pro-forma invoices <https://example.com/doc/sales/proforma.html#activate-the-feature>`_

   * - .. code-block:: text

          .. seealso::
             - :doc:`customer_invoices`
             - `Pro-forma invoices <../sales/sales/invoicing/proforma.html#activate-the-feature>`_

.. _contributing/note:

Note
----

.. list-table::
   :class: o-showcase-table

   * - .. note::
          Use this alert block to grab the reader's attention about additional information.

   * - .. code-block:: text

          .. note::
             Use this alert block to grab the reader's attention about additional information.

.. _contributing/tip:

Tip
---

.. list-table::
   :class: o-showcase-table

   * - .. tip::
          Use this alert block to inform the reader about a useful trick that requires an action.

   * - .. code-block:: text

          .. tip::
             Use this alert block to inform the reader about a useful trick that requires an action.

.. _contributing/example:

Example
-------

.. list-table::
   :class: o-showcase-table

   * - .. example::
          Use this alert block to show an example.

   * - .. code-block:: text

          .. example::
             Use this alert block to show an example.

.. _contributing/exercise:

Exercise
--------

.. list-table::
   :class: o-showcase-table

   * - .. exercise::
          Use this alert block to suggest an exercise to the reader.

   * - .. code-block:: text

          .. exercise::
             Use this alert block to suggest an exercise to the reader.

.. _contributing/important:

Important
---------

.. list-table::
   :class: o-showcase-table

   * - .. important::
          Use this alert block to notify the reader about important information.

   * - .. code-block:: text

          .. important::
             Use this alert block to notify the reader about important information.

.. _contributing/warning:

Warning
-------

.. list-table::
   :class: o-showcase-table

   * - .. warning::
          Use this alert block to require the reader to proceed with caution with what is described in the
          warning.

   * - .. code-block:: text

          .. warning::
             Use this alert block to require the reader to proceed with caution with what is described in the
             warning.

.. _contributing/danger:

Danger
------

.. list-table::
   :class: o-showcase-table

   * - .. danger::
          Use this alert block to bring the reader's attention to a serious threat.

   * - .. code-block:: text

          .. danger::
             Use this alert block to bring the reader's attention to a serious threat.

.. _contributing/custom-alert-blocks:

Custom
------

.. list-table::
   :class: o-showcase-table

   * - .. admonition:: Title

          Customize this alert block with a **Title** of your choice.

   * - .. code-block:: text

          .. admonition:: Title

             Customize this alert block with a **Title** of your choice.

.. _contributing/tables:

Tables
======

List tables
-----------

List tables use two-level bulleted lists to convert data into a table. The first level represents
the rows and the second level represents the columns.

.. list-table::
   :class: o-showcase-table

   * - .. list-table::
          :header-rows: 1
          :stub-columns: 1

          * - Name
            - Country
            - Favorite color
          * - Raúl
            - Montenegro
            - Purple
          * - Mélanie
            - France
            - Red

   * - .. code-block:: text

          .. list-table::
             :header-rows: 1
             :stub-columns: 1

             * - Name
               - Country
               - Favorite colour
             * - Raúl
               - Montenegro
               - Purple
             * - Mélanie
               - France
               - Turquoise

Grid tables
-----------

Grid tables represent the rendered table and are more visual to work with.

.. list-table::
   :class: o-showcase-table

   * - +-----------------------+--------------+---------------+
       |                       | Shirts       | T-shirts      |
       +=======================+==============+===============+
       | **Available colours** | Purple       | Green         |
       |                       +--------------+---------------+
       |                       | Turquoise    | Orange        |
       +-----------------------+--------------+---------------+
       | **Sleeves length**    | Long sleeves | Short sleeves |
       +-----------------------+--------------+---------------+

   * - .. code-block:: text

          +-----------------------+--------------+---------------+
          |                       | Shirts       | T-shirts      |
          +=======================+==============+===============+
          | **Available colours** | Purple       | Green         |
          |                       +--------------+---------------+
          |                       | Turquoise    | Orange        |
          +-----------------------+--------------+---------------+
          | **Sleeves length**    | Long sleeves | Short sleeves |
          +-----------------------+--------------+---------------+

.. tip::
   - Use `=` instead of `-` to define header rows.
   - Remove `-` and `|` separators to merge cells.
   - Make use of `this convenient table generator <https://www.tablesgenerator.com/text_tables>`_ to
     build your tables. Then, copy-paste the generated formatting into your document.

.. _contributing/code-blocks:

Code blocks
===========

.. list-table::
   :class: o-showcase-table

   * - .. code-block:: python

          def main():
              print("Hello world!")

   * - .. code-block:: text

          .. code-block:: python

             def main():
                 print("Hello world!")

.. _contributing/spoilers:

Spoilers
========

.. list-table::
   :class: o-showcase-table

   * - .. spoiler:: Answer to the Ultimate Question of Life, the Universe, and Everything

          **42**

   * - .. code-block:: text

          .. spoiler:: Answer to the Ultimate Question of Life, the Universe, and Everything

             **42**

.. _contributing/tabs:

Content tabs
============

.. caution::
   The `tabs` markup may not work well in some situations. In particular:

   - The tabs' headers cannot be translated.
   - A tab cannot contain :ref:`headings <contributing/headings>`.
   - An :ref:`alert block <contributing/alert-blocks>` cannot contain tabs.
   - A tab cannot contain :ref:`custom anchors <contributing/custom-anchors>`.

.. _contributing/tabs/basic:

Basic tabs
----------

Basic tabs are useful to split the content into multiple options. The `tabs` markup is used to
define sequence of tabs. Each tab is then defined with the `tab` markup followed by a label.

.. list-table::
   :class: o-showcase-table

   * - .. tabs::

          .. tab:: Odoo Online

             Content dedicated to Odoo Online users.

          .. tab:: Odoo.sh

             Alternative for Odoo.sh users.

          .. tab:: On-premise

             Third version for On-premise users.

   * - .. code-block:: text

          .. tabs::

             .. tab:: Odoo Online

                Content dedicated to Odoo Online users.

             .. tab:: Odoo.sh

                Alternative for Odoo.sh users.

             .. tab:: On-premise

                Third version for On-premise users.

.. _contributing/tabs/nested:

Nested tabs
-----------

Tabs can be nested inside one another.

.. list-table::
   :class: o-showcase-table

   * - .. tabs::

          .. tab:: Stars

             .. tabs::

                .. tab:: The Sun

                   The closest star to us.

                .. tab:: Proxima Centauri

                   The second closest star to us.

                .. tab:: Polaris

                   The North Star.

          .. tab:: Moons

             .. tabs::

                .. tab:: The Moon

                   Orbits the Earth.

                .. tab:: Titan

                   Orbits Jupiter.

   * - .. code-block:: text

          .. tabs::

             .. tab:: Stars

                .. tabs::

                   .. tab:: The Sun

                      The closest star to us.

                   .. tab:: Proxima Centauri

                      The second closest star to us.

                   .. tab:: Polaris

                      The North Star.

             .. tab:: Moons

                .. tabs::

                   .. tab:: The Moon

                      Orbits the Earth.

                   .. tab:: Titan

                      Orbits Jupiter.

.. _contributing/tabs/group:

Group tabs
----------

Group tabs are special tabs that synchronize based on a group label. The last selected group is
remembered and automatically selected when the user returns to the page or visits another page with
the tabs group. The `group-tab` markup is used to define group tabs.

.. list-table::
   :class: o-showcase-table

   * - .. tabs::

          .. group-tab:: C++

             C++

          .. group-tab:: Python

             Python

          .. group-tab:: Java

             Java

       .. tabs::

          .. group-tab:: C++

             .. code-block:: c++

                int main(const int argc, const char **argv) {
                    return 0;
                }

          .. group-tab:: Python

             .. code-block:: python

                def main():
                    return

          .. group-tab:: Java

             .. code-block:: java

                class Main {
                    public static void main(String[] args) {}
                }

   * - .. code-block:: text

          .. tabs::

             .. group-tab:: C++

                C++

             .. group-tab:: Python

                Python

             .. group-tab:: Java

                Java

          .. tabs::

             .. group-tab:: C++

                .. code-block:: c++

                   int main(const int argc, const char **argv) {
                       return 0;
                   }

             .. group-tab:: Python

                .. code-block:: python

                   def main():
                       return

             .. group-tab:: Java

                .. code-block:: java

                   class Main {
                       public static void main(String[] args) {}
                   }

.. _contributing/tabs/code:

Code tabs
---------

Code tabs are essentially :ref:`group tabs <contributing/tabs/group>` that treat the content as a
:ref:`code block <contributing/code-blocks>`. The `code-tab` markup is used to define a code tab.
Just as for the `code-block` markup, the language defines the syntax highlighting of the tab. If
set, the label is used instead of the language for grouping tabs.

.. list-table::
   :class: o-showcase-table

   * - .. tabs::

          .. code-tab:: c++ Hello C++

             #include <iostream>

             int main() {
                 std::cout << "Hello World";
                 return 0;
             }

          .. code-tab:: python Hello Python

             print("Hello World")

          .. code-tab:: javascript Hello JavaScript

             console.log("Hello World");

   * - .. code-block:: text

          .. tabs::

             .. code-tab:: c++ Hello C++

                #include <iostream>

                int main() {
                    std::cout << "Hello World";
                    return 0;
                }

             .. code-tab:: python Hello Python

                print("Hello World")

             .. code-tab:: javascript Hello JavaScript

                console.log("Hello World");

.. _contributing/cards:

Cards
=====

.. list-table::
   :class: o-showcase-table

   * - .. cards::

          .. card:: Documentation
             :target: ../documentation
             :tag: Step-by-step guide
             :large:

             Use this guide to acquire the tools and knowledge you need to write documentation.

          .. card:: Content guidelines
             :target: content_guidelines

             List of guidelines and trips and tricks to make your content shine at its brightest!

          .. card:: RST guidelines
             :target: rst_guidelines

             List of technical guidelines to observe when writing with reStructuredText.

   * - .. code-block:: text

          .. cards::

             .. card:: Documentation
                :target: ../documentation
                :tag: Step-by-step guide
                :large:

                Use this guide to acquire the tools and knowledge you need to write documentation.

             .. card:: Content guidelines
                :target: content_guidelines

                List of guidelines and trips and tricks to make your content shine at its brightest!

             .. card:: RST guidelines
                :target: rst_guidelines

                List of technical guidelines to observe when writing with reStructuredText.

.. _contributing/document-metadata:

Document metadata
=================

| Sphinx supports document-wide metadata markups that specify a behavior for the entire page.
| They must be placed between colons (`:`) at the top of the source file.

+-----------------+--------------------------------------------------------------------------------+
| **Metadata**    | **Purpose**                                                                    |
+-----------------+--------------------------------------------------------------------------------+
| `show-content`  |  Make a toctree page accessible from the navigation menu.                      |
+-----------------+--------------------------------------------------------------------------------+
| `show-toc`      |  Show the table of content on a page that has the `show-content` metadata      |
|                 |  markup.                                                                       |
+-----------------+--------------------------------------------------------------------------------+
| `code-column`   |  | Show a dynamic side column that can be used to display interactive          |
|                 |    tutorials or code excerpts.                                                 |
|                 |  | For example, see                                                            |
|                 |    :doc:`/applications/finance/accounting/get_started/cheat_sheet`.            |
+-----------------+--------------------------------------------------------------------------------+
| `hide-page-toc` | Hide the "On this page" sidebar and use full page width for the content.       |
+-----------------+--------------------------------------------------------------------------------+
| `custom-css`    | Link CSS files (comma-separated) to the document.                              |
+-----------------+--------------------------------------------------------------------------------+
| `custom-js`     | Link JS files (comma-separated) to the document.                               |
+-----------------+--------------------------------------------------------------------------------+
| `classes`       | Assign the specified classes to the `<main/>` element of the document.         |
+-----------------+--------------------------------------------------------------------------------+
| `orphan`        | Suppress the need to include the document in a toctree.                        |
+-----------------+--------------------------------------------------------------------------------+
| `nosearch`      | Exclude the document from search results.                                      |
+-----------------+--------------------------------------------------------------------------------+

.. _contributing/formatting-tips:

Formatting tips
===============

.. _contributing/line-break:

Break the line but not the paragraph
------------------------------------

.. list-table::
   :class: o-showcase-table

   * - | A first long line that you break in two
         -> here <- is rendered as a single line.
       | A second line that follows a line break.

   * - .. code-block:: text

          | A first long line that you break in two
            -> here <- is rendered as a single line.
          | A second line that follows a line break.

.. _contributing/escaping:

Escape markup symbols (Advanced)
--------------------------------

Markup symbols escaped with backslashes (``\``) are rendered normally. For instance, ``this
\*\*line of text\*\* with \*markup\* symbols`` is rendered as “this \*\*line of text\*\* with
\*markup\* symbols”.

When it comes to backticks (`````), which are used in many cases such as :ref:`external hyperlinks
<contributing/external-hyperlinks>`, using backslashes for escaping is no longer an option because
the outer backticks interpret enclosed backslashes and thus prevent them from escaping inner
backticks. For instance, ```\`this formatting\```` produces an ``[UNKNOWN NODE title_reference]``
error. Instead, `````this formatting````` should be used to produce the following result:
```this formatting```.

.. _contributing/icons:

Icons
=====

Icons are used to visually enhance the content and match the icons used on the Odoo user interface.
There are two main icon sets used: :ref:`Odoo UI <contributing/odoo-ui-icons>` and :ref:`Font
Awesome <contributing/fa-icons>`.

In order to use an icon in documentation, you **must** first include the icon set in the RST
document. This is done by adding the following line at the top of the document:

`.. include:: /icons.txt`

Then, you can use the icon by adding the corresponding markup to the document.

.. list-table::
   :class: o-showcase-table

   * - The graph view is represented by the |fa-bar-chart| :guilabel:`(bar chart)` icon.

   * - .. code-block:: text

          The graph view is represented by the |fa-bar-chart| :guilabel:`(bar chart)` icon.

.. _contributing/odoo-ui-icons:

Odoo UI
-------

.. list-table::
   :class: o-showcase-table table-columns

   * - |oi-view-pivot| `|oi-view-pivot|`

       |oi-text-break| `|oi-text-break|`

       |oi-text-inline| `|oi-text-inline|`

       |oi-voip| `|oi-voip|`

       |oi-odoo| `|oi-odoo|`

       |oi-search| `|oi-search|`

       |oi-group| `|oi-group|`

       |oi-settings-adjust| `|oi-settings-adjust|`

       |oi-apps| `|oi-apps|`

       |oi-panel-right| `|oi-panel-right|`

       |oi-launch| `|oi-launch|`

       |oi-studio| `|oi-studio|`

       |oi-view-kanban| `|oi-view-kanban|`

       |oi-text-wrap| `|oi-text-wrap|`

       |oi-view-cohort| `|oi-view-cohort|`

       |oi-view-list| `|oi-view-list|`

       |oi-gif-picker| `|oi-gif-picker|`

       |oi-chevron-down| `|oi-chevron-down|`

       |oi-chevron-left| `|oi-chevron-left|`

       |oi-chevron-right| `|oi-chevron-right|`

       |oi-chevron-up| `|oi-chevron-up|`

       |oi-arrows-h| `|oi-arrows-h|`

       |oi-arrows-v| `|oi-arrows-v|`

       |oi-arrow-down-left| `|oi-arrow-down-left|`

       |oi-arrow-down-right| `|oi-arrow-down-right|`

       |oi-arrow-down| `|oi-arrow-down|`

       |oi-arrow-left| `|oi-arrow-left|`

       |oi-arrow-right| `|oi-arrow-right|`

       |oi-arrow-up-left| `|oi-arrow-up-left|`

       |oi-arrow-up-right| `|oi-arrow-up-right|`

       |oi-arrow-up| `|oi-arrow-up|`

       |oi-draggable| `|oi-draggable|`

       |oi-view| `|oi-view|`

       |oi-archive| `|oi-archive|`

       |oi-unarchive| `|oi-unarchive|`

       |oi-text-effect| `|oi-text-effect|`

       |oi-smile-add| `|oi-smile-add|`

       |oi-close| `|oi-close|`

.. _contributing/fa-icons:

Font Awesome
------------

.. list-table::
   :class: o-showcase-table table-columns

   * - |fa-glass| `|fa-glass|`

       |fa-music| `|fa-music|`

       |fa-search| `|fa-search|`

       |fa-envelope-o| `|fa-envelope-o|`

       |fa-heart| `|fa-heart|`

       |fa-star| `|fa-star|`

       |fa-star-o| `|fa-star-o|`

       |fa-user| `|fa-user|`

       |fa-film| `|fa-film|`

       |fa-th-large| `|fa-th-large|`

       |fa-th| `|fa-th|`

       |fa-th-list| `|fa-th-list|`

       |fa-check| `|fa-check|`

       |fa-times| `|fa-times|`

       |fa-search-plus| `|fa-search-plus|`

       |fa-search-minus| `|fa-search-minus|`

       |fa-power-off| `|fa-power-off|`

       |fa-signal| `|fa-signal|`

       |fa-gear| `|fa-gear|`

       |fa-trash-o| `|fa-trash-o|`

       |fa-home| `|fa-home|`

       |fa-file-o| `|fa-file-o|`

       |fa-clock-o| `|fa-clock-o|`

       |fa-road| `|fa-road|`

       |fa-download| `|fa-download|`

       |fa-arrow-circle-o-down| `|fa-arrow-circle-o-down|`

       |fa-arrow-circle-o-up| `|fa-arrow-circle-o-up|`

       |fa-inbox| `|fa-inbox|`

       |fa-play-circle-o| `|fa-play-circle-o|`

       |fa-repeat| `|fa-repeat|`

       |fa-refresh| `|fa-refresh|`

       |fa-list-alt| `|fa-list-alt|`

       |fa-lock| `|fa-lock|`

       |fa-flag| `|fa-flag|`

       |fa-headphones| `|fa-headphones|`

       |fa-volume-off| `|fa-volume-off|`

       |fa-volume-down| `|fa-volume-down|`

       |fa-volume-up| `|fa-volume-up|`

       |fa-qrcode| `|fa-qrcode|`

       |fa-barcode| `|fa-barcode|`

       |fa-tag| `|fa-tag|`

       |fa-tags| `|fa-tags|`

       |fa-book| `|fa-book|`

       |fa-bookmark| `|fa-bookmark|`

       |fa-print| `|fa-print|`

       |fa-camera| `|fa-camera|`

       |fa-font| `|fa-font|`

       |fa-bold| `|fa-bold|`

       |fa-italic| `|fa-italic|`

       |fa-text-height| `|fa-text-height|`

       |fa-text-width| `|fa-text-width|`

       |fa-align-left| `|fa-align-left|`

       |fa-align-center| `|fa-align-center|`

       |fa-align-right| `|fa-align-right|`

       |fa-align-justify| `|fa-align-justify|`

       |fa-list| `|fa-list|`

       |fa-dedent| `|fa-dedent|`

       |fa-indent| `|fa-indent|`

       |fa-video-camera| `|fa-video-camera|`

       |fa-picture-o| `|fa-picture-o|`

       |fa-pencil| `|fa-pencil|`

       |fa-map-marker| `|fa-map-marker|`

       |fa-adjust| `|fa-adjust|`

       |fa-tint| `|fa-tint|`

       |fa-edit| `|fa-edit|`

       |fa-share-square-o| `|fa-share-square-o|`

       |fa-check-square-o| `|fa-check-square-o|`

       |fa-arrows| `|fa-arrows|`

       |fa-step-backward| `|fa-step-backward|`

       |fa-fast-backward| `|fa-fast-backward|`

       |fa-backward| `|fa-backward|`

       |fa-play| `|fa-play|`

       |fa-pause| `|fa-pause|`

       |fa-stop| `|fa-stop|`

       |fa-forward| `|fa-forward|`

       |fa-fast-forward| `|fa-fast-forward|`

       |fa-step-forward| `|fa-step-forward|`

       |fa-eject| `|fa-eject|`

       |fa-chevron-left| `|fa-chevron-left|`

       |fa-chevron-right| `|fa-chevron-right|`

       |fa-plus-circle| `|fa-plus-circle|`

       |fa-minus-circle| `|fa-minus-circle|`

       |fa-times-circle| `|fa-times-circle|`

       |fa-check-circle| `|fa-check-circle|`

       |fa-question-circle| `|fa-question-circle|`

       |fa-info-circle| `|fa-info-circle|`

       |fa-crosshairs| `|fa-crosshairs|`

       |fa-times-circle-o| `|fa-times-circle-o|`

       |fa-check-circle-o| `|fa-check-circle-o|`

       |fa-ban| `|fa-ban|`

       |fa-arrow-left| `|fa-arrow-left|`

       |fa-arrow-right| `|fa-arrow-right|`

       |fa-arrow-up| `|fa-arrow-up|`

       |fa-arrow-down| `|fa-arrow-down|`

       |fa-mail-forward| `|fa-mail-forward|`

       |fa-share| `|fa-share|`

       |fa-expand| `|fa-expand|`

       |fa-compress| `|fa-compress|`

       |fa-plus| `|fa-plus|`

       |fa-minus| `|fa-minus|`

       |fa-asterisk| `|fa-asterisk|`

       |fa-exclamation-circle| `|fa-exclamation-circle|`

       |fa-gift| `|fa-gift|`

       |fa-leaf| `|fa-leaf|`

       |fa-fire| `|fa-fire|`

       |fa-eye| `|fa-eye|`

       |fa-eye-slash| `|fa-eye-slash|`

       |fa-warning| `|fa-warning|`

       |fa-plane| `|fa-plane|`

       |fa-calendar| `|fa-calendar|`

       |fa-random| `|fa-random|`

       |fa-comment| `|fa-comment|`

       |fa-magnet| `|fa-magnet|`

       |fa-chevron-up| `|fa-chevron-up|`

       |fa-chevron-down| `|fa-chevron-down|`

       |fa-retweet| `|fa-retweet|`

       |fa-shopping-cart| `|fa-shopping-cart|`

       |fa-folder| `|fa-folder|`

       |fa-folder-open| `|fa-folder-open|`

       |fa-arrows-v| `|fa-arrows-v|`

       |fa-arrows-h| `|fa-arrows-h|`

       |fa-bar-chart-o| `|fa-bar-chart-o|`

       |fa-bar-chart| `|fa-bar-chart|`

       |fa-twitter-square| `|fa-twitter-square|`

       |fa-facebook-square| `|fa-facebook-square|`

       |fa-camera-retro| `|fa-camera-retro|`

       |fa-key| `|fa-key|`

       |fa-gears| `|fa-gears|`

       |fa-comments| `|fa-comments|`

       |fa-thumbs-o-up| `|fa-thumbs-o-up|`

       |fa-thumbs-o-down| `|fa-thumbs-o-down|`

       |fa-star-half| `|fa-star-half|`

       |fa-heart-o| `|fa-heart-o|`

       |fa-sign-out| `|fa-sign-out|`

       |fa-linkedin-square| `|fa-linkedin-square|`

       |fa-thumb-tack| `|fa-thumb-tack|`

       |fa-external-link| `|fa-external-link|`

       |fa-sign-in| `|fa-sign-in|`

       |fa-trophy| `|fa-trophy|`

       |fa-github-square| `|fa-github-square|`

       |fa-upload| `|fa-upload|`

       |fa-lemon-o| `|fa-lemon-o|`

       |fa-phone| `|fa-phone|`

       |fa-square-o| `|fa-square-o|`

       |fa-bookmark-o| `|fa-bookmark-o|`

       |fa-phone-square| `|fa-phone-square|`

       |fa-twitter| `|fa-twitter|`

       |fa-facebook-f| `|fa-facebook-f|`

       |fa-facebook| `|fa-facebook|`

       |fa-github| `|fa-github|`

       |fa-unlock| `|fa-unlock|`

       |fa-credit-card| `|fa-credit-card|`

       |fa-rss| `|fa-rss|`

       |fa-hdd-o| `|fa-hdd-o|`

       |fa-bullhorn| `|fa-bullhorn|`

       |fa-bell| `|fa-bell|`

       |fa-certificate| `|fa-certificate|`

       |fa-hand-o-right| `|fa-hand-o-right|`

       |fa-hand-o-left| `|fa-hand-o-left|`

       |fa-hand-o-up| `|fa-hand-o-up|`

       |fa-hand-o-down| `|fa-hand-o-down|`

       |fa-arrow-circle-left| `|fa-arrow-circle-left|`

       |fa-arrow-circle-right| `|fa-arrow-circle-right|`

       |fa-arrow-circle-up| `|fa-arrow-circle-up|`

       |fa-arrow-circle-down| `|fa-arrow-circle-down|`

       |fa-globe| `|fa-globe|`

       |fa-wrench| `|fa-wrench|`

       |fa-tasks| `|fa-tasks|`

       |fa-filter| `|fa-filter|`

       |fa-briefcase| `|fa-briefcase|`

       |fa-arrows-alt| `|fa-arrows-alt|`

       |fa-users| `|fa-users|`

       |fa-link| `|fa-link|`

       |fa-cloud| `|fa-cloud|`

       |fa-flask| `|fa-flask|`

       |fa-scissors| `|fa-scissors|`

       |fa-copy| `|fa-copy|`

       |fa-paperclip| `|fa-paperclip|`

       |fa-save| `|fa-save|`

       |fa-square| `|fa-square|`

       |fa-bars| `|fa-bars|`

       |fa-list-ul| `|fa-list-ul|`

       |fa-list-ol| `|fa-list-ol|`

       |fa-strikethrough| `|fa-strikethrough|`

       |fa-underline| `|fa-underline|`

       |fa-table| `|fa-table|`

       |fa-magic| `|fa-magic|`

       |fa-truck| `|fa-truck|`

       |fa-pinterest| `|fa-pinterest|`

       |fa-pinterest-square| `|fa-pinterest-square|`

       |fa-google-plus-square| `|fa-google-plus-square|`

       |fa-google-plus| `|fa-google-plus|`

       |fa-money| `|fa-money|`

       |fa-caret-down| `|fa-caret-down|`

       |fa-caret-up| `|fa-caret-up|`

       |fa-caret-left| `|fa-caret-left|`

       |fa-caret-right| `|fa-caret-right|`

       |fa-columns| `|fa-columns|`

       |fa-unsorted| `|fa-unsorted|`

       |fa-sort| `|fa-sort|`

       |fa-sort-desc| `|fa-sort-desc|`

       |fa-sort-asc| `|fa-sort-asc|`

       |fa-envelope| `|fa-envelope|`

       |fa-linkedin| `|fa-linkedin|`

       |fa-undo| `|fa-undo|`

       |fa-gavel| `|fa-gavel|`

       |fa-tachometer| `|fa-tachometer|`

       |fa-comment-o| `|fa-comment-o|`

       |fa-comments-o| `|fa-comments-o|`

       |fa-bolt| `|fa-bolt|`

       |fa-sitemap| `|fa-sitemap|`

       |fa-umbrella| `|fa-umbrella|`

       |fa-clipboard| `|fa-clipboard|`

       |fa-lightbulb-o| `|fa-lightbulb-o|`

       |fa-exchange| `|fa-exchange|`

       |fa-cloud-download| `|fa-cloud-download|`

       |fa-cloud-upload| `|fa-cloud-upload|`

       |fa-user-md| `|fa-user-md|`

       |fa-stethoscope| `|fa-stethoscope|`

       |fa-suitcase| `|fa-suitcase|`

       |fa-bell-o| `|fa-bell-o|`

       |fa-coffee| `|fa-coffee|`

       |fa-cutlery| `|fa-cutlery|`

       |fa-file-text-o| `|fa-file-text-o|`

       |fa-building-o| `|fa-building-o|`

       |fa-hospital-o| `|fa-hospital-o|`

       |fa-ambulance| `|fa-ambulance|`

       |fa-medkit| `|fa-medkit|`

       |fa-fighter-jet| `|fa-fighter-jet|`

       |fa-beer| `|fa-beer|`

       |fa-h-square| `|fa-h-square|`

       |fa-plus-square| `|fa-plus-square|`

       |fa-angle-double-left| `|fa-angle-double-left|`

       |fa-angle-double-right| `|fa-angle-double-right|`

       |fa-angle-double-up| `|fa-angle-double-up|`

       |fa-angle-double-down| `|fa-angle-double-down|`

       |fa-angle-left| `|fa-angle-left|`

       |fa-angle-right| `|fa-angle-right|`

       |fa-angle-up| `|fa-angle-up|`

       |fa-angle-down| `|fa-angle-down|`

       |fa-desktop| `|fa-desktop|`

       |fa-laptop| `|fa-laptop|`

       |fa-tablet| `|fa-tablet|`

       |fa-mobile| `|fa-mobile|`

       |fa-circle-o| `|fa-circle-o|`

       |fa-quote-left| `|fa-quote-left|`

       |fa-quote-right| `|fa-quote-right|`

       |fa-spinner| `|fa-spinner|`

       |fa-circle| `|fa-circle|`

       |fa-reply| `|fa-reply|`

       |fa-github-alt| `|fa-github-alt|`

       |fa-folder-o| `|fa-folder-o|`

       |fa-folder-open-o| `|fa-folder-open-o|`

       |fa-smile-o| `|fa-smile-o|`

       |fa-frown-o| `|fa-frown-o|`

       |fa-meh-o| `|fa-meh-o|`

       |fa-gamepad| `|fa-gamepad|`

       |fa-keyboard-o| `|fa-keyboard-o|`

       |fa-flag-o| `|fa-flag-o|`

       |fa-flag-checkered| `|fa-flag-checkered|`

       |fa-terminal| `|fa-terminal|`

       |fa-code| `|fa-code|`

       |fa-reply-all| `|fa-reply-all|`

       |fa-star-half-o| `|fa-star-half-o|`

       |fa-location-arrow| `|fa-location-arrow|`

       |fa-crop| `|fa-crop|`

       |fa-code-fork| `|fa-code-fork|`

       |fa-chain-broken| `|fa-chain-broken|`

       |fa-question| `|fa-question|`

       |fa-info| `|fa-info|`

       |fa-exclamation| `|fa-exclamation|`

       |fa-superscript| `|fa-superscript|`

       |fa-subscript| `|fa-subscript|`

       |fa-eraser| `|fa-eraser|`

       |fa-puzzle-piece| `|fa-puzzle-piece|`

       |fa-microphone| `|fa-microphone|`

       |fa-microphone-slash| `|fa-microphone-slash|`

       |fa-shield| `|fa-shield|`

       |fa-calendar-o| `|fa-calendar-o|`

       |fa-fire-extinguisher| `|fa-fire-extinguisher|`

       |fa-rocket| `|fa-rocket|`

       |fa-maxcdn| `|fa-maxcdn|`

       |fa-chevron-circle-left| `|fa-chevron-circle-left|`

       |fa-chevron-circle-right| `|fa-chevron-circle-right|`

       |fa-chevron-circle-up| `|fa-chevron-circle-up|`

       |fa-chevron-circle-down| `|fa-chevron-circle-down|`

       |fa-html5| `|fa-html5|`

       |fa-css3| `|fa-css3|`

       |fa-anchor| `|fa-anchor|`

       |fa-unlock-alt| `|fa-unlock-alt|`

       |fa-bullseye| `|fa-bullseye|`

       |fa-ellipsis-h| `|fa-ellipsis-h|`

       |fa-ellipsis-v| `|fa-ellipsis-v|`

       |fa-rss-square| `|fa-rss-square|`

       |fa-play-circle| `|fa-play-circle|`

       |fa-ticket| `|fa-ticket|`

       |fa-minus-square| `|fa-minus-square|`

       |fa-minus-square-o| `|fa-minus-square-o|`

       |fa-level-up| `|fa-level-up|`

       |fa-level-down| `|fa-level-down|`

       |fa-check-square| `|fa-check-square|`

       |fa-pencil-square| `|fa-pencil-square|`

       |fa-external-link-square| `|fa-external-link-square|`

       |fa-share-square| `|fa-share-square|`

       |fa-compass| `|fa-compass|`

       |fa-toggle-down| `|fa-toggle-down|`

       |fa-toggle-up| `|fa-toggle-up|`

       |fa-toggle-right| `|fa-toggle-right|`

       |fa-eur| `|fa-eur|`

       |fa-gbp| `|fa-gbp|`

       |fa-usd| `|fa-usd|`

       |fa-inr| `|fa-inr|`

       |fa-jpy| `|fa-jpy|`

       |fa-rub| `|fa-rub|`

       |fa-krw| `|fa-krw|`

       |fa-btc| `|fa-btc|`

       |fa-file| `|fa-file|`

       |fa-file-text| `|fa-file-text|`

       |fa-sort-alpha-asc| `|fa-sort-alpha-asc|`

       |fa-sort-alpha-desc| `|fa-sort-alpha-desc|`

       |fa-sort-amount-asc| `|fa-sort-amount-asc|`

       |fa-sort-amount-desc| `|fa-sort-amount-desc|`

       |fa-sort-numeric-asc| `|fa-sort-numeric-asc|`

       |fa-sort-numeric-desc| `|fa-sort-numeric-desc|`

       |fa-thumbs-up| `|fa-thumbs-up|`

       |fa-thumbs-down| `|fa-thumbs-down|`

       |fa-youtube-square| `|fa-youtube-square|`

       |fa-youtube| `|fa-youtube|`

       |fa-xing| `|fa-xing|`

       |fa-xing-square| `|fa-xing-square|`

       |fa-youtube-play| `|fa-youtube-play|`

       |fa-dropbox| `|fa-dropbox|`

       |fa-stack-overflow| `|fa-stack-overflow|`

       |fa-instagram| `|fa-instagram|`

       |fa-flickr| `|fa-flickr|`

       |fa-adn| `|fa-adn|`

       |fa-bitbucket| `|fa-bitbucket|`

       |fa-bitbucket-square| `|fa-bitbucket-square|`

       |fa-tumblr| `|fa-tumblr|`

       |fa-tumblr-square| `|fa-tumblr-square|`

       |fa-long-arrow-down| `|fa-long-arrow-down|`

       |fa-long-arrow-up| `|fa-long-arrow-up|`

       |fa-long-arrow-left| `|fa-long-arrow-left|`

       |fa-long-arrow-right| `|fa-long-arrow-right|`

       |fa-apple| `|fa-apple|`

       |fa-windows| `|fa-windows|`

       |fa-android| `|fa-android|`

       |fa-linux| `|fa-linux|`

       |fa-dribbble| `|fa-dribbble|`

       |fa-skype| `|fa-skype|`

       |fa-foursquare| `|fa-foursquare|`

       |fa-trello| `|fa-trello|`

       |fa-female| `|fa-female|`

       |fa-male| `|fa-male|`

       |fa-gratipay| `|fa-gratipay|`

       |fa-sun-o| `|fa-sun-o|`

       |fa-moon-o| `|fa-moon-o|`

       |fa-archive| `|fa-archive|`

       |fa-bug| `|fa-bug|`

       |fa-vk| `|fa-vk|`

       |fa-weibo| `|fa-weibo|`

       |fa-renren| `|fa-renren|`

       |fa-pagelines| `|fa-pagelines|`

       |fa-stack-exchange| `|fa-stack-exchange|`

       |fa-arrow-circle-o-right| `|fa-arrow-circle-o-right|`

       |fa-arrow-circle-o-left| `|fa-arrow-circle-o-left|`

       |fa-caret-square-o-left| `|fa-caret-square-o-left|`

       |fa-dot-circle-o| `|fa-dot-circle-o|`

       |fa-wheelchair| `|fa-wheelchair|`

       |fa-vimeo-square| `|fa-vimeo-square|`

       |fa-try| `|fa-try|`

       |fa-plus-square-o| `|fa-plus-square-o|`

       |fa-space-shuttle| `|fa-space-shuttle|`

       |fa-slack| `|fa-slack|`

       |fa-envelope-square| `|fa-envelope-square|`

       |fa-wordpress| `|fa-wordpress|`

       |fa-openid| `|fa-openid|`

       |fa-university| `|fa-university|`

       |fa-graduation-cap| `|fa-graduation-cap|`

       |fa-yahoo| `|fa-yahoo|`

       |fa-google| `|fa-google|`

       |fa-reddit| `|fa-reddit|`

       |fa-reddit-square| `|fa-reddit-square|`

       |fa-stumbleupon-circle| `|fa-stumbleupon-circle|`

       |fa-stumbleupon| `|fa-stumbleupon|`

       |fa-delicious| `|fa-delicious|`

       |fa-digg| `|fa-digg|`

       |fa-pied-piper-pp| `|fa-pied-piper-pp|`

       |fa-pied-piper-alt| `|fa-pied-piper-alt|`

       |fa-drupal| `|fa-drupal|`

       |fa-joomla| `|fa-joomla|`

       |fa-language| `|fa-language|`

       |fa-fax| `|fa-fax|`

       |fa-building| `|fa-building|`

       |fa-child| `|fa-child|`

       |fa-paw| `|fa-paw|`

       |fa-spoon| `|fa-spoon|`

       |fa-cube| `|fa-cube|`

       |fa-cubes| `|fa-cubes|`

       |fa-behance| `|fa-behance|`

       |fa-behance-square| `|fa-behance-square|`

       |fa-steam| `|fa-steam|`

       |fa-steam-square| `|fa-steam-square|`

       |fa-recycle| `|fa-recycle|`

       |fa-car| `|fa-car|`

       |fa-taxi| `|fa-taxi|`

       |fa-tree| `|fa-tree|`

       |fa-spotify| `|fa-spotify|`

       |fa-deviantart| `|fa-deviantart|`

       |fa-soundcloud| `|fa-soundcloud|`

       |fa-database| `|fa-database|`

       |fa-file-pdf-o| `|fa-file-pdf-o|`

       |fa-file-word-o| `|fa-file-word-o|`

       |fa-file-excel-o| `|fa-file-excel-o|`

       |fa-file-powerpoint-o| `|fa-file-powerpoint-o|`

       |fa-file-image-o| `|fa-file-image-o|`

       |fa-file-archive-o| `|fa-file-archive-o|`

       |fa-file-audio-o| `|fa-file-audio-o|`

       |fa-file-video-o| `|fa-file-video-o|`

       |fa-file-code-o| `|fa-file-code-o|`

       |fa-vine| `|fa-vine|`

       |fa-codepen| `|fa-codepen|`

       |fa-jsfiddle| `|fa-jsfiddle|`

       |fa-life-ring| `|fa-life-ring|`

       |fa-circle-o-notch| `|fa-circle-o-notch|`

       |fa-rebel| `|fa-rebel|`

       |fa-empire| `|fa-empire|`

       |fa-git-square| `|fa-git-square|`

       |fa-git| `|fa-git|`

       |fa-hacker-news| `|fa-hacker-news|`

       |fa-tencent-weibo| `|fa-tencent-weibo|`

       |fa-qq| `|fa-qq|`

       |fa-weixin| `|fa-weixin|`

       |fa-paper-plane| `|fa-paper-plane|`

       |fa-paper-plane-o| `|fa-paper-plane-o|`

       |fa-history| `|fa-history|`

       |fa-circle-thin| `|fa-circle-thin|`

       |fa-header| `|fa-header|`

       |fa-paragraph| `|fa-paragraph|`

       |fa-sliders| `|fa-sliders|`

       |fa-share-alt| `|fa-share-alt|`

       |fa-share-alt-square| `|fa-share-alt-square|`

       |fa-bomb| `|fa-bomb|`

       |fa-futbol-o| `|fa-futbol-o|`

       |fa-tty| `|fa-tty|`

       |fa-binoculars| `|fa-binoculars|`

       |fa-plug| `|fa-plug|`

       |fa-slideshare| `|fa-slideshare|`

       |fa-twitch| `|fa-twitch|`

       |fa-yelp| `|fa-yelp|`

       |fa-newspaper-o| `|fa-newspaper-o|`

       |fa-wifi| `|fa-wifi|`

       |fa-calculator| `|fa-calculator|`

       |fa-paypal| `|fa-paypal|`

       |fa-google-wallet| `|fa-google-wallet|`

       |fa-cc-visa| `|fa-cc-visa|`

       |fa-cc-mastercard| `|fa-cc-mastercard|`

       |fa-cc-discover| `|fa-cc-discover|`

       |fa-cc-amex| `|fa-cc-amex|`

       |fa-cc-paypal| `|fa-cc-paypal|`

       |fa-cc-stripe| `|fa-cc-stripe|`

       |fa-bell-slash| `|fa-bell-slash|`

       |fa-bell-slash-o| `|fa-bell-slash-o|`

       |fa-trash| `|fa-trash|`

       |fa-copyright| `|fa-copyright|`

       |fa-at| `|fa-at|`

       |fa-eyedropper| `|fa-eyedropper|`

       |fa-paint-brush| `|fa-paint-brush|`

       |fa-birthday-cake| `|fa-birthday-cake|`

       |fa-area-chart| `|fa-area-chart|`

       |fa-pie-chart| `|fa-pie-chart|`

       |fa-line-chart| `|fa-line-chart|`

       |fa-lastfm| `|fa-lastfm|`

       |fa-lastfm-square| `|fa-lastfm-square|`

       |fa-toggle-off| `|fa-toggle-off|`

       |fa-toggle-on| `|fa-toggle-on|`

       |fa-bicycle| `|fa-bicycle|`

       |fa-bus| `|fa-bus|`

       |fa-ioxhost| `|fa-ioxhost|`

       |fa-angellist| `|fa-angellist|`

       |fa-cc| `|fa-cc|`

       |fa-ils| `|fa-ils|`

       |fa-meanpath| `|fa-meanpath|`

       |fa-buysellads| `|fa-buysellads|`

       |fa-connectdevelop| `|fa-connectdevelop|`

       |fa-dashcube| `|fa-dashcube|`

       |fa-forumbee| `|fa-forumbee|`

       |fa-leanpub| `|fa-leanpub|`

       |fa-sellsy| `|fa-sellsy|`

       |fa-shirtsinbulk| `|fa-shirtsinbulk|`

       |fa-simplybuilt| `|fa-simplybuilt|`

       |fa-skyatlas| `|fa-skyatlas|`

       |fa-cart-plus| `|fa-cart-plus|`

       |fa-cart-arrow-down| `|fa-cart-arrow-down|`

       |fa-diamond| `|fa-diamond|`

       |fa-ship| `|fa-ship|`

       |fa-user-secret| `|fa-user-secret|`

       |fa-motorcycle| `|fa-motorcycle|`

       |fa-street-view| `|fa-street-view|`

       |fa-heartbeat| `|fa-heartbeat|`

       |fa-venus| `|fa-venus|`

       |fa-mars| `|fa-mars|`

       |fa-mercury| `|fa-mercury|`

       |fa-transgender| `|fa-transgender|`

       |fa-transgender-alt| `|fa-transgender-alt|`

       |fa-venus-double| `|fa-venus-double|`

       |fa-mars-double| `|fa-mars-double|`

       |fa-venus-mars| `|fa-venus-mars|`

       |fa-mars-stroke| `|fa-mars-stroke|`

       |fa-mars-stroke-v| `|fa-mars-stroke-v|`

       |fa-mars-stroke-h| `|fa-mars-stroke-h|`

       |fa-neuter| `|fa-neuter|`

       |fa-genderless| `|fa-genderless|`

       |fa-facebook-official| `|fa-facebook-official|`

       |fa-pinterest-p| `|fa-pinterest-p|`

       |fa-whatsapp| `|fa-whatsapp|`

       |fa-server| `|fa-server|`

       |fa-user-plus| `|fa-user-plus|`

       |fa-user-times| `|fa-user-times|`

       |fa-bed| `|fa-bed|`

       |fa-viacoin| `|fa-viacoin|`

       |fa-train| `|fa-train|`

       |fa-subway| `|fa-subway|`

       |fa-medium| `|fa-medium|`

       |fa-y-combinator| `|fa-y-combinator|`

       |fa-optin-monster| `|fa-optin-monster|`

       |fa-opencart| `|fa-opencart|`

       |fa-expeditedssl| `|fa-expeditedssl|`

       |fa-battery-full| `|fa-battery-full|`

       |fa-battery-three-quarters| `|fa-battery-three-quarters|`

       |fa-battery-half| `|fa-battery-half|`

       |fa-battery-quarter| `|fa-battery-quarter|`

       |fa-battery-empty| `|fa-battery-empty|`

       |fa-mouse-pointer| `|fa-mouse-pointer|`

       |fa-i-cursor| `|fa-i-cursor|`

       |fa-object-group| `|fa-object-group|`

       |fa-object-ungroup| `|fa-object-ungroup|`

       |fa-sticky-note| `|fa-sticky-note|`

       |fa-sticky-note-o| `|fa-sticky-note-o|`

       |fa-cc-jcb| `|fa-cc-jcb|`

       |fa-cc-diners-club| `|fa-cc-diners-club|`

       |fa-clone| `|fa-clone|`

       |fa-balance-scale| `|fa-balance-scale|`

       |fa-hourglass-o| `|fa-hourglass-o|`

       |fa-hourglass-start| `|fa-hourglass-start|`

       |fa-hourglass-half| `|fa-hourglass-half|`

       |fa-hourglass-end| `|fa-hourglass-end|`

       |fa-hourglass| `|fa-hourglass|`

       |fa-hand-rock-o| `|fa-hand-rock-o|`

       |fa-hand-paper-o| `|fa-hand-paper-o|`

       |fa-hand-scissors-o| `|fa-hand-scissors-o|`

       |fa-hand-lizard-o| `|fa-hand-lizard-o|`

       |fa-hand-spock-o| `|fa-hand-spock-o|`

       |fa-hand-pointer-o| `|fa-hand-pointer-o|`

       |fa-hand-peace-o| `|fa-hand-peace-o|`

       |fa-trademark| `|fa-trademark|`

       |fa-registered| `|fa-registered|`

       |fa-creative-commons| `|fa-creative-commons|`

       |fa-gg| `|fa-gg|`

       |fa-gg-circle| `|fa-gg-circle|`

       |fa-tripadvisor| `|fa-tripadvisor|`

       |fa-odnoklassniki| `|fa-odnoklassniki|`

       |fa-odnoklassniki-square| `|fa-odnoklassniki-square|`

       |fa-get-pocket| `|fa-get-pocket|`

       |fa-wikipedia-w| `|fa-wikipedia-w|`

       |fa-safari| `|fa-safari|`

       |fa-chrome| `|fa-chrome|`

       |fa-firefox| `|fa-firefox|`

       |fa-opera| `|fa-opera|`

       |fa-internet-explorer| `|fa-internet-explorer|`

       |fa-television| `|fa-television|`

       |fa-contao| `|fa-contao|`

       |fa-500px| `|fa-500px|`

       |fa-amazon| `|fa-amazon|`

       |fa-calendar-plus-o| `|fa-calendar-plus-o|`

       |fa-calendar-minus-o| `|fa-calendar-minus-o|`

       |fa-calendar-times-o| `|fa-calendar-times-o|`

       |fa-calendar-check-o| `|fa-calendar-check-o|`

       |fa-industry| `|fa-industry|`

       |fa-map-pin| `|fa-map-pin|`

       |fa-map-signs| `|fa-map-signs|`

       |fa-map-o| `|fa-map-o|`

       |fa-map| `|fa-map|`

       |fa-commenting| `|fa-commenting|`

       |fa-commenting-o| `|fa-commenting-o|`

       |fa-houzz| `|fa-houzz|`

       |fa-vimeo| `|fa-vimeo|`

       |fa-black-tie| `|fa-black-tie|`

       |fa-fonticons| `|fa-fonticons|`

       |fa-reddit-alien| `|fa-reddit-alien|`

       |fa-edge| `|fa-edge|`

       |fa-credit-card-alt| `|fa-credit-card-alt|`

       |fa-codiepie| `|fa-codiepie|`

       |fa-modx| `|fa-modx|`

       |fa-fort-awesome| `|fa-fort-awesome|`

       |fa-usb| `|fa-usb|`

       |fa-product-hunt| `|fa-product-hunt|`

       |fa-mixcloud| `|fa-mixcloud|`

       |fa-scribd| `|fa-scribd|`

       |fa-pause-circle| `|fa-pause-circle|`

       |fa-pause-circle-o| `|fa-pause-circle-o|`

       |fa-stop-circle| `|fa-stop-circle|`

       |fa-stop-circle-o| `|fa-stop-circle-o|`

       |fa-shopping-bag| `|fa-shopping-bag|`

       |fa-shopping-basket| `|fa-shopping-basket|`

       |fa-hashtag| `|fa-hashtag|`

       |fa-bluetooth| `|fa-bluetooth|`

       |fa-bluetooth-b| `|fa-bluetooth-b|`

       |fa-percent| `|fa-percent|`

       |fa-gitlab| `|fa-gitlab|`

       |fa-wpbeginner| `|fa-wpbeginner|`

       |fa-wpforms| `|fa-wpforms|`

       |fa-envira| `|fa-envira|`

       |fa-universal-access| `|fa-universal-access|`

       |fa-wheelchair-alt| `|fa-wheelchair-alt|`

       |fa-question-circle-o| `|fa-question-circle-o|`

       |fa-blind| `|fa-blind|`

       |fa-audio-description| `|fa-audio-description|`

       |fa-volume-control-phone| `|fa-volume-control-phone|`

       |fa-braille| `|fa-braille|`

       |fa-assistive-listening-systems| `|fa-assistive-listening-systems|`

       |fa-american-sign-language-interpreting| `|fa-american-sign-language-interpreting|`

       |fa-deaf| `|fa-deaf|`

       |fa-glide| `|fa-glide|`

       |fa-glide-g| `|fa-glide-g|`

       |fa-sign-language| `|fa-sign-language|`

       |fa-low-vision| `|fa-low-vision|`

       |fa-viadeo| `|fa-viadeo|`

       |fa-viadeo-square| `|fa-viadeo-square|`

       |fa-snapchat| `|fa-snapchat|`

       |fa-snapchat-ghost| `|fa-snapchat-ghost|`

       |fa-snapchat-square| `|fa-snapchat-square|`

       |fa-pied-piper| `|fa-pied-piper|`

       |fa-first-order| `|fa-first-order|`

       |fa-yoast| `|fa-yoast|`

       |fa-themeisle| `|fa-themeisle|`

       |fa-google-plus-circle| `|fa-google-plus-circle|`

       |fa-google-plus-official| `|fa-google-plus-official|`

       |fa-font-awesome| `|fa-font-awesome|`

       |fa-handshake-o| `|fa-handshake-o|`

       |fa-envelope-open| `|fa-envelope-open|`

       |fa-envelope-open-o| `|fa-envelope-open-o|`

       |fa-linode| `|fa-linode|`

       |fa-address-book| `|fa-address-book|`

       |fa-address-book-o| `|fa-address-book-o|`

       |fa-address-card| `|fa-address-card|`

       |fa-address-card-o| `|fa-address-card-o|`

       |fa-user-circle| `|fa-user-circle|`

       |fa-user-circle-o| `|fa-user-circle-o|`

       |fa-user-o| `|fa-user-o|`

       |fa-id-badge| `|fa-id-badge|`

       |fa-id-card| `|fa-id-card|`

       |fa-id-card-o| `|fa-id-card-o|`

       |fa-quora| `|fa-quora|`

       |fa-free-code-camp| `|fa-free-code-camp|`

       |fa-telegram| `|fa-telegram|`

       |fa-thermometer-full| `|fa-thermometer-full|`

       |fa-thermometer-three-quarters| `|fa-thermometer-three-quarters|`

       |fa-thermometer-half| `|fa-thermometer-half|`

       |fa-thermometer-quarter| `|fa-thermometer-quarter|`

       |fa-thermometer-empty| `|fa-thermometer-empty|`

       |fa-shower| `|fa-shower|`

       |fa-bath| `|fa-bath|`

       |fa-podcast| `|fa-podcast|`

       |fa-window-maximize| `|fa-window-maximize|`

       |fa-window-minimize| `|fa-window-minimize|`

       |fa-window-restore| `|fa-window-restore|`

       |fa-window-close| `|fa-window-close|`

       |fa-window-close-o| `|fa-window-close-o|`

       |fa-bandcamp| `|fa-bandcamp|`

       |fa-grav| `|fa-grav|`

       |fa-etsy| `|fa-etsy|`

       |fa-imdb| `|fa-imdb|`

       |fa-ravelry| `|fa-ravelry|`

       |fa-eercast| `|fa-eercast|`

       |fa-microchip| `|fa-microchip|`

       |fa-snowflake-o| `|fa-snowflake-o|`

       |fa-superpowers| `|fa-superpowers|`

       |fa-wpexplorer| `|fa-wpexplorer|`

       |fa-meetup| `|fa-meetup|`
