#!/usr/bin/env python3
# Import the tools we need from Werkzeug
from werkzeug.wrappers import Request, Response

# Create our main function that handles requests
@Request.application
def application(request):
    # Print who's visiting (shows in terminal)
    print(f'This web server is running at {request.remote_addr}')
    
    # Send back a response (shows in browser)
    return Response('A WSGI generated this response!')

# Only run this if we're running THIS file directly
if __name__ == '__main__':
    # Import the function to run our server
    from werkzeug.serving import run_simple
    
    # Start the server!
    run_simple(
        hostname='localhost',    # Run on MY computer
        port=5555,              # Use apartment door #5555
        application=application  # Use OUR application function
    )