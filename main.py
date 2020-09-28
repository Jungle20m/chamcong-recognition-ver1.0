

from fastapi import FastAPI
from pydantic import BaseModel

from recognition_process import recognition


from database import schemas


PROCESSES = {}


@app.post("/chamcong/recognition/start")
def start_recognition(parameter:schemas.Parameter):
    recognite_process_id = parameter.recognite_process_id
    source_topic = parameter.source_topic
    destination_topic = parameter.destination_topic
    source_servers = parameter.source_servers
    destination_server = parameter.destination_servers
    
    if recognite_process_id not in PROCESSES.keys():
        # process = multiprocessing.Process(target=camera_recognite, args=(source_topic.name, source_servers, destination_topic.name, destination_servers))
		# process.start()
        return {"status": True, "message": "success"}
    else:
        return {"status": False, "message": "error"}
    

@app.get("/chamcong/recognition/stop")
def stop_recognition(process_id: int):
    pass