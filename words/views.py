from django.shortcuts import render
import logging
from os import path
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger('root')

def index(request):
	logger.info('index')
	return render(request, 'words/quest.html', {})
    


def new(request):
	logger.info('new')
	return render(request, 'words/new.html', {})
	
	

def created(request):
	logger.info('created')
	return index(request)