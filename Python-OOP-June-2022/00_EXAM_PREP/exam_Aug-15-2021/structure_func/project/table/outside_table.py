from project.table.table import Table

class OutsideTable(Table):
    MIN_TABLE_NUM = 51
    MAX_TABLE_NUM = 100
    TABLES_TYPE = 'Outside'

    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)