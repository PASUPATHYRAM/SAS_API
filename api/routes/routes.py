#home,login.logout,singup

from flask_restful import Api

from api.resources.resources_routes import Home,Login,Logout,Signup,Con,Getall

def generate_routes(app):
    api=Api(app)

    api.add_resource(Home,'/home')

    api.add_resource(Login,'/login')

    api.add_resource(Logout,'/logout')

    api.add_resource(Signup,'/signup')

    api.add_resource(Con,'/content')

    api.add_resource(Getall,'/getall')

    return api
