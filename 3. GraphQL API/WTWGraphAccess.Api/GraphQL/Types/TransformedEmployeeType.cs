using GraphQL;
using GraphQL.Types;
using WTWGraphAccess.Domain;

namespace WTWGraphAccess.Api.GraphQL.Types
{
    public class TransformedEmployeeType : ObjectGraphType<TransformedEmployee>
    {
        public TransformedEmployeeType()
        {
            Name = nameof(TransformedEmployee);
            Description = "Transformed Employee information";

            Field(b => b.EmployeeID, type: typeof(IntGraphType)).Description("Employee's ID");
            Field(b => b.FullName, type: typeof(StringGraphType)).Description("Employee's First and Last name");
            Field(b => b.Department, type: typeof(StringGraphType)).Description("Employee's Department");
            Field(b => b.AnnualSalary, type: typeof(DecimalGraphType)).Description("Employee's Annual Salary");
        }
    }



}
