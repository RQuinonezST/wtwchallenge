using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using WTWGraphAccess.Core.Interfaces.Persistence;
using WTWGraphAccess.Persistence.DatabaseContext;
using WTWGraphAccess.Persistence.Repository;

namespace WTWGraphAccess.Persistence
{
    public static class PersistenceServiceRegistration
    {
        public static IServiceCollection AddPersistenceServiceRegistration
            (this IServiceCollection services, IConfiguration configuration)
        {
            services.AddDbContext<WTWGraphAccesDataContext>(options =>
            {
                options.UseSqlServer(configuration.GetConnectionString("WTWTargetDBConnectionString"))
                        .UseQueryTrackingBehavior(QueryTrackingBehavior.NoTracking);
            });

            services.AddScoped<ITransformedEmployeeRepository, TransformedEmployeeRepository>();

            return services;
        }
    }
}
