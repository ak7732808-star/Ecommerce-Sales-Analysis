USE EcommerceSalesDB;
GO

-- 1. Display all sales records
SELECT *
FROM dbo.Sales;

-- 2. Calculate total revenue
SELECT SUM(Quantity * UnitPrice) AS TotalRevenue
FROM dbo.Sales;

-- 3. Count total orders
SELECT COUNT(DISTINCT OrderID) AS TotalOrders
FROM dbo.Sales;

-- 4. Category-wise revenue
SELECT
    Category,
    SUM(Quantity * UnitPrice) AS Revenue
FROM dbo.Sales
GROUP BY Category
ORDER BY Revenue DESC;

-- 5. City-wise revenue
SELECT
    City,
    SUM(Quantity * UnitPrice) AS Revenue
FROM dbo.Sales
GROUP BY City
ORDER BY Revenue DESC;

-- 6. Product-wise revenue
SELECT
    ProductName,
    SUM(Quantity * UnitPrice) AS Revenue
FROM dbo.Sales
GROUP BY ProductName
ORDER BY Revenue DESC;

-- 7. Monthly revenue
SELECT
    FORMAT(OrderDate, 'yyyy-MM') AS SalesMonth,
    SUM(Quantity * UnitPrice) AS Revenue
FROM dbo.Sales
GROUP BY FORMAT(OrderDate, 'yyyy-MM')
ORDER BY SalesMonth;