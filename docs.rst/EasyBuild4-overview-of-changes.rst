.. _eb4_changes_overview:

Overview of changes in EasyBuild version 4.0
============================================

This page provides a concise overview of the most prominent changes in EasyBuild version 4.0,
compared to the latest EasyBuild v3.x (version 3.9.4).

A detailed overview with links to the pull requests in which the changes are made is available in the
:ref:`release_notes` (see :ref:`release_notes_eb400` in particular).

.. contents::
    :depth: 2
    :backlinks: none
    :local:


.. _eb4_changes_significant_enhancements:

Significant enhancements in EasyBuild v4.0
------------------------------------------

Various significant enhancements are included in EasyBuild v4.0, including:

* :ref:`eb4_no_required_deps`
* :ref:`eb4_python3_support`
* :ref:`eb4_custom_easyblocks`
* :ref:`eb4_2019b_common_toolchains`
* :ref:`eb4_changes_local_variables`

.. _eb4_no_required_deps:

No more required Python packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To simplify the installation of EasyBuild, **no Python packages other than the ones included in the Python standard
library are required** for EasyBuild v4.0. More specifically:

* ``setuptools`` **is no longer a required dependency**, neither for using EasyBuild nor for installing it.
  This change was motivated by the various problems with installing EasyBuild that were reported, which could
  often be attributed to ``setuptools`` in one way or another (ancient versions being installed via the OS package
  manager, quirky or broken functionality in specific versions, etc.).

* ``vsc-base`` **and** ``vsc-install`` **are no longer required dependencies**. The relevant parts of these packages
  were ingested into the EasyBuild framework codebase itself (see also :ref:`eb4_changes_ingested_vsc_base`),
  mostly to facilitate making EasyBuild compatible with Python 3.

Note that specific Python packages may currently still be required for certain EasyBuild functionality outside
of the core functionality of building and installing scientific software, including ``keyring`` for the GitHub
integration features (see :ref:`integration_with_github`), etc.


.. _eb4_python3_support:

Support for running EasyBuild on top of Python 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A significant effort has been made to ensure that the EasyBuild framework and the easyblocks included with EasyBuild
are **compatible with Python 3**, while retaining the compatibility with Python 2.

Currently supported Python versions include: ``2.6``, ``2.7``, ``3.5``, ``3.6``, ``3.7``.

To achieve this in a maintainable way, the ``easybuild.tools.py2vs3`` package was introduced.
For more details, please see :ref:`py2_py3_compatibility`.


.. _eb4_custom_easyblocks:

Custom software-specific easyblocks for ``iccifort``, ``numexpr``, ``OpenMPI``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A couple of **additional custom software-specific easyblocks** were added in EasyBuild v4.0, including:

* ``iccifort``: to install ``icc`` and ``ifort`` together in a single prefix, and use that installation as a toolchain

* ``numexpr``: to ensure that ``numexpr`` is linked with Intel MKL's VML when it is available

* ``OpenMPI``: to improve the (default) configuration of ``OpenMPI`` based on installed OS packages (for example for
  InfiniBand support) and available dependencies

In addition, various (generic and software-specific) easyblocks were improved and enhanced
(see :ref:`release_notes` for more details).


.. _eb4_2019b_common_toolchains:

2019b update of common toolchains
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``2019b`` update of the common toolchains is included with EasyBuild v4.0; see also :ref:`common_toolchains`.


.. _eb4_changes_local_variables:

Local variables in easyconfigs should follow recommended naming scheme
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A recommended naming scheme for local variables in easyconfig files was introduced.

If an easyconfig file contains local variables that do not follow the recommended naming scheme,
a warning will be printed (by default).

For more information, see :ref:`easyconfig_files_local_variables`.


.. _eb4_changes_backwards_incompatible:

Backwards-incompatible changes in EasyBuild v4.0
------------------------------------------------

A couple of *backwards-incompatible* changes were made in EasyBuild v4.0:

* :ref:`eb4_changes_fixed_installdir_naming_scheme`
* :ref:`eb4_changes_relocated_stuff`
* :ref:`eb4_changes_ingested_vsc_base`
* :ref:`eb4_changes_py2vs3`

.. note:: **Other than the changed default configuration, these changes are mainly important for developers
          of the EasyBuild framework and easyblock implementers.**

.. _eb4_changes_fixed_installdir_naming_scheme:

``--fixed-installdir-naming-scheme`` enabled by default
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**The** ``--fixed-installdir-naming-scheme`` **was changed to be** *enabled* **by default,
which makes the name of the software installation directory independent of the module naming scheme being used.**

With this configuration setting enabled, the name of software installation directories will match the module name
generated by the (default) ``EasyBuildMNS`` module naming scheme.

So, for an easyconfig file ``example-1.2.3-foss-2019b.eb``, the software installation directory will always be
``<prefix>/software/example/1.2.3-foss-2019b``, regardless of the active module naming scheme.

