namespace WTWGraphAccess.Domain
{
    public class TransformedEmployee
    {
        public int EmployeeID { get; set; }
        public string FullName { get; set; } = string.Empty;
        public string Department { get; set; } = string.Empty;
        public double AnnualSalary { get; set; }
    }
}
