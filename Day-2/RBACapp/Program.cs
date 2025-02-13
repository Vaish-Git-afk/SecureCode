using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Dictionary<string, Dictionary<string, bool>> permissions = new Dictionary<string, Dictionary<string, bool>>
        {
            { "Radiologist", new Dictionary<string, bool> { { "ReadFull", true }, { "ReadMinimal", false }, { "Create", true }, { "UpdateFull", true }, { "UpdateMetadata", false }, { "UpdateComments", false }, { "DeleteFull", false }, { "DeleteRestricted", true } } },
            { "Physician", new Dictionary<string, bool> { { "ReadFull", false }, { "ReadMinimal", true }, { "Create", false }, { "UpdateFull", false }, { "UpdateMetadata", false }, { "UpdateComments", true }, { "DeleteFull", false }, { "DeleteRestricted", false } } },
            { "Lab Technician", new Dictionary<string, bool> { { "ReadFull", false }, { "ReadMinimal", true }, { "Create", false }, { "UpdateFull", false }, { "UpdateMetadata", true }, { "UpdateComments", false }, { "DeleteFull", false }, { "DeleteRestricted", false } } },
            { "Administrator", new Dictionary<string, bool> { { "ReadFull", true }, { "ReadMinimal", false }, { "Create", true }, { "UpdateFull", true }, { "UpdateMetadata", true }, { "UpdateComments", true }, { "DeleteFull", true }, { "DeleteRestricted", true } } },
            { "Patient", new Dictionary<string, bool> { { "ReadFull", false }, { "ReadMinimal", true }, { "Create", false }, { "UpdateFull", false }, { "UpdateMetadata", false }, { "UpdateComments", false }, { "DeleteFull", false }, { "DeleteRestricted", false } } },
            { "Billing Staff", new Dictionary<string, bool> { { "ReadFull", false }, { "ReadMinimal", true }, { "Create", false }, { "UpdateFull", false }, { "UpdateMetadata", false }, { "UpdateComments", false }, { "DeleteFull", false }, { "DeleteRestricted", false } } }
        };

        Console.WriteLine("RBAC Permissions Table");
        Console.WriteLine("--------------------------------------------------------------------------------------------");
        Console.WriteLine("| Role           | Read (Full) | Read (Minimal) | Create | Update (Full) | Update (Metadata) | Update (Comments) | Delete (Full) | Delete (Restricted) |");
        Console.WriteLine("--------------------------------------------------------------------------------------------");

        foreach (var role in permissions)
        {
            Console.Write("| {0,-14} |", role.Key);
            foreach (var perm in role.Value)
            {
                Console.Write(" {0,-12} |", perm.Value ? "True" : "False");
            }
            Console.WriteLine();
        }
        Console.WriteLine("--------------------------------------------------------------------------------------------");
    }
}