Questions and Answers
=====================

How can I adapt this code for other pubmed searches?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This can be done in two steps:
1) Adapting the xml search
By right-clicking on Google chrome, it is possible to select "Inspect" and hover over elements of a website. When you click it, you will
be able to see the xml structure.

2) Adapting the looping index
If your website has an index page at the end (e.g. www.site.com/page/1), you can just copy the entire link up to the page number
(e.g. www.site.com/page/) and replace it on the source = requests.get() line.

If your website has an index page in the middle (e.g. www.site.com/something/1.html), you should concatenate the string using the
following syntax:

.. code-block:: python

    for i in range(1:5): # whatever number of pages
      source = requests.get("www.site.com/something/" + str(i) + ".html")

How can I update the documentation later?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to open cmd and move the current directory to where your make file is.
Then you can just run:

.. code-block:: console

    make html

.. image:: C:/Users/Administrator2/Dropbox/Programming/Automated_content_analysis/Final_project/docs/build/html/updating.png
    :alt: It is crucial that the current working directory is correct.
