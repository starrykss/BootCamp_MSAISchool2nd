CREATE TABLE member (
    Idx INT IDENTITY(1, 1) PRIMARY KEY,
    Names VARCHAR(45) NOT NULL,
    Addr VARCHAR(100),
    Mobile VARCHAR(13),
    Email VARCHAR(50)
)