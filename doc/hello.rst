Hello World
===================

Hello this is a demo page

Title 2 example
----------------------

Installation guide
------------------

Install doing ::

    pip install mypackage-mp

Then use with ::

    import example_package

    from example_package import AClass # another way to import

Third way to do it

.. code-block:: python

    import example_package

    myclass = example_package.AClass("abc", 1, 42)

    print(myclass)
    # output : AClass(abc="abc", 1=1, 42=42)
