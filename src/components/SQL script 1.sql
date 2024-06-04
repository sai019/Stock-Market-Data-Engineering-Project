select 
stockData.[Index],
    stockData.[Date],
    stockData.[Open],
    stockData.[High],
    stockData.[Low],
    stockData.[Close],
    stockData.[Adj Close],
    stockData.[Volume],
    stockData.[CloseUSD]
from 
    OPENROWSET(
        BULK 'https://uploadblob123.dfs.core.windows.net/stock-market-data/data/*.json',
        FORMAT = 'CSV',
        FIELDQUOTE = '0x0b',
        FIELDTERMINATOR ='0x0b',
        ROWTERMINATOR = '0x0b'
    )
    WITH (
        jsonContent varchar(MAX)
    ) AS [result] 
CROSS APPLY OPENJSON(jsonContent)
WITH 
(
    [Index] NVARCHAR(50),
    [Date] DATE,
    [Open] FLOAT,
    [High] FLOAT,
    [Low] FLOAT,
    [Close] FLOAT,
    [Adj Close] FLOAT,
    [Volume] FLOAT,
    [CloseUSD] FLOAT
) AS stockData;