import time

import duckdb
import numpy as np
import pandas as pd


## example dataframe
rng = np.random.default_rng(1)

nrows = 5_0000
df = pd.DataFrame(
    dict(
        id=rng.integers(1, 1_000, nrows),
        id2=rng.integers(1, 10, nrows),
        id3=rng.integers(1, 500, nrows),
        v1=rng.normal(0, 1, nrows),
        v2=rng.normal(0, 1, nrows),
    )
)
print(df)

start = time.perf_counter()
res = duckdb.sql(
    """
    WITH cte AS (
        SELECT df.id2, df.id3, df2.id3 AS id3_right,
            df.v1, df2.v1 AS v1_right,
            df.v2, df2.v2 AS v2_right
        FROM df
        JOIN df AS df2
        ON (
            df.id = df2.id
            AND df.id2 = df2.id2
            AND df.id3 > df2.id3
            AND df.id3 < df2.id3 + 30
        )
    )
    SELECT id2, id3, id3_right, corr(v1, v1_right) AS v1, corr(v2, v2_right) AS v2
    FROM cte
    GROUP BY id2, id3, id3_right
    """
).df()
print(time.perf_counter() - start)

## rank correlation
start = time.perf_counter()
res2 = duckdb.sql(
    """
    WITH cte AS (
        SELECT df.id2, df.id3, df2.id3 AS id3_right,
            RANK() OVER (g ORDER BY df.v1) AS v1,
            RANK() OVER (g ORDER BY df2.v1) AS v1_right,
            RANK() OVER (g ORDER BY df.v2) AS v2,
            RANK() OVER (g ORDER BY df2.v2) AS v2_right
        FROM df
        JOIN df AS df2
        ON (
            df.id = df2.id
            AND df.id2 = df2.id2
            AND df.id3 > df2.id3
            AND df.id3 < df2.id3 + 30
        )
        WINDOW g AS (PARTITION BY df.id2, df.id3, df2.id3)
    )
    SELECT id2, id3, id3_right, corr(v1, v1_right) AS v1, corr(v2, v2_right) AS v2
    FROM cte
    GROUP BY id2, id3, id3_right
    """
).df()
print(time.perf_counter() - start)
