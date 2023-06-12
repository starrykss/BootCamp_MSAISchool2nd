INSERT INTO [SalesLT].[Product] ( 
      [Name]
    , [ProductNumber]
    , [Color]
    , [ProductCategoryID]
    , [StandardCost]
    , [ListPrice]
    , [SellStartDate]
)
VALUES(
    'myNewProduct'
    , 123456789
    , 'NewColor'
    , 1
    , 100
    , 100
    , GETDATE() 
);