from django.shortcuts import render,redirect
from django.contrib import messages
import os

# Create your views here.
files = os.listdir('logs')
files=[x.split('.')[0] for x in files]
files.reverse()

# logs
def logs(request):
    if request.user.is_authenticated and request.user.user_role_id_id == 1:
        logs = []
        for file in files:
            log_data = {}
            all = 0
            error = 0
            info = 0
            debug = 0
            warning = 0

            with open('logs/'+file+'.log') as fp:
                for line in fp:
                    if line.strip():
                        all += 1
                    if line.find('DEBUG') != -1:
                        debug += 1
                    if line.find('INFO') != -1:
                        info += 1
                    if line.find('ERROR') != -1:
                        error += 1
                    if line.find('WARNING') != -1:
                        warning += 1

            log_data['date'] = file
            log_data['all'] = all
            log_data['info'] = info
            log_data['debug'] = debug
            log_data['error'] = error
            log_data['warning'] = warning
            logs.append(log_data)
        # print(logs)
        todays_log = logs[0]
        userscreens = request.session['userscreens']
        usersubmodules = request.session['usersubmodules']
        usermodules = request.session['usermodules']
        modules = request.session['modules']
        return render(request,'adminlte/logs.html',{'modules':modules, 'usermodules': usermodules, 'usersubmodules': usersubmodules, 'userscreens':userscreens, 'sideScreen': 'Logs', 'logs':logs, 'todays_log':todays_log})
    messages.error(request,'Please sign in as Admin!')
    return redirect('login')
