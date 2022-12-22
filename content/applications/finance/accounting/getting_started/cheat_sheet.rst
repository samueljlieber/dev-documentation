:code-column:
:custom-css: accounting.css
:custom-js: accounts.js,chart-of-accounts.js,entries.js,misc.js,reconciliation.js

======================
Accounting cheat sheet
======================

.. h:div:: intro-list

   .. rst-class:: intro-balance

   The **Balance Sheet** is a snapshot of the company's finances at a specific date (as opposed to
   the Profit and Loss, which is an analysis over a period);

   * .. rst-class:: intro-assets

     **Assets** represent the company's wealth and the goods it owns. Fixed assets include buildings
     and offices, while current assets include bank accounts and cash. A client owing money is an
     asset. An employee is not an asset.

   * .. rst-class:: intro-liabilities

     **Liabilities** are obligations from past events that the company will have to pay in the
     future (utility bills, debts, unpaid suppliers). Liabilities could also be defined as a source
     of financing which is provided to the company, also called *leverage*.

   * .. rst-class:: intro-equity

     **Equity** is the amount of the funds contributed by the owners of the company (founders or
     shareholders) plus previously retained earnings (or losses). Each year, net profits (or losses)
     may be reported as retained earnings or distributed to the shareholders (as a dividend).

What is owned (an asset) has been financed through debts to reimburse (liabilities) or equity
(profits, capital).

A difference is made between **assets** and **expenses**:
   - An **asset** is a resource with economic value that an individual, corporation, or country owns
     or controls with the expectation that it will provide a future benefit. Assets are reported on
     a company's balance sheet. They are bought or created to increase a firm's value or benefit its
     operations.
   - An **expense** is the cost of operations a company incurs to generate revenues.

.. h:div:: intro-list

   .. rst-class:: intro-p-l

    The **profit and loss** (P&L) report shows the company's performance over a specific period,
    usually the fiscal year. After every period, the profit and loss report is restarted to 0.

     * .. rst-class:: intro-gross-profit

         The **revenue** refers to the money earned by the company by selling goods and/or services

     * .. rst-class:: intro-gross-profit

         The **cost of goods sold** (also known as “Cost of Sale”) refers to the costs directly
         incurred to the sale of goods (e.g.,  the cost of the materials and labor used to create the
         goods)

       * .. rst-class:: intro-gross-profit

         The **Gross profit** equals the revenues from sales minus the cost of goods sold.

       * .. rst-class:: intro-opex

         **Operating expenses** (OPEX) include administration, sales and R&D salaries, rent and
         utilities, miscellaneous costs, insurances, and anything beyond the costs of products sold or
         the cost of sale.

.. h:div:: doc-aside accounts-table

   .. placeholder

.. rst-class:: doc-aside

.. highlights:: Assets = Liabilities + Equity

Chart of accounts
=================

The chart of accounts is the company's DNA, represented by lists of all the accounts. It gathers
both Balance sheet accounts and P&L accounts. Every item in the company is related to an account
provided by the chart of accounts. Every accounting transaction impacts the accounts by moving value
from at least one account (credit) to one or more accounts (debit).

Every item provided by the chart of accounts belongs to a specific category. In Odoo, each account
has a unique code and belongs to one of these categories:

**Equity and subordinated debts**
   - **Equity** is the amount of money invested by a company's shareholders to finance the company's
     activities.
   - **Subordinated debts** are the amount of money lent by a third party to a company to finance
     its activities. In the event of the dissolution of a company, these third parties are
     reimbursed before the shareholders.

**Fixed assets** are tangible (i.e., physical) items or property that a company purchases and uses
to produce its goods and services. Fixed assets are long-term assets. This means the assets have a
useful life of more than one year. Fixed assets include property, plant, and equipment (PP&E) and
are recorded on the balance sheet with that classification.

**Current assets and liabilities**
   - The current assets account is a balance sheet line item listed under the Assets section, which
     accounts for all company-owned assets that can be converted to cash within one year.  Current
     assets include cash, cash equivalents, accounts receivable, stock inventory, marketable
     securities, prepaid liabilities, and other liquid assets.
   - Current liabilities are a company’s short-term financial obligations due within on year. An
     example of a current liability is money owed to suppliers in the form of accounts payable.

**Bank and cash accounts**
   - A bank account is a financial account maintained by a bank or other financial institution in
     which the financial transactions between the bank and a customer are recorded.
   - A cash account, or cash book, may refer to a ledger in which all cash transactions are
     recorded. The cash account includes both the cash receipts and the cash payment journals.

**Expenses and income**
   - An expense is the cost of operations a company incurs to generate revenue. It is simply defined
     as the cost one is required to spend on obtaining something. Common expenses include supplier
     payments, employee wages, factory leases, and equipment depreciation.
   - The term “income” generally refers to the amount of money, property, and other transfers of
     value received over a set period of time in exchange for services or products.

Example
^^^^^^^

.. h:div:: example

   \*: Customer Refund and Customer Payment boxes cannot be simultaneously selected as they are contradictory.

.. h:div:: doc-aside

   .. highlights:: Balance = Debit - Credit

   .. h:div:: chart-of-accounts

      .. placeholder

