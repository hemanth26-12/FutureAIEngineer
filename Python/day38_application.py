class Application:
    def __init__(self, Company, Role, Status, Experience):
        self.Company = Company
        self.Role = Role
        self.Status = Status
        self.Experience = Experience

        
    def to_dict(self):
        return {
            "Company": self.Company,
            "Role": self.Role,
            "Status": self.Status,
            "Experience": self.Experience,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data.get("Company", ""),
            data.get("Role", ""),
            data.get("Status", ""),
            data.get("Experience", 0),
        )

    def __repr__(self):
        return (
            f"Application(Company={self.Company!r}, Role={self.Role!r}, "
            f"Status={self.Status!r}, Experience={self.Experience!r})"
        )
