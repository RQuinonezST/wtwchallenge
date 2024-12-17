using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Builders;
using WTWGraphAccess.Domain;

namespace WTWGraphAccess.Persistence.Configurations
{
    public class TransformedEmployeeConfiguration : IEntityTypeConfiguration<TransformedEmployee>
    {
        public void Configure(EntityTypeBuilder<TransformedEmployee> builder)
        {
            // Define the primary key
            builder.HasKey(c => c.EmployeeID);
            builder.Property(c => c.FullName).HasMaxLength(100);
            builder.Property(c => c.Department).HasMaxLength(50);
            builder.Property(c => c.AnnualSalary).HasColumnType("decimal(18, 2)");

            builder.ToTable("TransformedEmployees");
        }
    }
}
