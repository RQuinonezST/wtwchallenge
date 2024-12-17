
using GraphQL;
using WTWGraphAccess.Api.GraphQL;
using WTWGraphAccess.Api.GraphQL.Queries;
using WTWGraphAccess.Persistence;
using WTWGraphAccess.Persistence.Repository;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddScoped<TransformedEmployeeRepository>();
builder.Services.AddScoped<EmployeeQuery>();
builder.Services.AddScoped<AppShema>();

// Add services to the container.
builder.Services.AddPersistenceServiceRegistration(builder.Configuration);

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();



// Add GraphQL Services
builder.Services.AddGraphQL(b => b
    .AddSystemTextJson());


var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.UseGraphQL<AppShema>();
app.UseGraphQL("/graphql");

// url to host GraphQL endpoint
app.UseGraphQLGraphiQL(
    "/",                               // url to host GraphiQL at
    new GraphQL.Server.Ui.GraphiQL.GraphiQLOptions
    {
        GraphQLEndPoint = "/graphql",         // url of GraphQL endpoint
        SubscriptionsEndPoint = "/graphql",   // url of GraphQL endpoint
    });

app.Run();
