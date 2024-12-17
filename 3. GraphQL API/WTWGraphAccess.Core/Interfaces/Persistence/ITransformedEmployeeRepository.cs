using WTWGraphAccess.Domain;

namespace WTWGraphAccess.Core.Interfaces.Persistence
{
    public interface ITransformedEmployeeRepository
    {
        Task<List<TransformedEmployee>> GetAllEmployees();

        Task<List<TransformedEmployee>> GetAllEmployeesByDepartment(string department);

    }
}
