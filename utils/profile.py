class UserProfile:
    def __init__(self, user_id, name, email, language="English") -> None:
        self.user_id = user_id
        self.name = name
        self.email = email
        self.language = language
        self.reservations = []

    def update_profile(self, name=None, email=None, language=None) -> None:
        if name:
            self.name = name
        if email:
            self.email = email
        if language:
            self.language = language

    def __str__(self) -> str:
        return f"User: {self.name} | Email: {self.email} | Lang: {self.language}"
