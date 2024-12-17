SET NOCOUNT ON;

USE master;
GO

/*Create TargetDB Database*/
 IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'TargetDB')
    BEGIN
        CREATE DATABASE TargetDB;
    END

GO


USE TargetDB
GO

IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dbo].[TransformedEmployees]'))
BEGIN

CREATE TABLE [dbo].[TransformedEmployees] (
    EmployeeID INT,
    FullName NVARCHAR(100),
    Department NVARCHAR(50),
    AnnualSalary DECIMAL(18, 2),
	CONSTRAINT PK_TransformedEmployees_EmployeeID PRIMARY KEY (EmployeeID)
);

END

GO

GO

PRINT 'DATABASE: TargetDB, TABLES: TargetDB.dbo.TransformedEmployees'