Step 1: create resource group

![1.1](/images/1.1.png)
![1.2](/images/1.2.png)

Step 2: create IoT Hub
![2.1](/images/2.1.png)
![2.2](/images/2.2.png)
![2.3](/images/2.3.png)

Step 3: create device in IoT Hub
![3.1](/images/3.1.png)

Step 4: write python app and add connection string to code
![4.1](/images/4.1.png)
![4.2](/images/4.2.png)

Step 5: create storage account
![5.1](/images/5.1.png)
![5.2](/images/5.2.png)

Step 6: create containers
![6.1](/images/6.1.png)

Step 7: set up azure stream analytics
![7.1](/images/7.1.png)
![7.2](/images/7.2.png)
![7.3](/images/7.3.png)

Step 8: create input and output in stream analytics
![8.1](/images/8.1.png)
![8.2](/images/8.2.png)

Step 9: write query and run it
![9.1](/images/9.1.png)
![9.2](/images/9.2.png)
![9.3](/images/9.3.png)

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
![10.1](/images/10.1.png)

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
I have deleted all resources created during the exam