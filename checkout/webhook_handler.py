from django.http import HTTPResponse


class StripeWH_Handler:
    """"Handles Stope webhooks"""
   
    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HTTPResponse(
            content=f"Webhook recieved: {event["type"]}",
            status=200)
