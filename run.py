from app import create_app

config_name = 'development'
# method to run app.py
if __name__ == '__main__':

    app = create_app(config_name)
    app.run()
