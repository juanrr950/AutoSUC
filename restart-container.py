import requests

contenedor="autosuc_container"
credenciales ={"username":"admin",
      "password":"jarguezr1991"}

r = requests.post('http://juanas-as6404t.myasustor.com:19900/api/auth',
                  json=credenciales)

token = r.json()['jwt']

authorization={'Authorization':'Bearer '+token}

r = requests.post('http://juanas-as6404t.myasustor.com:19900'+
                '/api/endpoints/1/docker/containers/'+contenedor+'/restart',
                  headers=authorization)

r.status_code==204:
      print("Contenedor reiniciado satisfactoriamente")