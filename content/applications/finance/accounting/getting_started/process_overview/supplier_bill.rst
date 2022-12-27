===========================
From vendor bill to payment
===========================

Prior to payment, vendor bills can be registered manually or automatically in Odoo. The
:guilabel:`Aged Payable balance` provides a visual of all of your outstanding bills to help you pay
your vendors for the correct amount at the right time.

.. seealso::
   - Tutorial `Registering a vendor bill <https://www.odoo.com/slides/slide/registering-a-vendor-bill-1683?fullscreen=1>`_
   - :ref:`Manage-vendor-bills`

Bills creation
==============

From the Accounting app, vendor bills can either be created manually or automatically.

Manually
--------

It is possible to manually create a vendor bill by going to :menuselection:`Vendors --> Bills` and
then clicking :guilabel:`Create`.

Automatically
-------------

Vendor bills can be automatically created by **sending an email** to an :ref:`email alias
<invoice-digitization/email-alias>` associated with the purchase journal, or by **uploading a .pdf**
in :menuselection:`Accounting app --> Vendors --> Bills` and then clicking :guilabel:`Upload`.

Bills completion
================

Whether you create the bill manually or if it is generated automatically, make sure the following
fields are appropriately completed:

.. image:: supplier_bill/bill-completion.png
   :align: center
   :alt: filling the vendor bill

Select the :guilabel:`Vendor`. Odoo automatically fills in some fields based on the vendor's
registered information, previous purchase orders, or bills.

The :guilabel:`Bill Reference` field includes the sales order reference provided by the vendor.
It is used to do the :ref:`matching <payments-matching>` when you receive the products.

The :guilabel:`Auto-Complete` field allows to automatically complete the document from a past
bill/purchase order. The :guilabel:`Vendor` field should be completed prior to completing this
field.

The :guilabel:`Bill Date` is the issuance date of the document, and the :guilabel:`Accounting Date`
is the date on which it is registered in your accounting.

Fill in the :guilabel:`Payment Reference` to set on journal items. When registering the payment, it
is automatically indicated in the :guilabel:`Memo` field.

The :guilabel:`Recipient Bank` indicates to which account number the payment has to be made.

Fill in the :guilabel:`Due Date` or :guilabel:`Terms` to pay the bill.

Finally, fill in the :guilabel:`Journal` in which to record the bill, and the
:ref:`Currency <multi-currency-system>`.

.. note::
   - Once uploaded, bills can be :ref:`digitized <invoice-digitization>` for automatic completion,
     by clicking :guilabel:`Send for Digitization`.
   - If you upload the bill, the .pdf document is displayed on the right of the screen, allowing you
     to easily fill in the bill information.

Bill confirmation
=================

Click :guilabel:`Confirm` when the document is completed. The status of your document changes to
:guilabel:`Posted` and a journal entry is generated based on the configuration on the invoice.

.. note::
   Once confirmed, it is no longer possible to update it. Click :guilabel:`Reset to draft` if
   changes are required.

Bill Payment
============

Upon payment of the vendor bill, click on :guilabel:`Register Payment`. A new window pops up. Select
the :guilabel:`Journal`, the :guilabel:`Payment Method`, the :guilabel:`Amount` you wish to pay
(full or partial payment), and the :guilabel:`Currency`. Odoo fills in the :guilabel:`Memo` field
automatically if the :guilabel:`Payment Reference` has been set correctly in the vendor bill. If the
field is empty, we recommend you select the vendor invoice number as a reference.

Once confirmed, an :guilabel:`In Payment` banner appears on the bill until it is :ref:`reconciled
<bank-reconciliation-process>`.

Aged payable balance
====================

To get an overview of your open vendor bills and their related due dates, you can use the
**Aged Payable report**. Go to :menuselection:`Accounting app --> Reporting --> Partner Report
section --> Aged payable`.

Click on a vendor's name to open up the details of all outstanding bills, the amounts due, the due
dates, etc.

.. Note::
   - By clicking the :guilabel:`Save` button, you can export the information available on the screen
     as .PDF or XLSX file and save it in the folder of your choice.
   - You might receive several bills for the same purchase order if your vendor is in back-order and is sending
     you invoices as they ship the products, or if your vendor is sending you a partial bill or
     asking for a deposit.
