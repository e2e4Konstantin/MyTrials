sql_creates = {
    #
    # --- > Расценки ----------------------------------------------------------
    "drop_table_quotes": """DROP TABLE tblQuotes;""",

    "create_table_quotes": """
        CREATE TABLE IF NOT EXISTS tblQuotes (
            ID_tblQuote              INTEGER PRIMARY KEY NOT NULL,
            last_update              TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            period                   INTEGER NOT NULL,
            code                     TEXT NOT NULL,
            absolute_code            TEXT NOT NULL,
            description              TEXT NOT NULL,
            measure                  TEXT NOT NULL,
            UNIQUE (code)
        );
        """,

    "create_index_quotes": """
        CREATE UNIQUE INDEX IF NOT EXISTS idx_code_tblQuotes
        ON tblQuotes (code);
        """,
}        