This change was done to make it easier to generate module files using one or more additional module naming scheme
(using ``--module-only``) for already existing software installations. Only when the name of the software installation
directories is independent of the module naming scheme being used during the (first) installation is it possible to
later generate additional module files using a different module naming scheme.

.. note:: Having ``--fixed-installdir-naming-scheme`` enabled should not cause problems in existing setups.

          Mixing different naming schemes for software installations directories in a single software stack
          works just fine; it's mostly a matter of inconsistency that could be confusing for humans.

.. _eb4_changes_fixed_installdir_naming_scheme_disabling:

Disabling ``--fixed-installdir-naming-scheme``
++++++++++++++++++++++++++++++++++++++++++++++

If you are using a module naming scheme other than the default ``EasyBuildMNS``, you may prefer disabling
``--fixed-installdir-naming-scheme`` to maintain consistency in the names of software installation directories.
*Do note that this implies that you won't be able to generate additional modules files using a different module
naming scheme for existing installations.*

To disable ``--fixed-installdir-naming-scheme``, you can either

* disable the ``fixed-installdir-naming-scheme`` configuration option
  in the ``[override]`` section of an EasyBuild configuration file::

    [override]
    fixed-installdir-naming-scheme = 0

  (see also :ref:`configuration_file`)

* set the ``$EASYBUILD_DISABLE_FIXED_INSTALLDIR_NAMING_SCHEME`` environment variable::

    export EASYBUILD_DISABLE_FIXED_INSTALLDIR_NAMING_SCHEME=1

  (see also :ref:`configuration_env_vars`)

* use the ``--disable-fixed-installdir-naming-scheme ...`` command line option::

    eb --disable-fixed-installdir-naming-scheme ...

  (see also :ref:`configuration_cmdline`)


.. _eb4_changes_relocated_stuff:

Relocated functions, classes and constants in EasyBuild framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**A limited number of functions, classes and constants have been relocated in the EasyBuild framework.**

This was done mostly to ensure that the ``__init__.py`` files that define packages are empty, other
than the ``pkgutil.extend_path`` (which replaces the ``pkg_resources.declare_namespace`` which requires ``setuptools``,
see also :ref:`eb4_no_required_deps`).

Making EasyBuild compatible with Python 3 also required some similar changes, see :ref:`eb4_changes_py2vs3`.

A detailed overview of relocated functions and constants is available at :ref:`eb4_relocated_functions_classes_constants`.


.. _eb4_changes_ingested_vsc_base:

Ingested functionality from ``vsc-base`` and ``vsc-install``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **functionality from the** ``vsc-base`` **and** ``vsc-install`` **packages required by EasyBuild has been ingested
in the EasyBuild framework**, see also :ref:`eb4_no_required_deps`.

This has primarily been done in the new ``easybuild.base`` package, so in general imports
from a module in the ``vsc.utils`` package should be replaced with a corresponding import statement
from that same module in the ``easybuild.base`` package.

A number of specific functions and classes have been placed in existing modules in the ``easybuild.tools`` package instead.

The affected functions are listed in :ref:`eb4_relocated_functions_classes_constants`.

.. _eb4_changes_ingested_vsc_base_fake_vsc_namespace:

Fake ``vsc`` namespace
++++++++++++++++++++++

To avoid that any functionality is imported from an already installed ``vsc-base`` (or ``vsc-install``) package,
which could lead to strange side-effects, a fake ``vsc`` namespace is injected since EasyBuild v4.0.

If an import from ``vsc.utils.*`` is detected (for example from an easyblock or from a module that is included
via one of the ``--include-*`` options), an error like this will be produced::

  ERROR: Detected import from 'vsc' namespace in /home/example/old_easyblock.py (line 7)
  vsc-base & vsc-install were ingested into the EasyBuild framework in EasyBuild v4.0
  The functionality you need may be available in the 'easybuild.base.*' namespace.


.. _eb4_changes_py2vs3:

Functions & classes that must be imported from the ``easybuild.tools.py2vs3`` namespace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**A handful functions and classes that could be imported directly from the Python standard library should now be
imported from the** ``easybuild.tools.py2vs3`` **namespace instead** (perhaps under a different name),
to ensure compatibility with Python 2 and 3.

See :ref:`py2_py3_compatibility` for more information.

The affected functions are also included in :ref:`eb4_relocated_functions_classes_constants`.


.. _eb4_changes_deprecated:

Deprecated functionality in EasyBuild v4.0
------------------------------------------

Some functionality was deprecated in EasyBuild v4.0, and will no longer be supported in EasyBuild v5.0.

If you trigger any deprecated functionality, a warning message will be printed.

.. _eb4_changes_dummy_tc:

Deprecated ``dummy`` toolchain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``dummy`` toolchain is now deprecated, and has been replaced with the ``system`` toolchain.

For more information, please consult :ref:`system_toolchain`.
