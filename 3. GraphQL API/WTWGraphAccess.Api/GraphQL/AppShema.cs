using GraphQL.Types;
using WTWGraphAccess.Api.GraphQL.Queries;
using WTWGraphAccess.Api.GraphQL.Types;
using WTWGraphAccess.Domain;
using WTWGraphAccess.Persistence.DatabaseContext;

namespace WTWGraphAccess.Api.GraphQL
{
    public class AppShema : Schema
    {
        public AppShema(EmployeeQuery query)
        {
            this.Query = query;
            //RegisterType<TransformedEmployeeType>();
        }
    }
}
