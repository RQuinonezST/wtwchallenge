using Microsoft.EntityFrameworkCore;
using WTWGraphAccess.Domain;
using WTWGraphAccess.Persistence.Configurations;

namespace WTWGraphAccess.Persistence.DatabaseContext
{
    public class WTWGraphAccesDataContext : DbContext
    {
        public WTWGraphAccesDataContext(DbContextOptions<WTWGraphAccesDataContext> options)
            : base(options) 
        {
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.ApplyConfiguration(new TransformedEmployeeConfiguration());
        }

        public DbSet<TransformedEmployee> TransformedEmployees { get; set; }
    }
}