Journal Entries
===============

Every financial document of the company (e.g., an invoice, a bank statement, a pay slip, a capital
increase contract) is recorded as a journal entry, impacting several accounts.

For a journal entry to be balanced, the sum of all its debits must be equal to the sum of all its
credits.

.. h:div:: doc-aside journal-entries

   examples of accounting entries for various transactions. Example:

   Example 1: Customer Invoice:

   Explanation:

     - You generate a revenue of $1,000
     - You have a tax to pay of $90
     - The customer owes $1,090

   Configuration:

     - Income: defined on the product, or the product category
     - Account Receivable: defined on the customer
     - Tax: defined on the tax set on the invoice line

     The fiscal position used on the invoice may have a rule that
     replaces the Income Account or the tax defined on the product by another
     one.

   Example 2: Customer Payment:

   Explanation:

     - Your customer owes $1,090 less
     - Your receive $1,090 on your bank account

   Configuration:

     - Bank Account: defined on the related bank journal
     - Account Receivable: defined on the customer

.. _accounting/reconciliation:

Reconciliation
==============

:doc:`Reconciliation <../../accounting/bank/reconciliation/use_cases>` is the process of linking
journal items of a specific account and matching credits and debits.

Its primary purpose is to link payments to their related invoices to mark paid invoices and clear
the customer/vendor statement. This is done by doing a reconciliation on the accounts receivable
account and/or the accounts payable account.

An invoice is marked as paid when its accounts receivable journal items are reconciled with the
related payment journal items.

Reconciliation is performed automatically by the system when:

* the payment is registered directly on the invoice
* the links between the payments and the invoices are detected at the bank
  matching process


.. h:div:: doc-aside reconciliation-example

   .. rubric:: Customer Statement Example

   .. rst-class:: table-sm d-c-table

   +-------------------------+-------------------------+-----------------------+
   |Accounts Receivable      |Debit                    |Credit                 |
   +=========================+=========================+=======================+
   |Invoice 1                |100                      |                       |
   +-------------------------+-------------------------+-----------------------+
   |Partial payment 1/2      |                         |70                     |
   +-------------------------+-------------------------+-----------------------+
   |Invoice 2                |65                       |                       |
   +-------------------------+-------------------------+-----------------------+
   |Partial payment 2/2      |                         |30                     |
   +-------------------------+-------------------------+-----------------------+
   |Payment 2                |                         |65                     |
   +-------------------------+-------------------------+-----------------------+
   |Invoice 3                |50                       |                       |
   +-------------------------+-------------------------+-----------------------+
   |                         |                         |                       |
   +-------------------------+-------------------------+-----------------------+
   |Total to pay             |50                       |                       |
   +-------------------------+-------------------------+-----------------------+


Bank Reconciliation
===================

Bank reconciliation is the matching of bank statement lines (provided by your bank) with
transactions recorded internally (payments to suppliers or from customers). For each line in a bank
statement, it can be:

**matched with a previously recorded payment**: a payment is registered when a check is received
from a customer, then matched when checking the bank statement.

**recorded as a new payment**: the payment’s journal entry is created and reconciled with the
related invoice when processing the bank statement

**recorded as another transaction**: bank transfer, direct charge, etc.

Odoo should automatically reconcile most transactions; only a few should need manual review. When
the bank reconciliation process is finished, the balance on the bank account in Odoo should match
the bank statement’s balance.

.. rst-class:: checks-handling

Checks Handling
===============

There are two approaches to managing checks and internal wire transfers:

* Two journal entries and a reconciliation
* One journal entry and a bank reconciliation

.. h:div:: doc-aside

   The first journal entry is created by registering the payment on the
   invoice. The second one is created when registering the bank statement.

   .. rst-class:: table-sm d-c-table

   +-------------------------+--------------+------------+---------------+
   |Account                  |Debit         |Credit      |Reconciliation |
   +=========================+==============+============+===============+
   |Account Receivable       |              |100         |Invoice ABC    |
   +-------------------------+--------------+------------+---------------+
   |Undeposited funds        |100           |            |Check 0123     |
   +-------------------------+--------------+------------+---------------+

   .. rst-class:: table-sm d-c-table

   +-------------------------+--------------+------------+---------------+
   |Account                  |Debit         |Credit      |Reconciliation |
   +=========================+==============+============+===============+
   |Undeposited funds        |              |100         |Check 0123     |
   +-------------------------+--------------+------------+---------------+
   |Bank                     |100           |            |               |
   +-------------------------+--------------+------------+---------------+

.. h:div:: doc-aside

   A journal entry is created by registering the payment on the invoice. When
   reconciling the bank statement, the statement line is linked to the
   existing journal entry.

   .. rst-class:: table-sm d-c-table

   +-------------------------+--------------+------------+---------------+---------------+
   |Account                  |Debit         |Credit      |Reconciliation |Bank Statement |
   +=========================+==============+============+===============+===============+
   |Account Receivable       |              |100         |Invoice ABC    |               |
   +-------------------------+--------------+------------+---------------+---------------+
   |Bank                     |100           |            |               |Statement XYZ  |
   +-------------------------+--------------+------------+---------------+---------------+
