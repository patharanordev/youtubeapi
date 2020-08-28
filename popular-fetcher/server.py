import os
import argparse
import csv
import httplib2

from googleapiclient import discovery, errors
from oauth2client import client
from oauth2client.file import Storage
from oauth2client import tools

def get_auth_credentials():
  flow = client.flow_from_clientsecrets(
    '{}/token/{}'.format(os.getcwd(), 'client_secret.json'),  # file downloaded from Google Developers Console
    scope='https://www.googleapis.com/auth/youtube.readonly',
    redirect_uri='urn:ietf:wg:oauth:2.0:oob')

  storage = Storage('{}/token/storage.dat'.format(os.getcwd()))
  credentials = storage.get()
  if credentials is None or credentials.invalid:
      parser = argparse.ArgumentParser(parents=[tools.argparser])
      flags = parser.parse_args(['--noauth_local_webserver'])
      credentials = tools.run_flow(flow=flow, storage=storage, flags=flags)

  return credentials

def main():
  credentials = get_auth_credentials()
  http_auth = credentials.authorize(httplib2.Http())
  # build the service object
  youtube = discovery.build('youtube', 'v3', http=http_auth)

  request = youtube.videos().list(
      part="snippet,contentDetails,statistics",
      chart="mostPopular",
      maxResults=10,
      regionCode="US"
  )
  response = request.execute()

  print(response)


if __name__ == "__main__":
  main()