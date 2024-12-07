Step 1: create resource group

![1.1](/images/1.1.png)

Step 2: create IoT Hub

Step 3: create device in IoT Hub

Step 4: write python app and add connection string to code

Step 5: create storage account

Step 6: create containers

Step 7: set up azure stream analytics

Step 8: create input and output in stream analytics

Step 9: write query and run it

SELECT
    name AS Name,
    AVG(price) AS AvgStockPrice,
    System.Timestamp AS EventTime
INTO
    [output]
FROM
    [input]
WHERE
    price > 30
GROUP BY
    name, TumblingWindow(second, 60)

Step 10: update query with trade range, volume, market cap value

SELECT
    name AS Name,
    price AS Price,
    traderange AS TradeRange,
    volume AS Volume,
    market_Cap AS MarketCapValue,
    System.Timestamp AS EventTime
INTO
    [output]
FROM
    IoTHubInput
WHERE
    price > 20
GROUP BY
    name, TumblingWindow(second, 60)


Step 11: clean up resources
