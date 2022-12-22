======================================
Allow customers to close their tickets
======================================

Allowing customers to close their tickets gives them autonomy and minimize misunderstandings about
when an issue is considered solved or not.

Configure the feature
=====================

To configure the feature, go to :menuselection:`Helpdesk --> Configuration --> Helpdesk Teams`,
click on the team, and click :guilabel:`Edit` and enable :guilabel:`Ticket closing`.

.. image:: close_tickets/close-ticket-settings.png
   :alt: Ticket closing feature in Odoo Helpdesk.

To designate which stage the ticket migrates to once it is closed, navigate to the ticket pipeline
by going to :menuselection:`Helpdesk --> Overview` and clicking :guilabel:`Tickets` on the team's
card.

There are two options: create a new Kanban stage or work with an existing one. For both scenarios,
click the gear icon next to the stage name, select :guilabel:`Edit Stage`, and enable
:guilabel:`Closing Stage`.

If a closing stage is not specified, by default, the ticket is moved to the last stage. If more
than one stage is set as a closing stage, the ticket is put in the first one.

The customer portal
===================

Now, once the customer logs into their portal, the option :guilabel:`Close this ticket` is
available.

.. image:: close_tickets/customer-view-close-ticket.png
   :alt: Customer view of ticket closing in Odoo Helpdesk.

Get reports on tickets closed by customers
==========================================

To analyze the tickets that have been closed by customers, go to :menuselection:`Helpdesk -->
Reporting --> Tickets`. Then, click on the :guilabel:`Filters` menu and add a :guilabel:`Add Custom
filter`. Next, set the custom filter parameters to :guilabel:`Closed by partner` and :guilabel:`is
true`. Finally, click :guilabel:`Apply`.

.. image:: close_tickets/closed-by-search-filter.png
   :alt: Filter for tickets closed by customers on Odoo Helpdesk's reporting page.
