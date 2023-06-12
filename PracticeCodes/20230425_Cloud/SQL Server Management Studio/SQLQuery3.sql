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
    'myNewProduct7'
    , 1234567891
    , 'NewColor'
    , 1
    , 100
    , 100
    , GETDATE() 
);