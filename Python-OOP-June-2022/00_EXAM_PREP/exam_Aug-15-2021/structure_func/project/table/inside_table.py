from project.table.table import Table

class InsideTable(Table):
    MIN_TABLE_NUM = 1
    MAX_TABLE_NUM = 50
    TABLES_TYPE = 'Inside'

    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)