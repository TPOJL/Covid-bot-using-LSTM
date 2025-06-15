from application import Application
from model_manager import ModelManager

#start the program
if __name__ == '__main__':
    model = ModelManager()
    app = Application(model)
    app.start()
