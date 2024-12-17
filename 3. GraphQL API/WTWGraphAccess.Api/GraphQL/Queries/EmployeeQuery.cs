using GraphQL;
using GraphQL.Types;
using WTWGraphAccess.Api.GraphQL.Types;
using WTWGraphAccess.Persistence.Repository;

namespace WTWGraphAccess.Api.GraphQL.Queries
{
    public class EmployeeQuery : ObjectGraphType
    {
        public EmployeeQuery(TransformedEmployeeRepository repository)
        {
            Field<ListGraphType<TransformedEmployeeType>>("employee")
                .Description("list of transformed employees")
                .ResolveAsync(async context => await repository.GetAllEmployees());

            Field<ListGraphType<TransformedEmployeeType>>("employeebydepartment")
                .Description("list of transformed employees filtered by department")
                .Arguments(new QueryArgument<NonNullGraphType<StringGraphType>> { Name= "department", Description="department's name"})
                .ResolveAsync(async context => await repository.GetAllEmployeesByDepartment(context.GetArgument("department", "")));
        }

       
    }
}
