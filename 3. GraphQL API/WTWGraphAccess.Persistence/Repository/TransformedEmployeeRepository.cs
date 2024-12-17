using Microsoft.EntityFrameworkCore;
using WTWGraphAccess.Core.Interfaces.Persistence;
using WTWGraphAccess.Domain;
using WTWGraphAccess.Persistence.DatabaseContext;

namespace WTWGraphAccess.Persistence.Repository
{
    public class TransformedEmployeeRepository: ITransformedEmployeeRepository
    {
        private readonly WTWGraphAccesDataContext db;

        public TransformedEmployeeRepository(WTWGraphAccesDataContext db)
        {
            this.db = db;
        }

        public async Task<List<TransformedEmployee>> GetAllEmployees()
        {
            return await db.TransformedEmployees
                .ToListAsync();
        }

        public async Task<List<TransformedEmployee>> GetAllEmployeesByDepartment(string department)
        {
            return await db.TransformedEmployees
                .Where(e => e.Department.Equals(department))
                .ToListAsync();
        }

    }
}
