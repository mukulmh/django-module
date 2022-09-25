from django.shortcuts import render,redirect
from django.contrib import messages
import os
import logging

logger = logging.getLogger(__name__)


# Create your views here.
# logs
def dashboard(request):
    if request.user.is_authenticated and request.user.user_role_id_id == 1:
        files = os.listdir('logs')
        files=[x.split('.')[0] for x in files]
        files.reverse()
        logs = []
        for file in files:
            log_data = {}
            all_count = 0
            debug_count = 0
            info_count = 0
            error_count = 0
            warning_count = 0
            critical_count = 0

            with open('logs/'+file+'.log') as fp:
                all_logs = []
                debug_logs = []
                info_logs = []
                warning_logs = []
                error_logs = []
                critical_logs = []
                for line in fp:
                    if line.strip():
                        if line.find('DEBUG') != -1:
                            debug_count += 1
                            debug_logs.append(line)
                            all_count += 1
                            all_logs.append(line)
                        if line.find('INFO') != -1:
                            info_count += 1
                            info_logs.append(line)
                            all_count += 1
                            all_logs.append(line)
                        if line.find('ERROR') != -1:
                            error_count += 1
                            error_logs.append(line)
                            all_count += 1
                            all_logs.append(line)
                        if line.find('WARNING') != -1:
                            warning_count += 1
                            warning_logs.append(line)
                            all_count += 1
                            all_logs.append(line)
                        if line.find('CRITICAL') != -1:
                            critical_count += 1
                            critical_logs.append(line)
                            all_count += 1
                            all_logs.append(line)

            log_data['date'] = file
            log_data['all_count'] = all_count
            log_data['info_count'] = info_count
            log_data['debug_count'] = debug_count
            log_data['error_count'] = error_count
            log_data['warning_count'] = warning_count
            log_data['critical_count'] = critical_count
            all_logs.reverse()
            log_data['all_logs'] = all_logs
            debug_logs.reverse()
            log_data['debug_logs'] = debug_logs
            info_logs.reverse()
            log_data['info_logs'] = info_logs
            warning_logs.reverse()
            log_data['warning_logs'] = warning_logs
            error_logs.reverse()
            log_data['error_logs'] = error_logs
            critical_logs.reverse()
            log_data['critical_logs'] = critical_logs
            logs.append(log_data)
        # print(logs)
        todays_log = logs[0]
        return render(request,'logger/dashboard.html',{'logs':logs, 'todays_log':todays_log})
    messages.error(request,'Please sign in as Admin!')
    logger.debug('Unauthorized access blocked.')
    return redirect('login')

# logs
def logs(request, file):
    with open('logs/'+file+'.log') as fp:
        logs = []
        for line in fp:
            if line.strip():
                if line.find('DEBUG') != -1:
                    logs.append(line)
                if line.find('INFO') != -1:
                    logs.append(line)
                if line.find('WARNING') != -1:
                    logs.append(line)
                if line.find('ERROR') != -1:
                    logs.append(line)
                if line.find('CRITICAL') != -1:
                    logs.append(line)
        logs.reverse()
    return render(request,'logger/logs.html',{'logs':logs})
