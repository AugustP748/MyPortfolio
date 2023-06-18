
class DarkModeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
    # Verificar si el modo oscuro está activado en la sesión del usuario
        if request.session.get('dark'):
            # Aplicar estilos o cualquier otra lógica correspondiente al modo oscuro
            request.dark_mode = True
        else:
            request.dark_mode = False

        return self.get_response(request)