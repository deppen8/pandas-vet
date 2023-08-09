# Supported warnings

These are the warnings that `pandas-vet` currently supports.

PD001
: pandas should always be imported as 'import pandas as pd'

PD002
: 'inplace = True' should be avoided; it has inconsistent behavior

PD003
: '.isna' is preferred to '.isnull'; functionality is equivalent

PD004
: '.notna' is preferred to '.notnull'; functionality is equivalent

PD005
: Use arithmetic operator instead of method

PD006
: Use comparison operator instead of method

PD007
: '.ix' is deprecated; use more explicit '.loc' or '.iloc'

PD008
: Use '.loc' instead of '.at'.  If speed is important, use numpy.

PD009
: Use '.iloc' instead of '.iat'.  If speed is important, use numpy.

PD010
: '.pivot_table' is preferred to '.pivot' or '.unstack'; provides same functionality

PD011
: Use '.to_numpy()' instead of '.values'; 'values' is ambiguous

PD012
: '.read_csv' is preferred to '.read_table'; provides same functionality

PD013
: '.melt' is preferred to '.stack'; provides same functionality

PD015
: Use '.merge' method instead of 'pd.merge' function. They have equivalent functionality.

PD901
: 'df' is a bad variable name. Be kinder to your future self.
