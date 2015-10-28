"""Simple entry point of the application, does nothing more
than construct an Application instance and run it."""

from ctpcj import Application

def main():
    """Called when the application is starting, runs the web server."""
    app = Application()
    app.run()

if __name__ == '__main__':
    main()
