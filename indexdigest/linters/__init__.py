"""
Contains linters used to check the database for improvements.
"""
# expose linters
from .linter_0002_not_used_indices import check_not_used_indices, check_queries_not_using_indices
from .linter_0006_not_used_columns_and_tables import check_not_used_tables, check_not_used_columns
from .linter_0004_redundant_indices import check_redundant_indices
from .linter_0020_filesort_temporary_table import \
    check_queries_using_filesort, check_queries_using_temporary
