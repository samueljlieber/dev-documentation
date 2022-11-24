=====
Italy
=====

Configuration
=============
The first necessary module to start booking accounting transactions on an Italian localization is
:guilabel:`Italy - Accounting` module. Once installed it allows to:

- Generate electronic invoices in **FatturaPA's** format.
- Send and receive electronic invoicing through SDIcoop.

.. warning::
   Once this module is installed, it's no longer possible to send invoices via :ref:`PEC mails
   <italy/pec>`.

Company information
-------------------

The company information is also an important configuration to ensure the proper set up of your
Accounting database. To add the information, go to :menuselection:`Configuration --> Settings -->
General Settings --> Update info`. In this menu, make sure to have at least the following:

- the company address
- :guilabel:`GSTIN` code
- :guilabel:`Codice Fiscale`
- :guilabel:`Tax System`
- :guilabel:`PEC address email`

PEC
---
The PEC email is a specific type of certified email providing a legal equivalent to the traditional
registered mail. The PEC email of the main company must be the same as the one registered by the
Agenzia delle Entrate authorities.

E-Invoicing
-----------

**SdI** is the public technical system that allows sending and receiving invoices. It enables the
transmission and receipt of electronic billing in XML as well as validating and sending it from
businesses to third parties.
In order to receive invoices and notifications, you need to inform the FatturaPA service that Odoo
is the allowed party to process files for you. To do so, you must set up Odoo's
**Codice Destinatario** on the FatturaPA portal.

#. Go to https://ivaservizi.agenziaentrate.gov.it/portale/ and authenticate.
#. Go to section :menuselection:`Fatture e Corrispettivi`.
#. Set the user as Legal Party for the VAT number you wish to configure the electronic address.
#. In :menuselection:`Servizi Disponibili --> Fatturazione Elettronica --> Registrazione
   dell’indirizzo telematico dove ricevere tutte le fatture elettroniche`, insert Odoo's Codice
   Destinatario (`K95IV18`), then confirm.

Give Odoo permission to process files
-------------------------------------

Since the files are transmitted through Odoo's server before being sent to SDICoop or received by
your database, you need to authorize Odoo to process your files from your database.

To do so, go to :menuselection:`Accounting --> Configuration --> Settings --> Electronic
Document Invoicing`. In the :guilabel:`Electronic Document Invoicing`, you can see three different
modes:

- Demo
- Test (experimental)
- Official (production)

Choosing the right mode
-----------------------

- :guilabel:`Demo` mode in Odoo is a simulation environment where all invoices created are **not**
  automatically sent to the government. In such mode, the invoices need to be manually downloaded
  as xml files and you then have to upload them on the Agenzia dell'Entrate website.
- :guilabel:`Test` mode sends invoices to a non-production service. THerefore a communication is
  established between Odoo and the test server of the Public Administration and only send invoices
  to a selected few `fake` destinations.
- :guilabel:`Official` is a production mode that sends your invoices directly to the Agenzia
  dell'Entrate.

.. warning::
   The choice of the mode is **not reversible**. Once in :guilabel:`Official` mode it is not
   possible to get back to the :guilabel:`Test` and :guilabel:`Demo`. Equally is not possible to go
   from :guilabel:`Test` to :guilabel:`Official`.

After having selected the right mode, you need to accept the terms and conditions right below the
mode selection. Once you have :guilabel:`Saved` the mode you want, you can start recording your
Accounting transactions in Odoo.

Issue invoices
==============

The **FatturaPA** feature is automatically active, you can check it in
:menuselection:`Configuration --> Journals --> Customer Invoices -->  Advanced Settings`.
You can create a new invoice by going to :menuselection:`Accounting dashboard --> New invoice`, once
confirmed the e-invoice will be generated and sent.

.. warning::
   The e-invoice is only sent to the government if you are in :guilabel:`Official` mode.

You can check the current status of your customer invoice under the :guilabel:`Electronic invoicing`
field. The xml file is accessible in the chatter of the invoice.

.. image:: italy/processing.png
   :align: center
   :alt: Electronic invoicing status (waiting for confirmation)

Vendor bills
============

As for invoices, when creating a vendor bill, the :guilabel:`FatturaPA` option is automatically
activated in the Vendor bill Journals' advanced settings.
When inserting taxes in a vendor bill, you have the possibility to choose **Reverse Charge** taxes,
these are automatically activated in the Italian fiscal position. By going to
:menuselection:`Configuration --> Taxes`, you will see that the 10% and 22% services and goods taxes
are activated and have the correct tax grids; these are set up automatically to ensure the correct
booking of accounting entries and display of the tax report.
Once the bill is confirmed, a banner appears, and the bill can be sent to the EDI service.

Taxes
=====

Specific configurations are required for **Reverse Charge** type of taxes. In such case, the seller
does not charge the client for VAT but the buyer is paying for it. There are two main cases,
Internal and External Reverse Charge.

External Reverse Charge
-----------------------

Vendors of Italian companies selling and buying goods from other EU countries or services from
non-EU countries are responsible for collecting VAT from the buyer and giving it back to the State.
When the buyer is from another State, he is the responsible for collecting the right VAT amount and
sending it to the Tax Agency.

Invoices
--------

- the seller will put a 0% tax on the invoice line, specifying on the :guilabel:`Natura`
  field that the reason for this tax exemption is **External Reverse Charge**.
- :guilabel:`SdI address` must be filled in both for EU or non-EU.
- :guilabel:`Country Id` needs to contain the country of the foreign seller, in the two-letter ISO
   code.
- :guilabel:`CAP` must be filled with "00000".
- :guilabel:`Partita Iva`: must contain VAT number for **EU businesses** and `0099999999999` for
  **non-EU businesses**, and `0000000` for **individuals** without a VAT number.
- :guilabel:`Fiscal Code` for foreign entites, without an actual **Codice Fiscale**, is any
   recognizable identifier is valid.

Vendor bills:
-------------

The Italian buyer sends the SdI the information of the invoice received, setting the seller as
`Cedente/Prestatore` and the buyer as the `Cessionario/Committente` and filling out the missing tax
information that he needs to pay to the State.

.. note::
   The Natura code needs to be specified only if the line is tax-exempt, in the case of non-taxable
   goods.

Self invoices or VAT invoice integrations must be issued and sent to the Tax Agency.
Three types of configurations are technically identified by a code called `Tipo Documento`:

#. **TD17** - Buying services from EU and non-EU

   The foreign seller sends an invoice for a service with the price but without taxes, as it will
   not be taxable in Italy, and the VAT is paid from the buyer in Italy.

   - From EU: the buyer integrates the invoice received with the VAT information due in his own
     country
   - Non-EU: the buyer sends himself a self-invoice

   Odoo exports a transaction as TD17 if these conditions are met:

   - Vendor bill
   - At least one tax on the invoice lines targets the tax grids `VJ`
   - All the invoice lines have either :guilabel:`services` as products, or a tax with the
     :guilabel:`service` tax scope

#. **TD18** - Buying goods from EU
   In the European Union, invoices are already in a standard format, so this consist of an
   integration of the existing invoice, no self-invoice is needed.

   Odoo exports a transaction as TD18 if these conditions are met:

   - Vendor bill
   - At least one tax on the invoice lines targets the tax grids `VJ`
   - All the invoice lines have either :guilabel:`consumable` as products, or a tax with the
     :guilabel:`good` tax scope

#. **TD19** - Buying goods from a foreign vendor, but the goods are already in Italy in a VAT
   deposit

   - From EU: the buyer integrates the invoice received for VAT
   - Outside the EU: the buyer sends himself a self-invoice

   Odoo exports a move as a TD19 if these conditions are met:

  - Vendor bill
  - At least one tax on the invoice lines targets the tax grid `VJ3`
  - All the invoice lines have either :guilabel:`consumables` products, or a tax with
    :guilabel:`goods` tax scope.








