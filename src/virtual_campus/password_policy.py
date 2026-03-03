class PasswordPolicyError(ValueError):
    pass


class PasswordPolicy:
    def __init__(self, min_length: int = 10) -> None:
        self.min_length = min_length

    def validate(self, password: str) -> None:
        if len(password) < self.min_length:
            raise PasswordPolicyError(
                f"La contrasena debe tener al menos {self.min_length} caracteres."
            )
        if not any(char.islower() for char in password):
            raise PasswordPolicyError(
                "La contrasena debe incluir al menos una letra minuscula."
            )
        if not any(char.isupper() for char in password):
            raise PasswordPolicyError(
                "La contrasena debe incluir al menos una letra mayuscula."
            )
        if not any(char.isdigit() for char in password):
            raise PasswordPolicyError(
                "La contrasena debe incluir al menos un numero."
            )
        if not any(not char.isalnum() for char in password):
            raise PasswordPolicyError(
                "La contrasena debe incluir al menos un caracter especial."
            )
