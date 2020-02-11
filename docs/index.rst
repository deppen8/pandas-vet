pandas-vet |version| documentation
==================================

|pandas-vet| is a plugin for |flake8| that provides opinionated linting for |pandas| code.

It began as a project during the `PyCascades`_ 2019 sprints.

.. _PyCascades: https://www.pycascades.com/

Motivation
----------

Starting with |pandas| can be daunting. The usual internet help sites are littered with different ways to do the same thing and some features that the |pandas| docs themselves discourage live on in the API. |pandas-vet| is (hopefully) a way to help make |pandas| a little more friendly for newcomers by taking some opinionated stances about |pandas| best practices. It is designed to help users reduce the |pandas| universe.

The idea to create a linter was sparked by `Ania Kapuścińska`_\’s talk at PyCascades 2019, `Lint your code responsibly!`_

Many of the opinions stem from `Ted Petrou`_\'s excellent `Minimally Sufficient Pandas`_. Other ideas are drawn from |pandas| docs or elsewhere. The `Pandas in Black and White`_ flashcards have a lot of the same opinions too.

.. _Ania Kapuścińska: https://twitter.com/lambdanis
.. _Lint your code responsibly!: https://youtu.be/hAnCiTpxXPg?t=21814
.. _Ted Petrou: https://twitter.com/TedPetrou
.. _Minimally Sufficient Pandas: https://medium.com/dunder-data/minimally-sufficient-pandas-a8e67f2a2428
.. _Pandas in Black and White: https://deppen8.github.io/pandas-bw/


.. toctree::
   :maxdepth: 1

   usage
   error-codes
   contributing
   API Documentation <autoapi/pandas_vet/index.rst>

* :ref:`genindex`
* :ref:`search`
