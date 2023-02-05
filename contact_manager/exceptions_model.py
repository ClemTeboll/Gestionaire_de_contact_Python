class InvalidContactNameException():
    def __init__(self, message="Votre nom doit avoir plus de 2 caractères. Veuillez réessayer."):
        super().__init__(message)

class InvalidContactSurnameException():
    def __init__(self, message="Votre prénom doit avoir plus de 2 caractères. Veuillez réessayer."):
        super().__init__(message)

class InvalidContactEmailException():
    def __init__(self, message="Votre email n'est pas valide. Veuillez réessayer."):
        super().__init__(message)