from fabric.api import lcd, local

def deploy():
    with lcd('/Users/NickStefan/Documents/PythonProjects/nickswebsite/')
        
        local('git pull /Users/NickStefan/Documents/PythonProjects/dev/')
        
        local('python nickswebsite/manage.py migrate blog')
        local('python nickswebsite/manage.py test blog')
        local('python nickswebsite/manage.py runserver')
        
        #if deploying on dif machine than developing on,
        # use run() rather than local() see fabric documentation
        
        # commands:
        # fab prepare_deployment
        # fab deploy